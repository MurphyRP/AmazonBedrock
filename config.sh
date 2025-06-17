#!/bin/bash

# Export AWS credentials as environment variables
export AWS_ACCESS_KEY_ID="your_access_key_here"
export AWS_SECRET_ACCESS_KEY="your_secret_key_here"
export AWS_DEFAULT_REGION="us-east-1"

# Optional: Set session token if using temporary credentials
# export AWS_SESSION_TOKEN="your_session_token_here"
# make file executable with chmod +x ./config.sh
# run with ./config.sh

echo "AWS environment variables set"
