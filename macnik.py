import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listerner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def talk(text):
 engine.say(text)
 engine.runAndWait()
#so in this block i made mic as a source and make listern to listern the voice in the form of source
def take_command():
    try:
        with sr.Microphone() as source:
           print("listerning....")
           voice = listerner.listen(source)
           command = listerner.recognize_google(voice)
           command = command.lower()
           if 'nikki' in command:
              command = command.replace('nikki','')
              print(command)
        
    except:
         pass
    return command

def run_nikki():
    command = take_command()
    #print(command)
    if 'play' in command:
      song= command.replace('play','')
      talk('playing ' + song)
      pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p ')
        print(time)
        talk("current time is :" + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'exit' in command:
        return False    
    else:
        talk('Please say the command again.')
   
while True:    
  run_nikki() 
      
      