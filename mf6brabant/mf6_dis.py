"""Bouw de ondergrond discretisatie package"""

from pathlib import Path

import flopy
import numpy as np

from .utils import read_3d_array, read_array


def build_dis_package(gwf, conf):
    idomain = __read_idomain(conf.idomainfile)
    tops = __read_masked_levels(conf.topfiles)
    bots = __read_masked_levels(conf.bottomfiles)

    top, bottoms = __build_grid(tops, bots)
    idomain = np.broadcast_to(idomain, bottoms.shape)
    # initialize the DIS package
    return flopy.mf6.modflow.mfgwfdis.ModflowGwfdis(gwf,
        pname='dis', nlay=(conf.nlay*2 - 1),
        nrow=conf.nrow, ncol=conf.ncol,
        delr=conf.delr, delc=conf.delc,
        top=top, botm=bottoms,
        idomain=idomain,
    )

def __read_idomain(idomainfile):
    return read_array(idomainfile).filled(0.)

def __read_masked_levels(levelfiles):
    lvls = read_3d_array(levelfiles)
    # mask bad nodata values
    lvls = np.ma.masked_where(lvls.mask | (lvls < -9990.), lvls)
    # fill masked with zeros
    return lvls.filled(0.)

def __build_grid(tops, bots):
    grid = np.empty((tops.size+bots.size), dtype=tops.dtype)
    grid[0::2, :, :] = tops
    grid[1::2, :, :] = bots
    top = grid[0, :, :]
    botm = grid[1:, :, :]
    return top, botm
