import click
import simpleaudio as sa
from simpleaudio import WaveObject


@click.group()
def cli():
    """A CLI tool for playing .wav files."""
    pass


@cli.command()
@click.argument('wav_file', type=click.Path(exists=True))
def play(wav_file):
    """Play a .wav file."""
    try:
        # Load the .wav file
        wave_obj: WaveObject = sa.WaveObject.from_wave_file(wav_file)

        # Play the .wav file
        click.echo(f"Playing {wav_file}...")
        play_obj = wave_obj.play()

        # Wait for playback to finish
        play_obj.wait_done()
        click.echo("Playback finished.")
    except Exception as e:
        click.echo(f"Error playing file: {e}")


if __name__ == '__main__':
    cli()
