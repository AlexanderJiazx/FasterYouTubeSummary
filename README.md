# Faster YouTube Summary

**Faster YouTube Summary** is a powerful tool designed to quickly generate detailed summaries of YouTube videos using the Groq API. This tool can deliver a comprehensive summary of a YouTube video in just 2 seconds (provided the video has native captions).

## Features

- **Fast summaries:** Generate detailed summaries in a few seconds.
- **Multilingual support:** Generate summaries in multiple languages.
- **FASTER mode:** Toggle between faster summary generation or higher-quality summaries.
- **CLI support:** Generate YouTube summaries directly from your terminal.

---

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install fasteryoutubesummary
```

## Setup

Faster YouTube Summary leverages the Groq API to provide fast and accurate responses from large language models (LLMs). To use this tool, you'll need a Groq API key.

1. Obtain your API key from the Groq Console:  
   [Get your Groq API key](https://console.groq.com/keys)

2. Once you have your API key, set it as an environment variable:

```bash
export FYS_GROQ="YOUR_API_KEY"
```

### **For Windows users**:

- **Command Prompt**:

  ```cmd
  set FYS_GROQ="YOUR_API_KEY"
  ```

- **PowerShell**:

  ```powershell
  $env:FYS_GROQ="YOUR_API_KEY"
  ```

---

## Basic Usage in Python

After setting up, you can use Faster YouTube Summary in your Python project with the following code:

```python
from fasteryoutubesummary import get_video_summary
import os

url = input("Enter the URL of the YouTube video: ")
api_key = os.environ.get("FYS_GROQ")
summary = get_video_summary(url, api_key, return_summary_only=False)

print(summary)
```

### Programmatic Options:

- **url** and **api_key** are required parameters.
- **`return_summary_only`**: If `True`, returns only the summary text (default: `True`). If `False`, it generates a website summary.

To receive the summary as plain text only:

```python
from fasteryoutubesummary import get_video_summary
import os  

url = input("Enter the URL of the YouTube video: ")
api_key = os.environ.get("FYS_GROQ")
summary = get_video_summary(url, api_key, return_summary_only=True)

print(summary)
```

---

## Command-Line Interface (CLI) Usage

You can also generate YouTube summaries directly from the command line using the **fys** command after installing the package.

### **Basic CLI Command**

```bash
fys https://www.youtube.com/watch?v=VIDEO_ID
```

This will generate a text summary of the specified YouTube video.

### **Command-Line Options**

```bash
fys [URL] [OPTIONS]
```

- `URL`: The YouTube video URL (required).
- `-f`, `--faster`: Enables faster mode (`FASTER`), prioritizing speed over accuracy.
- `-w`, `--website`: Generates a website summary instead of plain text.
- `-l`, `--language [LANGUAGE]`: Sets the output language. Supported languages: `ENGLISH`, `SPANISH`, `GERMAN`, `FRENCH`, `ITALIAN`, `JAPANESE`.

### **Example Usages**

#### 1. Basic text summary:

```bash
fys https://www.youtube.com/watch?v=o-2ybJPgtjA
```

#### 2. Generate summary in faster mode:

```bash
fys https://www.youtube.com/watch?v=o-2ybJPgtjA --f
```

#### 3. Generate a website summary:

```bash
fys https://www.youtube.com/watch?v=o-2ybJPgtjA --w
```

#### 4. Generate a summary in Japanese:

```bash
fys https://www.youtube.com/watch?v=o-2ybJPgtjA --language JAPANESE
```

#### 5. Combine multiple options (faster mode and website summary in Japanese):

```bash
fys https://www.youtube.com/watch?v=o-2ybJPgtjA --f --w --language JAPANESE
```

---

## Multilingual Output

Thanks to the Groq API, Faster YouTube Summary supports multiple languages. To generate a summary in a different language, use the `language` parameter:

```python
from fasteryoutubesummary import get_video_summary
import os  

url = input("Enter the URL of the YouTube video: ")
api_key = os.environ.get("FYS_GROQ")
summary = get_video_summary(url, api_key, language='JAPANESE', return_summary_only=True)

print(summary)
```

### Supported Languages:

| Language  | Language Code |
|-----------|---------------|
| English   | ENGLISH       |
| Spanish   | SPANISH       |
| German    | GERMAN        |
| French    | FRENCH        |
| Italian   | ITALIAN       |
| Japanese  | JAPANESE      |

---

## FASTER Mode

Although the default model is optimized for accuracy, Faster YouTube Summary provides an optional **FASTER** mode for speed optimization:

```bash
fys https://www.youtube.com/watch?v=o-2ybJPgtjA --f
```

In this mode, summaries are generated faster, though with slightly reduced accuracy.

---

## License

Faster YouTube Summary is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contribution

Contributions are welcome! If you'd like to improve this package, feel free to submit a pull request or open an issue on GitHub.

---

## Contact

For any questions or support, feel free to reach out via [email](mailto:hellolightning321@gmail.com).

---
