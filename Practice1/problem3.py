import pyttsx3
engine = pyttsx3.init()


rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 1)

engine.say("I will be participating in a 5 days workshop on Python for Automation.")
engine.runAndWait()