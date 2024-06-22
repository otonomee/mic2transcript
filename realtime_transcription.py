import sounddevice as sd
import numpy as np
import whisper
import queue
import datetime
import os
import sys
import threading


class RealtimeTranscriber:
    def __init__(self):
        self.audio_queue = queue.Queue()
        self.models = ["tiny", "base", "small", "medium", "large"]

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.audio_queue.put(indata.copy())

    def check_and_load_model(self, model_name):
        print(f"Loading model: {model_name}")
        return whisper.load_model(model_name)

    def transcribe_stream(self, model, output_file):
        audio_buffer = np.array([], dtype=np.float32)
        transcription = ""

        with open(output_file, "a") as f:
            while True:
                if not self.audio_queue.empty():
                    chunk = self.audio_queue.get()
                    if chunk is None:
                        break
                    audio_buffer = np.concatenate((audio_buffer, chunk[:, 0]))

                    if len(audio_buffer) >= 16000 * 1:
                        result = model.transcribe(audio_buffer, task="transcribe")
                        transcription = result["text"]
                        timestamp = datetime.datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                        print(f"\r{timestamp}: {transcription}", end="")
                        f.write(f"{timestamp}: {transcription}\n")
                        audio_buffer = np.array([], dtype=np.float32)

    def run(self):
        print("Select a model for transcription:")
        for i, model in enumerate(self.models, start=1):
            print(f"{i}: {model}")
        choice = input("Enter your choice (1-5): ")
        model_name = self.models[int(choice) - 1]

        output_file = input("Enter the output file name: ")
        if not output_file.endswith(".txt"):
            output_file += ".txt"

        model = self.check_and_load_model(model_name)

        try:
            with sd.InputStream(
                callback=self.audio_callback,
                dtype="float32",
                channels=1,
                samplerate=16000,
            ):
                print(
                    "Starting transcription. Speak into your microphone. Press 'q' to stop."
                )
                self.transcribe_stream(model, output_file)
        except KeyboardInterrupt:
            print("\nTranscription stopped.")
        os.system(f"open {output_file}")

    def check_for_termination(self):
        def check():
            while True:
                if input() == "q":
                    self.audio_queue.put(None)
                    break

        threading.Thread(target=check, daemon=True).start()
