#!/usr/bin/env python3
"""
Simple Claude Sonnet 3.5 Chat Application
==========================================
This is a beginner-friendly application to chat with Claude Sonnet 3.5 on AWS Bedrock.
It includes lots of comments to explain what each part does!

Before running this:
1. Set your AWS credentials in your terminal (see README)
2. Install boto3: pip install boto3
3. Run this file: python simple_claude_chat.py
"""

# Import the libraries we need
import boto3  # This is Amazon's library for talking to AWS services
import json   # This helps us work with JSON data
import sys    # This helps us exit the program cleanly
import os

client = boto3.client(
    service_name="bedrock-runtime",
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

# =============================================================================
# CONFIGURATION SECTION - Settings you might want to change
# =============================================================================

# The AWS region where Bedrock is available
# us-west-2 is Oregon, which usually has the latest models
AWS_REGION = "us-east-1"

# The exact name of the Claude Sonnet 3.5 model we want to use
# This is like choosing which AI assistant to talk to
#MODEL_ID = "anthropic.claude-3-5-sonnet-20240620-v1:0"
MODEL_ID ="anthropic.claude-3-haiku-20240307-v1:0"

# Temperature controls how creative the AI is
# 0.0 = Very predictable, always gives similar answers
# 1.0 = Very creative, might give wild answers
# 0.7 = A nice balance for most conversations
TEMPERATURE = 0.7

# Maximum number of tokens (words) the AI can respond with
# 1 token ≈ 0.75 words, so 512 tokens ≈ 380 words
MAX_RESPONSE_TOKENS = 512

# =============================================================================
# SETUP SECTION - Connect to AWS Bedrock
# =============================================================================

def create_bedrock_connection():
    """
    This function creates our connection to AWS Bedrock.
    Think of it like dialing a phone number to reach the AI.
    """
    print("Connecting to AWS Bedrock...")
    
    try:
        # Create the connection using your AWS credentials
        # boto3 automatically looks for the credentials you set in your terminal
        client = boto3.client(
            service_name="bedrock-runtime",  # We want the runtime service (for chatting)
            region_name=AWS_REGION           # The region we specified above
        )
        print("SUCCESS: Connected to AWS Bedrock!")
        return client
        
    except Exception as error:
        # If something goes wrong, print a helpful message
        print("ERROR: Could not connect to AWS Bedrock")
        print(f"Error details: {error}")
        print("\nTroubleshooting tips:")
        print("1. Did you set your AWS credentials? (AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY)")
        print("2. Are you connected to the internet?")
        print("3. Are your credentials correct?")
        # Exit the program since we can't continue without a connection
        sys.exit(1)

# =============================================================================
# CHAT SECTION - Functions to talk to Claude Sonnet 3.5
# =============================================================================

def send_message_to_claude(bedrock_client, user_message):
    """
    This function sends your message to Claude Sonnet 3.5 and gets the response.
    
    Parameters:
    - bedrock_client: Our connection to AWS Bedrock
    - user_message: What you want to say to the AI
    
    Returns:
    - The AI's response as text
    """
    
    try:
        # Prepare the message in the format Bedrock expects
        # It's like filling out a form with specific fields
        request = {
            "modelId": MODEL_ID,  # Which AI model to use
            "messages": [         # List of messages in the conversation
                {
                    "role": "user",  # Who's speaking (user = you)
                    "content": [     # What you're saying
                        {
                            "text": user_message  # Your actual message
                        }
                    ]
                }
            ],
            "inferenceConfig": {  # Settings for how the AI should respond
                "temperature": TEMPERATURE,        # How creative to be
                "maxTokens": MAX_RESPONSE_TOKENS, # Maximum response length
                "topP": 0.9,                      # Another creativity setting
            }
        }
        
        # Send the message and wait for a response
        # This is like hitting "send" on a text message
        response = bedrock_client.converse(**request)
        
        # Extract the AI's message from the response
        # The response has lots of data, but we just want the text
        ai_message = response["output"]["message"]["content"][0]["text"]
        
        # Also get some statistics about the response
        usage = response.get("usage", {})
        input_tokens = usage.get("inputTokens", 0)
        output_tokens = usage.get("outputTokens", 0)
        
        # Print token usage (helpful for understanding costs)
        print(f"\n[Token Usage] Input: {input_tokens}, Output: {output_tokens}")
        
        return ai_message
        
    except Exception as error:
        # If something goes wrong, return an error message
        print(f"ERROR: Error getting response: {error}")
        
        # Check for specific types of errors
        if "AccessDeniedException" in str(error):
            return "Your AWS account doesn't have permission to use this model. Contact your administrator."
        elif "ThrottlingException" in str(error):
            return "Too many requests. Please wait a moment and try again."
        else:
            return f"Something went wrong: {error}"

# =============================================================================
# MAIN PROGRAM - The chat loop
# =============================================================================

def main():
    """
    This is the main function that runs our chat program.
    It's like the conductor of an orchestra, coordinating everything.
    """
    
    # Print a welcome message
    print("=" * 60)
    print("Welcome to Claude Sonnet 3.5 Chat!")
    print("=" * 60)
    print("Type your messages and press Enter to send.")
    print("Type 'quit', 'exit', or 'bye' to end the conversation.")
    print("Type 'help' for tips on what to ask.")
    print("=" * 60)
    
    # Create our connection to Bedrock
    bedrock = create_bedrock_connection()
    
    # Start the conversation loop
    # This keeps running until you choose to quit
    while True:
        # Get input from the user
        # The \n adds a blank line for better readability
        user_input = input("\nYou: ").strip()
        
        # Check if the user wants to quit
        if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
            print("\nThanks for chatting! Goodbye!")
            break
        
        # Check if the user wants help
        if user_input.lower() == 'help':
            print("\nHere are some things you can try:")
            print("- Ask questions: 'What is machine learning?'")
            print("- Request explanations: 'Explain quantum computing like I'm 5'")
            print("- Get creative: 'Write a haiku about databases'")
            print("- Solve problems: 'How do I make chocolate chip cookies?'")
            print("- Analyze text: 'What's the sentiment of this review: ...'")
            continue  # Go back to the start of the loop
        
        # Check if the user actually typed something
        if not user_input:
            print("Please type a message!")
            continue
        
        # Show a thinking indicator
        print("\nClaude is thinking...")
        
        # Send the message and get the response
        response = send_message_to_claude(bedrock, user_input)
        
        # Display the response
        print(f"\nClaude: {response}")
        
        # Add a separator line for clarity
        print("-" * 60)

# =============================================================================
# PROGRAM ENTRY POINT
# =============================================================================

# This is Python's way of saying "if someone runs this file directly, do this:"
if __name__ == "__main__":
    try:
        # Run the main program
        main()
    except KeyboardInterrupt:
        # This catches when someone presses Ctrl+C to quit
        print("\n\nChat interrupted. Goodbye!")
    except Exception as error:
        # This catches any other unexpected errors
        print(f"\nERROR: Unexpected error: {error}")
        print("Please try again or contact support.")
