import random

max_loops = 3
swears = ["Cunt",
          "Shit",
          "Turd",
          "Fuck",
          "Ass",
          "Douche",
          "Ball",
          "Testicle",
          "Cock",
          "Dick",
          "Nut",
          "Sack",
          "Pussy",
          "Piss",
          "Cum",
          "Bitch",
          "Twat",
          "Tit",
          "Whore",
          "Nazi",
          "Queef",
          "Slut",
          "Asshole",
          "Bastard",
          "Anal"]
verbs = ["Licking",
         "Eating",
         "Loving",
         "Sucking",
         "Kissing",
         "Worshiping",
         "Guzzling",
         "Chugging",
         "Sniffing",
         "Pounding",
         "Gobbling",
         "Riding",
         "Grinding",
         "Banging",
         "Drinking",
         "Inhaling",
         "Huffing",
         "Rubbing",
         "Busting",
         "Squeezing",
         "Peddling",
         "Raping",
         "Fucking",
         "Douching",
         "Sounding",
         "Tossing",]
nouns = ["Waffle",
         "Egg",
         "Juice",
         "Butter",
         "Froth",
         "Foam",
         "Fluff",
         "Cheese",
         "Dumpling",
         "Noodle",
         "Nugget",
         "Toastada",
         "Fritter",
         "Cream",
         "Salami",
         "Taco",
         "Jelly",
         "Sausage",]

def insult():
    insult = []
    #Get loops
    loops = random.randrange(1,max_loops-1)
    #build insult list
    for i in range(1, max_loops-1):
        insult.append(random.choice(swears))
        insult.append(random.choice(verbs))
    insult.append(random.choice(swears))
    insult.append(random.choice(nouns))
    #join insult
    return ' '.join(insult)

print insult()