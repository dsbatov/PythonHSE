import os
import re

def openfile(filename):
	with open('news/' + filename, encoding='utf-8') as f:
		text = f.read().split('\n')
	return text
		
start_path = './news'
for root, dirs, files in os.walk(start_path):
	filelist = files
for filename in filelist:
	text = openfile(filename)
	with open(filename[:-5] + '.txt', 'w', encoding='cp1251') as fout:
			if not fout.writable():
				print('Файл закрыт')
			else:
				for line in text:
					tag = re.compile(r'<.*?>')
					line = tag.sub('', line)
					line = re.sub('`', '', line)
					if line.endswith(' '):
						fout.write(line)
					else:
						fout.write(line + ' ')

