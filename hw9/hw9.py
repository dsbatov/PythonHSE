import re

def make_simple(lst):
    seen = set()
    res = []
    for x in lst:
        if x not in seen:
        	seen.add(x)
	        res.append(x)
    return res
def main(filename):
	with open(filename, encoding='utf-8') as f:
		text = f.read().lower().replace('\n', ' ').replace('\t', ' ').replace('\r', ' ').replace('\f', ' ').replace('\v', ' ').replace('!', ' ').replace('.', ' ').replace(';', ' ').replace(',', ' ').replace(':', ' ').replace('?', ' ').replace('/', ' ')
	res = []
	res1 = re.findall('программиру[а-я] ', text)
	res2 = re.findall('программиру[а-я][а-я] ', text)
	res3 = re.findall('программиру[а-я][а-я][а-я] ', text)
	res4 = re.findall('программирова[а-я] ', text)
	res5 = re.findall('программирова[а-я][^и] ', text)
	res6 = re.findall('программирова[а-я][^и][а-я] ', text)
	res7 = re.findall('программирова[а-я][^и][а-я][а-я] ', text)
	res = res1 + res2 + res3 + res4 + res5 + res6 + res7
	res = make_simple(res)
	print(*res)

main(input('Введите название файла: '))