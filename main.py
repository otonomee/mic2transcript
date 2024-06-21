from realtime_transcription import RealtimeTranscriber

if __name__ == "__main__":
    transcriber = RealtimeTranscriber()
    transcriber.check_for_termination()
    transcriber.run()
