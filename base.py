import urllib

class Base():
        def __init__(self):
                print "Kahoot Converter v1"
                print "\"What a shitty name\""
		self.url = {"testURL":"https://quizlet.com/110838121/test"}
base = Base()

try:
        # Get URL from user input.
        #url = raw_input("URL:")
	url = base.url["testURL"]
	
        # Open the given URL on url2.
        url2 = urllib.urlopen(url)

        # Read the data from the url to 'data'
        data = url2.read()

        # Close the url.
        url2.close()

        # Split the question data into an array of strings.
        qData = data.split("<span class='TermText qDef lang-en'>")[1].split("</span>")[0]
                        
        # Split the answer data into an array of strings.
        aData = data.split("<span class='TermText qWord lang-en'>")[1].split("<\/span>")[0]
except:
        # Exit if an error occurs.
        print ("Invalid URL")
        raw_input()
        exit()

print data
raw_input()
nudata = data.split("<span class='TermText qWord lang-en'>")
for i in range(3, 50):	
	print "[" + str(i) + "]" + nudata[i].split("</span>")[0]
raw_input()

while True:
        i = raw_input("Question:")
        print ""
        print data.split("<span class='TermText qDef lang-en'>")[int(i)].split("</span>")[0]
        print ""
        print data.split("<span class='TermText qWord lang-en'>")[int(i)].split("<\/span>")[0]
        print ""
        

raw_input()
