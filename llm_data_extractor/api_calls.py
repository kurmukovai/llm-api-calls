import json
from collections import abc
from typing import Any
from abc import ABC, abstractmethod

class LLMDataExtractor(ABC):
    """
    Abstract base class for LLM data extraction.
    
    This class defines the interface for extracting structured data from LLM APIs.
    """

    def __init__(self, model_name: str):
        """
        Initialize the LLMDataExtractor.

        Args:
            model_name (str): The name of the LLM model to use.
        """
        self.model_name = model_name

    @abstractmethod
    def call_api(self, prompt: str) -> str:
        """
        Abstract method to call the LLM API.

        Args:
            prompt (str): The prompt to send to the LLM.

        Returns:
            str: The response from the LLM.
        """
        ...
    
    @abstractmethod
    def count_input_tokens(self, prompt: str) -> int:
        ...

    @staticmethod
    def decode_dict(text: str) -> dict[str, Any]:
        """
        Decode a JSON string into a dictionary.

        Args:
            text (str): The JSON string to decode.

        Returns:
            dict[str, Any]: The decoded dictionary.
        """
        return json.loads(text)

    def get_dict(self, prompt: str) -> dict[str, Any]:
        """
        Get a structured dictionary response from the LLM.

        Args:
            prompt (str): The prompt to send to the LLM.

        Returns:
            dict[str, Any]: A dictionary containing the status, context, and response.
        """
        response = self.call_api(prompt)
        context = [(prompt, response)]
        try:
            record = self.decode_dict(response)
            return {"status": True, "context": context, "response": record}
        except json.JSONDecodeError as exception:
            return {"status": False, "context": context, "response": None}