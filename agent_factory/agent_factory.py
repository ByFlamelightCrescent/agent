"""Agent factory that returns concrete agent implementations based on a type string.

Usage:
    from agent_factory import AgentFactory
    factory = AgentFactory("openai", logger)
    agent = factory.create()
"""
import os

from typing import Optional

# Import the concrete agent classes from the package
from agent import OpenAI_Agent, FreeFlow_Agent, Gemini_Agent


class AgentFactory:
    """Create agent instances by type.

    Supported types (case-insensitive): "openai", "freeflow".

    The factory takes a logger and optional api_var_name and name which are
    forwarded to the created agent instance.
    """

    def __init__(self, logger, name: Optional[str] = None) -> None:
        self.agent_type = (os.getenv("AGENT_TYPE") or "").strip().lower()
        self.logger = logger
        self.name = name
        self.available_agents = {
            "openai": OpenAI_Agent,
            "freeflow": FreeFlow_Agent,
            "gemini": Gemini_Agent,
        }

    def create(self):
        """Create and return an agent instance.

        Raises:
            ValueError: if an unknown agent_type is requested.
        """

        self.logger.info(f"Creating agent of type '{self.agent_type}'")
        agent = self.available_agents.get(self.agent_type)

        if not agent:
            raise ValueError(f"Unknown agent_type '{self.agent_type}'")

        return agent(logger=self.logger, name=self.name or "Agent")
