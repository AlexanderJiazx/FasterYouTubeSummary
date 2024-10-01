from pytubefix import YouTube
import re

def get_video_caption(url):
    try:
        # Fetch the YouTube video
        yt = YouTube(url)

        # Get available captions
        subtitles = yt.captions

        # Priority list of language codes
        language_priority = [
            'en', 'en-US', 'en-GB', 'en-AU',
            'es', 'fr', 'it', 'ja',
            'zh-Hans', 'zh-Hant', 'zh',
            'a.en', 'a.jp', 'a.zh'
        ]

        # Try to get the caption based on priority
        caption = None
        for lang in language_priority:
            if lang in subtitles:
                caption = subtitles[lang]
                break

        # If a caption was found, process it
        if caption:
            # Generate the SRT content
            srt_content = caption.generate_srt_captions()

            # Convert SRT to plain text
            def srt_to_plain_text(srt_content):
                # Remove numbers and timecodes using regex
                plain_text = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n', '', srt_content)
                
                # Remove any remaining sequence numbers and blank lines
                plain_text = re.sub(r'\d+\n', '', plain_text)
                plain_text = re.sub(r'\n+', '\n', plain_text).strip()

                return plain_text
            
            # Convert and return plain text
            return srt_to_plain_text(srt_content)
        else:
            return "No captions available in the specified languages."
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

