"""
Пробуем делать waw из m4a
"""
import os
from pydub import AudioSegment
#import ffmpeg

def get_wav(file_name, new_name):#videoname: str
	path = "D:\\PYTHON\\Programms\\audio"
	m4a_file = os.path.join(path, file_name)
	wav_filename = r"D:\\PYTHON\\Programms\\audio\\" + new_name
	track = AudioSegment.from_file(m4a_file, format='m4a')
	file_handle = track.export(wav_filename, format='wav')

	"""com1 = f"ffmpeg -i {videoname} speech.mp3"
	com2 = "ffmpeg -i speech.mp3 speech.wav"
	os.system(com1)
	os.system(com2)"""
if (1==1):
	file_name = "speech.m4a"
	new_name = "speech_.wav"
else:
	file_name = "20230315_121601.m4a"
	new_name = "20230315_121601_.wav"
get_wav(file_name, new_name)
