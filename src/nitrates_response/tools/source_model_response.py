import pytest
import numpy as np
from astropy.io import fits
import os
import numpy as np
from astropy.table import Table
import nitrates_response as nr



def get_bldmask_alldets():

    detxs_by_sand0 = np.arange(0, 286-15, 18)
    detxs_by_sand1 = detxs_by_sand0 + 15

    detys_by_sand0 = np.arange(0, 173-7, 11)
    detys_by_sand1 = detys_by_sand0 + 7

    all_good_detxs = np.ravel([np.arange(detxs_by_sand0[i], detxs_by_sand1[i]+1,\
                                          1, dtype=np.int) for i in range(16)])
    all_good_detys = np.ravel([np.arange(detys_by_sand0[i], detys_by_sand1[i]+1,\
                                         1, dtype=np.int) for i in range(16)])

    detxax = np.arange(286, dtype=np.int)
    detyax = np.arange(173, dtype=np.int)
    detx_dpi, dety_dpi = np.meshgrid(detxax, detyax)
    bl_alldets = np.isin(detx_dpi, all_good_detxs)&np.isin(dety_dpi, all_good_detys)
    return bl_alldets


def generate_response_dpis(theta, phi, ebins0, ebins1):

    flux_mod = nr.models.flux_models.Cutoff_Plaw_Flux(E0=100.0)
    bl_alldets = get_bldmask_alldets()
    rt_obj = nr.response.ray_trace_funcs.RayTraces(nr.config.rt_dir)

    sig_mod = nr.models.models.Source_Model_InOutFoV(flux_mod, (ebins0,ebins1),\
                                        bl_alldets, rt_obj, use_deriv=True,\
                                        resp_tab_dname=nr.config.resp_tabs)

    sig_mod.set_theta_phi(theta, phi)
    tot_resp_dpis = sig_mod.resp_obj.lines_resp_dpi + sig_mod.resp_obj.comp_flor_resp_dpis
    
    return tot_resp_dpis, sig_mod.resp_obj.PhotonEmins, sig_mod.resp_obj.PhotonEmaxs
    
    
def summed_response(theta, phi, ebins0, ebins1, directory=nr.config.NITRATES_RESP_DIR):

    tot_resp_dpis, PhotonEmins, PhotonEmaxs = generate_response_dpis(theta, phi, ebins0, ebins1)
    resps = np.sum(tot_resp_dpis, axis=0)

    dic = {'ENERG_LO':PhotonEmins, 
           'ENERG_HI':PhotonEmaxs,
           'N_GRP':np.ones(187, dtype=np.int),
           'F_CHAN':np.zeros(187, dtype=np.int),
           'N_CHAN':np.zeros(187, dtype=np.int) + 5,
           'MATRIX':resps}
    drm_tab = Table(data=dic)

    ebounds_tab = Table(data=[np.arange(len(ebins0),dtype=np.int),ebins0,ebins1],
                        names=['CHANNEL', 'E_MIN', 'E_MAX'], dtype=[np.int,np.float,np.float])

    primary_hdu = fits.PrimaryHDU()
    drm_hdu = fits.table_to_hdu(drm_tab)
    ebounds_hdu = fits.table_to_hdu(ebounds_tab)

    drm_hdu.name = 'SPECRESP MATRIX'
    ebounds_hdu.name = 'EBOUNDS'

    hdul = fits.HDUList([primary_hdu, drm_hdu, ebounds_hdu])
    os.chdir(directory)
    save_fname = 'NITRATES_alldet_theta_%.3f_phi_%.3f_.rsp'%(theta,phi)
    hdul.writeto(save_fname, overwrite=True)


if __name__ == "__main__":

    ebins0 = np.array([15.0, 24.0, 35.0, 48.0, 64.0])
    ebins0 = np.append(ebins0, np.logspace(np.log10(84.0), np.log10(500.0), 5+1))[:-1]
    ebins0 = np.round(ebins0, decimals=1)[:-1]
    ebins1 = np.append(ebins0[1:], [350.0])
    ebins = [ebins0, ebins1]

    summed_response(0., 0., ebins0, ebins1)