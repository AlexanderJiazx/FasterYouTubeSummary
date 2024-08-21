# Faster YouTube Summary

**Faster YouTube Summary** is a powerful tool designed to quickly generate detailed summaries of YouTube videos using the Groq API. This tool can deliver a comprehensive summary of a YouTube video in just 2 seconds, provided the video has native captions.

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install pytubefix groq fasteryoutubesummary
```

## Setup

Faster YouTube Summary leverages the Groq API to provide fast and accurate responses from large language models (LLMs). To use this tool, you'll need a Groq API key.

1. Obtain your API key from the Groq Console:  
   [Get your Groq API key](https://console.groq.com/keys)

2. Once you have your API key, set it as an environment variable:

```bash
export GROQ_API_KEY="YOUR_API_KEY"
```

## Usage

After setup, you can use Faster YouTube Summary in your project with the following code:

```python
from fasteryoutubesummary import get_video_summary
import os  

url = input("Enter the URL of the YouTube video: ")
api_key = os.environ.get("GROQ_API_KEY")
summary = get_video_summary(url, api_key, return_summary_only=False)
  
print(summary)
```

- **url** and **api_key** are required parameters.
- To receive the summary as plain text only, set `return_summary_only` to `True`.

```python
from fasteryoutubesummary import get_video_summary
import os  

url = input("Enter the URL of the YouTube video: ")
api_key = os.environ.get("GROQ_API_KEY")
summary = get_video_summary(url, api_key, return_summary_only=Ture)
  
print(summary)
```