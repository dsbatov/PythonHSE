import re
with open('linguistics.txt', encoding='utf-8') as f:
	text = f.read()
text = text.splitlines()
result = re.sub('язык', 'шашлык', str(text))
result = re.sub('шашлыко', 'языко', str(result))
result = re.sub('Язык', 'Шашлык', str(result))
result = re.sub('Шашлыко', 'Языко', str(result))
result = re.sub('меташашлык', 'метаязык', str(result))
result = re.sub('Меташашлык', 'Метаязык', str(result))
with open('output.txt', 'w', encoding='utf-8') as fout:
	fout.write(result)
	print('Результат находится в файле output.txt')
if not fout.writable:
    print("Файл закрыт")