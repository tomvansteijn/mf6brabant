"""Utility functies"""
import numpy as np
import rasterio


def read_array(rasterfile, masked=True, band=1):
    with rasterio.open(rasterfile) as src:
        return src.read(band, masked=masked)


def read_3d_array(rasterfiles, stack_axis=0, masked=True):
    arrays = []
    for rasterfile in rasterfiles:
        arrays.append(read_array(rasterfile, masked=masked))
    return np.ma.stack(arrays, axis=stack_axis)


def read_profile(rasterfile):
    with rasterio.open(rasterfile) as src:
        return src.profile


def write_array(rasterfile, values, profile):
    with rasterio.open(rasterfile, 'w', **profile) as dst:
        return dst.write(values, 1)
