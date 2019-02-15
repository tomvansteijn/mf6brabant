"""Initialiseer de simulatie"""
import flopy


def setup_simulation(conf):
    return flopy.mf6.MFSimulation(
        sim_name=conf["name"],
        exe_name=str(conf.get("executable", "mf6")),
        version="mf6",
        sim_ws=str(conf["workspace"])
    )


def run_simulation(sim):
    sim.write_simulation()
    sim.run_simulation()
