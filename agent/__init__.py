"""Agent package initializer.

Exports the most commonly used symbols for convenient imports, e.g.:

    from agent import OpenAI_Agent
    from agent import freeflow_Agent

"""

from agent.gemini_agent import Gemini_Agent
from .openai_agent import OpenAI_Agent
from .freeflow_agent import FreeFlow_Agent

# Provide conventional CamelCase aliases for convenience
OpenAIAgent = OpenAI_Agent
FreeflowAgent = FreeFlow_Agent
GeminiAgent = Gemini_Agent

__all__ = [ "FreeFlow_Agent", "OpenAI_Agent", "OpenAIAgent", "FreeflowAgent", "GeminiAgent", "Gemini_Agent"]

# Optional package version
__version__ = "0.1.0"
