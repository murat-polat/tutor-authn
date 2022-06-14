FROM docker.io/node:16.14-bullseye-slim

LABEL MAINTAINER=MP
RUN apt-get update && apt-get -y upgrade

# Installing python packages with nano, vim and telnet
RUN apt update \
  && apt install -y git \
    # required for cwebp-bin
    gcc git libgl1 libxi6 make \
    # additionally required for gifsicle, mozjpeg, and optipng (on arm)
    autoconf libtool pkg-config zlib1g-dev \
    # additionally required for node-sass (on arm)
    python g++

RUN apt-get -y install python3-pip  git curl 
# RUN pip3 install mysqlclient

# Installing node and React dependencies
RUN apt-get -y install node-gyp nodejs npm && npm install npm@latest -g

# Making directory
RUN mkdir -p /openedx/authn
WORKDIR /openedx/authn
ENV PATH ./node_modules/.bin:${PATH}

# cloning the MFA repository
RUN git clone https://github.com/openedx/frontend-app-authn/ /openedx/authn

# Create environment file directories
#RUN mkdir -p /openedx/env/production /openedx/env/development
#COPY .env.development  /openedx/env/development
RUN rm -rf /openedx/authn/package-lock.json
COPY package.json /openedx/authn/package.json
COPY env.development /openedx/authn/.env.development
COPY env /openedx/authn/.env
RUN cd /openedx/authn
## Installing and building app
 
RUN npm i -D source-map-loader
RUN npm install
RUN  npm run  build 
## Installing Caddy ## 

RUN  apt install -y debian-keyring debian-archive-keyring apt-transport-https
RUN curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' |  gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
RUN curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' |  tee /etc/apt/sources.list.d/caddy-stable.list
RUN  apt update
RUN  apt install caddy

COPY ./Caddyfile /etc/caddy/Caddyfile

CMD ["npm", "start" ]

EXPOSE 1999/tcp
