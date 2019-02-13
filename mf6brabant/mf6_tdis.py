"""Bouw de tijd-discretisatie package"""
import flopy


def build_tdis_package(simulation, conf):
    return flopy.mf6.modflow.mftdis.ModflowTdis(
        simulation,
        pname='tdis',
        time_units=conf.get('time_units', 'DAYS'),
        nper=conf.n_periods,
        perioddata=conf.stress_periods,
    )
