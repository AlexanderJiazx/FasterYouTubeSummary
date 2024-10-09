# fasteryoutubesummary/cli.py

import os
import sys
import click
from .get_video_summary import get_video_summary

# Define supported languages
LANGUAGES = {
    'ENGLISH': 'English',
    'SPANISH': 'Spanish',
    'GERMAN': 'German',
    'FRENCH': 'French',
    'ITALIAN': 'Italian',
    'JAPANESE': 'Japanese'
}

def validate_youtube_url(url):
    from urllib.parse import urlparse, parse_qs

    parsed_url = urlparse(url)
    if parsed_url.hostname not in ['www.youtube.com', 'youtube.com', 'youtu.be']:
        return False
    if parsed_url.hostname == 'youtu.be':
        return bool(parsed_url.path)
    if parsed_url.path != '/watch':
        return False
    query = parse_qs(parsed_url.query)
    return 'v' in query

@click.command()
@click.argument('url')
@click.option('-f', '--faster', is_flag=True, help='Enable faster mode (FASTER).')
@click.option('-w', '--website', is_flag=True, help='Generate website (disable text_only).')
@click.option('-l', '--language', type=click.Choice(LANGUAGES.keys(), case_sensitive=False),
              default='ENGLISH', help='Set the output language.')
def fys(url, faster, website, language):
    """
    Faster YouTube Summary CLI Tool

    Summarize YouTube videos quickly using Faster YouTube Summary.
    """
    # Validate YouTube URL
    if not validate_youtube_url(url):
        click.echo("Error: Invalid YouTube URL.")
        sys.exit(1)

    # Fetch API key from environment variable
    api_key = os.environ.get("FYS_GROQ")
    if not api_key:
        click.echo("Error: The environment variable FYS_GROQ is not set.")
        sys.exit(1)

    # Prepare parameters
    mode = 'FASTER' if faster else 'BETTER'
    lang = language.upper()
    return_summary_only = not website  # Default is True; set to False if --website is used

    # Generate summary
    try:
        summary = get_video_summary(
            url=url,
            api_key=api_key,
            mode=mode,
            language=lang,
            return_summary_only=return_summary_only
        )
        click.echo(summary)
    except Exception as e:
        click.echo(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    fys()
