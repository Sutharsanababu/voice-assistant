import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            engine.say("sir i am responsible")
            engine.say("i what can help for you")
            engine.runAndWait()
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if "tiger" in command:
                command = command.replace("tiger", "")
    except:
        pass
    return command

def run_assistant():
    command = get_command()
    
    if "play" in command or "need video" in command or "want video" in command or "need song" in command or "want song" in command:
        song = command.replace("play", "")
        pywhatkit.playonyt(song)
        talk("my process done")
        
    elif "what is time" in command or "now time" in command or "time" in command:
        time = datetime.datetime.now().strftime("%H:%M %p")
        talk("Now time is " + time)
        print(time)
        

    elif "tell me about" in command:
        about = command.replace("tell me about", "")
        info = wikipedia.summary(about, 5)
        talk(info)
        
    elif "exit now" in command or "turn off" in command or "stop the chat" in command:
        talk("good bye")
        return False  # Instead of using 'break', return False to stop the loop
            
    elif "search" in command:
         query = command.replace("search", "")
         search_url = f"https://www.google.com/search?q={query}"
         webbrowser.open(search_url)
         talk("my process done")
         
    elif "locatio" in command:
        query1 = command.replace("location", "")
        search_map = f"https://www.google.com/maps/search/{query1}"
        webbrowser.open(search_map)
        talk("my process done")
    
    else:
        talk("sorry i can't understand tell me again")
    
    return True  # Return True to continue the loop

while True:
    if not run_assistant():  # Check if run_assistant returns False, then break the loop
        break
