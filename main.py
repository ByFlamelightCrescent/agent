import logging
from agent_factory import AgentFactory

def configure_logging(name: str = "agent") -> logging.Logger:
    """Create and return a configured logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        fmt = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s", "%Y-%m-%d %H:%M:%S")
        handler.setFormatter(fmt)
        logger.addHandler(handler)

    return logger


def main():
    logger = configure_logging("agent_main")

    factory = AgentFactory("freeflow", logger=logger, api_var_name="GROQ_API_KEY", name="MyAgent")
    my_agent = factory.create()

    response = my_agent.get_response()
    print("Agent Response:", response)



if __name__ == "__main__":
    main()