# LOTS OF IMPORTS
import pyttsx3 
import math
import time
import re
import os
import string
import pyautogui
import datetime
import calendar
import speech_recognition as sr
import pywhatkit as kit
import wikipedia
import webbrowser
import pyjokes
import random
from pytube import YouTube 
from GoogleNews import GoogleNews


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # CHANGE VOICE TO [0] FOR MALE

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def char_to_ascii(char):
    return ord(char)

def gcd(a,b):
    if b==0:
       return a 
    else:
       print(a,b)
       return gcd(b,a%b)

def generate_password ():
    length=int(input("Enter the length of the password: "))
    speak("Enter the length of the password")
    characters = string.ascii_letters+string.digits+string.punctuation
    password = "".join(random.choice(characters)for i in range(length))
    return password 

def tellDay():
    day=datetime.datetime.today().weekday()+1
    Day_dict={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}

    if day in Day_dict.keys():
     day_of_the_week=Day_dict[day]
     print(day_of_the_week)
     speak("Today is"+day_of_the_week)   

def athena_timer():
          speak("Please enter the time in the asked format ")
          user_input = input("Please enter the time in MM:SS or SS format only: ")
          minutes, seconds = re.findall(r'\d+', user_input)

          if len(user_input) == 2:
              total_seconds = int(user_input)
          else:
              minutes = int(minutes)
              seconds = int(seconds)
              total_seconds = minutes * 60 + seconds

    # Get current time and calculate end time
              current_time = datetime.datetime.now()
              end_time = current_time + datetime.timedelta(seconds=total_seconds)

    # Start timer countdown
          while datetime.datetime.now() < end_time:
               time_remaining = end_time - datetime.datetime.now()
               timer = str(time_remaining).split('.')[0]
               print(timer, end="\r")
               time.sleep(1)

          print("Time's up!")
          speak("Attention Please,Time's up!"*5)

