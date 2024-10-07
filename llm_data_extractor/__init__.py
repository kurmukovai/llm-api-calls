import os
import json
from pathlib import Path

from .io import read_json, read_text
from .api_calls import LLMDataExtractor
from .providers import Antropic, OpenAI, Gemini

__version__ = "0.1.0"


# Get the directory of the current file
current_dir = Path(__file__).parent

# Read assets
prompt_template = read_text(current_dir / 'assets' / 'prompt.jnj')

#TODO think of better way

aorta_dir = current_dir / 'assets' / 'aorta'
aorta_segmentation_template = read_json(aorta_dir / 'segmentation_template.json')
aorta_segmentation_template_example = read_json(aorta_dir / 'segmentation_template_example.json')
aorta_normal_template = read_json(aorta_dir / 'normal_size_anatomy.json')
aorta_normal_template_example = read_json(aorta_dir / 'normal_size_anatomy_example.json')

# Make assets accessible when importing the package
__all__ = ['LLMDataExtractor', 'Antropic', 'OpenAI', 'Gemini', 'prompt_template',
		    'aorta_segmentation_template', 'aorta_segmentation_template_example', 'aorta_normal_template',
			'aorta_normal_template_example']