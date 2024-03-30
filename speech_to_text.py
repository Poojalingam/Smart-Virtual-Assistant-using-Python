from pocketsphinx import LiveSpeech
import speak



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
if __name__=="__main__":
    result=speech_to_text()
    if result:
        print("you said:{}".format(result))
    else:
        print("speech recognition failed")
        