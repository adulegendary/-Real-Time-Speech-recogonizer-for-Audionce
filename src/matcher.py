from resemblyzer import VoiceEncoder, preprocess_wav

encoder = VoiceEncoder()

# Load pre-recorded samples
def get_reference_embeddings():
    roles = ["priest", "deacon", "audience"]
    embeddings = {}
    for role in roles:
        wav = preprocess_wav(f"data/voices/{role}.wav")
        embeddings[role] = encoder.embed_utterance(wav)
    return embeddings

reference_embeddings = get_reference_embeddings()
