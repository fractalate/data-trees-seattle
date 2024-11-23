import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, TypedDict

import time


TIME_ACTIONS = {} # action -> start time

def timestart(action):
    global TIME_ACTIONS
    TIME_ACTIONS[action] = time.time()
    depth = len(TIME_ACTIONS) - 1
    depth_string = '  ' * depth
    print(f'{depth_string}{action} - starting...')

def timeend(action):
    global TIME_ACTIONS
    depth = len(TIME_ACTIONS) - 1
    depth_string = '  ' * depth
    t0 = TIME_ACTIONS.pop(action)
    t1 = time.time()
    print(f'{depth_string}{action} - done - {t1-t0:.2f}')


timestart('LOADING')

# =====================================================================================================================
# Load Breeding Scientific Names Dataset
# =====================================================================================================================

timestart('dfbreedname load')
dfbreedname_raw = pd.read_csv('breeding_scientific_name.csv', sep='|')
dfbreedname = dfbreedname_raw
timeend('dfbreedname load')


# =====================================================================================================================
# Load SDOT Dataset
# =====================================================================================================================

timestart('dfsdot load')
dfsdot_raw = pd.read_csv('data/sdot_trees/SDOT_Trees_CDL_20241119.csv', dtype={
    'CONDITION': 'string',
    'CONDITION_ASSESSMENT_DATE': 'string',
    'ASBUILTPLANNO': 'string',
})
timeend('dfsdot load')

timestart('dfsdot load (fillna)')
# to squelch warnings about the data
dfsdot_raw['CONDITION'] = dfsdot_raw['CONDITION'].fillna('')
dfsdot_raw['CONDITION_ASSESSMENT_DATE'] = dfsdot_raw['CONDITION_ASSESSMENT_DATE'].fillna('')
dfsdot_raw['ASBUILTPLANNO'] = dfsdot_raw['ASBUILTPLANNO'].fillna('')
timeend('dfsdot load (fillna)')

# ---------------------------------------------------------------------------------------------------------------------
# Sanitizing SDOT Dataset
# ---------------------------------------------------------------------------------------------------------------------

# life's better without NaN in these columns
timestart('dfsdot sanitize')
dfsdot_raw['SCIENTIFIC_NAME'] = dfsdot_raw['SCIENTIFIC_NAME'].fillna('')
dfsdot_raw['COMMON_NAME'] = dfsdot_raw['COMMON_NAME'].fillna('')
timeend('dfsdot sanitize')

# ---------------------------------------------------------------------------------------------------------------------
# Supplementing SDOT Dataset
# ---------------------------------------------------------------------------------------------------------------------

timestart('sdot supplement')

dfsdot = dfsdot_raw

timestart('sdot breeding scientific name')
dfsdot = pd.merge(dfsdot, dfbreedname[['scientific_name', 'breeding_scientific_name']], left_on='SCIENTIFIC_NAME', right_on='scientific_name', how='left')
dfsdot = dfsdot.rename(
    columns={
        'breeding_scientific_name': 'BREEDING_SCIENTIFIC_NAME',
    },
)
dfsdot['BREEDING_SCIENTIFIC_NAME'] = dfsdot['BREEDING_SCIENTIFIC_NAME'].fillna(dfsdot['SCIENTIFIC_NAME'])
timeend('sdot breeding scientific name')

timeend('sdot supplement')


# =====================================================================================================================
# Load WCVP Datasets
# =====================================================================================================================

timestart('dfdist load')
dfdist_raw = pd.read_csv('data/wcvp_dwca/v13/wcvp_distribution.csv', sep='|')
timeend('dfdist load')

timestart('dftaxon load')
dftaxon_raw = pd.read_csv('data/wcvp_dwca/v13/wcvp_taxon.csv', sep='|')
timeend('dftaxon load')

# ---------------------------------------------------------------------------------------------------------------------
# Sanitizing WCVP Dataset
# ---------------------------------------------------------------------------------------------------------------------

# some spelling mistakes are present in the column names
timestart('dftaxon sanitize')
dftaxon_raw = dftaxon_raw.rename(columns={
    'scientfiicname': 'scientificname',
    'scientfiicauthorname': 'scientificauthorname'
})
timeend('dftaxon sanitize')

# ---------------------------------------------------------------------------------------------------------------------
# Supplementing WCVP Dataset
# ---------------------------------------------------------------------------------------------------------------------

dfdist = dfdist_raw
dftaxon = dftaxon_raw

timeend('LOADING')


# =====================================================================================================================
# Query Functions
# =====================================================================================================================

def is_indigenous(scientificname: str, locality: str):
    # possibly also check dftaxon['taxonrank'] == 'Species'
    taxon = dftaxon[
        (dftaxon['scientificname'] == scientificname) & (
            (dftaxon['taxonomicstatus'] == 'Accepted') |
            (dftaxon['taxonomicstatus'] == 'Synonym') |
            (dftaxon['taxonomicstatus'] == 'Provisionally Accepted')
        )
    ]
    if len(taxon) == 0:
        return 'Unknown'
    # todo - sort by taxonomicstatus
    for index, row in taxon.iterrows():
        dist = dfdist[dfdist['coreid'] == row['taxonid']]
        if len(dist) == 0:
            continue
        dist = dist[dist['locality'] == locality]
        if len(dist) == 0:
            continue
        for _, temp in dist.iterrows():
            return temp['establishmentmeans'] != 'introduced'
    return False


# =====================================================================================================================
# Query Functions
# =====================================================================================================================

timestart('analysis')
timeend('analysis')
