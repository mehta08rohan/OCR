from PIL import Image
import pytesseract
from textblob import TextBlob
from gtts import gTTS
import playsound
import cv2



pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




def image_to_text(path):
    try:
        # img = Image.open(path)
        img = cv2.imread(path)
        text=pytesseract.image_to_string(img,lang="hin")
        # print(TextBlob(text).detect_language())
        return text
    except FileNotFoundError :
        print('Path Does Not Exist')

def translate_to_eng(string, to_lang="en"):
    blob = TextBlob(string)
    lang_detect = blob.detect_language()
    translated = blob.translate(to=to_lang)
    return translated

def speak(text , lang):
    tts = gTTS(text, lang=lang)
    filename= "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


if __name__ =="__main__":
    pic_text_conversion = image_to_text(r'C:\Users\rohan.mehta\PycharmProjects\OCR\hindi.jpg')
    print(pic_text_conversion)
    print('*'*15)

    # translate_to_eng(pic_text_conversion, "en")
    # translate_to_eng("god","hi")

    text_in_eng = str(translate_to_eng(pic_text_conversion, "en"))
    print(text_in_eng)
    # speak(text_in_eng,lang="en")
    speak(pic_text_conversion,"hi")






