
import sounddevice as sd
import soundfile as sf
import os

def record(filename, duration=5):
    fs = 16000
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    #print(sd.query_devices())
    # #sd.default.device = 1  # 👈 use your mic input index here
    sd.default.device = 2

    print(f"🎤 Recording '{filename}' for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write(filename, audio, fs)
    print("✅ Recording saved to:", filename)
    
record("data/sample_voices/deacon.wav", duration=5)
