import speech_recognition as sr

# Función que permite reconocer la voz
listen = sr.Recognizer()

def escucho():
    try:

        with sr.Microphone() as source:
            print("Dime algo: ")
            pc = listen.listen(source)
            req = listen.recognize_google(pc, language="es-ES")
            print("Has dicho: {}".format(req))
    except Exception as e:

        print("No te he entendido", format(e))
    

escucho()