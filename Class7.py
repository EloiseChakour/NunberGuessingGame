import requests
import time

myServer = "http://142.157.81.60:5000"

#r = requests.get(myServer+"testGET/", params = {"testing":"123"})
#print(r.text)


# Number Guessing Game

#print(R.text)

name = input ("Enter your name")
guess = input ("Enter your guess")

R = requests.get("http://142.157.81.60:5000/guess", params = {"name": name.strip(), "number" : guess.strip()})

response = R.text
if response == "equal":
        print ("Yay! Congrats, you got it!")
#print (R.text)

while response != "equal":
    print(response)
    Guess = input ("Enter your new guess")
    newGuess = Guess.strip()
    request = requests.get("http://142.157.81.60:5000/guess", params = {"name": name, "number" : newGuess})
    response = request.text
    if response == "equal":
        print ("Yay! Congrats, you got it!")


