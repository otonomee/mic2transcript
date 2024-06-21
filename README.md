# Real-Time Transcription CLI Tool

This CLI tool continuously transcribes audio from the device's built-in microphone to a text file, providing an ongoing log of 
ambient audio as text. It utilizes the Whisper model for real-time audio transcription.

## Requirements

- Python 3.6+
- sounddevice
- numpy
- whisper

## Installation

1. Clone this repository: `https://github.com/otonomee/continuous-mic-transcribe`
2. Install the required packages: 
```
pip install -r requirements.txt
```

## Usage
To start the transcription, run the tool from the terminal: 
```
python main.py
```

You will be prompted to select a Whisper model and specify an output file name for the transcriptions.

The tool will run in the background, transcribing any detected audio into the specified text file. Press 'q' in the terminal to stop 
the transcription process.

## License
This project is open-sourced under the MIT License.
