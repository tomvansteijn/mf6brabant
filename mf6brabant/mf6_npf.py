"""Bouw de ondergrond discretisatie package"""

from pathlib import Path

import flopy
import numpy as np

from .utils import read_3d_array, read_array


def build_npf_package(gwf, conf):
    dis_shape = tuple(n.get_data()
                      for n in (gwf.dis.nlay, gwf.dis.nrow, gwf.dis.ncol))
    n_lay_quasi = int((dis_shape[0]+1)/2)
    kd = __read_files(conf["kd_files"], n_lay_quasi)
    c = __read_files(conf["c_files"], n_lay_quasi-1)

    tops = np.vstack((np.expand_dims(gwf.dis.top[:], 0), gwf.dis.botm[1::2]))
    bots = gwf.dis.botm[::2]

    kh = (kd / (tops-bots)).filled(1e-6)
    kv = ((bots[:-1] - tops[1:]) / c).filled(1e6)

    kh3d = np.ones(dis_shape) * 1e-6
    kh3d[::2] = kh
    kv3d = np.ones(dis_shape) * 1e6
    kv3d[1::2] = kv

    return flopy.mf6.modflow.mfgwfnpf.ModflowGwfnpf(
        model=gwf,
        k=kh3d,
        k22=kh3d,
        k33=kv3d,
    )


def __read_files(levelfiles, nlay):
    levelfiles = list(levelfiles.parent / levelfiles.name.format(ilay=i + 1)
                      for i in range(nlay))
    lvls = read_3d_array(levelfiles)
    return lvls
