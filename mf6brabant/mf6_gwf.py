"""Initialiseer het grondwater model"""
import flopy


def setup_gwf(simulation, conf):
    model_nam_file = '{}.nam'.format(conf["name"])
    return flopy.mf6.ModflowGwf(
        simulation,
        modelname=conf["name"],
        model_nam_file=model_nam_file,
    )
