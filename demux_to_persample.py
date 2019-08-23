import click
import os
from qiita_files.demux import to_per_sample_files


@click.command()
@click.option('--input', type=click.Path(exists=True), required=True)
@click.option('--output', type=click.Path(exists=False), required=True)
@click.option('--njobs', type=int, required=True)
def persample(input, output, njobs):
    os.mkdir(output)
    to_per_sample_files(input, out_dir=output, n_jobs=njobs)


if __name__ == '__main__':
    persample()
