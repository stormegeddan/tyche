import sys
import os
import random
import time

luck = 0
hasHadTea = False
theWindow = False
mirrorMirrorOTW = False
myClothes = False

def thestart(): 
    print()
    print("The waiting room is dingy, dark and stinks of cigarettes")
    print("The anticipation prickles down my spine.")
    print("It's almost time, time to test my luck...")
    print("time to fight to the death.")
    print()
    print("Who knows? Maybe I'll lose, my luck breaking for the first time in my life.")
    print("Finally the one left broken and bleeding on the filthy ground")
    print("The thought both terrifies and excites me.")
    print()
    print("I feel ready to fight.")
    print()
    when()

def when():
    print("Start the match? (y) / Take some more time? (n)")

    startinput = input()
    directions = ["y","Y","n","N"]
    
    while startinput not in directions:
        print("Please enter a valid option.")
        startinput = input()

    if startinput == "y" or startinput == "Y":
        print("I move to stand in front of the door,")
        print("the sound of the crowd echoing through the wood.")
        nerves()
        
    elif startinput == "n" or startinput == "N":
        print("I decide to stay a bit longer.") 
        print("Maybe I should calm my nerves a bit?")
        thechoice()
        
def nerves():
    global luck
    print("(aren't you nervous? you could die?) (y/n)")

    nerves = input()
    directions = ["y","Y","n","N"]

    while nerves not in directions:
        thegame()
    
    if nerves == "y" or nerves == "Y":
        luck += 1
        print("(okay follow my lead; breathe in, hold for five seconds...)")
        print()
        print()
        print("(now breathe out slowly... let your head clear...)")
        print()
        print("(breathe in...)")
        print("(...)")
        print("(...breathe out...)")
        print("(...)")
        print()
        print()
        print("I breathe deeply one final time and open the door...")
        thegame()

    elif nerves == "n" or nerves == "N":
        thegame()

def thechoice():
    global hasHadTea
    
    print("I look around the room")
    print("Maybe I could…")
    print()
    print("Drink some tea? (1) / Look out the window? (2) / Check my reflection? (3)")

    choiceinput= input()
    directions = ["1","2","3"]
    
    while choiceinput not in directions:
        print("Please enter a valid option.")
        print()
        choiceinput= input()

    if choiceinput == "1":
        if hasHadTea == True:
            print("I'm full up on tea for now...")
            thechoice()
        else:  
            print("My mouth is dry and my breath catches in my throat,")
            print("the strange tea that they gave me when I arrived is starting to look good,")
            print()
            tea()
        
    elif choiceinput == "2":
        if theWindow == True:
            print("I glance at the window but I've seen enough for now...")
            thechoice()
        else:
            print("There's a dusty porthole window next to the dresser,") 
            print("I lean closer, taking in the night sky")
            print()
            window()
        
    elif choiceinput == "3":
        if mirrorMirrorOTW == True:
            print("My reflection stares back at me...")
            thechoice()
        else:
            print("I lock eyes with my reflection, deep eyes boring holes through the stained surface.")
            print()
            mirror()
        
def tea():
    global luck
    global hasHadTea
    
    print("Theres a small jug of milk and a container of sugar next to the teapot.")
    print("I cringe at the thought of adding milk to the tea, my stomach already flipping and knotted.")
    print("Sugar however...")
    print()
    print("do I need the added rush? (y / n)")
    print()

    sugarinput= input()
    directions = ["y","Y","n","N"]
    
    while sugarinput not in directions:
        print("Please enter a valid option.")
        print()
        sugarinput= input()
    
    if sugarinput == "y" or sugarinput == "Y":
        luck += 1
        hasHadTea = True
        print("I add the sugar to the cup and pour the tea out slowly,")
        print("the steam hits my nose, the smell sweet and heady.")
        print("I sip slowly, savoring it as i feel the heat wind through my body.")
        print()
        print("I feel good. I feel ready.")
        print()
        when()
        
    elif sugarinput == "n" or sugarinput == "N":
        hasHadTea = True
        print("I pour out the tea slowly,") 
        print("the steam hits my nose, the smell earthy and deep.")
        print("I sip slowly, savoring it as I feel myself calm a bit.")
        print()
        when()
       
