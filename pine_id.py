def what_pine_is_this(): 
        needle_bunching = int(input("Are the needles in bunches of 1, 2, or 3? "))
        needle_length = int(input("What is the approximate length of the needles in inches? "))
        if needle_bunching == 1: 
                print("You've found a Douglas Fir")
        elif needle_bunching == 2 and (1 <= needle_length <= 2): 
                print("You're looking at a Pinyon Pine")
        elif needle_bunching == 2 and (3 <= needle_length <= 5): 
                print("That's a Shortleaf Pine")
        elif needle_bunching == 2 and (needle_length > 5): 
                needle_color = input("Are the needles light green and dull (LGD) or dark green and glossy (DGG)? ")
                if needle_color == "LGD": 
                        print("By golly, that's an Italian Stone Pine")
                if needle_color == "DGG": 
                        tree_height = input("Is it taller than 30 feet? Y/N ")
                        if tree_height == "Y": 
                                print("That's a Slash Pine!")
                        if tree_height == "N":
                                print("Holy moly, you've found a Japanese Black Pine")
        elif needle_bunching == 3 and needle_length < 5: 
                print("What do you think of that Mexican Pinyon Pine?") 
        elif needle_bunching == 3 and (5 <= needle_length <= 10): 
                print("That's a native Loblolly Pine")
        elif needle_bunching == 3 and needle_length > 10: 
                print("A native Longleaf Pine: wow!")

what_pine_is_this()