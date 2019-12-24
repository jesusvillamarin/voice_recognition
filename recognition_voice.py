import speech_recognition as sr
from time import ctime
import webbrowser
r =  sr.Recognizer()


def voice_recognition(ask = False): 
    recognition_result = ''
    with sr.Microphone() as source:
        if ask: print(ask) 
        else: print('¿Te puedo ayudar en algo?')
        audio_data = r.listen(source)
        try:
            recognition_result = r.recognize_google(audio_data, language='es-CO')
        except sr.UnknownValueError:
            print('Lo siento, no escuche que dijiste!')
        except sr.RequestError():
            print('Me estoy tomando un descanso! Intenta mas tarde')

    return recognition_result

def recognize_action(action_data):
    action_data = action_data.lower()
    print(action_data)
    if 'adiós' in action_data:
        print('Hasta luego, fue un gusto servirle')
        exit()
    if 'qué hora es' in action_data: 
        print(f'El tiempo actual es: {ctime()}')
    if 'buscar' in action_data:
        to_search = voice_recognition('¿Que quisieras buscar?')
        url = f'https://google.com/search?q={to_search}'
        webbrowser.get().open(url)
        print(f'Esto fue lo que encontro para: {to_search}')
    if 'encontrar ubicación' in action_data:
        location = voice_recognition('¿Cual es la ubicación?')
        url = f'https://google.nl/maps/place/{location}/&amp'
        webbrowser.get().open(url)
        print(f'Esto fue lo que encontro para: {location}')

if __name__ == "__main__":
    print('Initializing Voice Recognition...')
    while True:
        action_data = voice_recognition()
        recognize_action(action_data)