import math
import platform
from posixpath import commonpath
import pyttsx3
import pyaudio
import speech_recognition as sr
import pywhatkit as pk
import datetime

alexa = pyttsx3.init()
alexa.say('Hello My name is alexa. How can I hel You sir')
alexa.runAndWait()




def talk(text):
    alexa.say(text)
    alexa.runAndWait()

# rate = engine.getProperty('rate')
# engine.setProperty('rate', 100)
# print(rate)











listener= sr.Recognizer()


def talk_command():
        try:
         with sr.Microphone() as source:
            print('listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
          
            if 'alexa' in command:
                command = command.replace("alexa", " ")
                print(command)


        except:
            pass
        return command

    
        
def run_alexa ():
 try:
    command = talk_command()
    if'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("current time is "+ time)
        print("current time is"+ time)

    elif 'play' in command:
        command = command.replace("play"," ")
        talk("playing "+ command)
        pk.playonyt(command)
    
    elif "about" in command:
        command = command.replace("about", "")
        command = command.replace("please tell me","")
        talk("please wait! I am telling you about " + command)
        history = pk.info(command, 2, True)
        talk(history)
    elif "your name" in command:
        talk("my name is Alexa.")
    
    elif "what is my name" in command :
        talk("Your name is Mahadi hasan")

    elif "today" in command:
        today = datetime.datetime.now()
        x = today.strftime("%A")
        talk(f"today {x}")
    elif "many days" in command:
        today = datetime.datetime.now()
        x = today.strftime("%j")
        talk(f"already you passed {x} days in this year")

    
    elif "pi value" in command:
        x = math.pi
        print(x)
        talk(f"pi value is {x}")


    elif "are you robot" in command:
        talk("Yes. but now I am used to computer software. after a few days, I will be the best robot in the world insha-allah")
        
    # elif "operating system i use" or "i use" in command:
    #     x = platform.system()
    #     talk(f"You use the {x} operating system")
    
   

    elif "this month name" in command:
         today = datetime.datetime.now()
         x = today.strftime("%B")
         talk(f"this month is {x}")




    elif "write" in command :
        talk("Please wait I am writing")
        pk.text_to_handwriting(command)
    elif "send message" in command:
        pk.sendwhatmsg("+8801714008698", "hello I am alexa", 21, 51
        )
    
    elif "send email" in command:
        pk.send_mail("c6h6ch3h@gmail.com","mahadihasan4281", "test text","Hello i am alexa","mahadikaushik8888@gmail.com")

    else:
        talk("Sorry sir! I can not understand but don't worry. I am search the google")
        pk.search(command)
 except:
  pass



# while True:

run_alexa()


























# engine = pyttsx3.init()

# rate = engine.getProperty('rate')
# print(rate)
# engine.setProperty('rate', 100)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# for i in range(5):
#     engine.say("ami vat khaici")
#     if i>3:
#         engine.say("Thank You Mahadi")


# engine.runAndWait()
# print(sr.Microphone.list_microphone_names())



# def sound_receive ():
