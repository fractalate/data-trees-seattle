import os
import json

import pandas as pd

from sdot import SDOT
from wcvp import WCVP

print('Loading datasets...')

sdot = SDOT('SDOT_Trees_CDL_20241119.csv')
wcvp = WCVP('wcvp_taxon.csv', 'wcvp_distribution.csv')

print(f'Loaded {len(sdot.dfsdot)} trees from SDOT trees dataset.')

df = pd.DataFrame()
df['scientificname'] = sdot.dfsdot['SCIENTIFIC_NAME']
wcvp.assert_all_scientificnames_values_have_one_establishment_means_in_locality(df, 'Washington')
del df

'''
# This one will fail!
df = pd.DataFrame({ 'scientificname': ['Artemisia violacea'] })
wcvp.assert_all_scientificnames_values_have_one_establishmentmeans_in_locality(df, 'Washington')
'''

print('Checks passed!')

# We can do this because of the call to wcvp.assert_all_scientificnames_values_have_one_establishment_means_in_locality()
dftaxon = wcvp.get_dftaxon_for_locality('Washington')
dftaxon['indigenous'] = dftaxon.apply(lambda x: x['locality'] == 'Washington' and x['establishmentmeans'] != 'introduced', axis=1)
dftaxon = dftaxon[['scientificname', 'locality', 'indigenous']]
dftaxon = dftaxon.drop_duplicates()

'''
plants = [
    'Artemisia campestris subsp. borealis',
    'Artemisia vulgaris subsp. vulgaris',
    'Cercis canadensis',
    'Stump',
]

for plant in plants:
    print(plant, '-', wcvp.lookup_establishment_type('Washington', plant))
'''

print('Cleaning up SDOT trees dataset...')

dfsdot = sdot.dfsdot
discarded_record_count = 0
dfsdot_size_original = len(dfsdot)

dfsdot_size_before = len(dfsdot)
dfsdot = dfsdot[
    (dfsdot['SCIENTIFIC_NAME'] != 'Planting Site')
    & (dfsdot['SCIENTIFIC_NAME'] != 'stump')
    & (dfsdot['CURRENT_STATUS'] == 'INSVC')
]
discarded_nonliving_trees_record_count = dfsdot_size_before - len(dfsdot)
discarded_record_count += discarded_nonliving_trees_record_count
print(f'Discarded {discarded_nonliving_trees_record_count} ({discarded_nonliving_trees_record_count / dfsdot_size_original * 100:4.1f}%) non-living trees from the dataset.')
del dfsdot_size_before

dfsdot_size_before = len(dfsdot)
dfsdot = dfsdot[
    (dfsdot['SCIENTIFIC_NAME'] != 'Unknown')
]
discarded_unknown_trees_record_count = dfsdot_size_before - len(dfsdot)
discarded_record_count += discarded_unknown_trees_record_count
print(f'Discarded {discarded_unknown_trees_record_count} ({discarded_unknown_trees_record_count / dfsdot_size_original * 100:4.1f}%) unknown trees from the dataset.')
del dfsdot_size_before

print(f'Total: discarded {discarded_record_count} ({discarded_record_count / dfsdot_size_original * 100:4.1f}%) records.')

print(f'Merging {len(dfsdot)} SDOT trees records with {len(dftaxon)} WCVP taxonomy records...')

trees = pd.merge(
    dfsdot[['OBJECTID', 'SCIENTIFIC_NAME', 'GENUS', 'x', 'y']],
    dftaxon,
    left_on='SCIENTIFIC_NAME',
    right_on='scientificname',
    how='left',
)
trees['indigenous'].infer_objects(copy=False)
trees['indigenous'] = trees.apply(lambda x: x['indigenous'] == True, axis=1)  # Fill NaN with False. There's got to be a way to do this.
trees['local'] = trees['locality'] == 'Washington'
trees['scientificname'] = trees['SCIENTIFIC_NAME']
trees['genus'] = trees['GENUS']
trees['objectid'] = trees['OBJECTID']
trees = trees[['objectid', 'scientificname', 'genus', 'local', 'indigenous', 'x', 'y']]

assert len(trees) == len(dfsdot)

os.makedirs('data', exist_ok=True)

trees_csv = 'data/trees_of_seattle.csv'
trees.to_csv(trees_csv, sep = '|', index=False)
print(f'Saved {len(trees)} records to {trees_csv}')
trees_csv_metadata_json = 'data/trees_of_seattle.csv.metadata.json'
with open(trees_csv_metadata_json, 'w') as fout:
    fout.write(json.dumps({
        'version': '3',
        'record_count': len(trees),
        'discarded_record_count': discarded_record_count,
        'discarded_nonliving_trees_record_count': discarded_nonliving_trees_record_count,
        'discarded_unknown_trees_record_count': discarded_unknown_trees_record_count,
    }, indent='  ') + '\n')
print(f'Metadata saved to {trees_csv_metadata_json}')
