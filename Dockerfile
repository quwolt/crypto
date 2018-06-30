FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN pip install git+https://github.com/ethereum/web3.py.git
RUN apt-get update && apt-get upgrade -y && apt-get install -y git-core curl build-essential openssl libssl-dev

RUN curl -sL https://deb.nodesource.com/setup_10.x |  bash -
RUN apt-get update



#RUN apt-get update
#RUN apt-get install -y npm
#RUN apt-get install -y curl
#RUN curl -sL https://deb.nodesource.com/setup_7.x | bash
#RUN apt-get install -y nodejs
#RUN npm install -y web3@0.20.2
#RUN npm install -g ganache-cli
#RUN npm install solc
#RUN pip install web3==3.16.5
#RUN pip install ipython
#RUN pip install websockets



RUN apt-get install -y nodejs
RUN apt-get install -y nodejs npm
RUN npm install -g solc

RUN npm init -y
RUN npm install -y web3@0.20.2
RUN npm install -g truffle
