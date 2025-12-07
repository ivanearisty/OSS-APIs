from abc import ABC, abstractmethod
from enum import StrEnum
from typing import List, Optional

class TicketStatus(StrEnum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

class Ticket(ABC):
    """
    Abstract representation of a Ticket.
    """
    @property
    @abstractmethod
    def id(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def title(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def status(self) -> TicketStatus:
        raise NotImplementedError

    @property
    @abstractmethod
    def assignee(self) -> Optional[str]:
        raise NotImplementedError

class TicketInterface(ABC):
    """
    The contract for Ticketing services.
    """

    @abstractmethod
    def create_ticket(self, title: str, description: str, assignee: Optional[str] = None) -> Ticket:
        raise NotImplementedError

    @abstractmethod
    def get_ticket(self, ticket_id: str) -> Optional[Ticket]:
        raise NotImplementedError

    @abstractmethod
    def search_tickets(self, query: Optional[str] = None, status: Optional[TicketStatus] = None) -> List[Ticket]:
        raise NotImplementedError

    @abstractmethod
    def update_ticket(
        self, 
        ticket_id: str, 
        status: Optional[TicketStatus] = None, 
        title: Optional[str] = None
    ) -> Ticket:
        raise NotImplementedError

    @abstractmethod
    def delete_ticket(self, ticket_id: str) -> bool:
        raise NotImplementedError