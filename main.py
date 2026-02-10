from ollama import chat
from pydantic import BaseModel
from base_model_definition import Readme_Fields_Generator
from system_prompt import SYSTEM_PROMPT
from readme_gen import create_md

user_input = input("Enter a short description of your project stating it's functionalities and tech stack:\n")

response = chat(
    model='phi3:mini',
    messages = [
        {
            'role':'system',
            'content': SYSTEM_PROMPT
        },
        {
            'role':'user',
            'content': user_input
        }
    ],
    format=Readme_Fields_Generator.model_json_schema(),
    options={
            "temperature": 0.2,
    }
)

"""project_title : str
    project_description : str
    features : List[str]
    technical_requirements : List[str]
    tech_stack_overview: List[str]
    future_scope: List[str] 
    """
model_response = Readme_Fields_Generator.model_validate_json(response.message.content)
raw_md = create_md(model_response.project_title, model_response.project_description, model_response.features, model_response.technical_requirements, model_response.tech_stack_overview, model_response.future_scope)



file_name = input("Your readme has been successfully created! Give it a name!:\n")
with open(file_name, "w", encoding="utf-8") as md_file:
    md_file.write(raw_md)

print(f"Markdown file '{file_name}' created successfully!")
