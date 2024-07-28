import speech_recognition as sr

def recognize_speech_from_mic(mic_index=9):
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=mic_index) as source:
        print("Please speak something...")
        audio_data = recognizer.listen(source)
        print("Recognizing...")
        
        try:
            text = recognizer.recognize_google(audio_data)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your network connection.")

if __name__ == "__main__":
    recognize_speech_from_mic()
