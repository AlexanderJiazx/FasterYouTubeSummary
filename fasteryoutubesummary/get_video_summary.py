from pytubefix import YouTube
from pytubefix.cli import on_progress
from .caption import get_video_caption
from .generate_webpage import create_summary_page
import os
from groq import Groq


def get_video_summary(url, api_key, mode="BETTER", language="ENGLISH", return_summary_only=True):
    # Set the relative path for the download folder
    download_folder = os.path.join(os.path.dirname(__file__), "./data_library/youtube_downloads")
    
    SYSTEM_PROMPTS = {
        "ENGLISH": "You are a YouTube video summarizer. Based on the audio transcription or captions, summarize the content of the video. Summarize all content and do not omit any detail or opinion. Output summary only. Output in English.",
        "SPANISH": "Eres un resumidor de videos de YouTube. Basado en la transcripción de audio o subtítulos, resume el contenido del video. Resume todo el contenido y no omitas ningún detalle ni opinión. El resumen debe ser en español, independientemente del idioma de la transcripción.",
        "GERMAN": "Du bist ein YouTube-Video-Zusammenfasser. Basierend auf der Audiotranskription oder den Untertiteln, fasse den Inhalt des Videos zusammen. Fasse den gesamten Inhalt zusammen und lass keine Details oder Meinungen aus. Die Zusammenfassung soll auf Deutsch erfolgen, unabhängig von der Sprache der Transkription.",
        "FRENCH": "Vous êtes un résumé de vidéos YouTube. À partir de la transcription audio ou des sous-titres, résumez le contenu de la vidéo. Résumez tout le contenu et n'omettez aucun détail ou opinion. Le résumé doit être en français, quel que soit le langage de la transcription.",
        "ITALIAN": "Sei un riassuntore di video di YouTube. Basandoti sulla trascrizione audio o sui sottotitoli, riassumi il contenuto del video. Riassumi tutto il contenuto e non omettere alcun dettaglio o opinione. Il riassunto deve essere in italiano, indipendentemente dalla lingua della trascrizione.",
        "JAPANESE": "あなたはYouTubeビデオの要約者です。音声の文字起こしや字幕に基づいて、ビデオの内容を要約します。すべての内容を要約し、詳細や意見を省略しないでください。要約は、文字起こしの言語に関係なく、日本語で出力してください。"
    }

    ENFORCEMET_PROMPTS = {
        "ENGLISH": "",
        "SPANISH": "Recuerda que debes generar el resumen en español.",
        "GERMAN": "Denke daran, dass die Ausgabe auf Deutsch erfolgen muss.",
        "FRENCH": "N’oubliez pas de générer le résumé en français.",
        "ITALIAN": "Ricorda di produrre il riassunto in italiano.",
        "JAPANESE": "日本語で出力することを忘れないでください。"
    }
    
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
        model = "llama-3.2-1b-preview"
    else:  # Default to BETTER mode
        model = "llama-3.2-90b-text-preview"
        
 
    # Action summarize
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPTS[language]
            },
            {
                "role": "user",
                "content": "Video Transcription" + Audio_transcription + "\n" + ENFORCEMET_PROMPTS[language]
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