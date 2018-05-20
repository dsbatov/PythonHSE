import os

def this_level(extensions, start_path):
	for root, dirs, files in os.walk(start_path):
		for file in files:
			name, ext = os.path.splitext(file)
			extensions.append(ext)
		if dirs != []:	
			for direct in dirs:
				this_level(extensions, start_path + direct)
	return extensions

extensions_list = this_level([], '.')

def freq(extensions_list):
	freq = {}
	for ext in extensions_list:
		if ext in freq:
			freq[ext] += 1
		else:
			freq[ext] = 1
		new_freq = {value: key for key, value in freq.items()} 
		maxim = max(new_freq.keys())
		return new_freq[maxim]

print(freq(extensions_list))