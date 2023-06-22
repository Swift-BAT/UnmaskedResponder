import numpy as np

# Required
def ang_sep(ra0, dec0, ra1, dec1):
    dcos = np.cos(np.radians(np.abs(ra0 - ra1)))
    angsep = np.arccos(
        np.cos(np.radians(90 - dec0)) * np.cos(np.radians(90 - dec1))
        + np.sin(np.radians(90 - dec0)) * np.sin(np.radians(90 - dec1)) * dcos
    )
    return np.rad2deg(angsep)

