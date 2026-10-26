"""
    nJGL

    Raw data needs to be wrangeled a bit. This contains data-loaders for the files in `data/raw`


"""


import json
import conf
import pandas as pd
from src.logs import log
from pathlib import Path



def read_raw_json(pth_target: Path):
    """Read raw json."""
    with open(pth_target, encoding='utf-8') as f:
        raw = json.load(f)

    return raw



def clean_scb_data():
    """Produce `cleaned/election_results.csv` from raw downloaded data."""
    # Start with reading raw json.
    # the dimensions in `id` (Region x Parti x ContentsCode x Tid), last one varying fastest
    raw = read_raw_json(conf.PTH_RAW / 'election_results.json')

    # Follow the SCB database category quirks
    # Category codes per dimension, ordered by their position in the grid
    dims = raw['id']
    codes = [
        sorted(raw['dimension'][dim]['category']['index'], key=raw['dimension'][dim]['category']['index'].get)
        for dim in dims
    ]

    # The cartesian product of codes lines up one-to-one with the flat values
    idx = pd.MultiIndex.from_product(codes, names=dims)
    long = pd.Series(raw['value'], index=idx, name='seats').reset_index()
    # One row per municipality, one column per party
    df = long.pivot(index='Region', columns='Parti', values='seats').reset_index()

    # Same column names and order as `municipal_coalitions.csv` (FP is SCB's code for L)
    df = df.rename(columns={
        'Region': 'mun_code',
        'M': 'party_m',
        'C': 'party_c',
        'FP': 'party_l',
        'KD': 'party_kd',
        'S': 'party_s',
        'V': 'party_v',
        'MP': 'party_mp',
        'SD': 'party_sd',
        'ÖVRIGA': 'party_misc',
    })

    # Bring back the labels from the dimension where they were left behind
    df.insert(1, 'mun_label', df['mun_code'].map(raw['dimension']['Region']['category']['label']))
    # Re-order
    df = df[['mun_code','mun_label', 'party_m', 'party_c', 'party_l', 'party_kd', 'party_s', 'party_v', 'party_mp', 'party_sd', 'party_misc']]


    # Format the stuff that we have
    df['mun_code'] = df['mun_code'].astype(int)

    # How many seats are there in each municipal pairlament
    df['seats_total'] = df.loc[:, 'party_m':'party_misc'].sum(axis=1)

    # Raw database contains this wierd empty municipalitty
    anomalies = df.loc[df['seats_total'].eq(0), ]
    # It's the historical municipality of Bara (merged into Svedala 1976). Kill it:
    df = df[df['seats_total'].gt(0)].reset_index(drop=True)

    # We should have 290 municipalities!
    if len(df) != 290:
        log.warning(f'The downloaded data is probably corrupted. Sweden has 290 municipalities, not {len(df)}!')


    df.to_csv(conf.PTH_CLEANED / 'election_results.csv')





def clean_skr_data():
    """Produce `cleaned/municipal_coalitions.csv from raw downloaded data."""

    # Read data from raw excel format
    df = pd.read_excel(conf.PTH_RAW / 'municipal_coalitions.xlsx')

    # These are appropriate columns
    df.columns = [
        'mun_code',
        'mun_label',
        'party_m', 'party_c', 'party_l', 'party_kd', 'party_s', 'party_v', 'party_mp', 'party_sd', 'party_misc',
        'misc_parties',
        'compound_abrev',
        'kso_party',
        'kso_misc_name'
    ]

    # These columns cover party participation in gouverning coalition
    for col in df.columns[2:11]:
        # ... are set to 1 or 0 for coalition pressence
        df[col] = df[col].notna().astype(int)

    # Non-major parties are grouped inte `party_misc`
    n_non_major_coalition_parties = len(df.iloc[df['party_misc'].eq(1),])
    non_major_coalition_parties = sorted(df.loc[df['party_misc'].eq(1), 'misc_parties'].tolist())

    # Only these non-major parties hold KSO in municipalities
    # (Nora commun has an unconvensional rotation presidency (M and S))
    non_major_kso = df.loc[(~df['kso_misc_name'].isna()) & (~df['mun_label'].eq('Nora kommun')), 'kso_misc_name'].tolist()
    n_non_major_kso = len(non_major_kso)

    df['misc_parties'] = df['misc_parties'].fillna('')
    df['kso_misc_name'] = df['kso_misc_name'].fillna('')

    # The green party holds no KSO
    ksos = df['kso_party'].unique().tolist()

    df.to_csv(conf.PTH_CLEANED / 'municipal_coalitions.csv')