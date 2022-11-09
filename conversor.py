import pyttsx3

robo = pyttsx3.init()

msg_robo = input('O que você tem a dizer?')

robo.say(msg_robo)

robo.runAndWait()