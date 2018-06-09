#задание 2
import re

dic = {}
with open('mystem.xml', encoding='utf-8') as f:
	fin = f.read().split('\n')
for i in range(len(fin)):
	if re.search('<w>', fin[i]):
		if re.search('gr=".*"', fin[i+1]):
			splited_line = fin[i+1].split()
			if splited_line[1][4:-1] in dic:
				dic[splited_line[1][4:-1]] += 1
			else:
				dic[splited_line[1][4:-1]] = 1

with open('output_2.txt', 'w', encoding='utf-8') as fout:
	if not fout.writable():
		print('Файл закрыт')
	else:
		for key in sorted(dic, key=dic.get, reverse=True):
			fout.write(key + '\n')