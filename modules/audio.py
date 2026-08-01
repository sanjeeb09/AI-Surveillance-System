import sounddevice as sd
import numpy as np

# Shared audio level
audio_level = 0.0


def audio_callback(indata, frames, time, status):
    global audio_level

    if status:
        return

    volume = np.sqrt(np.mean(indata ** 2))

    # Scale it (adjust later if needed)
    audio_level = min(float(volume * 20), 1.0)


def start_audio_stream():

    stream = sd.InputStream(
        channels=1,
        samplerate=44100,
        callback=audio_callback
    )

    stream.start()

    return stream


def get_audio_level():
    return audio_level