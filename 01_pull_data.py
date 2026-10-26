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
    downloader.download('municipal_coalitions', 'xlsx')
    downloader.download('election_results', 'json')


if __name__ == "__main__":
    main()