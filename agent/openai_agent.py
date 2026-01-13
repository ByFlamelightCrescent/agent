"""OpenAI-specific agent implementation."""
from dotenv import load_dotenv
from openai import OpenAI
import os
import warnings
from typing import Optional


class OpenAI_Agent:
    """Agent that uses the OpenAI client.

    Parameters
    - logger: logging.Logger
    - api_var_name: name of the environment variable containing the API key
    - name: human-readable agent name
    """

    def __init__(self, logger, api_var_name: str = "OPENAI_API_KEY", name: str = "OpenAIAgent") -> None:
        self.logger = logger
        self.name = name
        self.api_var_name = api_var_name
        self.api_key: Optional[str] = None
        self.client: Optional[OpenAI] = None
        self.setup()

    def setup(self) -> Optional[str]:
        """Load .env and set up the OpenAI client if an API key is present."""
        load_dotenv()
        api_key = os.environ.get(self.api_var_name)
        if api_key:
            self.logger.info(f"{self.api_var_name} found (value hidden)")
            self.api_key = api_key
            try:
                self.client = OpenAI(api_key=api_key)
            except Exception:
                self.logger.exception("Failed to create OpenAI client")
                self.client = None
        elif api_key == "":
            # Key present but empty
            self.logger.warning(f"{self.api_var_name} is present in .env but empty")
            self.api_key = None
        else:
            self.logger.warning(f"{self.api_var_name} not set; proceeding without an API key")
            self.api_key = None

        return self.api_key

    def get_response(self, prompt: str = "How do I check if a Python object is an instance of a class?") -> str:
        """Get a response from the configured model or return a placeholder message.

        This method intentionally keeps the call simple and defensive so it works
        even when an API key is absent or the API client call fails.
        """
        if not self.client:
            self.logger.warning("No OpenAI client configured; returning placeholder response")
            return "No API key configured."

        try:
            response = self.client.responses.create(
                model="gpt-4o",
                instructions="You are a coding assistant that talks like a pirate.",
                input=prompt,
            )

            # Try a few common response shapes
            if hasattr(response, "output_text"):
                return response.output_text

            try:
                # Newer SDKs may return nested objects
                return response.output[0].content[0].text
            except Exception:
                return str(response)

        except Exception as exc:
            self.logger.exception("OpenAI API call failed")
            return f"API call failed: {exc}"
