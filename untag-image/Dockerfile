FROM python:3.12 AS runner

RUN cd ~ &&\
    wget https://github.com/digitalocean/doctl/releases/download/v1.104.0/doctl-1.104.0-linux-amd64.tar.gz && \
    tar xf ~/doctl-1.104.0-linux-amd64.tar.gz && \
    mv ~/doctl /usr/local/bin

WORKDIR app/

COPY /untag-image/untag-image.py .
COPY /untag-image/entrypoint.sh .

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Define the default entry point
ENTRYPOINT ["./entrypoint.sh"]


