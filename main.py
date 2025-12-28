# Audio Visual Language Learning App for Blackfoot
# Nov. 25. 2022
# Using our own extra module name helper in the file

import random
import time
import pygame
import cmpt120image
import helper


###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds. 
# soundfilename does not include the .wav extension, 
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

ENV = initEnv()
###############################################################


def menu():
    print("\n-------MAIN MENU-------")
    choice = ['. Learn - Word Flashcards', '. Play - Seek and Find Game',
              '. Setting - Change Difficulity', '. Exit']
    for i in range(4):
        print(str(i+1) + choice[i])
    print()
    

def learn(word_num):
    '''
    Input: Number of words want to learn (int)
    Output: Pics with Sound
    Return: list of pic names
    '''

    names = ['apples', 'bread', 'burger', 'child', 'coffee', 'dog', 'door',
             'eggs', 'fish', 'oranges', 'salt', 'tipi']

    print("--LEARN--")
    selected = []
    for i in range(word_num):
        
        canvas = cmpt120image.getWhiteImage(canvas_size[1], canvas_size[0])
        
        name = names.pop(random.randint(0, (len(names)-1)))
        selected = selected + [name]
        
        img = cmpt120image.getImage("images/{:}.png".format(name))
        helper.drawItem(canvas, img, 210, 210)
        playSound(name, ENV)
        input("{:}. Press to continue...".format(i+1))
    
    return selected


def play(words):
    print("--PLAY--")
    print("This is a seek and find game. You will hear a word.")
    print("Count how many of that item you find!\n")
    set_rounds = input("How many rounds you like to play? ")

    try:
        set_rounds = int(set_rounds)
    except:
        while isinstance(set_rounds, int) == False:
            if isinstance(set_rounds, int) == False:
                print("\n1That's not a valid number for game rounds")
                set_rounds = input("How many rounds you like to play? ")
                
                try:
                    set_rounds = int(set_rounds)
                except:
                    print("\n2That's not a valid number for game rounds")
                    set_rounds = input("How many rounds you like to play? ")
            else:
                break
                
    count = 1
    pics = words[:]
    while count <= set_rounds:
        
        selected_word = pics.pop(0)
        if len(pics) == 0:
            random.shuffle(words)
            pics = words[:]

        
        canvas = cmpt120image.getWhiteImage(canvas_size[1], canvas_size[0])
        #printing imgs to canvas
        for i in range(len(words)):
            img = cmpt120image.getImage("images/{:}.png".format(words[i]))
            
            if words[i] == selected_word:
                selected_amount = random.randint(1, 4)
                canvas = helper.distributeItems(canvas, img, selected_amount)
                
            else:
                amount = random.randint(1, 4)
                canvas = helper.distributeItems(canvas, img, amount)

            
           
        playSound(selected_word, ENV)
        ans = input("{:}. Listen to the word. How many of them can you find? ".format(count)).strip(" ,.~!?<>/")
        if ans == str(selected_amount):
            input("Right! Press Enter to continue.")
        else:
            input("Sorry, there were {:}. Press Enter to continue.\n". format(selected_amount))

        print()
        count += 1
    

def setting(word_num):
    '''
    Output: word_num = number player input
    
    '''
    print("--SETTING--")
    print("You are currently learning {:} words.".format(word_num))
    word_num = input("How many would you like to learn (3-12)? ")
    
    if int(word_num) < 3 or int(word_num) > 12:
        print("Sorry, that's not a valid number. Resetting to 3 words.")
        return 3
    
    return int(word_num)
    
    
#Starting
valid = False
word_num = 3
while valid == False:
    time.sleep(0.5)
    menu()
    numlst = ['1', '2', '3']
    canvas_size = [500, 500] #[h, w]
    canvas = cmpt120image.getWhiteImage(canvas_size[1], canvas_size[0])
    
    reply = input("Choose an option: ").strip(" ,.~!?<>/")
    if reply in numlst:
        if reply == '1':
            words = learn(word_num)
        elif reply == '2':
            try:
                play(words)
            except:
                print("You haven't learn any word yet")
        else:
            word_num = setting(word_num)

    elif reply == '4':
        valid = True
    
    else:
        pass

print('\nGood Bye!')
exit()

###Notes
'''
MAIN MENU
1. Learn - Word Flashcards
2. Play - Seek and Find Game
3. Setting - Change Difficulity
4. Exit
'''
