from langchain_aws import ChatBedrock
import boto3

def get_bedrock_model():
    """
    Initialize and return an AWS Bedrock model instance.
    
    Returns:
        BedrockChat: Configured Bedrock model instance
    """
    # Initialize AWS Bedrock client
    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1"  # Replace with your desired region
    )

    # Initialize and return Bedrock model
    return ChatBedrock(
        client=bedrock_client,
        model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",  # Latest Claude 3 Sonnet model
        model_kwargs={
            "temperature": 0.1,
            "max_tokens": 20000
        }
    ) 
