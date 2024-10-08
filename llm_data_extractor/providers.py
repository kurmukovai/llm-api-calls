from typing import Any
from anthropic import Anthropic
from .api_calls import LLMDataExtractor


class Antropic(LLMDataExtractor):
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


class OpenAI(LLMDataExtractor):
  ...


class Gemini(LLMDataExtractor):
  ...