def window():
    global luck
    global theWindow
    
    print("The city looks insignificant from this high up,")
    print("cars and people reduced to the size of ants.")
    print("I wonder if this is how gods feel as they survey humanity.")
    
    shootingstar = random.choice([True, False])
    if shootingstar is True:
        luck += 1
        theWindow = True
        print()
        print("As I gaze at the city spread below me a ribbon of light shoots through the sky.")
        print("I feel something build in my gut, something good.")
        print()
        when()
    elif shootingstar is False:
        theWindow = True
        when()

def mirror():
    global luck
    global mirrorMirrorOTW
    
    print("My skin looks paler in this light,")
    print("the heavy bags under them standing out in stark contrast.")
    print("There's something on my face...")
    print("on my cheek (1) / on the tip of my nose (2) / in the corner of my mouth (3)")

    freckles= input()
    directions = ["1","2","3"]
    
    while freckles not in directions:
        print("Please enter a valid option.")
        print()
        freckles= input()

    if freckles == "1":
        mirrorMirrorOTW = True
        print("I rub at the mark on my cheek,")
        print("It wipes away easily, nothing more than a smudge of dust smeared on my fingertips.")
        mirror1()
        
    
    elif freckles == "2":
        luck += 1
        mirrorMirrorOTW = True
        print("I rub at the mark on my nose.")
        print("It doesn't budge.")
        print("I lean in closer to the mirror, my breath fogging up the glass.")
        print("It's a new freckle, rounded and dark on the tip of my nose.")
        print("I frown slightly... weird that I never noticed it...")
        print("It kind of suits me, makes me look even more unique,")
        print("I fix my hair and smirk at my reflection, looking good.")
        print()
        print("I'm feeeling good about this whole thing")
        mirror1()
        
    elif freckles == "3":
        mirrorMirrorOTW = True
        print("I run my toungue over the smudge in the corner of my mouth.")
        print("It's sweet and creamy,")
        print("must be the chocolate I ate earlier...")
        mirror1()

def mirror1():
    global luck
    global myClothes

    print("I straighten my shirt, fixing the collar and ironing out any creases with my palms.")
    print("It's my favourite colour;")
    print("blue (1) / black (2) / red (3)")

    color= input()
    directions = ["1","2","3"]

    while color not in directions:
        print("Please enter a valid option.")
        print()
        color= input()

    if color == "1":
        myClothes = True
        print("The deep, royal blue compliments my skintone perfectly and I preen at my own reflection.")
        thechoice()

    elif color == "2":
        myClothes = True
        print("The black makes me look dark, giving me a dangerous edge that shows in the steely set of my shoulders.")
        thechoice()

    elif color == "3":
        myClothes = True
        luck += 1
        
        print("The red is rich, bloody and makes me feel invincible.")
        print("I can feel the power thrumming beneath my skin,")
        print("my battle clothes make me invincible.")
        thechoice()

def thegame():
    global luck

    match luck:
        case 0:
            print("The match is a blowout,")
            print("I lose and the blow to my ego is enormous.")
            quit()

        case 1:
            print("Your luck value is 1")

        case 2:
            print("Your luck value is 2")

        case 3:
            print("Your luck value is 3")

        case 4:
            print("Your luck value is 3")

        case 5:
            print("Your luck value is 3")
            
#Main function
print()
print("     ________________________")
print("     |                      |")
print("     |        Tyche:        |")
print("     | how far can luck go? |")
print("     |______________________|")
print()
print()
print("I was born perfect, nothing could break my luck.")
print("Then I met him... he's no human, he's a thing, a monster,")
print("a rumor that spreads like a disease through the seedy betting shops in the cities underbelly...")
print()      
print("A man of legend,")
print("The Luck Breaker")
print()
print("Would you like to start the game? (y / n):")

startGame = input()

if startGame == "n" or startGame == "N":
    print("What are you afraid of? Losing your life?")
    print("Coward.")
    quit()
    
elif startGame == "y" or startGame == "Y":
    thestart()     
