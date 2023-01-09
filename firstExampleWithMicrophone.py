"""
Главный файл экспериментов

Вводим слово, число и число
"""



import speech_recognition as sr


def firstFunctionToSpeechRecognition(r,mic):
    #Главная функция для распознавания речи
    # Возможно использование нескольких вариантов библиотек обработки языка
    # recognizer_instance.recognize_sphinx,
    # recognizer_instance.recognize_google,
    # recognizer_instance.recognize_wit,
    # recognizer_instance.recognize_bing,
    # recognizer_instance.recognize_api,
    # recognizer_instance.recognize_houndify,
    # recognizer_instance.recognize_ibm.
    with mic as source:
        print("Говорите что нибудь!")
        audio = r.listen(source)



    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        result = r.recognize_google(audio, language="ru-RU")
        print("Google Speech Recognition думает, что вы сказали: " + result)
    except sr.UnknownValueError:
        print("Google Speech Recognition не понимает, что вы сказали")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return result
# obtain audio from the microphone
list_mic = sr.Microphone.list_microphone_names()
dict_mic = {}
for i in range(0, len(list_mic)):
    dict_mic[i] = list_mic[i]
    # Проверка, какой девайс работает
    if (0 == 1):
        r = sr.Recognizer()
        with sr.Microphone(device_index=i) as source:
            try:
                audio = r.listen(source)
                print("Устройство " + str(i) + " принимает аудио")
            except:
                print("Устройство " + str(i) + " не работает")

mic = sr.Microphone(device_index=0)
r = sr.Recognizer()

#Пробный тест сказать что-нибудь
firstSentence = firstFunctionToSpeechRecognition(r,mic)

print("Назовите число A")
firstNumber = firstFunctionToSpeechRecognition(r,mic)
print("Назовите число B")
secondNumber = firstFunctionToSpeechRecognition(r,mic)
print("Результат сложения двух чисел = "+ str(int(firstNumber) + int(secondNumber)))