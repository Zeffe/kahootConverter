import urllib

class Base():
        def __init__(self):
                print "Kahoot Converter v1"
                print "\"What a shitty name\""
                self.url = {"testURL":"https://quizlet.com/110838121/test?mult_choice=on&prompt-with=1&limit=40"}
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
except:
        # Exit if an error occurs.
        print ("Invalid URL")
        raw_input()
        exit()

aData = data.split("<span class='TermText qWord lang-en'>")
qData = data.split("<span class='TermText qDef lang-en'>")

count = 0
for i in range(1, len(qData)):
        print "[Q" + str(i) + "]" + qData[i].split("</span>")[0]
        count = 0
	for j in range(1, 5):
                count += 1
                print "[A" + str(j) + "]" + aData[i + count].split("</span>")[0]
raw_input()
