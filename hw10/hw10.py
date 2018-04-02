import re
def search(filename):
	with open(filename, encoding='utf-8') as f:
		text = f.read()
	text = text.splitlines()
	year = re.search('[0-9][0-9][0-9][0-9] год', str(text))
	year = year.group()
	return year

year = search(input('Введите название html-файла: '))

with open('output.txt', 'w', encoding='utf-8') as fout:
	fout.write(year)
	print('Результат находится в файле output.txt')
if not fout.writable:
    print("Файл закрыт")