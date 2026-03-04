from core.search_tool import google_search
from utils.helpers import ask_llm
from utils.logger import logger


def market_research_agent(idea):
    logger.info("Market Research Agent started")

    try:
        search_data = google_search(f"{idea} market size trends TAM SAM SOM")

        prompt = f"""
        You are a Market Research Expert.
        Startup Idea: {idea}
        Market Data: {search_data}

        Provide:
        - TAM
        - SAM
        - SOM
        - Growth Rate
        - Target Audience
        """

        result = ask_llm(prompt)

        logger.info("Market Research Agent completed successfully")
        return result

    except Exception as e:
        logger.error(f"Market Research Agent failed: {str(e)}")
        return "Market research failed."