"""FreeFlow-specific agent implementation."""
from dotenv import load_dotenv
from freeflow_llm import FreeFlowClient
import os
import warnings
from typing import Optional


class FreeFlow_Agent:
    """Agent that uses the FreeFlow client.

    Parameters
    - logger: logging.Logger
    - api_var_name: name of the environment variable containing the API key
    - name: human-readable agent name
    """

    def __init__(self, logger, name: str = "FreeFlowAgent") -> None:
        self.logger = logger
        self.name = name
        self.api_var_name = "GROQ_API_KEY"
        self.api_key: Optional[str] = None
        self.client: Optional[FreeFlowClient] = None
        self.setup()

    def setup(self) -> Optional[str]:
        """Load .env and set up the FreeFlow client if an API key is present."""
        load_dotenv()
        api_key = os.environ.get(self.api_var_name)
        if api_key:
            self.logger.info(f"{self.api_var_name} found (value hidden)")
            self.api_key = api_key
            try:
                self.client = FreeFlowClient()
                self.client.API_KEY = api_key
            except Exception:
                self.logger.exception("Failed to create FreeFlow client")
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
            self.logger.warning("No FreeFlow client configured; returning placeholder response")
            return "No API key configured."

        try:
            response = self.client.chat(
            messages=[
                {"role": "user", "content": "Explain quantum computing in one sentence."}
            ]
        )
            
            return response

        except Exception as exc:
            self.logger.exception("FreeFlow API call failed")
            return f"API call failed: {exc}"
