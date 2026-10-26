"""
    nJGL 2026-10-26

    Pull raw data from
     - Swedish municipalities and Regions
     - Official Swedish election results
"""

import conf
from src import downloader
from src.logs import log
import tqdm



def main():
    """Main."""
    log.info('Downloading raw data…')
    downloader.get_skr_data()
    downloader.get_election_data()



if __name__ == "__main__":
    main()