import sounddevice as sd
import numpy as np
import whisper
import queue

# Initialize a queue to hold audio chunks
audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    """ This is called for each audio chunk """
    if status:
        print(status)
    # Add the audio chunk to the queue
    audio_queue.put(indata.copy())

def transcribe_stream():
    """ Transcribe the audio from the queue """
    model = whisper.load_model("large")  # Load a larger model for better accuracy
    audio_buffer = np.array([], dtype=np.float32)  # Buffer to accumulate audio
    transcription = ""  # String to hold the transcription

    while True:
        # Get an audio chunk from the queue
        chunk = audio_queue.get()
        if chunk is None:
            break
        audio_buffer = np.concatenate((audio_buffer, chunk[:, 0]))

        # Check if we have enough audio to transcribe
        if len(audio_buffer) >= 16000 * 1:  # e.g., 3 seconds of audio
            result = model.transcribe(audio_buffer, task="transcribe")
            transcription += result['text'] + " "
            print("\rTranscription: " + transcription, end="")
            audio_buffer = np.array([], dtype=np.float32)  # Clear the buffer

def main():
    try:
        # Start the audio stream
        with sd.InputStream(callback=audio_callback, dtype='float32', channels=1, samplerate=16000):
            print("Starting transcription. Speak into your microphone.")
            transcribe_stream()
    except KeyboardInterrupt:
        print("\nTranscription stopped.")
        exit()

if __name__ == "__main__":
    main()
