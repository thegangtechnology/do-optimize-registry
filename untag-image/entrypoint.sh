#!/bin/sh

# Exit on any error
set -e

# Check if the required environment variables are set
if [ -z "$DO_TOKEN" ]; then
  echo "DO_TOKEN environment variable is required."
  exit 1
fi

# Authenticate with DigitalOcean
echo "Authenticating with DigitalOcean..."
doctl auth init -t "$DO_TOKEN" || { echo "Authentication failed"; exit 1; }

# Create list of image that will be untagged
echo "Create untagged list..."
doctl registry repository lm "$REGISTRY_NAME" --format Digest,Tags,UpdatedAt  | grep '\[sha[-0-9a-z]*\]' > tag-list.txt
awk '{print $1, $2, $3}' tag-list.txt > normalize-list.txt
cat normalize-list.txt

# Run the Python script with any arguments passed to the container
echo "Executing Python script..."
exec python3 untag-image.py --repo $REGISTRY_NAME "$@"