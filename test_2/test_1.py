#задание 1
import re
cnt = 0
sign = False
with open('mystem.xml', encoding='utf-8') as f:
	fin = f.read().split('\n')
for line in fin:
	if re.search('<body>', line):
		sign = True
	if re.search('</body>', line):
		sign = False
	if sign == True:
		cnt += len(line)

with open('output_1.txt', 'w', encoding='utf-8') as fout:
	if not fout.writable():
		print('Файл закрыт')
	else:	
		fout.write(str(cnt))