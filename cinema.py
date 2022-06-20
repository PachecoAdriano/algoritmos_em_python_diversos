films = {
    "Finding Dory": [3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Gost Busters":[12,5]
    }

while True:

    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age= int(input("How old are you?: ").strip())
        if age >= films[choice][0]:
            print("Enjoy the film!")
        else:
            print("You are too young to see that film!")
        
    else:
        print("We don't have that film...")
