"""Bouw de ondergrond discretisatie package"""

from pathlib import Path

import flopy
import numpy as np

from .utils import read_3d_array, read_array


def build_dis_package(gwf, conf):
    idomain = __read_idomain(conf["idomain_file"])
    tops = __read_masked_levels(conf["top_files"], conf["n_layers"])
    bots = __read_masked_levels(conf["bottom_files"], conf["n_layers"])

    top, bottoms = __build_grid(tops, bots)
    idomain = np.broadcast_to(idomain, bottoms.shape)
    # initialize the DIS package
    return flopy.mf6.modflow.mfgwfdis.ModflowGwfdis(
        gwf,
        pname='dis', nlay=(conf["n_layers"]*2 - 1),
        nrow=conf["n_rows"], ncol=conf["n_cols"],
        delr=conf["del_rows"], delc=conf["del_cols"],
        top=top, botm=bottoms,
        idomain=idomain,
    )


def __read_idomain(idomainfile):
    return read_array(idomainfile).filled(0.)


def __read_masked_levels(levelfiles, nlay):
    levelfiles = list(levelfiles.parent / levelfiles.name.format(ilay=i + 1)
                      for i in range(nlay))
    lvls = read_3d_array(levelfiles)
    # mask bad nodata values
    lvls = np.ma.masked_where(lvls.mask | (lvls < -9990.), lvls)
    return lvls


def __build_grid(tops, bots):
    top = tops[0, :, :].filled(0.)
    botm = []
    nlay = bots.shape[0]
    for ilay in range(nlay):
        botm.append(bots[ilay, :, :].filled((2*ilay + 1) * -1e-3))
        if (ilay + 1) < nlay:
            botm.append(tops[ilay + 1, :, :].filled((2*ilay + 2) * -1e-3))
    botm = np.ma.stack(botm)
    return top, botm
