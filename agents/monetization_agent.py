from utils.helpers import ask_llm
from utils.logger import logger


def monetization_agent(idea):
    logger.info("Monetization Agent started")

    try:
        prompt = f"""
        You are a SaaS Monetization Expert.
        Startup Idea: {idea}

        Provide:
        - Best revenue model
        - Suggested pricing tiers
        - Upsell strategy
        - 1-year revenue projection assumptions
        """

        result = ask_llm(prompt)

        logger.info("Monetization Agent completed successfully")
        return result

    except Exception as e:
        logger.error(f"Monetization Agent failed: {str(e)}")
        return "Monetization analysis failed."