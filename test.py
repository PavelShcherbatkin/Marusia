import speech_recognition as sr
import time
import os
from gtts import gTTS
from pygame import mixer
from questions import questions


def say(phrase, lg='ru', file_name='standart.mp3'):
    tts = gTTS(text=phrase, lang='ru')
    with open(file_name, 'wb') as f:
        tts.write_to_fp(f)
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.1)   
    mixer.music.unload()
    mixer.quit()
    os.remove(file_name)


def record_answer(try_answer):
    r = sr.Recognizer()
    file_name = 'answer.mp3'
    with sr.Microphone() as source:
        say('Итак, ваш ответ', file_name=file_name)
        print("Скажите что-нибудь!")
        audio = r.listen(source)
    try:
        phrase = "Вы сказали: " + r.recognize_google(audio, language='ru')
        print(phrase)
        say(phrase, file_name=file_name)
        if try_answer in phrase or try_answer.upper() in phrase:
            lead = 'Это абслолютно правильный ответ\nПереходим к следующему вопросу!'
            say(lead)
        else:
            lead = 'Увы, но вы дали неправильный ответ и проиграли'
            say(lead)
            exit()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        say("Google Speech Recognition could not understand audio", lg='en', file_name=file_name)
        # запустить запись еще раз record_answer()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        say("Google Speech Recognition could not understand audio", lg='en', file_name=file_name)

for i in range(15):
    if i == 0:
        say('Добро пожаловать в игру "Кто хочет стать миллионером". Сегодня Паша попытаеться выиграть три миллиона рублей. Получиться ли у него. Узнаем сегодня. Привет Паша.')
        say('Итак, первый вопрос на 500 рублей.')
    elif i == 1:
        say('Итак, второй вопрос на 1000 рублей.')
    elif i == 2:
        say('Итак, третий вопрос на 2000 рублей.')
    elif i == 3:
        say('Итак, четвертый вопрос на 3000 рублей.')
    elif i == 4:
        say('Итак, пятый вопрос на 5000 рублей.')
    elif i == 5:
        say('Итак, шестой вопрос на 10000 рублей.')
    elif i == 6:
        say('Итак, седьмой вопрос на 15000 рублей.')
    elif i == 7:
        say('Итак, восьмой вопрос на 25000 рублей.')
    elif i == 8:
        say('Итак, девятый вопрос на 50000 рублей.')
    elif i == 9:
        say('Итак, десятый вопрос на 100000 рублей.')
    elif i == 10:
        say('Итак, одиннадцатый вопрос на 200000 рублей.')
    elif i == 11:
        say('Итак, двенадцатый вопрос на 400000 рублей.')
    elif i == 12:
        say('Итак, тринадцатый вопрос на 800000 рублей.')
    elif i == 13:
        say('Итак, четырнадцатый вопрос на 1500000 рублей.')
    elif i == 14:
        say('Итак, последний пятнадцатый вопрос на 3000000 рублей.')
    

    file_name = 'question.mp3'
    say(questions[i], file_name=file_name)
    say('У вас 10 секунд на подумать!')
    print('У вас 10 секунд на подумать!')
    print(questions[i])
    time.sleep(10)
    record_answer('б')
