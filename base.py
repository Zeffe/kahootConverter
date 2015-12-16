import urllib
#import requests

class Base():
        def __init__(self):
                print "Kahoot Converter v1"
                print "\"Wowzers!\""
                self.url = {"testURL":"https://quizlet.com/110838121/test?mult_choice=on&prompt-with=1&limit=40"}
base = Base()

def login():
        username = raw_input("Kahoot User: ")
        password = raw_input("Kahoot Pass: ")

        login_data = {'action': 'login', 'username' : username, 'password': password}

        with session() as c:
                c.post('https://create.kahoot.it/?_ga=1.134240756.405763457.1450244410&deviceId=416f204e-7f4f-4f88-a547-524c3e96541a#login?next=', login_data)
                response = c.get('https://create.kahoot.it/?_ga=1.74582866.1723042493.1450152659&deviceId=36a26ec0-9c01-4508-842a-c568568d5d85#quiz/685130be-26c5-48d2-a376-ec7c0b656e03/edit')
                print(response.headers)
                print(response.text)
        

#def login():
#        logUrl = "https://getkahoot.com/"
#        session = requests.session()
#        kUser = raw_input("Kahoot User: ")
#        kPass = raw_input("Kahoot Pass: ")
#        email = ''
#        password = ''
#        login_data = {
#                kUser : email,
#                kPass : password,
#                'submit' : 'login',
#                }
#        r = session.post(url, data=login_data)
#        r = session.get('https://create.kahoot.it/?_ga=1.74582866.1723042493.1450152659&deviceId=36a26ec0-9c01-4508-842a-c568568d5d85#quiz/685130be-26c5-48d2-a376-ec7c0b656e03/edit')
#        print r

firstLoop = True
while firstLoop:
        try:
                # Get URL from user input.
                url = raw_input("URL:")
                
                if url == "test":
                        url = base.url["testURL"]
                
                # Open the given URL on url2.
                url2 = urllib.urlopen(url)

                # Read the data from the url to 'data'
                data = url2.read()

                title = data.split("<title>Test: ")[1].split(" | Quizlet</title>")[0]
                
                # Close the url.
                url2.close()

                confirm = raw_input("Read from Quizlet: " + title + " (Y/N):")
                if confirm.lower() == "y":
                        firstLoop = False
        except:
                # Exit if an error occurs.
                print ("Invalid URL")
                raw_input()

# Split the html at the question identifiers.
aData = data.split("<span class='TermText qWord lang-en'>")
# Split the html at the answer identifiers.
qData = data.split("<span class='TermText qDef lang-en'>")
# Get the title of the quizlet as a string.
title = data.split("<title>Test: ")[1].split(" | Quizlet</title>")[0]

print title

correct = 0

# Loop for each member of the list.
for i in range(1, len(qData)):
        # Print the question with question number.
        print "[Q" + str(i) + "]" + qData[i].split("</span>")[0]
        # Loop 4 times, once for each answer.
        for j in range(1, 5):
                # Print the answer with numbers 1-4.
                nuString = "[A" + str(j) + "]" + aData[i + j].split("</span>")[0]
		if "='1'" in aData[i + j].split("value")[1]:
			nuString = nuString + "@CORRECT" 
                print nuString
                correct += 1
#login()
print str(correct)
raw_input()
