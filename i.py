def input_function(prev_empty, type_name):
    valid = False
    while valid == False:
        try:
            x = input("give me a "+str(type_name)+": ")
            if prev_empty == 1:
                if not x:
                    raise ValueError('empty string')
            valid = True
        except ValueError:
            print("Invalid Input!")
    return x  