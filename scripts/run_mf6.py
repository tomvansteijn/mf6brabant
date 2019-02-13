import click
import mf6brabant as mf6

@click.command()
@click.argument(
    'config',
    type=click.Path(exists=True)
)
def main(config):
    config = mf6.load_config(config)

    sim = mf6.setup_simulation(config.modelname, config.model_workspace)
    tdis = mf6.build_tdis_package(sim, config.stress_periods)
    gwf = mf6.setup_gwf(tdis)

    mf6.build_dis_package(gwf, config.dis)

    mf6.run_simulation(sim)
