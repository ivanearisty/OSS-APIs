from abc import ABC, abstractmethod
from typing import List, Optional

class Message(ABC):
    """
    Abstract representation of a chat message.
    Students must implement this to wrap their platform-specific message objects.
    """
    @property
    @abstractmethod
    def id(self) -> str:
        """Unique identifier for the message."""
        raise NotImplementedError

    @property
    @abstractmethod
    def content(self) -> str:
        """The actual text content of the message."""
        raise NotImplementedError

    @property
    @abstractmethod
    def sender_id(self) -> str:
        """The ID of the user who sent the message."""
        raise NotImplementedError

class ChatInterface(ABC):
    """
    A minimal interface for sending and receiving messages.
    """

    @abstractmethod
    def send_message(self, channel_id: str, content: str) -> bool:
        """
        Sends a message to a specific destination (channel/thread).
        Returns True if successful.
        """
        raise NotImplementedError

    @abstractmethod
    def get_messages(self, channel_id: str, limit: int = 10) -> List[Message]:
        """
        Reads the last N messages from a destination.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_message(self, channel_id: str, message_id: str) -> bool:
        """
        Deletes a specific message. Returns True if successful.
        """
        raise NotImplementedError