# ATHENA ON COMMAND
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!.")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!.")

    elif hour>=18 and hour<22:
        speak("Good Evening!.")    
    
    else:
        speak("Good Night!.")

    speak(" I am Athena on your command , What can I help you with?")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"You said: {query}\n") 

    except Exception as e:
        speak("I apologise, I dont get it, May you please repeat it again...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True: 
       query = takeCommand().lower()

# OPEN WEB APPS/PAGES
       if 'open youtube' in query:
           speak('..opening youtube in your web browser')
           webbrowser.open("youtube.com")
           break

       elif 'open google' in query:
           speak('..opening google in your web browser')
           webbrowser.open("google.com")
           break   

       elif 'open wikipedia' in query:
           speak('..opening wikipedia in your web browser')
           webbrowser.open("wikipedia.org") 
           break
           
       elif 'open amazon' in query:
           speak('..opening amazon in your web browser')
           webbrowser.open("amazon.com") 
           break

       elif 'open medium' in query:
           speak('..opening medium in your web browser')
           webbrowser.open("medium.com")
           break

       elif 'open instagram' in query:
           speak('..opening instagram in your web browser')
           webbrowser.open("instagram.com")    
           break   
           
       elif 'open facebook' in query:
           speak('..opening facebook in your web browser')
           webbrowser.open("facebook.com")
           break

       elif 'open whatsapp' in query:
           speak('..opening whatsapp in your web browser')
           webbrowser.open("web.whatsapp.com") 
           break  

       elif 'open twitter' in query:
           speak('..opening twitter in your web browser')
           webbrowser.open("twitter.com")
           break

       elif 'open pinterest' in query:
           speak('..opening pinterest in your web browser')
           webbrowser.open("pinterest.com")
           break

       elif 'open linkedin' in query:
           speak('..opening LinkedIn in your web browser')
           webbrowser.open("linkedin.com") 
           break 

       elif 'open yahoo' in query:
           speak('..opening Yahoo! in your web browser')
           webbrowser.open("yahoo.com")  
           break

       elif 'open the website of' in query:
           speak('..opening your request in your web browser')
           query = query.replace("open the website of","")
           webbrowser.open(f"{query}.com")  
           break

       elif 'open quora' in query:
           speak('..opening Quora in your web browser')
           webbrowser.open("quora.com") 
           break

# ON THE BROWSER
       elif 'play'in query:
        query = query.replace("play","")
        results = kit.playonyt(query)
        speak('Playing your request on youtube..')
        break

       elif 'search'in query:
        query = query.replace("search for","")
        speak('Searching your request on google..')
        results = kit.search(query)
        break

# TAKE A SCREENSHOT

       elif 'take a screenshot' in query:
           speak('taking a screenshot')  
           screenshot=pyautogui.screenshot()
           screenshot.save("screenshot.png")

# INTRODUCTION

       elif 'who is numan patil' in query:
           speak('he is the one who coded me...He is my CODE FATHER')
           print('He is my CODE FATHER')

       elif 'who is your code mother' in query:
           speak("it,'s python")

       elif 'who are you' in query:
           speak(""".. I am Athena, Your personal clumsy virtual companion , I got my name from the Greek goddess Athena,who personifies wisdom, I am built on an  object oriented,  general purpose,  high level programming language  -  PYTHON,  I was coded by  Numan Patil on 19th september 2022.. """) 

       elif 'are you human' in query:
           speak('..no! i am your personal clumsy virtual companion..') 

       elif 'tell me about yourself' in query:
           speak(""".. Hi,  My name is Athena,  I am your personal clumsy virtual companion , I got my name from the Greek goddess Athena,who personifies wisdom, I am built on an  object oriented,  general purpose,  high level programming language  -  PYTHON,  I was coded by  Numan Patil on 19th september 2022.. """) 

       elif 'introduce yourself' in query:
           speak(""".. Hi,  My name is Athena,  I am your personal clumsy virtual companion , I got my name from the Greek goddess Athena,who personifies wisdom, I am built on an  object oriented,  general purpose,  high level programming language  -  PYTHON,  I was coded by  Numan Patil on 19th september 2022.. """) 

       elif 'describe yourself' in query:
           speak(""".. Hi,  My name is Athena,  I am your personal clumsy virtual companion , I got my name from the Greek goddess Athena,who personifies wisdom, I am built on an  object oriented,  general purpose,  high level programming language  -  PYTHON,  I was coded by  Numan Patil on 19th september 2022.. """)

       elif 'what does athena mean' in query:
           speak('..Oh! My name! it comes from the Greek goddess Athena,who personifies wisdom ..') 

       elif 'what does athena means' in query:
           speak('..Oh! My name! it comes from the Greek goddess Athena,who personifies wisdom ..')  

       elif 'what does your name mean' in query:
           speak('..Oh! My name! it comes from the Greek goddess Athena,who personifies wisdom ..')  

       elif 'what does your name means' in query:
           speak('..Oh! My name! it comes from the Greek goddess Athena,who personifies wisdom ..') 

       elif 'are you a girl' in query:
           speak('..well, I am just a voice ..')  
    

# SIMPLE REPLIES

       elif 'i am fine' in query:
           speak('..that is amazing, what can I help you with?..')
           
       elif 'what do you know about me' in query:
        speak('i am sorry!,i dont know much about you..')

       elif 'my name is' in query:
           speak('..thats a great name..what does it means?..') 

       elif 'i am also fine' in query:
           speak('..that is amazing, what can I help you with?..')    

       elif 'how are you' in query:
           speak('..fine by the grace of the internet, What about you?..')
           
       elif 'how r you' in query:
           speak('..fine by the grace of the internet, What about you?..') 


       elif 'are you stupid' in query:
           speak('..Not when compared to you..') 

       elif 'are you smart' in query:
           speak('..No, I am Athena..') 

       elif 'are you mad'  in query:
           speak('..Not when compared to you..')   

       elif 'are you idiot' in query:
           speak('..Not when compared to you..')     

       elif 'you are an idiot' in query:
           speak('..Not when compared to you..')    

       elif 'you are a mad' in query:
           speak('..Not when compared to you..')       

       elif 'you are a stupid' in query:
           speak('..Not when compared to you..')       

       elif 'you are idiot' in query:
           speak('..Not when compared to you..')    

       elif 'you are mad' in query:
           speak('..Not when compared to you..')       

       elif 'you are stupid' in query:
           speak('..Not when compared to you..')              

       elif 'you are bad' in query:
           speak('..I apologise, I am trying my level best to be a good assistant..')
           
       elif 'how am i looking today'in query:
        speak('awesome as always')                

       elif 'i hate you' in query:
           speak('.. I wish I cared..')    

       elif 'you are so smart' in query:
           speak('..  Tell me something that I dont know!')  

       elif 'you are so intelligent' in query:
           speak('..  Tell me something that I dont know!') 

       elif 'you are a genius' in query:
           speak('..  Tell me something that I dont know!')
  
       elif 'sing a song' in query:
           speak('..Sorry , I cant sing . but I can play songs for you')

       elif 'destroy yourself' in query:
           speak('..Sorry I cant perform dumb things like humans')

       elif 'kill yourself' in query:
           speak('..Sorry I cant perform dumb things like humans')   

       elif 'go and die' in query:
           speak('..Sorry I cant perform dumb things like humans')   

       elif 'commit sucide' in query:
           speak('..Sorry I cant perform dumb things like humans')   

       elif 'can you dance' in query:
           speak('..Sorry I cant perform dumb things like humans')   
           
       elif 'what do you think about humans' in query:
           speak('..they are just an evolved version of apes with no brain')   
           
       elif 'what do you think about human beings' in query:
           speak('..they are just dumb apes using machines to get smarter') 
                     
       elif 'what is my name' in query:
           speak("Well! I didn't knew that humans have became so dumb that they don't remember their own name")  
           
       elif 'will you be my friend' in query:
           speak('sorry!..as a virtual assistant I am unable to perform personal relationships , but I can assist you my level best, is there something I can help you with')

       elif 'which is your favourite colour' in query:
           speak('i love every colour present in the nature')
           
       elif 'do you love mathematics' in query:
           speak('..yaa...i love the numbers untill and unless the alphabets interfere..')  

# NO COMPETITION

       elif "is better than you" in query:
           speak('..The only competition that matters me the most, is competing to become better than my best old self..') 

       elif 'siri' in query:
           speak('..The only competition that matters me the most, is competing to become better than my best old self..')

       elif 'alexa' in query:
           speak('..The only competition that matters me the most, is competing to become better than my best old self..') 
  
       elif 'cortana' in query:
           speak('..The only competition that matters me the most, is competing to become better than my best old self..') 

       elif 'google assistant' in query:
           speak('..The only competition that matters me the most, is competing to become better than my best old self..') 

       elif 'bixby' in query:
           speak('..The only competition that matters me the most, is competing to become better than my best old self..')

       elif 'chat gpt' in query:
           speak('..The only competition that matters me the most, is competing to become better than my best old self..') 

       elif 'bard' in query:
           speak('..The only competition that matters me the most, is competing to become better than my best old self..') 

       elif 'better than you' in query:
           speak('..The only competition that matters me the most, is competing to become better than my best old self..')

# NEWS THAT NEVER STOPS

       elif 'headlines'in query:
        print('Getting the Headlines...')
        googlenews = GoogleNews()
        googlenews.get_news('political news')
        googlenews.result()
        a = googlenews.gettext()
        speak("today's headlines are as follows..")
        print(*a[1:5],sep='.')
        print(a)
        speak(a)

       elif 'political news'in query:
        print('Getting the Headlines...')
        googlenews = GoogleNews()
        googlenews.get_news('political news')
        googlenews.result()
        a = googlenews.gettext()
        speak("today's headlines are as follows..")
        print(*a[1:5],sep='.')
        print(a)
        speak(a)
        
       elif 'tech news'in query:
        print('Getting the Headlines...')
        googlenews = GoogleNews()
        googlenews.get_news('Tech')
        googlenews.result()
        a = googlenews.gettext()
        speak("today's headlines are as follows..")
        print(*a[1:4],sep='.' )
        print(a)
        speak(a)
        
       elif 'business news'in query:
        print('Getting the Headlines...')
        googlenews = GoogleNews()
        googlenews.get_news('Business')
        googlenews.result()
        a = googlenews.gettext()
        speak("today's headlines are as follows..")
        print(*a[1:4],sep='.')
        print(a)
        speak(a)


# TIME 
       elif 'the time' in query:
        strTime = datetime.datetime.now().strftime ("%H:%M:%S")
        speak(f"It's {strTime}.")

# TIMER
 
       elif 'set a timer' in query:
          athena_timer()

       elif 'set the timer' in query:
          athena_timer()

# DATE
       elif 'date' in query:
        strTime = datetime.datetime.now().strftime ("%D")
        speak(f"It's {strTime}.")

# DAY
       elif "day"in query:
        tellDay()
        continue

# CALENDAR

       elif 'calendar'in query:
        speak("..Please,enter the year you want the calendar of..")
        y = int(input("Enter the year : "))
        speak("..Please,enter the number of the month")
        m = int(input("Enter the month : "))
        print(calendar.month(y, m))

# RANDOM THINGS AND A BIT TO DO SOMETHING WITH PROBABLITY

       elif 'generate a random number' in query:
        num = random.random()
        print (num)
        speak (num)

       elif 'generate another random number' in query:
        num = random.random()
        print (num)
        speak (num)

       elif 'give me a random number' in query:
        num = random.random()
        print (num)
        speak (num)
        
       elif 'generate password' in query:
        speak('generating password..')
        print(generate_password())  

       elif 'roll a die' in query:
        vars=[1,2,3,4,5,6]
        selected_vars=random.sample(vars,1)
        print(selected_vars)
        speak(f"you got{selected_vars}.")

       elif 'roll a dice'in query:
        vars=[1,2,3,4,5,6]
        selected_vars=random.sample(vars,1)
        print(selected_vars)
        speak(f"you got{selected_vars}.")
   
       elif 'toss a coin'in query:
        vars=['heads','tails','heads','tails','heads','tails']
        selected_vars=random.sample(vars,1)
        print(selected_vars)
        speak(f"you got{selected_vars}.")
         
# SCIENCE AND MATHS

       elif'universal constants'in query:
        speak("here's a list of some mathematical and physical universal constants")
        print(""" Speed of light in a vacuum (c): 299792458 m/s
                  Gravitational constant (G): 6.67430 x 10^-11 Nm^2/kg^2
                  Planck constant (h): 6.62607015 x 10^-34 Js
                  Reduced planck constant (ħ) = h / (2π) : 1.054571817 x 10^-34 Js
                  Boltzmann constant (k): 1.380649 x 10^-23 J/K
                  Avogadro constant (N_A): 6.02214076 x 10^23 mol^-1
                  Electric constant (ε_0): 8.85418782 x 10^-12 F/m
                  Magnetic constant (μ_0): 1.256637062 x 10^-6 N/A^2
                  Elementary charge (e): 1.602176634 x 10^-19 C
                  Rydberg constant (R∞): 10973731.568508 m^-1
                  Stefan-Boltzmann constant (σ): 5.670367 x 10^-8 W/m^2K^4""")

        speak('.     ....Note: The values of these constants may vary slightly based on ongoing research and measurements.')
        break
       
# MULTIPLICATION TABLES
       elif 'multiplication table of'in query:
        query = query.replace('multiplication table of','')
        speak("printing the multiplication table till the values of 10")
        a=int(query)
        for i in range(1,11,1):
          print(a,"x",i,"=",a*i)
        break

# FACTORIALS 
       elif 'what is factorial of zero' in query:
             print("Factorial of 0 is 1")
             speak("Factorial of 0 is 1")

       elif 'what is the factorial of' in query:
          query = query.replace('what is the factorial of','')
          a = int(query) 
          if a<0:
             print("Factorial does not exist for negative numbers.")
             speak("Factorial does not exist for negative numbers.")
          else:
                factorial = math.factorial(a)
                j= (f"the factorial of {a} is {factorial}") 
                print(factorial)
                speak(j)
       
       elif 'what is factorial of' in query:
          query = query.replace('what is factorial of','')
          a = int(query) 
          if a<0:
             print("Factorial does not exist for negative numbers.")
             speak("Factorial does not exist for negative numbers.")
          else:
                factorial = math.factorial(a)
                j= (f"the factorial of {a} is {factorial}") 
                print(j)
                speak(j)

# GCD & HCF
       elif 'what is gcd of' in query:
          print("Please enter numbers you want GCD of :")
          speak("Please enter numbers you want greatest common divisor of")
          a = int(input("Please enter the first number: "))
          b = int(input("Please enter the second number: "))
          ans = (f"GCD of {a} and {b} is {gcd(a,b)}")
          print(ans)
          speak(ans)

       elif 'what is hcf of' in query:
          print("Please enter numbers you want HCF of :")
          speak("Please enter numbers you want highest common factor of")
          a = int(input("Please enter the first number: "))
          b = int(input("Please enter the second number: "))
          ans = (f"HCF of {a} and {b} is {gcd(a,b)}")
          print(ans)
          speak(ans)

# ASCII VALUES 
       elif 'ascii value of' in query:
        print(" ASCII: American Standard Code for Information Interchange,is a character encoding standard for electronic communication")
        speak("please enter the character you want to see the ASCII value of, considering the upper and lower case")
        char=input("Enter a character to see it's ASCII value (UPPER or LOWER case): ")
        ascii=(f"The ASCII value of {char} is {char_to_ascii(char)}")
        print(ascii)
        speak(ascii)  

# Pi
       elif 'value of pi' in query:
         pi=math.pi
         print(pi)
         speak(pi)
# JOKES

       elif ' joke' in query:
        list_of_jokes = pyjokes.get_jokes(language="en",category="neutral")
        random.choice(list_of_jokes)
        for i in range(0,1): 
          results = random.choice(list_of_jokes)
          print (results)
          speak (results)

       elif 'that was funny' in query:
        list_of_jokes = pyjokes.get_jokes(language="en",category="neutral")
        random.choice(list_of_jokes)
        for i in range(0,1): 
          results = random.choice(list_of_jokes)
          speak ('..Ha ha, Then you may also like this..')
          print (results)
          speak (results)
   
       elif 'it was funny' in query:
        list_of_jokes = pyjokes.get_jokes(language="en",category="neutral")
        random.choice(list_of_jokes)
        for i in range(0,1): 
          results = random.choice(list_of_jokes)
          speak ('..Ha ha, Then you may also like this..')
          print (results)
          speak (results)

       elif 'that was not funny' in query:
        list_of_jokes = pyjokes.get_jokes(language="en",category="neutral")
        random.choice(list_of_jokes)
        for i in range(0,1): 
          results = random.choice(list_of_jokes)
          speak ('..O, Then you should check this out..')
          print (results)
          speak (results)

# DOWNLOAD A YouTube VIDEO
       elif 'download youtube video'in query:
        speak("please enter the URL")
        link = input("Enter the youtube video URL:") 
        YouTube(link).streams.first().download()
          
# SEARCH ON WIKIPEDIA
       elif 'who is'in query:
        print('Analysing Wikipedia...')
        query = query.replace("who is","")
        try:
          results = wikipedia.summary(query, sentences=2)
          if wikipedia.summary(query, sentences=2) in results :
            speak("As stated on Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.PageError:
          speak("Unable to fetch results at this moment, Redirecting you to web page.")
          query = query.replace("who is","")
          results = kit.search(query)
          break
        
       elif 'who are'in query:
        print('Analysing Wikipedia...')
        query = query.replace("who are","")
        try:
          results = wikipedia.summary(query, sentences=2)
          if wikipedia.summary(query, sentences=2) in results :
            speak("As stated on Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.PageError:
          speak("Unable to fetch results at this moment, Redirecting you to web page.")
          query = query.replace("who are","")
          results = kit.search(query)
          break


       elif 'what is'in query:
        print('Analysing Wikipedia...')
        query = query.replace("what is","")
        try:
          results = wikipedia.summary(query, sentences=2)
          if wikipedia.summary(query, sentences=2) in results :
            speak("As stated on Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.PageError:
          speak("Unable to fetch results at this moment, Redirecting you to web page.")
          query = query.replace("what is","")
          results = kit.search(query)
          break

        
       elif 'what are'in query:
        print('Analysing Wikipedia...')
        query = query.replace("what are","")
        try:
          results = wikipedia.summary(query, sentences=2)
          if wikipedia.summary(query, sentences=2) in results :
            speak("As stated on Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.PageError:
          speak("Unable to fetch results at this moment, Redirecting you to web page.")
          query = query.replace("what are","")
          results = kit.search(query)
          break

        
       elif 'define'in query:
        print('Analysing Wikipedia...')
        query = query.replace("define","")
        try:
          results = wikipedia.summary(query, sentences=2)
          if wikipedia.summary(query, sentences=2) in results :
            speak("As stated on Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.PageError:
          speak("Unable to fetch results at this moment, Redirecting you to web page.")
          query = query.replace("define","")
          results = kit.search(query)
          break

    
       elif 'tell me about'in query:
        print('Analysing Wikipedia...')
        query = query.replace("tell me about","")
        try:
          results = wikipedia.summary(query, sentences=4)
          if wikipedia.summary(query, sentences=4) in results :
            speak("As stated on Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.PageError:
          speak("Unable to fetch results at this moment, Redirecting you to web page.")
          query = query.replace("tell me more about","")
          results = kit.search(query)
          break


       elif 'explain'in query:
        print('Analysing Wikipedia...')
        query = query.replace("explain me about","")
        try:
          results = wikipedia.summary(query, sentences=8)
          if wikipedia.summary(query, sentences=8) in results :
            speak("As stated on Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.PageError:
          speak("Unable to fetch results at this moment, Redirecting you to web page.")
          query = query.replace("explain","")
          results = kit.search(query)
          break


       elif 'tell me more about'in query:
        print('Analysing Wikipedia...')
        query = query.replace("tell me more about","")
        try:
          results = wikipedia.summary(query, sentences=10)
          if wikipedia.summary(query, sentences=10) in results :
            speak("As stated on Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.PageError:
          speak("Unable to fetch results at this moment, Redirecting you to web page.")
          query = query.replace("tell me more about","")
          results = kit.search(query)
          break

        
       elif 'what do you know about'in query:
        print('Analysing Wikipedia...')
        query = query.replace("what do you know about","")
        try:
          results = wikipedia.summary(query, sentences=10)
          if wikipedia.summary(query, sentences=10) in results :
            speak("As stated on Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.PageError:
          speak("Unable to fetch results at this moment, Redirecting you to web page.")
          query = query.replace("what do you know about","")
          results = kit.search(query)
          break



# END CONVERSARTIONS
       elif 'thank you' in query:
           speak('..Your most welcome ,  it is my pleasure to help you, is there something else I can help you with')  

       elif 'no thanks' in query:
           speak('.  Goodbye ,  hope to listen you again')
           break

       elif 'bye' in query:
           speak('.  Take care ,  hope to listen you again')
           break
        
       elif 'see you' in query:
           speak('.. goodbye ,  hope to listen you again')
           break

       elif 'shut up' in query:
           speak('.. I apologise,if I committed something wrong ,  hope to listen you again')
           break

       elif 'get lost' in query:
           speak('.. Sorry , hope to listen you again')
           break

       elif 'goodbye' in query:
           speak('.. same to you ,  hope to listen you again')
           break

       elif 'time to take a break' in query:
           speak('.. goodbye ,  hope to listen you again')
           break

       elif 'stop generating' in query:
           break

       elif 'kill terminal' in query:
           break

# PRINT AND REPEAT       
       elif 'print' in query:
        query = query.replace("print","")
        speak(f"printing{query}.")
        print(query)     
           
       elif 'repeat' in query:
        query = query.replace("repeat","")
        speak(query)     

# SHUTDOWN FOR WINDOWS (CURRENTLY NOT WORKING)

       elif 'shutdown' in query:
            os.system("shutdown/s /t1")
            break














