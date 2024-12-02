import os
import json

import pandas as pd

pairs = [
    # We see in dftaxon that there is no record for the cross, but we assume this is equivalent to the variety.
    ('Acer truncatum x A platanoides', 'Acer truncatum var. platanoides'),
]

scientificnames, scientificnames_clean = zip(*pairs)
alternative_scientific_names = pd.DataFrame({
    'scientificname': scientificnames,
    'scientificname_clean': scientificnames_clean,
})

os.makedirs('data', exist_ok=True)

alternative_scientific_names_csv = 'data/alternative_scientific_names.csv'

alternative_scientific_names.to_csv(alternative_scientific_names_csv, sep = '|', index=False)
print(f'Saved {len(alternative_scientific_names)} records to {alternative_scientific_names_csv}')
alternative_scientific_names_csv_metadata_json = 'data/alternative_scientific_names.csv.metadata.json'
with open(alternative_scientific_names_csv_metadata_json, 'w') as fout:
    fout.write(json.dumps({
        'version': '0',
        'record_count': len(alternative_scientific_names),
    }, indent='  ') + '\n')
print(f'Metadata saved to {alternative_scientific_names_csv_metadata_json}')
