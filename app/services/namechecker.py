import logging

logger = logging.getLogger(__name__)
IMIONA = ["kasia", "basia", "ela", "marcelina", "martyna"]

def checkname(name: str) -> bool:
    logger.debug(f"Sprawdzam imię: {name}")
    return name.lower() in IMIONA