# texto a voz
import pyttsx3
motor = pyttsx3.init()
texto="hola mundo,te leo un cuento"
motor.say(texto)
motor.runAndWait()