# Seattle Department of Transportation Trees

Exploration of the Seattle Department of Transportation (SDOT) Trees dataset.
You can find the dataset on the [Seattle GeoData SDOT Trees Page](https://data-seattlecitygis.opendata.arcgis.com/datasets/sdot-trees/explore).
Download the CSV version to use it with the code included in this repository.
For my purposes, I've renamed the CSV to `SDOT_Trees_CDL_20241119.csv` from its original name to note the date it was downloaded.
You may have to adjust the CSV file name in files to account for your particular file.

This project also relies on the World Checklist of Vascular Plants (WCVP) dataset.
You can download it [on the WCVP file server](http://sftp.kew.org/pub/data-repositories/WCVP/). You want to download `wcvp_dwca.zip`, version 13.

<!-- clean this up when I have a complete idea of which datasets I'll use -->

## Reprocessing

After downloading and extracting the referenced datasets, you should have the following extra files in the project root:

* `SDOT_Trees_CDL_20241119.csv`
* `wcvp_dwca.zip`
  - `eml.xml`
  - `meta.xml`
  - `wcvp_distribution.csv`
  - `wcvp_replacementNames.csv`
  - `wcvp_taxon.csv`

To generate `data/trees_of_seattle.csv` again from source files, run `prepare_trees_of_seattle_csv.py` after downloading the SDOT and WCVP datasets.

## Citations

```
SDOT Trees (2024). "SDOT Trees. Version 2024.11.19. Published on the Internet; https://data-seattlecitygis.opendata.arcgis.com/datasets/sdot-trees/explore. Accessed on: 2024.11.19"

WCVP (2024). "Govaerts R (ed.). 2024. WCVP: World Checklist of Vascular Plants. Facilitated by the Royal Botanic Gardens, Kew. [WWW document] URL http://sftp.kew.org/pub/data-repositories/WCVP/ [accessed 21 May 2024]."
```
