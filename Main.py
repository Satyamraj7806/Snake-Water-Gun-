import random
c = ['snake', 'water', 'gun']
computer = random.choice(c)
Choices = ['snake', 'water', 'gun']
fullforms = {
    's' : 'snake',
    'w':  'water',
    'g' : 'gun'
}
a = input("enter your choice: snake/s, water/w, gun/g :")
a = fullforms.get(a,a)
if a not in Choices:
    print ("invalid choice. choose again!!")
    exit()
if a == computer:
    print("Both choosed the same, GAME TIE !!")
else :
    if (a == 'snake' and computer == 'water'):
        print (f"you chose {a}, computer chose {computer}\nyou won")
    elif (a=='water' and computer == 'gun'):
        print(f"you chose {a}, computer chose {computer}\nyou won")
    elif (a== 'gun' and computer == 'snake'):
        print(f"you chose {a}, computer chose {computer}\nyou won")
    else :
        print(f"you chose {a}, computer chose {computer}\nyou loose! better luck next time")
