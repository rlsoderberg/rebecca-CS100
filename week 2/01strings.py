print("You enter an aviary with three doors. Which will it be?")
door = input("1, 2, or 3?")
type = ["0", "uppercase", "lowercase", "title case"]
#i wish i could do this whole thing in a for loop, including string functionalities
for s in range (0, 4):
    int = int(door)
    #introduce program, request user input
    print("Hello! I'm the",type[int],"parrot!")
    user_status = input("How are you doing today? ")
    #split user input at spaces
    array = user_status.split(" ")
    #convert words to uppercase
    print(array[0].upper(), "\n", array[0].upper(), "\n")
    if len(array) > 0:
        for s in array:
            print(s.upper())


