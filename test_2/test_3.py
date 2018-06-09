import re
with open('mystem.xml', encoding='utf-8') as f:
	fin = f.read().split('\n')
with open('output_3.txt', 'w', encoding='utf-8') as fout:
	if not fout.writable():
		print('Файл закрыт')
	else:
		for i in range(len(fin)):
			if re.search('сов', fin[i]) and not re.search('несов', fin[i]) and re.search('ед', fin[i]):
				fout.write(fin[i+1] + '\n')

with open('mystem.xml', encoding='utf-8') as f:
	fin = f.read().split('\n')
sign = False
mystem_prom = []
for line in fin:
	if re.search('<body>', line):
		sign = True
	if re.search('</body>', line):
		sign = False
	if sign == True:
		line = re.sub('<ana ', '', line)
		line = re.sub('</?w>', '', line)
		line = re.sub('</?se>', '', line)
		line = re.sub('/?>', '', line)
		if line != '':
			mystem_prom.append(line)
with open('mystem.csv', 'w', encoding='utf-8') as fout:
	if not fout.writable():
		print('Файл закрыт')
	else:
		for i in range(len(mystem_prom)-1):
			line = mystem_prom[i]
			if re.search('gr=".*"', line):
				res = line.split()
				fout.write(res[1][5:-1])
				fout.write(',')
				gr = re.sub(',', ' ', res[0][4:-1])
				fout.write(gr)
				fout.write(',')
				fout.write(mystem_prom[i+1])
				fout.write('\n')