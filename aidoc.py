#!/usr/bin/env python3
#########################################
# Documentation Generation Script
###########################################

import os
import sys
import random
import requests 
import argparse
import json
import dotenv
import openai 
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
print (openai.api_key)

# Function to parse command line arguments for the project directory
def parse_args():
    parser = argparse.ArgumentParser(description="Documentation Generation Script")
    parser.add_argument('-p', '--projectdir', type=str, help="Project directory", required=True)
    return parser.parse_args()

# Function to generate documentation for a single file using OpenAI
def generate_documentation_for_file(file_path,prompt):
    """Generate Markdown documentation for a given file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()


    client = OpenAI(api_key=openai.api_key)
    
    # print("Prompt: " + prompt)
    completion = client.chat.completions.create(
      # model="gpt-3.5-turbo",
      model="gpt-4-1106-preview",
      messages=[
        {
          "role": "system", 
          "content": f"You are a skilled code analyst, an expert in reading code and generating documentaion that explains code in human understandable manner. You will explain the logic and structure of this code in Markdown format:\n\n{file_content}"
        },
        {"role": "user", "content": prompt},  
    ]
)
    
    documentation=completion.choices[0].message.content
    return documentation

# Function to save the generated documentation
def save_documentation(documentation, doc_path):
    """Save the generated documentation to a file."""
    os.makedirs(os.path.dirname(doc_path), exist_ok=True)
    with open(doc_path, 'w', encoding='utf-8') as doc_file:
        doc_file.write(documentation)

# Function to traverse the project directory and generate documentation
def generate_project_documentation(project_dir):
    documentation_root = os.path.join(project_dir, 'Documentation')
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.php') or file.endswith('.py'):  # Customize based on your file types
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, start=project_dir)
                doc_path = os.path.join(documentation_root, f"{relative_path}.md")
                prompt="Generate documentation for this file."
                print(f"Generating documentation for {file_path}")
                documentation = generate_documentation_for_file(file_path,prompt)
                save_documentation(documentation, doc_path)
                print(f"Documentation saved to {doc_path}")

# Main execution
def main():
    args = parse_args()
    if args.projectdir:
        print(f"Generating documentation for project at {args.projectdir}")
        generate_project_documentation(args.projectdir)

if __name__ == "__main__":
    main()
