import logging

logging.basicConfig(
    level=logging.INFO,  # Must be logging.INFO (not logging.info)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("BriefAI")
