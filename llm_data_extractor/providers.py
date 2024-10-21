from typing import Any
from anthropic import Anthropic
import google.generativeai as genai
from .api_calls import LLMDataExtractor


class Antropic(LLMDataExtractor):
  # TODO add count_input_tokens implementation
  def __init__(self,
               api_key: str,
               model_name: str="claude-3-5-sonnet-20240620",
               max_tokens: int = 2048,
               **client_kwargs: Any):
    super().__init__(model_name=model_name)
    self.client = Anthropic(api_key=api_key)
    self.max_tokens = max_tokens
    self.client_kwargs = client_kwargs

  def _call_api(self, prompt: str) -> str:
     return self.client.messages.create(
        model=self.model_name,
        max_tokens=self.max_tokens,
        messages=[{
            "role": 'user', "content":  prompt
        }],
        **self.client_kwargs
    )
  
  def call_api(self, prompt: str) -> str:
    return self._call_api(prompt).content[0].text


class Gemini(LLMDataExtractor):
  def __init__(self,
               api_key: str,
               model_name: str="gemini-1.5-flash",
               max_tokens: int = 2048,
               **client_kwargs: Any):
    super().__init__(model_name=model_name)
    genai.configure(api_key=api_key)
    self.client = genai.GenerativeModel(model_name)
    self.max_tokens = max_tokens # keep it for consistency
    self.generation_config = genai.types.GenerationConfig(
      max_output_tokens=max_tokens,
      # response_mime_type="application/json" # set to return json, see 
    )
    # TODO check out Gemini json schema, see https://ai.google.dev/gemini-api/docs/structured-output?lang=python
    # it allows to specify **exact** json output schema by predefining a typed-like class
    self.client_kwargs = client_kwargs

  def _call_api(self, prompt: str) -> str:
     # TODO store raw result in some field, return text in self.call_api 
     return self.client.generate_content(prompt, generation_config=self.generation_config)
  
  def call_api(self, prompt: str) -> str:
    return self._call_api(prompt).text
  
  def count_input_tokens(self, prompt: str) -> int:
    return self.client.count_tokens(prompt).total_tokens
  
  
class OpenAI(LLMDataExtractor):
  ...
