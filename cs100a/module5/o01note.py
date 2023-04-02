#input function
def inputio():
    valid = False
    while valid == False:
        try:
            x =  input()
            while x == "":
                print("Out of range!")
                x = input()
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x

#open and write
#title = input("File to write to: ")
note = open("note.txt", 'w')
note.write('Hey, you totally need to figure out this email thing. And what were you going to call that Fawlty Towers video game???')
note.close

note = open('note.txt', 'r')
text = note.read()
print(text)
note.close()
