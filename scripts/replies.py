import pyttsx3
from calculateCoffeeCups import numCupsLeft
from getCoffeeHabits import cupsPerDay

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

daysLeft = round(numCupsLeft / cupsPerDay)
daysLeft
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sayNumCupsDays():
    speak(f"{numCupsLeft} cups left. You're good for {daysLeft} days.")

def sayFullTank():
    speak("Your Coffee Tank CC is really full.")

def sayLowTank():
    speak("Your Coffee Tank CC is low.")

def halfTank():
    speak("Your Coffee Tank CC is half full.")

def sayMoreHalfTank():
    speak("You have more than Half of your Coffee Tank CC.")

def sayLessHalfTank():
    speak("You have less than Half of your Coffee Tank CC.")

def sayNoCups():
    speak("Your Coffee Tank CC is empty.")

def sayOrder():
    speak("Go to your app to refuel and order more coffee.")

def sayAddQueue():
    speak("Go to your app to add next coffee to the queue.")

# test
#sayLowTank()