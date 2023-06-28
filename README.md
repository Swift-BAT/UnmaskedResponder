# UnmaskedResponder
Python response generator for the Swift Burst Alert Telescope (BAT). Creates full non mask-weighted responses.

In order to build and install this package to your python, first ensure that you're within the /UnmaskedResponder directory. We first want to install our dependencies listed in requirements.txt (using python3 for example):

	python -m pip install -r requirements.txt

In the base directory, run the command:

    python -m pip install .


# Response Files and Configuration

There are many internal data files (mostly used for generating the detector response) used in the codebase. Some are found in this repo and others are found in the [Zenodo community](https://zenodo.org/communities/swift-bat). 

The simplest way to organize these files is to put all of them into a single directory, and setting the path to that directory as an environment variable named `NITRATES_RESP_DIR`. If `NITRATES_RESP_DIR` is set and all of the response files are placed in there with their original file names (and directory structure for tarred directories) then `config.py` should be able to find the full path to all of the necessary files. `NITRATES_RESP_DIR` along with other paths can also be hard coded into the `config.py` file instead of being set as an env variable. If `NITRATES_RESP_DIR` is not hardcoded and an environmental variable is not set, `config.py` will assume that `NITRATES_RESP_DIR` is in the directory above `config.py`.

In the [Zenodo community](https://zenodo.org/communities/swift-bat), the [Swift-BAT Response Files for NITRATES](https://zenodo.org/record/5634207) dataset contains sevaral .tar.gz files that each contain a folder of data files to be downloaded and extracted into `NITRATES_RESP_DIR`. The tarred directories: `resp_tabs_ebins.tar.gz`, `comp_flor_resps.tar.gz`, `hp_flor_resps.tar.gz` need to be downloaded and extracted into `NITRATES_RESP_DIR`, along with the file `solid_angle_dpi.npy`. The other files either contain more energy bins or are used only for the seeding analyses. 

The .tar.gz files in the datasets [Swift-BAT Response Files for NITRATES: Forward Ray Tracings at IMX > 0](https://zenodo.org/record/5639481) and [Swift-BAT Response Files for NITRATES: Forward Ray Tracings at IMX < 0](https://zenodo.org/record/5639084) also need to be downloaded and extracted into `NITRATES_RESP_DIR`. These are the forward ray tracing files and are a few hundred GBs uncompressed. They're split up into seperate tarred files do to size limits, but should end up in the same directory, `NITRATES_RESP_DIR/ray_traces_detapp_npy/`. 

The `bright_src_cat.fits` file and the `element_cross_sections` folder in this repo should also be copied into `NITRATES_RESP_DIR`. 

Paths to these files can instead be given as arguments to some of the analysis objects, such as Source_Model_InOutFoV(). 

# Important Modules 

`models.py`
* Has the models that convert input paramaters into the count rate expectations for each det and energy bin in the LLH
* The models are sub classes of the `Model` class
* Currently used diffuse model is `Bkg_Model_wFlatA`
* Currently used point source model is `Source_Model_InOutFoV`, which supports both in and out of FoV positions
* Currently used simple point source model for known sources is `Point_Source_Model_Binned_Rates`
* `CompoundModel` takes a list of models to make a single model object that can give the total count expectations from all models used

`flux_models.py`
* Has functions and classes to handle computing fluxes for different flux models
* The different flux model object as subclasses of `Flux_Model`
  * `Flux_Model` contains methods to calculate the photon fluxes in a set of photon energy bins
  * Used by the response and point source model objects
* The different available flux models are:
  * `Plaw_Flux` for a simple power-law
  * `Cutoff_Plaw_Flux` for a power-law with an exponential cut-off energy
  * `Band_Flux` for a Band spectrum 

`response.py`
* Contains the functions and objects for the point source model
* Most current response object is `ResponseInFoV2` and is used in the `Source_Model_InOutFoV` model

`ray_trace_funcs.py`
* Contains the functions and objects to read and perform bilinear interpolation of the foward ray trace images that give the shadowed fraction of detectors at different in FoV sky positions
* `RayTraces` class manages the reading and interpolation and is used by the point source response function and simple point source model