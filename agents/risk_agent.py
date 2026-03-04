from utils.helpers import ask_llm
from utils.logger import logger


def risk_agent(idea):
    logger.info("Risk Estimator Agent started")

    try:
        prompt = f"""
        You are a Startup Risk Analyst.
        Startup Idea: {idea}

        Identify:
        - Technical Risks
        - Market Risks
        - Regulatory Risks
        - Overall Risk Score (Low/Medium/High)
        - Go or No-Go Recommendation
        """

        result = ask_llm(prompt)

        logger.info("Risk Estimator Agent completed successfully")
        return result

    except Exception as e:
        logger.error(f"Risk Estimator Agent failed: {str(e)}")
        return "Risk assessment failed."