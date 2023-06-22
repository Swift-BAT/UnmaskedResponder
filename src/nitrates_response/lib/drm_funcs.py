import numpy as np
from astropy.io import fits
import os

#Required
def get_ebin_ind_edges(drm, ebins0, ebins1):
    # drm = fits.open(os.path.join(b_dir, drm_arr['fname'][0]))
    drm_ebins0 = drm[2].data["E_MIN"]
    drm_ebins1 = drm[2].data["E_MAX"]
    ebin_ind_edges = [
        (
            np.argmin(np.abs(drm_ebins0 - ebins0[i])),
            np.argmin(np.abs(drm_ebins1 - ebins1[i])),
        )
        for i in range(len(ebins0))
    ]

    return ebin_ind_edges

