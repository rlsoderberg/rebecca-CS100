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

reverseteam = []
unreverseteam = []

print("List players on team, from longest time played on team, to shortest.")
print("Enter 'done' (just the word done, no quotation marks) when you're finished.")

player = ""
while player != "done":
    print("Give me a player name: ")
    player = inputio()
    if player != "done":
        reverseteam.insert(0, player)
        unreverseteam.append(player)

print("team members from newest to oldest are: \n", reverseteam)
print("team members from oldest to newest are: \n", unreverseteam)