import speech_recognition
import pyttsx3
from datetime import date, datetime
ai_ear = speech_recognition.Recognizer()
ai_mouth = pyttsx3.init()
ai_brain = ""
while True:
    with speech_recognition.Microphone() as mic:
        print("Ai:I'm listening")
        audio = ai_ear.listen(mic)

    print("Ai:...")

    try:
        you = ai_ear.recognize_google(audio)
    except:
        you == ""
    print ("You: " +you)

    if you == "":
        ai_brain = " i can't hear you, try again,please!"
    elif  "hello" in you:
        ai_brain =  "Hello Bella"
    elif "today" in you:
        today = date.today()
        ai_brain = today.strftime("%B %D, %Y")
    elif "time" in you:
        now = datetime.now()
        ai_brain =  now.strftime("%H hours %M minutes %S seconds")
    elif "Who are you?" in you:
        ai_brain = "Your friend!"
    elif "bye" in you:
        ai_brain = "Bye! Bella"
        print("Ai: " + ai_brain)
        ai_mouth.say(ai_brain)
        ai_mouth.runAndWait()
        break
    else:
        ai_brain="I didn't get that. Could yoy try again?"

    print("Ai: " +ai_brain)
    ai_mouth.say(ai_brain)
    ai_mouth.runAndWait()