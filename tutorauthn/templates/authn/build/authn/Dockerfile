FROM debian

LABEL MAINTAINER=MP
RUN apt-get update && apt-get -y upgrade

# Installing python packages with nano, vim and telnet
RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential nano vim 

RUN apt-get -y install python3-pip  git curl 
# RUN pip3 install mysqlclient

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
RUN rm -rf /openedx/authn/package-lock.json
COPY package.json /openedx/authn/package.json
COPY env.development /openedx/authn/.env.development
COPY env /openedx/authn/.env
RUN cd /openedx/authn
## Installing and building app

RUN npm install && npm run build 
## Installing Caddy ## 

RUN apt install -y debian-keyring debian-archive-keyring apt-transport-https
RUN curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | apt-key add -
RUN curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' |  tee -a /etc/apt/sources.list.d/caddy-stable.list
RUN apt-get update
RUN apt-get install caddy

COPY ./Caddyfile /etc/caddy/Caddyfile

CMD ["npm", "start" ]

EXPOSE 1999/tcp











