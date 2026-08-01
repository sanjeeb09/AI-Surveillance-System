from modules.audio import start_audio_stream
from modules.camera import start_camera

if __name__ == "__main__":

    audio_stream = start_audio_stream()

    try:
        start_camera()

    finally:
        audio_stream.stop()
        audio_stream.close()