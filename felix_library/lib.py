from art import *
from random import randint


def randtext(intext):
    options = ["rnd-small","rnd-medium","rnd-large","rnd-xlarge","wizard"]
    tprint(intext,options[randint(0,4)])

def randoart():
    randart()

if __name__ == "__main__":
    randart()
    tprint("Felix was here","rnd-medium")
    print("But wait...")
    randtext("Felix was here")
    randtext("Felix was here")
