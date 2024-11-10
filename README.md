# Text-to-Speech (TTS) with Accents

This Python script uses the **Google Text-to-Speech (gTTS)** library to convert text into speech, supporting multiple English accents. It provides a simple interface to input text and choose an accent (American, British, or Australian). The output speech is played back using the **playsound** library.

---

## Features

- Converts text to speech using Google TTS.
- Supports multiple English accents:
  - **American**
  - **British**
  - **Australian**
- Plays the generated speech immediately.
- Cleans up temporary files after playback.

---

## Prerequisites

Ensure the following Python packages are installed:

1. **gTTS**  
   Install using:
   ```bash
   pip install gTTS
   ```

2. **playsound**  
   Install using:
   ```bash
   pip install playsound
   ```

3. **tempfile** and **os**  
   These are built-in Python modules and require no additional installation.

---

## Usage

1. Clone or download the script to your local machine.
2. Run the script:
   ```bash
   python script_name.py
   ```
3. Input the sentence you want to be pronounced.
4. Select the desired accent: American, British, or Australian.
5. Listen to the generated speech.

---

## Example Workflow

- **Input Sentence**: "Hello, how are you?"  
- **Selected Accent**: British  
- **Output**: The script converts the text into speech with a British accent and plays it back.

---

## File Cleanup

The script uses a temporary file to store the TTS audio, which is automatically deleted after playback.

---

## Limitations

1. The gTTS library supports a limited set of accents. For non-English languages or accents, refer to the gTTS documentation.
2. British and Australian accents are approximated based on gTTS's capabilities and may not be fully accurate.

---

## Potential Issues

1. **Playsound Compatibility**: On some systems, the playsound library may not function as expected. For alternatives, consider using other audio playback libraries such as `pydub` or `pygame`.
2. **Internet Connection**: The gTTS library requires an active internet connection to generate speech.

---

Enjoy converting your text to speech! 😊
