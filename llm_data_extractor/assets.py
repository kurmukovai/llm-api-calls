from pathlib import Path
from .io import read_json, read_text

# Get the directory of the current file
ASSETS_DIR = Path(__file__).parent.parent / 'assets'

# Read assets
prompt_template = read_text(ASSETS_DIR / 'prompt.j2')

#TODO think of better way

aorta_dir = ASSETS_DIR / 'aorta'
aorta_segmentation_template = read_json(aorta_dir / 'segmentation_template.json')
aorta_segmentation_template_example = read_json(aorta_dir / 'segmentation_template_example.json')
aorta_normal_template = read_json(aorta_dir / 'normal_size_anatomy.json')
aorta_normal_template_example = read_json(aorta_dir / 'normal_size_anatomy_example.json')