from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Union

class AIInterface(ABC):
    """
    The contract for AI services.
    Focuses on generating text or structured data based on inputs.
    """

    @abstractmethod
    def generate_response(
        self, 
        user_input: str, 
        system_prompt: str, 
        response_schema: Optional[Dict[str, Any]] = None
    ) -> Union[str, Dict[str, Any]]:
        """
        Generates a response from the AI.

        :param user_input: The text provided by the chat user.
        :param system_prompt: The instruction set (e.g., "You are a helpful assistant...").
        :param response_schema: An optional JSON schema (dict). 
                                If provided, the AI must return a structured Dict matching this schema.
                                If None, the AI returns a conversational String.
        
        :return: A string (conversation) or a Dict (structured action data).
        """
        raise NotImplementedError