import os
import speech_recognition as sr
import docx
from datetime import datetime

def wav2ytext(language="ru-RU"):
	r = sr.Recognizer()
	path = "D:\\PYTHON\\Programms\\audio"
	AUDIO_FILE  = os.path.join(path,"speech.wav")
	try:
		with sr.WavFile(AUDIO_FILE) as source:
			audio0 = r.record(source, duration=100) #продолжительность 100 с.
			audio = r.record(source)
			# audio = r.listen(source)
		start_time = datetime.now()

		print(datetime.now() - start_time)
		text0 = r.recognize_google(audio0, language=language)
		text = r.recognize_google(audio, language=language)
		mydoc.add_paragraph(text)
		#Сохранение в документ word
		mydoc.save("doc\\speech.docx")
		print("Время выполнения: ")
		print(datetime.now() - start_time)
	except:
		print("Done")

mydoc = docx.Document()
wav2ytext("ru-RU")