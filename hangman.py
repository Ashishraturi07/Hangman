name=input("Enter your name ")
print("Welcome " +name+ " Lets play Hangman")
print()
word="alphabet"
guesses=''
mode=input("Choose any mode (easy/medium/hard)")
if(mode=='easy'):
    turns=15
elif mode=='medium':
    turns=10
elif mode=='hard':
    turns=5
else:
    turns=0
    print("Wrong input")
if(turns==0):
    print("Try again")
while(turns>0):
    wrong=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            wrong+=1
    if wrong==0:
        print("you won")
        break
    print()
    guess=input("Guess a character : ")
    if(len(guess)>1):
        guess=""
        turns-=1
        print("wrong")
        print("You have ",+turns,"more guesses")
    guesses+=guess
    
    if guess not in word:
        turns-=1
        print("wrong")
        print("You have ",+turns,"more guesses")
        if turns==0:
            print("you Loose")
