dic = {"BBS":"City", "XYZ":"Hunter"}
print dic
print dic["XYZ"]
dic["XYZ"] = "Connection"
print dic
print dic.has_key("XYZ")
print dic.has_key("ABC")
del dic["XYZ"]
print dic

dic["XYZ"] = "Hunter"
for i in dic:
	print i
	print dic[i]
print len(dic)

dic["Angel"] = "Heart"
print dic
print len(dic)
