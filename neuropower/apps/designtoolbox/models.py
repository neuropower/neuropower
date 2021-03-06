from __future__ import unicode_literals
from django.db import models
from picklefield.fields import PickledObjectField
import os
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class DesignModel(models.Model):
    # flow variables
    SID = models.CharField(max_length=300,default="")
    step = models.IntegerField(default=0,null=True,blank=True)
    shareID = models.CharField(max_length=300,default="")
    taskstatus = models.IntegerField(default=0)
    running = models.IntegerField(default=0)
    taskID = models.CharField(max_length=300,default="")
    cmd = models.CharField(max_length=10000,default="")
    metrics = PickledObjectField(default = "")
    bestdesign = PickledObjectField(default = "")
    conv_crit = models.IntegerField(default=1000)
    convergence = models.BooleanField(default = False)
    name = models.CharField(default = "",max_length=500)
    email = models.CharField(default = "",max_length=500)
    outdes = models.IntegerField(default=1)
    jobid = models.CharField(default="",max_length=100)
    timestart = models.CharField(default="",max_length=500)
    timestamp = models.CharField(default="",max_length=500)
    generation = models.IntegerField(default=0)

    # design options
    ITImodel = models.IntegerField(choices=((1,'fixed'),(2,'truncated exponential'),(3,'uniform')),default=3)
    ITIfixed = models.FloatField(default=None, null=True, blank=True)
    ITIunifmin = models.FloatField(default=None, null=True, blank=True)
    ITIunifmax = models.FloatField(default=None, null=True, blank=True)
    ITItruncmin = models.FloatField(default=None, null=True, blank=True)
    ITItruncmax = models.FloatField(default=None, null=True, blank=True)
    ITItruncmean = models.FloatField(default=None,null=True,blank=True)
    TR = models.FloatField(default=None, null=True, blank=True)
    L = models.IntegerField(null=True, blank=True)
    S = models.IntegerField(null=True, blank=True)
    duration = models.FloatField(default=None,null=True,blank=True)
    duration_unit_choices = ((1,"seconds"),(2,"minutes"))
    duration_unit = models.IntegerField(choices=duration_unit_choices,default=2)
    duration_unitfree = models.FloatField(default = None,null=True,blank=True)
    durspec = models.IntegerField(choices=((1,"duration"),(2,"trial count")),default=1)
    stim_duration = models.FloatField(default=1,null=True,blank=True)
    t_prestim = models.FloatField(default=0)
    t_poststim = models.FloatField(default=0)
    Call = models.BooleanField(default=False)
    Clen = models.IntegerField(default=0,null=True, blank=True)
    RestNum = models.IntegerField(default=0,null=True,blank=True)
    RestDur = models.FloatField(default=0,null=True,blank=True)
    seed = models.IntegerField(default=1)
    # nested structure
    G0 = models.FloatField(default=None, null=True, blank=True)
    G1 = models.FloatField(default=None, null=True, blank=True)
    G2 = models.FloatField(default=None, null=True, blank=True)
    G3 = models.FloatField(default=None, null=True, blank=True)
    G4 = models.FloatField(default=None, null=True, blank=True)
    G5 = models.FloatField(default=None, null=True, blank=True)
    G6 = models.FloatField(default=None, null=True, blank=True)
    G7 = models.FloatField(default=None, null=True, blank=True)
    G8 = models.FloatField(default=None, null=True, blank=True)
    G9 = models.FloatField(default=None, null=True, blank=True)
    # contrasts and probabilities
    PG0 = models.FloatField(default=None, null=True, blank=True)
    PG1 = models.FloatField(default=None, null=True, blank=True)
    PG2 = models.FloatField(default=None, null=True, blank=True)
    PG3 = models.FloatField(default=None, null=True, blank=True)
    PG4 = models.FloatField(default=None, null=True, blank=True)
    PG5 = models.FloatField(default=None, null=True, blank=True)
    PG6 = models.FloatField(default=None, null=True, blank=True)
    PG7 = models.FloatField(default=None, null=True, blank=True)
    PG8 = models.FloatField(default=None, null=True, blank=True)
    PG9 = models.FloatField(default=None, null=True, blank=True)
    # contrasts and probabilities
    P0 = models.FloatField(default=None, null=True, blank=True)
    P1 = models.FloatField(default=None, null=True, blank=True)
    P2 = models.FloatField(default=None, null=True, blank=True)
    P3 = models.FloatField(default=None, null=True, blank=True)
    P4 = models.FloatField(default=None, null=True, blank=True)
    P5 = models.FloatField(default=None, null=True, blank=True)
    P6 = models.FloatField(default=None, null=True, blank=True)
    P7 = models.FloatField(default=None, null=True, blank=True)
    P8 = models.FloatField(default=None, null=True, blank=True)
    P9 = models.FloatField(default=None, null=True, blank=True)
    C00 = models.FloatField(default=None, null=True, blank=True)
    C01 = models.FloatField(default=None, null=True, blank=True)
    C02 = models.FloatField(default=None, null=True, blank=True)
    C03 = models.FloatField(default=None, null=True, blank=True)
    C04 = models.FloatField(default=None, null=True, blank=True)
    C05 = models.FloatField(default=None, null=True, blank=True)
    C06 = models.FloatField(default=None, null=True, blank=True)
    C07 = models.FloatField(default=None, null=True, blank=True)
    C08 = models.FloatField(default=None, null=True, blank=True)
    C09 = models.FloatField(default=None, null=True, blank=True)
    C10 = models.FloatField(default=None, null=True, blank=True)
    C11 = models.FloatField(default=None, null=True, blank=True)
    C12 = models.FloatField(default=None, null=True, blank=True)
    C13 = models.FloatField(default=None, null=True, blank=True)
    C14 = models.FloatField(default=None, null=True, blank=True)
    C15 = models.FloatField(default=None, null=True, blank=True)
    C16 = models.FloatField(default=None, null=True, blank=True)
    C17 = models.FloatField(default=None, null=True, blank=True)
    C18 = models.FloatField(default=None, null=True, blank=True)
    C19 = models.FloatField(default=None, null=True, blank=True)
    C20 = models.FloatField(default=None, null=True, blank=True)
    C21 = models.FloatField(default=None, null=True, blank=True)
    C22 = models.FloatField(default=None, null=True, blank=True)
    C23 = models.FloatField(default=None, null=True, blank=True)
    C24 = models.FloatField(default=None, null=True, blank=True)
    C25 = models.FloatField(default=None, null=True, blank=True)
    C26 = models.FloatField(default=None, null=True, blank=True)
    C27 = models.FloatField(default=None, null=True, blank=True)
    C28 = models.FloatField(default=None, null=True, blank=True)
    C29 = models.FloatField(default=None, null=True, blank=True)
    C30 = models.FloatField(default=None, null=True, blank=True)
    C31 = models.FloatField(default=None, null=True, blank=True)
    C32 = models.FloatField(default=None, null=True, blank=True)
    C33 = models.FloatField(default=None, null=True, blank=True)
    C34 = models.FloatField(default=None, null=True, blank=True)
    C35 = models.FloatField(default=None, null=True, blank=True)
    C36 = models.FloatField(default=None, null=True, blank=True)
    C37 = models.FloatField(default=None, null=True, blank=True)
    C38 = models.FloatField(default=None, null=True, blank=True)
    C39 = models.FloatField(default=None, null=True, blank=True)
    C40 = models.FloatField(default=None, null=True, blank=True)
    C41 = models.FloatField(default=None, null=True, blank=True)
    C42 = models.FloatField(default=None, null=True, blank=True)
    C43 = models.FloatField(default=None, null=True, blank=True)
    C44 = models.FloatField(default=None, null=True, blank=True)
    C45 = models.FloatField(default=None, null=True, blank=True)
    C46 = models.FloatField(default=None, null=True, blank=True)
    C47 = models.FloatField(default=None, null=True, blank=True)
    C48 = models.FloatField(default=None, null=True, blank=True)
    C49 = models.FloatField(default=None, null=True, blank=True)
    C = PickledObjectField(default="")
    P = PickledObjectField(default="")
    rho = models.FloatField(default=0.3)
    W1 = models.FloatField(default=0)
    W2 = models.FloatField(default=0.5)
    W3 = models.FloatField(default=0.25)
    W4 = models.FloatField(default=0.25)
    W = PickledObjectField(default="")
    Aoptimality_c = ((1,"A-optimality"),(2,"D-optimality"))
    Aoptimality = models.IntegerField(choices=Aoptimality_c,default=1)
    Saturation_c = ((1,"Saturation"),(2,"No Saturation"))
    Saturation = models.IntegerField(choices=Saturation_c,default=1)
    Optimisation_c = ((1,"Genetic Algorithm"),(2,"Simulations"))
    Optimisation = models.IntegerField(choices=Optimisation_c,default=1)
    resolution = models.FloatField(default=0.25)
    G = models.IntegerField(default=20)
    q = models.FloatField(default=0.01)
    I = models.IntegerField(default=4)
    cycles = models.IntegerField(default=100)
    preruncycles = models.IntegerField(default=10)
    ConfoundOrder = models.IntegerField(default=3)
    MaxRepeat = models.IntegerField(default=6,validators=[MinValueValidator(3)])
    HardProb = models.BooleanField(default=False)

    def __unicode__(self): # Python 3: __str__
        return "<DesignModel:%s>" %self.SID

    @classmethod
    def create(cls,SID):
        desdata = cls(SID=SID)
        return desdata
