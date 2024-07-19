FROM ubuntu:focal as runner

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://github.com/digitalocean/doctl/releases/download/v1.109.1/doctl-1.109.1-linux-amd64.tar.gz | tar -xzv
RUN mv doctl /usr/local/bin

# Verify the installation
RUN doctl version

COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]