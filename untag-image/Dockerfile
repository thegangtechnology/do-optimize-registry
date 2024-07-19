FROM python:3.12 AS runner

WORKDIR app/
COPY untag-image.py .
COPY entrypoint.sh .

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Define the default entry point
ENTRYPOINT ["./entrypoint.sh"]


