from requests_html import HTMLSession
from pocketsphinx import LiveSpeech
from requests_html import HTMLSession
import speak
import weather

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
def Weather():
    s  =  HTMLSession()
    query = "patna"
    url = f'https://www.google.com/search?q=weather+{query}'
    r  = s.get(url , headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'})

    temp  = r.html.find('span#wob_tm' , first= True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t' , first= True).text
    desc  = r.html.find('span#wob_dc' , first= True).text
    return temp+" "+unit+" "+ desc

if __name__=="__main__":
    voice_data=speech_to_text()
    
    if voice_data:
        if "weather" in voice_data:
            result=weather()
            if result:
                print("weather:{}".format(result))
                speak.speak("the current weather is{}".format(result))
    else:
        print("action not recognized")
        print("speech recognition failed")
        
