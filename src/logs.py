"""
    nJGL

    Logging umbrella. Importing sets up logging for the running script:

        from src.logs import log
        log.info('Nice run')

    The logger is named after the script being executed (for example `01_pull_data`).
    The logger writes to the console and to logs/<script>.log.
"""

import logging
import sys
from pathlib import Path

import conf


def _script_name() -> str:
    """Resolve the executing script."""
    main_file = getattr(sys.modules.get('__main__'), '__file__', None)
    log_file = Path(main_file).stem if main_file else 'interactive'
    
    # The script name is a string
    return log_file



def _setup_logging(name: str) -> logging.Logger:
    """Set up logging to file and the console; return adapted logger."""
    logger = logging.getLogger(name)
    
    # Importing again (or from several modules) can't add duplicate handlers
    if logger.handlers:
        return logger

    # Behaviour
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    conf.PTH_LOGS.mkdir(exist_ok=True)
    for handler in ( logging.FileHandler(conf.PTH_LOGS / f'{name}.log', mode='w'), logging.StreamHandler(), ):
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


log = _setup_logging(_script_name())
