# AmazonBedrock
# Getting Started with AI Models on AWS Bedrock - Team Guide
A beginner-friendly guide to using AI language models through AWS Bedrock.

## What You'll Learn
- How to set up your AWS credentials on your computer
- How to run your first conversation with AI models on Bedrock
- Understanding the basics without being a developer

##  What You'll Need
1. **Your AWS credentials** (provided by your admin)
   - Access Key ID (looks like: AKIAIOSFODNN7EXAMPLE)
   - Secret Access Key (looks like: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY)
2. **Python installed** - Version 3.8 or newer
3. **A text editor** - Notepad++, VS Code, or even regular Notepad
4. **A convenience script** - We've included `config.sh` in the repo to make credential setup easier 

## Step 1: Set Up Your AWS Credentials

### Option A: Using the Convenience Script (Recommended)
We've included a helpful script to make this easier:

1. Open the `config.sh` file in your text editor
2. Add your AWS credentials to the file (replace the placeholder values)
3. **IMPORTANT**: DO NOT share this file or commit it to public repos!
4. Make the script executable:
```bash
chmod +x ./config.sh
```
5. Run the script:
```bash
. ./config.sh
```

### Option B: Manual Setup

#### For Mac/Linux Users
1. Open Terminal
2. Type these commands one at a time (replace with YOUR actual keys):
```bash
export AWS_ACCESS_KEY_ID="paste-your-access-key-here"
export AWS_SECRET_ACCESS_KEY="paste-your-secret-key-here"
export AWS_DEFAULT_REGION="us-west-2"
```
**Important**: These settings only last for your current terminal session. When you close Terminal, you'll need to run them again.

#### For Windows Users
1. Open Command Prompt (press Windows key, type "cmd", press Enter)
2. Type these commands one at a time (replace with YOUR actual keys):
```cmd
set AWS_ACCESS_KEY_ID=paste-your-access-key-here
set AWS_SECRET_ACCESS_KEY=paste-your-secret-key-here
set AWS_DEFAULT_REGION=us-west-2
```
**Important**: These settings only last for your current Command Prompt session. When you close it, you'll need to run them again.

## Step 2: Install Required Software
In the same Terminal or Command Prompt window, run:
```bash
pip install boto3
```

## Step 3: Run Your Bedrock Chat Script
```bash
python bedrock_chat.py
```

## What Success Looks Like
If everything is working, you'll see:
```
Connecting to AWS Bedrock...
✓ Connected to AWS successfully!
Welcome to AI Model Chat!
Type your messages and press Enter to send.
Type 'quit', 'exit', or 'bye' to end the conversation.

You: What is artificial intelligence? Explain in simple terms.
AI is thinking...
AI: [The AI's response will appear here]
```

## Common Issues and Fixes
### "Could not connect to AWS. Check your credentials."
- Make sure you set the credentials in the SAME terminal window
- Check for typos in your access keys
- Try copying and pasting instead of typing

### "AccessDeniedException"
- Your AWS account doesn't have permission to use Bedrock models
- Contact your administrator to enable Bedrock access

### "No module named 'boto3'"
- The installation didn't work
- Try: `python -m pip install boto3`

### Nothing happens / Can't find Python
- Make sure Python is installed
- Try `python3` instead of `python`
- On Windows, you might need to use the full path: `C:\Python39\python.exe`

## Available Models
Your administrator will configure which models are available to your team. Common options include:
- Amazon Nova Pro
- Amazon Nova Lite
- Claude Sonnet 3.5
- Other AI models as they become available

Contact your admin if you need access to specific models or have questions about which one to use for your project.
