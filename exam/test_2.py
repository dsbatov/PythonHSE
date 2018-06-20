import os
import re

def openfile(filename):
	with open('news/' + filename, encoding='utf-8') as f:
		text = f.read().split('\n')
	return text
	
dic = {}	
start_path = './news'
for root, dirs, files in os.walk(start_path):
	filelist = files
for filename in filelist:
	text = openfile(filename)
	for line in text:
		if re.search('<ana', line):
			splited_line = line.split()
			lem = splited_line[1][5:-1]
			lem = str(lem)
			if re.search('[А-ЯЁ][а-яё]', lem):
				print(lem)
				if lem in dic:
					dic[lem] += 1
				else:
					dic[lem] = 1
with open('output.txt', 'w', encoding='utf-8') as fout:
	for key, value in dic.items():
		if not fout.writable():
				print('Файл закрыт')
			else:
				fout.write(key + '\t' + value + '\n')