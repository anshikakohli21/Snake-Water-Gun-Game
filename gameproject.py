"""
rock=0
paper=1
scissor=-1
"""
import random
dic={"r":0,"p":1,"s":-1}
rev_dic={0:"r",1:"p",-1:'s'}
full={"r":"rock","s":"scissors","p":"paper"}
while True:

    comp=random.randint(-1,1)
    user=input("enter your choice r/p/s: ")
    num=dic[user.lower()]

    print("you chose",full[user],"\ncomputer chose",full[rev_dic[comp]])
    if num==comp:
        print("Its a draw.")
    elif num==0:
        if comp==1:
            print("you lost! better luck next time.")
        else:
            print("yay,you won!")

    elif num==-1:
        if comp==0:
            print("you lost! better luck next time.")
        else:
            print("yay,you won!")

    else:
        if comp==0:
            print("yay,you won!")
        else:
            print("you lost! better luck next time.")

    ch= input("do you want to play again (y/n):")
    if ch in["N","n"]:
        break