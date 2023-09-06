Audio Transcription from Video using Python
Overview
このプロジェクトは、与えられたビデオファイルから音声を抽出し、その音声を文字に変換（文字起こし）するPythonスクリプトです。並列処理を活用して高速に文字起こしを行います。

Requirements
Python 3.x
FFmpeg
pydub
speech_recognition
concurrent.futures (Python Standard Library)
Installation
Python Dependencies
Pythonの依存関係をインストールするには、以下のコマンドを実行してください。

bash
Copy code
pip install pydub
pip install SpeechRecognition
FFmpeg
このプロジェクトでは、ビデオファイルから音声を抽出するためにFFmpegが必要です。FFmpegのインストール方法はプラットフォームによって異なります。

macOS:

bash
Copy code
brew install ffmpeg
Ubuntu:

bash
Copy code
sudo apt-get install ffmpeg
Windows:
公式サイトからダウンロードしてインストール: FFmpeg Official Website

Usage
スクリプトと同じディレクトリにビデオファイル（your_large_video_file.mp4）を配置します。

スクリプトを実行します。

bash
Copy code
python your_script_name.py
How it Works
extract_audio_from_video関数でビデオから音声を抽出します。
split_audio関数で音声を小片に分割します。
ThreadPoolExecutorを使用して並列に音声を文字に変換します。
すべての変換結果をインデックスに基づいてソートし、最終的な文字起こしテキストを生成します。
