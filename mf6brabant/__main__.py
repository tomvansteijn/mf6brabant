from pathlib import Path

from mf6brabant import *

if __name__ == "__main__":
    data_dir = Path('../../mf6/data')
    bin_dir = Path('../../mf6/bin')
    config = {
        "simulation": {
            "name": "test_run",
            "workspace": Path("../output/test_run"),
            "executable": bin_dir / "mf6.0.3/bin/mf6.exe"
        },
        "time": {
            "time_units": "DAYS",
            "n_periods": 1,
            "stress_periods": [(1.0, 1, 1.0)]
        },
        "space": {
            "top_files": data_dir / 'topbot/RL{ilay:d}.tif',
            "bottom_files": data_dir / 'topbot/TH{ilay:d}.tif',
            "idomain_file": data_dir / 'boundary/ibound.tif',
            "n_layers": 19,
            "n_rows": 450,
            "n_cols": 601,
            "del_rows": 250,
            "del_cols": 250
        },
        "conductivity": {
            "kd_files": data_dir / 'kdc/TX{ilay:d}.tif',
            "c_files": data_dir / 'kdc/CL{ilay:d}.tif',
        }
    }

    sim = setup_simulation(config["simulation"])
    tdis = build_tdis_package(sim, config["time"])
    gwf = setup_gwf(sim, config["simulation"])

    dis = build_dis_package(gwf, config["space"])
    npf = build_npf_package(gwf, config["conductivity"])

    run_simulation(sim)
