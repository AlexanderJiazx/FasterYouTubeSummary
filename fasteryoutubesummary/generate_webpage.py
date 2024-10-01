import os
from urllib.parse import urlparse, parse_qs
import html

def create_summary_page(video_url, video_title, summary_text):
    # Extract video ID from the URL
    parsed_url = urlparse(video_url)
    video_id = parse_qs(parsed_url.query).get('v', [None])[0]
    if not video_id:
        video_id = parsed_url.path.split('/')[-1]

    # Process the summary text
    summary_html = html.escape(summary_text)  # Escape HTML special characters
    summary_html = summary_html.replace('\n', '<br>')  # Replace newlines with <br> tags

    # HTML template
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{html.escape(video_title)} - Summary</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; }}
            h1 {{ color: #333; }}
            .video-container {{ position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin-bottom: 20px; }}
            .video-container iframe {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; }}
        </style>
    </head>
    <body>
        <h1>{html.escape(video_title)}</h1>
        <div class="video-container">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </div>
        <h2>Summary:</h2>
        <p>{summary_html}</p>
    </body>
    </html>
    """

    # Use a fixed filename
    filename = "summary.html"

    # Write the HTML content to a file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Summary page created: {filename}")
    return filename