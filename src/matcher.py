# Load saved embedding
priest_embedding = np.load("data/embeddings/priest.npy")

# Record a new sample
from record_audio import record
record("temp.wav", duration=3)

# Embed new voice
test_wav = preprocess_wav("temp.wav")
test_embedding = encoder.embed_utterance(test_wav)

# Compare similarity
similarity = np.dot(priest_embedding, test_embedding)
print("🔍 Similarity score:", similarity)

if similarity > 0.75:
    print(" Speaker is likely the priest")
else:
    print(" Not the priest")
