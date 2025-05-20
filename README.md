# -Real-Time-Speech-recogonizer-for-Audionce
Personal Project

# 🎙️ Real-Time Subtitle Generator for Presentations

## 🧠 Overview

This project aims to build a real-time speech recognition system that uses voice input to transcribe spoken words and intelligently match them with content on presentation slides. The system will enhance audience engagement and accessibility by displaying synchronized subtitles as the presenter speaks, making it easier for viewers to follow along with the presentation in real time.

---

## 📌 Features (Planned)

- 🎤 Live speech-to-text transcription
- 🧩 Matching spoken content with slide text (semantic similarity)
- 🖥️ Overlay subtitles on current slide
- 🌐 Support for multiple languages (future extension)
- ⚡ Real-time performance (low-latency display)

---

## 🛠️ Tech Stack

| Component              | Tool/Framework                     |
|------------------------|------------------------------------|
| Speech Recognition     | [Whisper](https://github.com/openai/whisper) / Google Speech API / Vosk |
| Text Matching          | Sentence-BERT, spaCy, or TF-IDF cosine similarity |
| Slide Parsing          | PDF.js (for PDFs), or Python `python-pptx` |
| Overlay Subtitles      | PyGame / OpenCV / HTML Canvas (if browser-based) |
| Language Support       | Whisper multilingual / fine-tuning language models |
| UI/Frontend (Optional) | Electron / Flask + React           |

---

## 🧩 System Design

```mermaid
graph TD
A[Microphone Input] --> B[Speech Recognition Engine]
B --> C[Live Transcript]
C --> D[Slide Text Matching]
D --> E[Subtitle Display on Slide]
