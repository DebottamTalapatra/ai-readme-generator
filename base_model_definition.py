from pydantic import BaseModel
from typing import List

class Readme_Fields_Generator(BaseModel):
    project_title : str
    project_description : str
    features : List[str]
    technical_requirements : List[str]
    tech_stack_overview: List[str]
    future_scope: List[str]
