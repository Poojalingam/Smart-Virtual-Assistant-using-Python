
from pocketsphinx import LiveSpeech
import datetime
import speak
import webbrowser
import weather
import os
import pyjokes
import action

from newspaper import Newspaper
class Newspaper():
    def logging(self,s):
        import logging as lg
        lg.basicConfig(filename="News.log", level=lg.INFO, format='%(asctime)s %(message)s')
        lg.info(str(s))
        
    def readMe(self,str):
        from win32com.client import Dispatch
        try:
            speak=Dispatch("SAPI.SpVoice")
            speak.Speak(str)
        except Exception as e:
            self.logging(e)
        
    def getNews(self):
        import requests
        import json
        try:
            # Get api key from newsapi.org and sourse too
            url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=863a6520fd8a4991b9fcf9db77571f29')
            # converting request in text form
            news = requests.get(url).text
            news_dt = json.loads(news)
            articles = news_dt['articles']
            for i in articles:
                self.readMe(i['title'])
        except Exception as e:
            self.logging(e)
        
if __name__ == '__main__':
    obj1=Newspaper()
    obj1.readMe("News in India")
    obj1.getNews()
    obj1.readMe("Thanks for listening news.")


def speech_to_text():
    speech=LiveSpeech()
    
    try:
        for phrase in speech:    
         return str(phrase)
    except KeyboardInterrupt as e:
        pass
    
    except Exception as e:
        print("error:{}".format(e))
        speak.speak("sorry,an error occured during speech recognition")


def Action(send) :   
  
    data_btn  = send.lower()
    

    if "what is your name" in   data_btn :
      speak.speak("my name is virtual Assistant")  
      return "my name is virtual Assistant"

    elif "hello" in data_btn  or "hi" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey sir, How i can  help you !")  
        return "Hey sir, How i can  help you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "joke" in data_btn :
            p1=pyjokes.get_joke()
            speak.speak(p1)
            return p1  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://music.youtube.com/")   
        speak.speak("music.youtube.com is now ready for you, enjoy your music")                   
        return "music.youtube.com is now ready for you, enjoy your music"

    elif "whatsapp" in data_btn or "song" in data_btn:
        webbrowser.open("https://web.whatsapp.com/")   
        speak.speak("web.whatsapp.com is now ready for you")                   
        return "web.whatsapp.com is now ready for you"

    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn :
        ans   = weather.Weather()
        speak.speak(ans) 
        return ans
    
    elif 'read news' in data_btn :
        newspaper=Newspaper()
        news_result=newspaper.getNews()
        return news_result         
    elif 'notepad' in data_btn :
        ur1='C:\\Windows\\system32\\notepad.exe'
        os.startfile(os.path.join(ur1))
        speak.speak("open notepad...")
        return "open notepad..."
    
    elif 'cmd' in data_btn :
        ur1='C:\\Windows\\system32\\cmd.exe'
        os.startfile(os.path.join(ur1))
        speak.speak("open cmd prompt...")
        return "open cmd prompt..."  
    
    elif 'pictures' in data_btn :
        ur1='D:\\pictures'
        os.startfile(os.path.join(ur1))
        speak.speak("your pictiures...")
        return "your pictures..."  
    
    elif 'videos' in data_btn :
        ur1='D:\\videos'
        os.startfile(os.path.join(ur1))
        speak.speak("your videos...")
        return "your videos..."  
    
    elif 'desktop' in data_btn :
        ur1='C:\\Users\\ELCOT\\Desktop'
        os.startfile(os.path.join(ur1))
        speak.speak("desktop open...")
        return "desktop open..."  

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..."
    
    elif "newspaper" in data_btn:
        url = "https://www.thehindu.com/"
        webbrowser.get().open(url)
        speak.speak("Opening The Hindu newspaper in Chrome.")
        return "Opening The Hindu newspaper in Chrome."

    else :
        speak.speak( "i'm able to understand!")
        return "i'm able to understand!" 
    
if __name__=="__main__":
    voice_data=speech_to_text()

    if voice_data:
        result=action()
        print("you said:{}".format(result))
        
    else:
        print("speech recognition failed")
        

    