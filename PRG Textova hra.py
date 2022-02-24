from time import sleep
def Intro():
    print("Welcome to the Adventure game.\nYour ship has crashed into something. You can stay or Evaluate.\nAnswer only: Stay or Evaluate?")
    
    c1 = input()
    sleep(2)
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=="STAY"):
            print("\nLily decides to stay in the room\nAfter a while of waiting, you exit the room anyway.")
            ans = 'correct'
            print("\nLily exits the room silently.")
            Hall()
        elif(c1.upper()=="EVALUATE"):
            print("Lily exits the room silently.")
            ans='correct'
            Hall()
        else:
            print("ENTER THE CORRECT CHOICE! Stay or Evaluate?")
            c1=input()
def Hall():
    print("In the main hall, she finds a strange but cute teddy bear.\nDoes she pick it up or ignore it?\n Answer only: Pick or Ignore")
    sleep(2)
    c1 = input()
    ans = 'incorrect'
    while(ans=='incorrect'):
        if(c1.upper()=="PICK"):
            print("\nThe moment Lily picked up the teddy, it started talking.")
            sleep(2)
            print("\nThe bear gave her a rose")
            ans= 'correct'
            Cross()
        elif(c1.upper()=='IGNORE'):
            print("\nLily decided not to pick up the bear and walked away.\nOn her way to the dock, she took up a rose.")
            ans='correct'
            Cross()
        else:
            print("Wrong Input! You gotta enter either pick or ignore")
            sleep(2)
            c1 = input()
            ans = 'incorrect'

def Cross():
    print("Great, now you got a rose. \nYou can now enter the Gardening section. \nOr you can try to scratch yourself with the rose.\n Answer only: Garden or Scratch")
    ans = 'incorrect'
    c1=input()
    while(ans=='incorrect'):
        if(c1.upper()=="GARDEN"):
            print("\nYou went to the gardening section")
            sleep(2)
            ans = 'correct'
            Garden()
        elif(c1.upper()=="SCRATCH"):
            print("Congratulations, idiot, you scratched yourself, you went to the Gardening section anyway.")
            ans='incorrect'
            Garden()
        else:
            print("ENTER THE CORRECT CHOICE! Garden or Scratch?")
            ans= 'incorrect'
def Garden():
    print("In the gardening section, you see a monster, and it sees you, what will you do?\n Answer only: Fight or Run")
    ans="incorrect"
    c1=input()
    while(ans=='incorrect'):
        if(c1.upper()=="FIGHT"):
            print("\nYou decided to fight the monster. The monster was way stronger than you. \n\n GG, you died a heroic way.")
            sleep(2)
            ans = 'correct'
            break
        elif(c1.upper()=="RUN"):
            print("You almost managed to run away, but the monster caught up and killed you. \n\n GG, You died a coward..")
            ans='incorrect'
            break
        else:
            print("ENTER THE CORRECT CHOICE! Garden or Scratch?")
            ans= 'incorrect'



Intro()