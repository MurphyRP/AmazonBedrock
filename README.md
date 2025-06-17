# AmazonBedrock

# Getting Started with Llama 4 on AWS Bedrock - Team Guide

A beginner-friendly guide to using Meta's Llama 4 Maverick model through AWS Bedrock.

## 🎯 What You'll Learn

- How to set up your AWS credentials on your computer
- How to run your first conversation with Llama 4
- Understanding the basics without being a developer

## 📋 What You'll Need

1. **Your AWS credentials** (provided by your admin)
   - Access Key ID (looks like: AKIAIOSFODNN7EXAMPLE)
   - Secret Access Key (looks like: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY)
2. **Python installed** - Version 3.8 or newer
3. **A text editor** - Notepad++, VS Code, or even regular Notepad

## 🚀 Step 1: Set Up Your AWS Credentials

### For Mac/Linux Users

1. Open Terminal
2. Type these commands one at a time (replace with YOUR actual keys):

```bash
export AWS_ACCESS_KEY_ID="paste-your-access-key-here"
export AWS_SECRET_ACCESS_KEY="paste-your-secret-key-here"
export AWS_DEFAULT_REGION="us-west-2"
```

**Important**: These settings only last for your current terminal session. When you close Terminal, you'll need to run them again.

### For Windows Users

1. Open Command Prompt (press Windows key, type "cmd", press Enter)
2. Type these commands one at a time (replace with YOUR actual keys):

```cmd
set AWS_ACCESS_KEY_ID=paste-your-access-key-here
set AWS_SECRET_ACCESS_KEY=paste-your-secret-key-here
set AWS_DEFAULT_REGION=us-west-2
```

**Important**: These settings only last for your current Command Prompt session. When you close it, you'll need to run them again.

## 📦 Step 2: Install Required Software

In the same Terminal or Command Prompt window, run:

```bash
pip install boto3
```

This installs the AWS software library for Python. You should see some download progress.

## 🎬 Step 3: Test Your Connection

1. Create a new file called `test_llama4.py`
2. Copy this entire code block into it:

```python
import boto3
import json

print("Connecting to AWS Bedrock...")

# Create a connection to Bedrock
try:
    bedrock = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-west-2"
    )
    print("✓ Connected to AWS successfully!")
except Exception as e:
    print("✗ Could not connect to AWS. Check your credentials.")
    print(f"Error: {e}")
    exit()

# The model we want to use
MODEL_ID = "us.meta.llama4-maverick-17b-instruct-v1:0"

# Your question
question = "What is artificial intelligence? Explain in simple terms."

print(f"\nAsking Llama 4: {question}")
print("Waiting for response...")

try:
    # Send the question to Llama 4
    response = bedrock.converse(
        modelId=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [{"text": question}]
            }
        ]
    )
    
    # Get the answer
    answer = response["output"]["message"]["content"][0]["text"]
    print(f"\nLlama 4's Answer:\n{answer}")
    
except Exception as e:
    print(f"\n✗ Could not get response from Llama 4")
    print(f"Error: {e}")
    
    if "AccessDeniedException" in str(e):
        print("\nThis means your account doesn't have access to Llama 4.")
        print("Please contact your AWS administrator.")
    elif "ResourceNotFoundException" in str(e):
        print("\nThe model might not be available in your region.")
        print("Please contact your AWS administrator.")
```

3. Save the file
4. In your terminal/command prompt (where you set the credentials), navigate to where you saved the file:
   - Windows: `cd C:\Users\YourName\Desktop` (or wherever you saved it)
   - Mac/Linux: `cd ~/Desktop` (or wherever you saved it)

5. Run the test:
```bash
python test_llama4.py
```

## What Success Looks Like

If everything is working, you'll see:
```
Connecting to AWS Bedrock...
✓ Connected to AWS successfully!

Asking Llama 4: What is artificial intelligence? Explain in simple terms.
Waiting for response...

Llama 4's Answer:
[The AI's response will appear here]
```

## Common Issues and Fixes

### "Could not connect to AWS. Check your credentials."
- Make sure you set the credentials in the SAME terminal window
- Check for typos in your access keys
- Try copying and pasting instead of typing

### "AccessDeniedException"
- Your AWS account doesn't have permission to use Llama 4
- Contact your administrator to enable Bedrock access

### "No module named 'boto3'"
- The installation didn't work
- Try: `python -m pip install boto3`

### Nothing happens / Can't find Python
- Make sure Python is installed
- Try `python3` instead of `python`
- On Windows, you might need to use the full path: `C:\Python39\python.exe`

##  Next Steps

Once the test works, create a new file `chat_with_llama.py`:

```python
import boto3

# Set up connection
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-west-2"
)

MODEL_ID = "us.meta.llama4-maverick-17b-instruct-v1:0"

# Keep chatting until user types 'quit'
print("Chat with Llama 4! Type 'quit' to exit.\n")

while True:
    # Get user input
