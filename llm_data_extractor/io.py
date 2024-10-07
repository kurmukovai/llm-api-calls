import json
from pathlib import Path
from pypdf import PdfReader
from jinja2 import Template


def read_json(file_path: Path) -> str:
    with open(file_path, 'r') as file:
        return json.dumps(json.load(file))

def read_pdf(file_path: Path) -> str:
    reader = PdfReader(file_path)
    return ''.join(page.extract_text() for page in reader.pages)

def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def read_and_format_template(
    prompt_template: str,
    framework: str,
    example: str,
    text: str
) -> str:
    # Read the template file
    with open(prompt_template, 'r') as file:
        template_string = file.read()
    
    # Create a Jinja2 Template object
    template = Template(template_string)
    
    # Render the template with the provided parameters
    rendered_template: str = template.render(
        template=framework,
        example=example,
        text=text
    )
    
    return rendered_template