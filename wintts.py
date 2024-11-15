from email.policy import default

import click
import pyttsx3

def list_of_voices():
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Get all voices available on the system
    return [v for v in engine.getProperty('voices')]


def _voices():
    voices = list_of_voices()

    if not voices:
        click.echo("No voices found.")
    else:
        click.echo("Available voices:")
        for v in voices:
            click.echo(f"- {v.name}")

def _select_voice(name: str) -> str:
    for v in list_of_voices():
        if name in v.name:
            return v

def _read(text, voice_name, wpm_rate, output_file=None, play=True):
    engine = pyttsx3.init()

    selected_voice = _select_voice(voice_name)

    if selected_voice is None:
        click.echo(f"Error: Voice '{voice_name}' not found.")
        return
    click.echo(f"Selected Voice is: '{selected_voice.name}'.")

    # Set the voice
    engine.setProperty('voice', selected_voice.id)

    # Set velocity (rate of speech)
    engine.setProperty('rate', wpm_rate)

    if output_file:
        # Save the speech to an audio file
        engine.save_to_file(text, output_file)
        click.echo(f"Speech saved to: {output_file}")
    if play:
        # Play the speech
        print('words per minute:', wpm_rate)
        print(text)
        engine.say(text)
        engine.runAndWait()

@click.group()
def cli():
    """A CLI tool for text-to-speech using Windows Speech API."""
    pass


@cli.command()
def voices():
    """List all available voices for speech synthesis."""
    _voices()


@cli.command()
@click.argument('text')
@click.argument('voice_name')
@click.option('--wpm-rate', default=150, type=int, help="Set the words per minute rate (default 150).")
@click.option('--file', help="Optional: Output file name (e.g., 'output.wav')")
@click.option('--play', is_flag=True, default=True, help="Play the speech instead of saving to a file.")
def read(text, voice_name, wpm_rate, file, play):
    """Synthesize speech with the specified voice, velocity, and optional file output."""
    _read(text, voice_name, wpm_rate, output_file=file, play=play)


if __name__ == "__main__":
    cli()
