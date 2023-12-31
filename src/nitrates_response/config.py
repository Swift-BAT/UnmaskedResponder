"""
This file allows the user to configure where the data is located on their system and keeps the changes persistent through the whole code.
"""

import os

NITRATES_RESP_DIR = None    # If you would like to manually set your NITRATES_RESP_DIR path, type it here
if NITRATES_RESP_DIR is None:
    NITRATES_RESP_DIR = os.getenv("NITRATES_RESP_DIR")
if NITRATES_RESP_DIR is None:
    # if NITRATES_RESP_DIR is not set here or as an env var then
    # it's assumed to be in the current working direc
    NITRATES_RESP_DIR = ".."

# ray traces directory
rt_dir = os.path.join(NITRATES_RESP_DIR, "ray_traces_detapp_npy")
# Resp Table with direct response directory
RESP_TAB_DNAME = os.path.join(NITRATES_RESP_DIR, "resp_tabs_ebins")
# Directory with Compton + Flor response
COMP_FLOR_RESP_DNAME = os.path.join(NITRATES_RESP_DIR, "comp_flor_resps")
# Directory with Flor response only
HP_FLOR_RESP_DNAME = os.path.join(NITRATES_RESP_DIR, "hp_flor_resps")
# DPI with st per det exposed to sky
solid_angle_dpi_fname = os.path.join(NITRATES_RESP_DIR, "solid_angle_dpi.npy")

# a grid of spectral models folded through the response for the split rates analysis for a spectral norm of 1. This is for a grid of points in imx and imy.
# this is for in FOV
rates_resp_dir = os.path.join(NITRATES_RESP_DIR, "rates_resps")
# this is for out of FOV
rates_resp_out_dir = os.path.join(NITRATES_RESP_DIR, "rates_resps_outFoV2")

resp_tabs = os.path.join(NITRATES_RESP_DIR, "resp_tabs")

# get the directory that the data directory is located in
dir = os.path.split(__file__)[0]

# Directory with the element cross section data files
ELEMENT_CROSS_SECTION_DNAME = os.path.join(dir, "data", "element_cross_sections")

# Table of bright known sources from the Trans Monitor
bright_source_table_fname = os.path.join(dir, "data", "bright_src_cat.fits")



HEADAS = None  # env variable can be used or this can be set
if HEADAS is None:
    HEADAS = os.getenv("HEADAS")
if HEADAS is None:
    print(
        "Could not get the $HEADAS system variable. Please ensure that this is set and points to the HEASOFT directory."
    )
else:
    os.system(". %s" % (os.path.join(HEADAS, "headas-init.sh")))

CALDB = None  # env variable can be used or this can be set
if CALDB is None:
    CALDB = os.getenv("CALDB")
if CALDB is None:
    print(
        "Could not get the $CALDB system variable. Please ensure that this is set and points to the CALDB directory."
    )
else:
    os.system(". %s" % (os.path.join(CALDB, "caldbinit.sh")))


ftool_wrap = os.path.join(dir, "HeasoftTools", "run_ftool.sh")

fp_dir = "/gpfs/scratch/jjd330/bat_data/footprints_npy/"


drm_quad_dir = "/gpfs/scratch/jjd330/bat_data/drms4quads/"


quad_dicts = {
    "all": {
        "quads": [0, 1, 2, 3],
        "drm_fname": "drm_0.200_0.150_.fits",
        "imx": 0.2,
        "imy": 0.15,
        "id": 0,
    },
    "left": {
        "quads": [0, 1],
        "drm_fname": "drm_1.000_0.150_.fits",
        "imx": 1.0,
        "imy": 0.15,
        "id": 1,
    },
    "top": {
        "quads": [1, 2],
        "drm_fname": "drm_-0.000_-0.500_.fits",
        "imx": 0.0,
        "imy": -0.5,
        "id": 2,
    },
    "right": {
        "quads": [2, 3],
        "drm_fname": "drm_-1.000_0.150_.fits",
        "imx": -1.0,
        "imy": 0.15,
        "id": 3,
    },
    "bottom": {
        "quads": [3, 0],
        "drm_fname": "drm_-0.000_0.450_.fits",
        "imx": 0.0,
        "imy": 0.45,
        "id": 4,
    },
    "quad0": {
        "quads": [0],
        "drm_fname": "drm_1.000_0.500_.fits",
        "imx": 1.0,
        "imy": 0.5,
        "id": 5,
    },
    "quad1": {
        "quads": [1],
        "drm_fname": "drm_0.800_-0.400_.fits",
        "imx": 0.8,
        "imy": -0.4,
        "id": 6,
    },
    "quad2": {
        "quads": [2],
        "drm_fname": "drm_-0.750_-0.450_.fits",
        "imx": -0.75,
        "imy": -0.45,
        "id": 7,
    },
    "quad3": {
        "quads": [3],
        "drm_fname": "drm_-1.100_0.500_.fits",
        "imx": -1.1,
        "imy": 0.5,
        "id": 8,
    },
}
