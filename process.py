import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, TypedDict

from sdot import SDOT
from wcvp import WCVP

print('Loading datasets...')

wcvp = WCVP('wcvp_taxon.csv', 'wcvp_distribution.csv')
sdot = SDOT('SDOT_Trees_CDL_20241119.csv')

df = pd.DataFrame()
df['scientificname'] = sdot.dfsdot['SCIENTIFIC_NAME']
wcvp.assert_all_scientificnames_values_have_one_establishment_means_in_locality(df, 'Washington')

'''
# This one will fail!
df = pd.DataFrame({ 'scientificname': ['Artemisia violacea'] })
wcvp.assert_all_scientificnames_values_have_one_establishmentmeans_in_locality(df, 'Washington')
'''

print('Checks passed!')

plants = [
    'Artemisia campestris subsp. borealis',
    'Artemisia vulgaris subsp. vulgaris',
    'Cercis canadensis',
    'Stump',
]

for plant in plants:
    print(plant, '-', wcvp.lookup_establishment_type('Washington', plant))
