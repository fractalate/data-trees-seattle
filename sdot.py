import pandas as pd

class SDOT():
    def __init__(self, path):
        self.dfsdot = pd.read_csv(path, dtype={
            'CONDITION': 'string',
            'CONDITION_ASSESSMENT_DATE': 'string',
            'ASBUILTPLANNO': 'string',
        })

        # to squelch warnings about the data
        self.dfsdot['CONDITION'] = self.dfsdot['CONDITION'].fillna('')
        self.dfsdot['CONDITION_ASSESSMENT_DATE'] = self.dfsdot['CONDITION_ASSESSMENT_DATE'].fillna('')
        self.dfsdot['ASBUILTPLANNO'] = self.dfsdot['ASBUILTPLANNO'].fillna('')

        # life's better without NaN in these columns
        self.dfsdot['SCIENTIFIC_NAME'] = self.dfsdot['SCIENTIFIC_NAME'].fillna('')
        self.dfsdot['COMMON_NAME'] = self.dfsdot['COMMON_NAME'].fillna('')
