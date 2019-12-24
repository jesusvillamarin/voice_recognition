import speech_recognition as sr
r =  sr.Recognizer()

def voice_recognition(): 
    print('Initializing Voice Recognition...')
    recognition_result = ''
    with sr.Microphone() as source:
        print('¿Te puedo ayudar en algo?')
        audio_data = r.listen(source)
        try:
            recognition_result = r.recognize_google(audio_data, language='es-CO')
        except sr.UnknownValueError:
            print('Lo siento, no escuche que dijiste!')
        except sr.RequestError():
            print('Me estoy tomando un descanso! Intenta mas tarde')

    return recognition_result

if __name__ == "__main__":
    while True:
        print(voice_recognition())