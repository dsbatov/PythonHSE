import os
import re
cnt = 0
filelist = sorted(os.listdir())
for filename in filelist:
	path = './' + filename
	if os.path.isdir(path):
		filename = str(filename)
		match = re.search('[^а-яА-Я\n\t\r\f\v ]', filename)
		if match:
			pass
		else:
			cnt += 1
			print(filename)
	else:
		pass
print(cnt)