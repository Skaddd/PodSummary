from src.extract_transcription import transcribe_video


if __name__ == "__main__":
    audio_file = (
        r"./data/podcasts/Gagner de largent en codant comme débutant !.mp4"
    )
    transcriptions = transcribe_video(audio_file)
    print(transcriptions)
