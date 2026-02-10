from typing import List

def create_md(project_title:str, project_description:str, features:List[str], technical_requirements:List[str], tech_stack_overview:List[str], future_scope:List[str]):
    feature_list = ""
    for feature in features:
        feature_list += f"- {feature}\n"
        
    technical_requirements_list = ""
    for technical_req in technical_requirements:
        technical_requirements_list += f"- {technical_req}\n"
        
    tech_stack_list = ""
    for tech in tech_stack_overview:
        tech_stack_list += f"- {tech}\n"
        
    future_scope_list = ""
    for scopes in future_scope:
        future_scope_list += f"-{scopes}\n"
    
        
    md = f"""
# {project_title}

![demo_preview](image_name.png)

## Description

{project_description}

## Features

{feature_list}

## Installation

### Technical requirements

{technical_requirements_list}

### Steps

1. Clone the repository:

```
git clone https://github.com/YourUserName/repoName.git

cd <project_directory>
```

2. Compile the project:

```
INSERT COMPILATION COMMAND HERE 
```

3. Run the executable:

```
INSERT TEXT HERE 

```

## Technologies Used

{tech_stack_list}

## Future Enhancements

{future_scope_list}

## License

MIT License © <YOUR_NAME>
    """
    return md
