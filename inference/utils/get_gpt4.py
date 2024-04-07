
from openai import AzureOpenAI
import os
api_base = os.getenv('API_BASE')
api_key= os.getenv('API_KEY')
deployment_name = os.getenv('DEPLOYMENT_NAME')
api_version = '2024-03-01-preview' # this might change in the future

client = AzureOpenAI(
    api_key=api_key,  
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}"
)


############################################################################
############# If use OpenAI API, use the following code ####################
############################################################################


# from openai import OpenAI

# api_version = 'gpt-4-1106-preview'
# client = OpenAI(
#     api_key=
# )

def gpt4(prompt):
    
    completion = client.chat.completions.create(
        model=api_version,
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    prompt = "How do you say hello in Spanish?"
    print(gpt4(prompt))
    
    