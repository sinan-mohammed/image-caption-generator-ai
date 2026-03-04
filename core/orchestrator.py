from agents.market_agent import market_research_agent
from agents.competitor_agent import competitor_agent
from agents.monetization_agent import monetization_agent
from agents.risk_agent import risk_agent
from utils.logger import logger


def run_agents(idea):
    logger.info("Orchestrator started")

    try:
        market = market_research_agent(idea)
        competitors = competitor_agent(idea)
        monetization = monetization_agent(idea)
        risks = risk_agent(idea)

        logger.info("All agents executed successfully")

        return {
            "market": market,
            "competitors": competitors,
            "monetization": monetization,
            "risks": risks
        }

    except Exception as e:
        logger.error(f"Orchestrator failed: {str(e)}")
        return {}