# record_sample.py

import sounddevice as sd
import soundfile as sf

print(sd.query_devices())
print("it getting executed")
# def record(filename, duration=5):
#     fs = 16000  # 16 kHz sample rate
#     print(f"🎤 Recording '{filename}' for {duration} seconds...")
#     audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
#     sd.wait()
#     sf.write(filename, audio, fs)
#     print("✅ Recording saved to:", filename)
#
#
# # EXAMPLE USAGE:
# record("data/voices/priest.wav", duration=5)
