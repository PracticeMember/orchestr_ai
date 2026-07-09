import logging

logging.basicConfig(
    filename="orchestrator.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s"
)