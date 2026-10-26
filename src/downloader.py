"""
    nJGL 2026-10-26

"""

from pathlib import Path
from urllib.parse import quote
from urllib.request import urlopen
from src.logs import log

import conf




def download(name, ext):
    """Download a conf-defined data-source And store with `ext`."""
    url = quote(conf.RAW_DATA_SOURCES[name], safe=':/?&=,[]')
    pth_target = conf.PTH_RAW / f'{name}.{ext}'
    log.info(f'Downloading to {name}…')
    
    with urlopen(url) as r:
        pth_target.write_bytes(r.read())
    
    # Return path to target file
    return pth_target

