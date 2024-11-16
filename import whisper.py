import whisper # type: ignore
import sounddevice as sd # type: ignore
from scipy.io.wavfile import write # type: ignore

def record_audio(duration, fs=44100):
    print("Grabando...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Espera a que termine la grabación
    write("command.wav", fs, audio)  # Guardar como archivo de audio
    print("Grabación completa")

def recognize_speech():
    model = whisper.load_model("base")
    result = model.transcribe("command.wav")
    return result["text"]

# Grabamos audio y lo reconocemos
record_audio(5)  # Grabación de 5 segundos
text = recognize_speech()
print(f"Reconocido: {text}")
