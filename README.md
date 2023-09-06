# Audio Transcription from Video using Python

## Overview
This project contains a Python script that extracts audio from a given video file and transcribes the audio to text. It utilizes parallel processing for faster transcription.

## Requirements
- Python 3.x
- FFmpeg
- pydub
- speech_recognition
- concurrent.futures (Python Standard Library)

## Installation

### Python Dependencies
To install the Python dependencies, run the following commands:

```bash
pip install pydub
pip install SpeechRecognition
```

### FFmpeg
FFmpeg is required for extracting audio from the video file. Installation varies by platform.

- **macOS**: 
  ```bash
  brew install ffmpeg
  ```

- **Ubuntu**: 
  ```bash
  sudo apt-get install ffmpeg
  ```

- **Windows**: 
  Download and install from the official website: [FFmpeg Official Website](https://www.ffmpeg.org/download.html)

## Usage

1. Place the video file (`your_large_video_file.mp4`) in the same directory as the script.
  
2. Run the script.
    ```bash
    python your_script_name.py
    ```

## How it Works
1. `extract_audio_from_video` function is used to extract audio from the video.
2. `split_audio` function is used to split the audio into segments.
3. `ThreadPoolExecutor` is used for parallelizing the audio-to-text conversion.
4. All conversion results are sorted based on index to generate the final transcribed text.
