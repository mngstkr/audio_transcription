import subprocess
from pydub import AudioSegment
from concurrent.futures import ThreadPoolExecutor
import speech_recognition as sr

# MKVをMP4に変換する関数
def convert_to_mp4(input_file):
    output_file = input_file.replace('.mkv', '.mp4')
    command = f"ffmpeg -i {input_file} {output_file}"
    subprocess.run(command, shell=True)
    return output_file

# ビデオから音声を抽出する関数
def extract_audio_from_video(video_path, video_format):
    audio = AudioSegment.from_file(video_path, format=video_format)
    return audio

# 音声をセグメントに分割
def split_audio(audio, segment_length=10000):
    segments = []
    for i in range(0, len(audio), segment_length):
        segments.append((i, audio[i:i + segment_length]))
    return segments

# 音声をテキストに変換
def transcribe_audio(index, audio_segment):
    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(audio_segment.raw_data, audio_segment.frame_rate, audio_segment.frame_width)
    try:
        text = recognizer.recognize_google(audio_data, language='ja-JP')
        return (index, text)
    except sr.RequestError as e:
        return (index, f"APIリクエストエラー: {e}")
    except sr.UnknownValueError:
        return (index, "音声認識に失敗")

if __name__ == "__main__":
    # 入力となるビデオファイルのパス
    video_path = "your_large_video_file.mkv"  # MKV形式であることを仮定

    # MKV形式の場合はMP4に変換
    if video_path.endswith('.mkv'):
        video_path = convert_to_mp4(video_path)

    # ビデオのフォーマット（MP4に変換された場合は"mp4"になる）
    video_format = video_path.split('.')[-1]

    # ビデオから音声を抽出
    audio = extract_audio_from_video(video_path, video_format)

    # 音声をセグメントに分割(音声ファイルが大きい場合は、分割してAPIに送信する必要がある為)
    segments = split_audio(audio)

    # 音声認識を並列で実行
    # ThreadPoolExecutorを使用して、各音声セグメントに対してtranscribe_audio関数を非同期に適用。
    # lambda p: transcribe_audio(*p) は、split_audioで生成されたセグメント、インデックスをtranscribe_audio関数に適用するためのラムダ関数。
    # executor.mapは、各セグメントに対して非同期にtranscribe_audioを呼び出し、結果（インデックスとテキスト）を"results"リストに格納。
    transcriptions = []
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda p: transcribe_audio(*p), segments))

    # 結果をインデックスでソートしてテキストだけ取り出す
    # 各セグメントが非同期に処理されるため、結果は時間順には並んでいない可能性があるため、各結果に付与されたインデックスを使用してソート。
    sorted_results = sorted(results, key=lambda x: x[0])
    sorted_transcriptions = [text for _, text in sorted_results]

    # 全体の文字起こしを生成
    full_transcription = ' '.join(sorted_transcriptions)
    print("全文の文字起こし:")
    print(full_transcription)
