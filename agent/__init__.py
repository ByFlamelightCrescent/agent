"""Agent package initializer.

Exports the most commonly used symbols for convenient imports, e.g.:

    from agent import OpenAI_Agent
    from agent import freeflow_Agent

"""

from .openai_agent import OpenAI_Agent
from .freeflow_agent import FreeFlow_Agent

# Provide conventional CamelCase aliases for convenience
OpenAIAgent = OpenAI_Agent
FreeflowAgent = FreeFlow_Agent

__all__ = ["OpenAI_Agent", "freeflow_Agent", "OpenAIAgent", "FreeflowAgent"]

# Optional package version
__version__ = "0.1.0"
