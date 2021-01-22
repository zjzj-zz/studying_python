fileObj = open("sample.txt", "r")
while True:
	fileText = fileObj.readline()
	if not fileText:
		break
	print fileText
fileObj.close()
