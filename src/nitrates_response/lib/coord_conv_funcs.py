import numpy as np


#Required
def theta_phi2imxy(theta, phi):
    imr = np.tan(np.radians(theta))
    imx = imr * np.cos(np.radians(phi))
    imy = imr * np.sin(np.radians(-phi))
    return imx, imy

#Required
def imxy2theta_phi(imx, imy):
    theta = np.rad2deg(np.arctan(np.sqrt(imx**2 + imy**2)))
    phi = np.rad2deg(np.arctan2(-imy, imx))
    if np.isscalar(phi):
        if phi < 0:
            phi += 360.0
    else:
        bl = phi < 0
        if np.sum(bl) > 0:
            phi[bl] += 360.0
    return theta, phi
