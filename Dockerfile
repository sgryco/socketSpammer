# from https://github.com/Ubiwhere/docker-py3-gdal
FROM ubiwhere/py3-gdal

RUN apt-get update &&\
    apt-get install -y net-tools &&\
    apt-get autoremove &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

# set python3 to default
RUN update-alternatives --install /usr/bin/python python\
 /usr/bin/python3.5 1

# install code and python requirements
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
