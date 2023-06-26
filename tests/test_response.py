import pytest
import numpy as np
from astropy.io import fits
import os
import os
import numpy as np


def test_response_generation():
        
    import nitrates_response as nr
    
    ebins0 = np.array([15.0, 24.0, 35.0, 48.0, 64.0])
    ebins0 = np.append(ebins0, np.logspace(np.log10(84.0), np.log10(500.0), 5+1))[:-1]
    ebins0 = np.round(ebins0, decimals=1)[:-1]
    ebins1 = np.append(ebins0[1:], [350.0])
    ebins = [ebins0, ebins1]

    param_dict = {
            'Background_bkg_rate_0': 0.11466907091417632,
            'Background_bkg_rate_1': 0.07095786835188621,
            'Background_bkg_rate_2': 0.041567467512002416,
            'Background_bkg_rate_3': 0.04078392487583211,
            'Background_bkg_rate_4': 0.03551553007592515,
            'Background_bkg_rate_5': 0.03590992349048733,
            'Background_bkg_rate_6': 0.03379641587246757,
            'Background_bkg_rate_7': 0.025444525699223043,
            'Background_bkg_rate_8': 0.01798602804640096,
            'Background_flat_0': 0.0,
            'Background_flat_1': 0.0,
            'Background_flat_2': 0.005835134809895061,
            'Background_flat_3': 0.005967086920274559,
            'Background_flat_4': 0.26221065800705035,
            'Background_flat_5': 0.7334750410153207,
            'Background_flat_6': 0.8091356931249437,
            'Background_flat_7': 1.0,
            'Background_flat_8': 1.0,
            'GX 339-4_imx': 0.008738071340069587,
            'GX 339-4_imy': -0.6947855783608099,
            'GX 339-4_rate_0': 0.018159893494925635,
            'GX 339-4_rate_1': 0.008908844593258816,
            'GX 339-4_rate_2': 0.0044066721206024615,
            'GX 339-4_rate_3': 0.0032033385728500396,
            'GX 339-4_rate_4': 0.002694769162129345,
            'GX 339-4_rate_5': 0.0026060203566754436,
            'GX 339-4_rate_6': 0.001749409709948854,
            'GX 339-4_rate_7': 0.002171355810924897,
            'GX 339-4_rate_8': 0.000701888519626218,
            'err_Background_bkg_rate_0': 0.0003999061433281428,
            'err_GX 339-4_rate_0': 0.0014641700778411,
            'err_Background_bkg_rate_1': 0.0003141885941197609,
            'err_GX 339-4_rate_1': 0.0011372163908529667,
            'err_Background_bkg_rate_2': 0.00024052967375414112,
            'err_GX 339-4_rate_2': 0.0008674428557813444,
            'err_Background_bkg_rate_3': 0.00023798885068974658,
            'err_GX 339-4_rate_3': 0.0008496413904969421,
            'err_Background_bkg_rate_4': 0.0002222361787897516,
            'err_GX 339-4_rate_4': 0.000794782198233917,
            'err_Background_bkg_rate_5': 0.00022338134153099596,
            'err_GX 339-4_rate_5': 0.0007972014161971167,
            'err_Background_bkg_rate_6': 0.00021666139297444725,
            'err_GX 339-4_rate_6': 0.0007688817884286285,
            'err_Background_bkg_rate_7': 0.00018822362360600018,
            'err_GX 339-4_rate_7': 0.0006760621827675931,
            'err_Background_bkg_rate_8': 0.0001579688957616835,
            'err_GX 339-4_rate_8': 0.000557799659571041,
            'corr_Background_bkg_rate_0_GX 339-4_rate_0': -0.4507808226091319,
            'corr_Background_bkg_rate_1_GX 339-4_rate_1': -0.4518817292857254,
            'corr_Background_bkg_rate_2_GX 339-4_rate_2': -0.4542992130168804,
            'corr_Background_bkg_rate_3_GX 339-4_rate_3': -0.45524929459706365,
            'corr_Background_bkg_rate_4_GX 339-4_rate_4': -0.45670620606218254,
            'corr_Background_bkg_rate_5_GX 339-4_rate_5': -0.45639349871043056,
            'corr_Background_bkg_rate_6_GX 339-4_rate_6': -0.458248601422266,
            'corr_Background_bkg_rate_7_GX 339-4_rate_7': -0.45678889135078876,
            'corr_Background_bkg_rate_8_GX 339-4_rate_8': -0.45867034982750704,
            'nllh': 248324.33514527624,
            'time': 646018369.8666999,
            'dt': -13.312000036239624,
            'exp': 61.44000005722046
            }
        
    solid_angle_dpi = np.load('solid_angle_dpi.npy')
    rt_dir = nr.config.rt_dir
    dmask = fits.open(os.path.join('detmask.fits'))[0].data
        
    rt_obj_nr = nr.response.RayTraces(rt_dir)
    bl_dmask = (dmask == 0.)
    hdul = fits.open('src_tab.fits')
    src_tab = hdul[1].data
    rate_dpis_NR = np.load("rate_dpis_NR.npy")
        

    final_bkg_and_src_mod_nr = nr.models.Bkg_and_Point_Source_Model(solid_angle_dpi, ebins, rt_obj_nr, bl_dmask, src_tab['Name'], bkg_row=param_dict)
    rate_dpis_nr = final_bkg_and_src_mod_nr.get_rate_dpis(param_dict)


    assert(np.array_equal(rate_dpis_NR, rate_dpis_nr))
    hdul.close()

if __name__ == "__main__":
    
    test_response_generation()