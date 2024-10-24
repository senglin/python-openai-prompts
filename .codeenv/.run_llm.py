import sys
import os
from openai import AzureOpenAI

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))+'/..'

def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

def main():
    api_key = os.getenv('AZURE_OPENAI_API_KEY')
    
    if not api_key:
        print("API key not found", file=sys.stderr)
        return
    
    if len(sys.argv) == 3:
        prompt_filepath = sys.argv[1]
        system_filepath = sys.argv[2]
    else:
        prompt_filepath = PROJECT_ROOT+'/prompt.md'
        system_filepath = PROJECT_ROOT+'/system.md'

    if (not os.path.isfile(prompt_filepath)) or (not prompt_filepath.lower().endswith('.md')):
        print("File not in markdown format:", prompt_filepath, file=sys.stderr)
        return

    if (not os.path.isfile(system_filepath)) or (not system_filepath.lower().endswith('.md')):
        print("File not in markdown format:", system_filepath, file=sys.stderr)
        return

    prompt_content = read_file_content(prompt_filepath)
    system_content = read_file_content(system_filepath)

    client = AzureOpenAI(
        api_key=api_key,
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )
    
    messages = []
    
    if system_content is not None and system_content != '':
        messages.append({
            "role": "system",
            "content": system_content,
        })
        
    if prompt_content is not None and prompt_content != '':
        messages.append({
            "role": "user",
            "content": prompt_content,
        })
        
    if len(messages) == 0:
        print("Both system and prompt are empty", file=sys.stderr)
        return
    
    try:
        completion = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=messages,
            temperature=0.7,
            top_p=0.95,
            max_tokens=800
        )
        
        result = completion.choices[0].message.content
        print(result)
        
    except Exception as error:
        print("An error happend:", file=sys.stderr)
        print(error, file=sys.stderr)


if __name__ == "__main__":
    main()
