# mf6brabant
Brabantmodel implementation in Modflow 6 using flopy.

# usage

Git clone to create a local copy of data, scripts and notebooks. Download Modflow 6 executables from USGS and put them in the folder named `bin`. 

__Note__: Installation of git lfs (large file storage) is required for successfully downloading the datafiles from github. 

Written for Python 3. Required packages:

* numpy
* scipy
* pandas
* rasterio
* flopy


## contents

* `data`: Steady-state datasets of the Brabantmodel dated December 2018. Array data is stored in GeoTiff format. List data is stored in CSV files.
* `mf6brabant`: Python package for creating Brabantmodel in Modflow 6 (work in progress)
* `notebooks`: Jupyter notebooks with various implementations of the Brabantmodel in Modflow 6. The recommended version is run_mf6_using_external_files.ipynb


