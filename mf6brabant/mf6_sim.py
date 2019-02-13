"""Initialiseer de simulatie"""
import flopy


def setup_simulation(name, workspace):
    return flopy.mf6.MFSimulation(
        sim_name=name,
        exe_name='mf6',
        version='mf6',
        sim_ws=str(workspace)
    )

def run_simulation(sim):
    pass
