from core.search_tool import google_search
from utils.helpers import ask_llm
from utils.logger import logger


def competitor_agent(idea):
    logger.info("Competitor Agent started")

    try:
        search_data = google_search(f"{idea} competitors pricing features")

        prompt = f"""
        You are a Competitive Analyst.
        Startup Idea: {idea}
        Data: {search_data}

        Provide:
        - Top 5 competitors
        - Pricing models
        - Feature comparison table with specific details (use ✓ for available features, ✗ for unavailable, and specific pricing/info where applicable)
        
        IMPORTANT: Fill every cell in the feature comparison table with actual information. Do not leave any cells empty.
        """

        result = ask_llm(prompt)

        logger.info("Competitor Agent completed successfully")
        return result

    except Exception as e:
        logger.error(f"Competitor Agent failed: {str(e)}")
        return "Competitor analysis failed."