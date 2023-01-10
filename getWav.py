"""
Пробуем делать waw из m4a
"""
import os
from pydub import AudioSegment
#import ffmpeg

def get_wav():#videoname: str
	m4a_file = "D:\\PYTHON\\Programms\\audio\\speech.m4a"
	wav_filename = r"D:\\PYTHON\\Programms\\audio\\speech_.wav"
	track = AudioSegment.from_file(m4a_file, format='m4a')
	file_handle = track.export(wav_filename, format='wav')

	"""com1 = f"ffmpeg -i {videoname} speech.mp3"
	com2 = "ffmpeg -i speech.mp3 speech.wav"
	os.system(com1)
	os.system(com2)"""

get_wav()
