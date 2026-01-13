"""Agent factory that returns concrete agent implementations based on a type string.

Usage:
    from agent_factory import AgentFactory
    factory = AgentFactory("openai", logger)
    agent = factory.create()
"""
from typing import Optional

# Import the concrete agent classes from the package
from agent import OpenAI_Agent, FreeFlow_Agent


class AgentFactory:
    """Create agent instances by type.

    Supported types (case-insensitive): "openai", "freeflow".

    The factory takes a logger and optional api_var_name and name which are
    forwarded to the created agent instance.
    """

    def __init__(self, agent_type: str, logger, api_var_name: str = "OPENAI_API_KEY", name: Optional[str] = None) -> None:
        self.agent_type = (agent_type or "").strip().lower()
        self.logger = logger
        self.api_var_name = api_var_name
        self.name = name

    def create(self):
        """Create and return an agent instance.

        Raises:
            ValueError: if an unknown agent_type is requested.
        """
        if self.agent_type in ("openai", "openai_agent"):
            return OpenAI_Agent(logger=self.logger, api_var_name=self.api_var_name, name=self.name or "OpenAIAgent")

        if self.agent_type in ("freeflow", "freeflow_agent"):
            return FreeFlow_Agent(logger=self.logger, api_var_name=self.api_var_name, name=self.name or "FreeflowAgent")

        raise ValueError(f"Unknown agent type: {self.agent_type!r}")
