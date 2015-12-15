import urllib

class Base():
	def __init__(self):
		print "Kahoot Converter v1"
		print "\"What a shitty name\""
base = Base()

try:
	url = raw_input("URL:")
	
	url2 = urllib.urlopen(url)

	data = url2.read()

	url2.close()
	
	newData = data.split("<span class='TermText qDef lang-en'>")[1].split("</span>")[0]
except:
	print ("Invalid URL")
	raw_input()
	exit()

print newData

raw_input()
