# mic2transcript

mic2transcript is a CLI tool that will continuously transcribe audio from the device's built-in microphone to a text file using OpenAI Whisper.

## CLI User Inputs 
- <output-file-name>.txt
- <whisper-model>
  - `tiny`: Fastest, lowest accuracy. Suitable for quick transcriptions or resource-constrained environments.
  - `medium`: Balanced performance. Good for general use, offering a trade-off between speed and accuracy.
  - `large`: Highest accuracy, slowest speed. Best for scenarios requiring maximum transcription quality.

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
