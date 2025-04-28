import os
from dotenv import load_dotenv
from src.helper import call_openai

# Load environment variables from .env
load_dotenv()

# Directory containing prompts
PROMPT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'prompts'))


def get_folder_structure(base_path):
    folder_structure = {}

    for root, dirs, files in os.walk(base_path):
        # Ignore .venv and hidden folders
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '.venv']

        # Create a relative path
        rel_root = os.path.relpath(root, base_path)
        folder_structure[rel_root] = files

    output = ""
    for folder, files in folder_structure.items():
        output += f"{folder}/\n"
        for file in files:
            output += f"  └── {file}\n"
    return output


project_description_prompt = """
This project is to be a chatbot server. A frontend will send requests to this server and the server will process and return messages
This will be on AWS EC2 and use fastapi
"""

new_feature_prompt = """
    Edit to make it work
    1. what files do you want    
    """


fix_error_prompt = """
fix the error {error}
"""

feedback_prompt = """
does the code match the project and new feature description
"""

semantic_router = """
if
"""


def main():
    # Get the relative path from .env
    relative_repo_path = os.getenv("RELATIVE_REPO_PATH")
    if not relative_repo_path:
        raise ValueError("RELATIVE_REPO_PATH not set in your .env file")

    # Construct the absolute project path
    project_path = os.path.abspath(os.path.join(os.getcwd(), relative_repo_path))

    if not os.path.isdir(project_path):
        raise FileNotFoundError(f"Project path does not exist: {project_path}")

    print(f"Project Path: {project_path}")

    # Read project structure
    structure_text = get_folder_structure(project_path)
    print("\nProject Structure:\n")
    print(structure_text)

    # prompt = Folder structure + job +
    # call open ai



if __name__ == "__main__":
    main()
