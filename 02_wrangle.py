"""
    nJGL 2026-10-26

    Raw data needs some data wrangling to be:
     - importable for R
     - compatable between the sources
    
    This handles SCB and SKR data and stores
"""

import conf
from src import cleaners
from src.logs import log
import tqdm



def main():
    """Main."""
    log.info('Cleaning data from SKR')
    cleaners.clean_skr_data()

    log.info('Cleaning data from SCB')
    cleaners.clean_scb_data()



if __name__ == "__main__":
    main()