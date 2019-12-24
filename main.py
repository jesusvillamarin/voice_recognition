# install speechRecognition from https://pypi.org/project/SpeechRecognition/
# ====================================
#   REQUERIMENTS
#   * PyAudio from https://pypi.org/project/PyAudio/
# ====================================

import speech_recognition as sr
recognizer = sr.Recognizer()

def voice_recognition():
    print('Initializing Voice Recognition')
    with sr.Microphone() as source:
        voice_data = ''
        audio = ''
        audio = recognizer.listen(source)
        try:
            print('Say something')
            voice_data = recognizer.recognize_sphinx(audio)
        except sr.UnknownValueError:
            print('An error has occurred')
        except sr.RequestError:
            print('Voice recognition service is down😣')
    return voice_data


def recognize_action(voice_data):
    print('Recognize task')
    print(voice_data)
    if 'serie' in voice_data:
        print('La mejor serie de Netflix')


voice_data = voice_recognition()
recognize_action(voice_data)
# if __name__ == "__main__":
