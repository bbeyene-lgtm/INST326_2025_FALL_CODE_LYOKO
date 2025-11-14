print("One Piece is the best anime ever!") #Aggrey
print("Aric is a jerk (Joking, spare me)") #Lizandro 
print("I love cats") #Johana
print("lets skip this exam!!") #Beimnet


import sys
import argparse

alphabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#example topic not real
plants = ["trees", "flowers", "shrubs", "herbs","tulips","roses","daisies","bushes"
          "ferns","mosses","cacti","vines","grasses","palms","sunflowers","lilies",
          "orchids","daffodils","irises","marigolds","lavender","jasmine","peonies"]

animals = ["dog", "cat", "elephant", "tiger","lion","giraffe","zebra","bear",
           "wolf","fox","deer","rabbit","squirrel","monkey","gorilla","panda",
           "kangaroo","koala","hippopotamus","rhinoceros","crocodile","alligator",
           "snake","lizard","frog","toad","fish","shark","dolphin","whale", "octopus",
           "squid","crab","lobster","jellyfish","starfish","seahorse","coral", "rat",
           "mouse","bat","owl","eagle","parrot","penguin","peacock","turkey","chicken",
           "duck","goose","swan","ant","bee","butterfly","moth","grasshopper","cricket"]

sports = ["soccer", "basketball", "tennis", "baseball","football","hockey","golf",
          "cricket","rugby","volleyball","swimming","cycling","running","skiing",
          "boxing","wrestling","badminton","table tennis","fencing","archery",
          "surfing", "skiing","skateboarding","snowboarding","gymnastics","rowing",
          "equestrian","triathlon","handball","water polo","curling"]

topicdict = {"plants": plants, "animals": animals, "sports": sports}



def GCD():
    lettercount = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,
                   "k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,
                   "v":0,"w":0,"x":0,"y":0,"z":0}
    for topic in topicdict.values():
        for word in topic:
            for letter in word:
                if letter in lettercount:
                    lettercount[letter] += 1
    print(lettercount)
    return lettercount
    
    gamepick = input("Please pick a topic from the following list:\n"
                     "1.plants\n"
                     "2. animals\n"
                     "3. sports\n")
    for letter in alphabetlist:
        lettercount = letter()
    
    guess = input("Using the space given enter your plant guesses: ")
GCD()
    
   