# Use Ubuntu 16.04 LTS
FROM ubuntu:xenial-20161213

# Pre-cache neurodebian key
COPY docker/neurodebian.gpg /root/.neurodebian.gpg

# Prepare environment
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
                    curl \
                    bzip2 \
                    ca-certificates \
                    xvfb \
                    build-essential \
                    autoconf \
                    libtool \
                    pkg-config

RUN curl -sSL http://neuro.debian.net/lists/xenial.us-ca.full >> /etc/apt/sources.list.d/neurodebian.sources.list && \
    apt-key add /root/.neurodebian.gpg && \
    (apt-key adv --refresh-keys --keyserver hkp://ha.pool.sks-keyservers.net 0xA5D32F012649A5A9 || true) && \
    apt-get update

ENV FSL_DIR=/usr/share/fsl/5.0 \
    OS=Linux \
    FS_OVERRIDE=0 \
    FIX_VERTEX_AREA= \
    FSF_OUTPUT_FORMAT=nii.gz

# Installing Neurodebian packages (FSL, AFNI, git)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
                    fsl-core=5.0.9-5~nd16.04+1 \
                    fsl-mni152-templates=5.0.7-2

ENV FSLDIR=/usr/share/fsl/5.0 \
    FSLOUTPUTTYPE=NIFTI_GZ \
    LD_LIBRARY_PATH=/usr/lib/fsl/5.0:$LD_LIBRARY_PATH
ENV PATH=/usr/lib/fsl/5.0:$PATH

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    apt-get install wget && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.7.12-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

ENV PATH /opt/conda/bin:$PATH

RUN conda config --add channels conda-forge

RUN conda install numpy=1.17.3 && \
    conda install scipy=1.3.1 && \
    conda install pandas=0.25.3 && \
    conda install matplotlib=3.1.2

ENV LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH

# Clear apt cache to reduce image size
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /code

WORKDIR /code
ADD requirements.txt /code/

RUN conda install sqlalchemy==1.3.11 \
    psycopg2==2.8.4 \
    mpld3==0.3 \
    scikit-learn==0.21.3 \
    cycler==0.10.0 \
    uwsgi==2.0.18 \
    jinja2==2.10.3 \
    boto3==1.10.19 \
    boto==2.49.0 \
    pdfrw==0.4 

RUN pip install -r requirements.txt
RUN pip install awscli --upgrade --user

# Clear apt cache to reduce image size
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/neuropower/neuropower-core.git
RUN rm -rf neuropower-core/build/lib/neuropower/
WORKDIR /code/neuropower-core
RUN which python
RUN python setup.py install

WORKDIR /code
ENV PATH=~/.local/bin:$PATH
# ENV PATH=/usr/lib/python3.7:$PATH
