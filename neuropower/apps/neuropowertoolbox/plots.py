import matplotlib as mpl
mpl.use('Agg')
from .models import NeuropowerModel
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from palettable.colorbrewer.qualitative import Paired_12,Set1_9
from django.http import HttpResponse, HttpResponseRedirect
from neuropower import *
from .utils import get_session_id
from mpld3 import plugins
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import mpld3

def plotModel(request):
    plt.switch_backend('agg')
    sid = get_session_id(request)
    neuropowerdata = NeuropowerModel.objects.get(SID=sid)
    if not neuropowerdata.err == "":
        fig=plt.figure(facecolor="white")
    else:
        peaks = neuropowerdata.peaktable
        twocol = Paired_12.mpl_colors
        if neuropowerdata.pi1>0:
            xn = np.arange(-10,30,0.01)
            nul = [1-float(neuropowerdata.pi1)]*neuropowermodels.nulPDF(xn,exc=float(neuropowerdata.ExcZ),method="RFT")
            alt = float(neuropowerdata.pi1)*neuropowermodels.altPDF(xn,mu=float(neuropowerdata.mu),sigma=float(neuropowerdata.sigma),exc=float(neuropowerdata.ExcZ),method="RFT")
            mix = neuropowermodels.mixPDF(xn,pi1=float(neuropowerdata.pi1),mu=float(neuropowerdata.mu),sigma=float(neuropowerdata.sigma),exc=float(neuropowerdata.ExcZ),method="RFT")
        xn_p = np.arange(0,1,0.01)
        alt_p = float(neuropowerdata.pi1)*scipy.stats.beta.pdf(xn_p, float(neuropowerdata.a), 1)+1-float(neuropowerdata.pi1)
        null_p = [1-float(neuropowerdata.pi1)]*len(xn_p)
        mpl.rcParams['font.size']='11.0'

        fig,axs=plt.subplots(1,2,figsize=(14,5))
        fig.patch.set_facecolor('None')
        fig.subplots_adjust(hspace=.5,wspace=0.3)
        axs=axs.ravel()

        axs[0].hist(peaks.pval,lw=0,normed=True,facecolor=twocol[0],bins=np.arange(0,1.1,0.1),label="observed distribution")
        axs[0].set_ylim([0,3])
        axs[0].plot(xn_p,null_p,color=twocol[3],lw=2,label="null distribution")
        axs[0].plot(xn_p,alt_p,color=twocol[5],lw=2,label="alternative distribution")
        axs[0].legend(loc="upper right",frameon=False)
        axs[0].set_title("Distribution of "+str(len(peaks))+" peak p-values \n $\pi_1$ = "+str(round(float(neuropowerdata.pi1),2)))
        axs[0].set_xlabel("Peak p-values")
        axs[0].set_ylabel("Density")
        axs[1].hist(peaks.peak,lw=0,facecolor=twocol[0],normed=True,bins=np.arange(min(peaks.peak),30,0.3),label="observed distribution")
        axs[1].set_xlim([float(neuropowerdata.ExcZ),np.max(peaks.peak)+1])
        axs[1].set_ylim([0,1.3])

        if not neuropowerdata.pi1==0:
            axs[1].plot(xn,nul,color=twocol[3],lw=2,label="null distribution")
            axs[1].plot(xn,alt,color=twocol[5],lw=2, label="alternative distribution")
            axs[1].plot(xn,mix,color=twocol[1],lw=2,label="total distribution")
            axs[1].legend(loc="upper right",frameon=False)

        peak_heights_string = str(round(float(neuropowerdata.mu)/np.sqrt(neuropowerdata.Subj),2))
        axs[1].set_title("Distribution of peak heights \n $\delta_1$ = %s" %(peak_heights_string))
        axs[1].set_xlabel("Peak heights (z-values)")
        axs[1].set_ylabel("Density")
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def plotPower(sid,MCP='',pow=0,ss=0):
    neuropowerdata = NeuropowerModel.objects.get(SID=sid)
    powtab = neuropowerdata.data
    powtxt = powtab.round(2)
    cols = dict(zip(['BF','BH','RFT','UN'],Set1_9.mpl_colors))
    sub = int(neuropowerdata.Subj)
    newsubs = powtab.newsamplesize
    amax = int(np.min(powtab.newsamplesize)+50)

    css = """
    table{border-collapse: collapse}
    td{background-color: rgba(217, 222, 230,50)}
    table, th, td{border: 1px solid;border-color: rgba(217, 222, 230,50);text-align: right;font-size: 12px}
    """


    hover_BF = [pd.DataFrame(['Bonferroni','Sample Size: '+str(newsubs[i]),'Power: '+str(powtxt['BF'][i])]).to_html(header=False,index_names=False,index=False) for i in range(len(powtab)) if 'BF' in powtab.columns]
    hover_BH = [pd.DataFrame(['Benjamini-Hochberg','Sample Size: '+str(newsubs[i]),'Power: '+str(powtxt['BH'][i])]).to_html(header=False,index_names=False,index=False) for i in range(len(powtab)) if 'BH' in powtab.columns]
    hover_RFT = [pd.DataFrame(['Random Field Theory','Sample Size: '+str(newsubs[i]),'Power: '+str(powtxt['RFT'][i])]).to_html(header=False,index_names=False,index=False) for i in range(len(powtab)) if 'RFT' in powtab.columns]
    hover_UN = [pd.DataFrame(['Uncorrected','Sample Size: '+str(newsubs[i]),'Power: '+str(powtxt['UN'][i])]).to_html(header=False,index_names=False,index=False) for i in range(len(powtab)) if 'UN' in powtab.columns]

    fig,axs=plt.subplots(1,1,figsize=(8,5))
    fig.patch.set_facecolor('None')
    lty = ['--' if all(powtab.BF==powtab.RFT) else '-']
    BF=axs.plot(powtab.newsamplesize,powtab.BF,'o',markersize=15,alpha=0,label="") if 'BF' in powtab.columns else 'nan'
    BH=axs.plot(powtab.newsamplesize,powtab.BH,'o',markersize=15,alpha=0,label="") if 'BH' in powtab.columns else 'nan'
    RFT=axs.plot(powtab.newsamplesize,powtab.RFT,'o',markersize=15,alpha=0,label="") if 'RFT' in powtab.columns else 'nan'
    UN=axs.plot(powtab.newsamplesize,powtab.UN,'o',markersize=15,alpha=0,label="") if 'UN' in powtab.columns else 'nan'
    plugins.clear(fig)
    plugins.connect(fig, plugins.PointHTMLTooltip(BF[0], hover_BF,hoffset=0,voffset=10,css=css))
    plugins.connect(fig, plugins.PointHTMLTooltip(RFT[0], hover_RFT,hoffset=0,voffset=10,css=css))
    plugins.connect(fig, plugins.PointHTMLTooltip(UN[0], hover_UN,hoffset=0,voffset=10,css=css))
    if 'BH' in powtab.columns:
        plugins.connect(fig, plugins.PointHTMLTooltip(BH[0], hover_BH,hoffset=0,voffset=10,css=css))
        axs.plot(newsubs,powtab.BH,color=cols['BH'],lw=2,label="Benjamini-Hochberg")
    axs.plot(newsubs,powtab.BF,color=cols['BF'],lw=2,label="Bonferroni")
    axs.plot(newsubs,powtab.RFT,color=cols['RFT'],lw=2,linestyle=str(lty[0]),label="Random Field Theory")
    axs.plot(newsubs,powtab.UN,color=cols['UN'],lw=2,label="Uncorrected")
    text = "None"
    if pow != 0:
        if MCP == 'BH' and not 'BH' in powtab.columns:
            text = "There is not enough power to estimate a threshold for FDR control.  As such it's impossible to predict power for FDR control."
        elif all(powtab[MCP]<pow):
            text = "To obtain a statistical power of "+str(pow)+" this study would require a sample size larger than 600 subjects."
            amax = max(powtab.newsamplesize)
        else:
            min = int(np.min([i for i,elem in enumerate(powtab[MCP]>pow,1) if elem])+sub-1)
            axs.plot([min,min],[0,powtab[MCP][min-sub]],color=cols[MCP])
            axs.plot([sub,min],[powtab[MCP][min-sub],powtab[MCP][min-sub]],color=cols[MCP])
            text = "To obtain a statistical power of %s this study would require a sample size of %s subjects." %(pow,min)
            amax = max(min,amax)
    if ss != 0:
        if MCP == 'BH' and not 'BH' in powtab.columns:
            text = "There is not enough power to estimate a threshold for FDR control.  As such it's impossible to predict power for FDR control."
        else:
            ss_pow = powtab[MCP][ss]
            axs.plot([ss,ss],[0,ss_pow],color=cols[MCP],linestyle="--")
            axs.plot([sub,ss],[ss_pow,ss_pow],color=cols[MCP],linestyle="--")
            xticks = [x for x in list(np.arange((np.ceil(sub/10.))*10,100,10)) if not x == np.round(ss/10.)*10]
            axs.set_xticks(xticks+[ss])
            axs.set_yticks(list(np.arange(0,1.1,0.1)))
            text = "A sample size of %s subjects with %s control comes with a power of %s." %(ss,MCP,str(np.round(ss_pow,decimals=2)))
            amax = max(ss,amax)
    axs.set_ylim([0,1])
    axs.set_xlim([sub,amax])
    axs.set_title("Power curves")
    axs.set_xlabel("Subjects")
    axs.set_ylabel("Average power")
    axs.legend(loc="lower right",frameon=False,title="")
    code = mpld3.fig_to_html(fig)
    out = {
        "code":code,
        "text":text
    }
    return out
