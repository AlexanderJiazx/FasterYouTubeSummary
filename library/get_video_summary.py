from pytubefix import YouTube
from pytubefix.cli import on_progress
from caption import get_video_caption
import os
from groq import Groq
from generate_webpage import create_summary_page

def get_video_summary(url, api_key, mode="BETTER", return_summary_only=False):
    # Set the relative path for the download folder
    download_folder = os.path.join(os.path.dirname(__file__), "./data_library/youtube_downloads")
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Get the video caption
    caption_text = get_video_caption(url)
    yt = YouTube(url, on_progress_callback=on_progress)
    video_title = yt.title

    # Initialize the Groq client
    client = Groq(api_key=api_key)

    if caption_text == "No captions available in the specified languages.":
        if not return_summary_only:
            print("No captions available. Downloading and transcribing the audio.")
        
        # Initialize YouTube object with progress callback
        yt = YouTube(url, on_progress_callback=on_progress)

        if not return_summary_only:
            print(f"Downloading: {yt.title}")

        # Get the highest resolution stream
        ys = yt.streams.get_audio_only()

        # Action download
        filename = os.path.join(download_folder, "output.mp3")
        ys.download(output_path=download_folder, filename="output.mp3")

        if not return_summary_only:
            print("Download Completed, Transcribing the audio")

        # Action transcribe
        with open(filename, "rb") as file:
            translation = client.audio.translations.create(
                file=(filename, file.read()),
                model="whisper-large-v3",
                prompt="Specify context or spelling",
                response_format="json",
                temperature=0.0
            )
        Audio_transcription = translation.text
    else:
        if not return_summary_only:
            print("Captions available. Using them for summarization.")
        Audio_transcription = caption_text

    if not return_summary_only:
        print("Summarizing the content")

    # Set the model based on the mode
    if mode.upper() == "FASTER":
        model = "llama-3.1-8b-instant"
    else:  # Default to BETTER mode
        model = "llama-3.1-70b-versatile"

    # Action summarize
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a YouTube video summarizer. Based on the audio transcription or captions, summarize the content of the video. Summarize all content and do not omit any detail or opinion. Output summary only."
            },
            {
                "role": "user",
                "content": "Video Transcription" + Audio_transcription
            }
        ],
        temperature=0,
        max_tokens=2048,
        top_p=1,
        stream=False,
        stop=None,
    )

    summary = completion.choices[0].message.content

    if return_summary_only:
        return summary

    # Create and open summary page
    summary_page = create_summary_page(url, video_title, summary)

    if os.name == 'nt':  # For Windows
        os.startfile(summary_page)
    elif os.name == 'posix':  # For macOS and Linux
        os.system(f'open "{summary_page}"')

    print(f"Summary page created and opened: {summary_page}")
    return summary