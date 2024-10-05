# LLM Data Extractor

LLM Data Extractor is a Python library for extracting structured data from various Language Model APIs.

## Installation

You can install the LLM Data Extractor using pip:

```
pip install llm_data_extractor
```

## Usage

Here's a quick example of how to use the LLM Data Extractor:

```python
from llm_data_extractor import Antropic

extractor = Antropic(api_key="your-api-key")
result = extractor.get_dict("Your prompt here")

if result["status"]:
    print(result["response"])
else:
    print("Failed to extract data")
```

## License

This project is licensed under the MIT License.