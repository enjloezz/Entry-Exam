import requests
import re
from PIL import Image, ImageDraw

s = requests.Session()
flag = ""
while "sun" not in flag:
	f = s.get("http://ee.sunshinectf.org/exam")
	regex = r"<li>(.*?)<\/li>"
	matches = re.finditer(regex, f.text, re.MULTILINE | re.DOTALL)
	results = []
	for matchNum, match in enumerate(matches, start=1):
		for groupNum in range(0, len(match.groups())):
			groupNum = groupNum + 1
			results.append(match.group(groupNum))
	result = []
	for i in range(0, 100, 5):
		r = (int(eval(results[i])))
		if r == int(results[i+1]):
			result.append("A")
		elif r == int(results[i+2]):
			result.append("B")
		elif r == int(results[i+3]):
			result.append("C")
		elif r == int(results[i+4]):
			result.append("D")
	im = Image.open("scantron.png")
	draw = ImageDraw.Draw(im)
	for i in range(0, 20):
		x = 333 if i < 10 else 823
		y = 431
		if result[i] == "A":
			x += 0
		elif result[i] == "B":
			x += 68
		elif result[i] == "C":
			x += 136
		elif result[i] == "D":
			x += 204
		y += (i % 10) * 90
		draw.ellipse((x, y, x+59, y+59), fill = 'black', outline ='black')
	im.save("test.png")
	f = s.post("http://ee.sunshinectf.org/exam", files = {'file': open('test.png','rb')})
	flag = f.text
	print("FLAG is coming, just be patient")
print(flag)


