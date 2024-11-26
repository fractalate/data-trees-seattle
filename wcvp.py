import pandas as pd


class WCVP():
    def __init__(self, path_taxon, path_dist):
        # Maybe del self.dftaxon to save some space since we'll work with self.dftaxon_accepted_synonyms.
        self.dftaxon = pd.read_csv(path_taxon, sep='|')
        self.dftaxon = self.dftaxon.rename(columns={
            'scientfiicname': 'scientificname',
            'scientfiicauthorname': 'scientificauthorname'
        })

        self.dfdist = pd.read_csv(path_dist, sep='|')

        self.assert_taxonid_eq_acceptednameusageid_are_accepted()

        self.dftaxon_accepted_synonyms = self.dftaxon[
            (self.dftaxon['taxonid'] == self.dftaxon['acceptednameusageid'])
            | (self.dftaxon['taxonomicstatus'] == 'Synonym')
        ]

    def assert_taxonid_eq_acceptednameusageid_are_accepted(self):
        dfeq = self.dftaxon[self.dftaxon['taxonid'] == self.dftaxon['acceptednameusageid']]
        dfacc = self.dftaxon[
            (self.dftaxon['taxonomicstatus'] == 'Accepted')
            | (self.dftaxon['taxonomicstatus'] == 'Artificial Hybrid')
            | (self.dftaxon['taxonomicstatus'] == 'Local Biotype')
        ]
        dfmerge = pd.merge(dfeq, dfacc)
        assert len(dfeq) == len(dfmerge)
        assert len(dfacc) == len(dfmerge)

    # E.g. from sdot data, rename `SCIENTIFIC_NAME` to `scientificname` and call this function before doing your work
    # to ensure `establishmentmeans` lookup is valid.
    def assert_all_scientificnames_values_have_one_establishment_means_in_locality(self, foreign_df, locality: str):
        df = self.get_dftaxon_for_locality(locality)
        df = df[df['scientificname'].isin(foreign_df['scientificname'])]
        dfg = df.groupby('scientificname')['establishmentmeans'].agg(set).reset_index()
        dfg['count'] = dfg['establishmentmeans'].apply(lambda x: len(x))
        assert dfg['count'].max() <= 1

    def get_dftaxon_for_locality(self, locality: str):
        dfd = self.dfdist[
            (self.dfdist['locality'] == locality)
        ]
        return pd.merge(
            self.dftaxon_accepted_synonyms,
            dfd[['coreid', 'locality', 'establishmentmeans']],
            left_on='acceptednameusageid',
            right_on='coreid',
            how='left',
        )

    # Did you call assert_all_scientificnames_values_have_one_establishment_means_in_locality() with your names yet?
    def lookup_establishment_type(self, locality: str, scientificname: str):
        df = self.get_dftaxon_for_locality(locality)
        df = df[df['scientificname'] == scientificname]
        if len(df) == 0:
            return 'unknown'
        if df.iloc[0]['locality'] != locality:
            return 'not established'
        if df.iloc[0]['establishmentmeans'] == 'introduced':
            return 'introduced'
        return 'indigenous'
