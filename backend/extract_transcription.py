from faster_whisper import WhisperModel


def transcribe_video(audio_file: str) -> list[str]:
    model_size = "large-v2"
    whisper_model = WhisperModel(
        model_size,
        device="cuda",
        device_index=0,
        compute_type="float32",
        local_files_only=True,
    )
    segments, _ = whisper_model.transcribe(
        audio_file,
        vad_filter=True,
        word_timestamps=True,
        language="fr",
        task="transcribe",
    )

    return segments
