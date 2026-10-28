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


def make_dirs():
    """Create every PTH_* directory defined in conf."""
    for name in dir(conf):
        if name.startswith('PTH_'):
            pth = getattr(conf, name)
            pth.mkdir(parents=True, exist_ok=True)
            log.info(f'Ensured {name}: {pth}')


def main():
    """Main."""
    make_dirs()
    log.info('Downloading raw data…')
    downloader.download('municipal_coalitions', 'xlsx')
    downloader.download('election_results', 'json')


if __name__ == "__main__":
    main()