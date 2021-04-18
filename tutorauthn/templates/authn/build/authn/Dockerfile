FROM debian

LABEL MAINTAINER=MP
RUN apt-get update && apt-get -y upgrade

# Installing python packages with nano, vim and telnet
RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential nano vim telnet

RUN apt-get -y install python3-pip  git curl 
RUN pip3 install mysqlclient

# Installing node and React dependencies
RUN apt-get -y install node-gyp nodejs npm && npm install npm@latest -g

# Making directory
RUN mkdir -p /openedx/authn
WORKDIR /openedx/authn

# cloning the MFA repository
RUN git clone https://github.com/edx/frontend-app-authn/ /openedx/authn

# Create environment file directories
#RUN mkdir -p /openedx/env/production /openedx/env/development
#COPY .env.development  /openedx/env/development
COPY package.json /openedx/authn/package.json
COPY env.development /openedx/authn/.env.development
COPY env /openedx/authn/.env
RUN cd /openedx/authn
## Installing and building app
RUN npm install && npm run build 


CMD ["npm", "start" ]










