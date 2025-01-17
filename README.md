# Seattle Department of Transportation Trees

Analysis of the Seattle Department of Transportation (SDOT) Trees dataset. This project also relies on the World Checklist of Vascular Plants (WCVP) dataset for taxonomic and geographic distribution information.

Please see the following documents containing the analysis:

* [Indigenous Trees (Notebook)](./indigenous_trees.ipynb)
* [Meet the Indigenous Trees of Seattle](./indigenous_trees.md)

Please see the following notebooks containing general notes about the primary datasets:

* [Explore SDOT](./explore_sdot.ipynb)
* [Explore WCVP](./explore_wcvp.ipynb)

Please see the following notebooks containing general notes about the derived datasets:

* [Explore Trees](./explore_sdot.ipynb)

You can find the SDOT dataset on the [Seattle GeoData SDOT Trees Page](https://data-seattlecitygis.opendata.arcgis.com/datasets/sdot-trees/explore).
Download the CSV version to use it with the code included in this repository.
For this analysis, the CSV is renamed to `SDOT_Trees_CDL_20241119.csv` from its original name to note the date it was downloaded.
You may have to adjust the CSV file name in [sdot.py](sdot.py) to account for your particular file name.

You can find the WCVP dataset on the [WCVP file server](http://sftp.kew.org/pub/data-repositories/WCVP/).
You want to download `wcvp_dwca.zip` for version 13.

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

SDOT Trees (2024). "SDOT Trees. Version 2024.11.19. Published on the Internet; https://data-seattlecitygis.opendata.arcgis.com/datasets/sdot-trees/explore. Accessed on: 2024.11.19"

WCVP (2024). "Govaerts R (ed.). 2024. WCVP: World Checklist of Vascular Plants. Facilitated by the Royal Botanic Gardens, Kew. [WWW document] URL http://sftp.kew.org/pub/data-repositories/WCVP/ [accessed 21 May 2024]."

### Media

* [media/acer_macrophyllum/Acer_macrophyllum_1199.jpg](./media/acer_macrophyllum/Acer_macrophyllum_1199.jpg) - Big Leaf Maple Leaves
  - Tony Perodeau (2006), [https://commons.wikimedia.org/wiki/File:Acer_macrophyllum_1199.jpg?uselang=en](https://commons.wikimedia.org/wiki/File:Acer_macrophyllum_1199.jpg?uselang=en), Public Domain
* [media/acer_macrophyllum/Acer_macrophyllum_3158.jpg](./media/acer_macrophyllum/Acer_macrophyllum_3158.jpg) - Big Leaf Maple Seeds
  - Walter Siegmund (2004), [https://commons.wikimedia.org/wiki/File:Acer_macrophyllum_3158.jpg](https://commons.wikimedia.org/wiki/File:Acer_macrophyllum_3158.jpg), CC BY-SA 3.0
* [media/acer_macrophyllum/Bigleaf_maple_(Acer_macrophyllum)_closeup_of_flowers.jpg](./media/acer_macrophyllum/Bigleaf_maple_(Acer_macrophyllum)_closeup_of_flowers.jpg) - Big Leaf Maple Flowers
  - Kollibri1969 (2024), [https://commons.wikimedia.org/wiki/File:Bigleaf_maple_(Acer_macrophyllum)_closeup_of_flowers.jpg](https://commons.wikimedia.org/wiki/File:Bigleaf_maple_(Acer_macrophyllum)_closeup_of_flowers.jpg), CC BY-SA 4.0
* [media/acer_macrophyllum/Acer_macrophyllum_kz06.jpg](./media/acer_macrophyllum/Acer_macrophyllum_kz06.jpg) - Big Leaf Maple Bark
  - Krzysztof Ziarnek, Kenraiz (2020), [https://commons.wikimedia.org/wiki/File:Acer_macrophyllum_kz06.jpg](https://commons.wikimedia.org/wiki/File:Acer_macrophyllum_kz06.jpg), CC BY-SA 4.0
