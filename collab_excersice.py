print("One Piece is the best anime ever!") #Aggrey
print("Aric is a jerk (Joking, spare me)") #Lizandro 
print("I love cats") #Johana
print("lets skip this exam!!") #Beimnet


import sys
import argparse


#example topic not real
plants = ["trees", "flowers", "shrubs", "herbs","tulips","roses","daisies","bushes"
          "ferns","mosses","cacti","vines","grasses","palms","sunflowers","lilies",
          "orchids","daffodils","irises","marigolds","lavender", "jasmine","peonies",
          "begonias","chrysanthemums","hydrangeas","azaleas","camellias","gardenias","grasses",
          "bamboo","succulents","aloe vera","sage","thyme","rosemary","basil","mint","oregano",
          "cilantro","parsley","dill","fennel","chives","lemongrass","tarragon","bay leaves",
          "coriander","lavender","echinacea","ginseng","chamomile","valerian"]

animals = ["dog", "cat", "elephant", "tiger","lion","bear","wolf","fox",
           "giraffe","zebra","kangaroo","panda","monkey","rabbit","deer",
           "squirrel","hedgehog","otter","raccoon","badger","beaver", "moose"
           ,"buffalo","bison","antelope","cheetah","leopard","hyena","jaguar",
           "cougar","lynx","bobcat","caracal","ocelot","tapir","armadillo",
           "sloth","anteater","porcupine","wombat","echidna","platypus","dingo",\
            "quokka","quoll","numbat","bandicoot","monkeypox","lemur","tarsier",
           "marmoset","capuchin","howler","spider monkey","sakin","uakari",
           "colobus","langur","gibbon","siamang","orangutan","chimpanze","lizard",
            "gecko","iguana","chameleon","anole","skink","monitor","python",]

sports = ["soccer", "basketball", "baseball", "tennis","golf","cricket",
          "rugby","hockey","volleyball","badminton","table tennis","swimming",
          "cycling","running","boxing","wrestling","skiing","snowboarding", "skateboarding",
          "surfing","sailing","rowing","fishing","archery","fencing","gymnastics",
          "weightlifting","yoga","pilates","aerobics","dance","cheerleading",
          "karate","judo","taekwondo","kickboxing","mixed martial arts","triathlon",
          "marathon","ultramarathon","hiking","climbing","caving","orienteering",
          "parkour","bouldering","curling","luge","skeleton","bobsledding",
          "handball","water polo","synchronized swimming","diving","triathlon",]

topicdict = {
    "plants": plants,
    "animals": animals,
    "sports": sports,}


alphabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def LCD():
    print("Welcome to the word game!")
    gamepick = input("Please pick a topic from the following list:\n"
                     "1.plants\n"
                     "2. animals\n")
    guess = input("Using the space given enter your plant guesses: ")
    
   