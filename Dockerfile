FROM python:3.12.0a4-alpine3.17

# Install Chrome and ChromeDriver
RUN apk update && \
    apk add --no-cache chromium chromium-chromedriver tzdata && \
    rm -rf /var/cache/apk/*

# Install glibc compatibility for Alpine
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk && \
    apk add --force-overwrite glibc-2.30-r0.apk glibc-bin-2.30-r0.apk && \
    rm glibc-2.30-r0.apk glibc-bin-2.30-r0.apk


# Install Allure
RUN apk update && \
    apk add openjdk11-jre curl tar && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    [ ! -f /usr/bin/allure ] && ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure || true && \
    rm allure-2.13.8.tgz && \
    rm -rf /var/cache/apk/*

WORKDIR /usr/workspace

# Copy the dependencies file to the working directory
COPY ./requirements.txt /usr/workspace

# Install Python dependencies
RUN pip install -r requirements.txt
