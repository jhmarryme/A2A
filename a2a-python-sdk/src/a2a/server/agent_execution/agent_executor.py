from abc import ABC, abstractmethod

from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue


class AgentExecutor(ABC):
    @abstractmethod
    async def execute(self, context: RequestContext, event_queue: EventQueue):
        pass

    @abstractmethod
    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        pass
