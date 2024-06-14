print("hey,buddy welcome to the adventure game")
status = input("do you want to continue yes/no ").lower()

if status == "yes":
    way = input("which way would you like to go ? fron road/river/sky ")
    
    
    if way in ["road","river","sky"]:
        
        
        if way == "road":
            print("you are on the road")
            turn = input("here's  you got an turn ,which turn do you want to take right or left " )
            if turn in ["right","left"]:
                if turn == "right":
                    print("you got the monster")                    
                else:
                    print("you are on the next level")
            else:
                print("you lose because yovnt choose right path")
                
                
        elif way == "river":
            
            
            swim = input("do you know how to swim yes/no ").lower()
            if swim in ["yes","no"]:
                if swim == "yes":
                    print("you are swimming now")
                    sharks_way = input("sharks are comming would you like to turn right/left ").lower()
                    if sharks_way in ["right","left"]:
                        if sharks_way == "right":
                            print("you won")
                            print("you're going to the next level")
                        else:
                            print("you lose sharks eaten you")
                    else:
                        print("you lose you have taken invalid action")
                else:
                    print("you lose because you cant swim")
            else:
                print("you lose you have taken wrong deision ")
            
    
        elif way == "sky":
            
            plane = input("do you have plane to fly in the sky yes/no ").lower()
            if plane in ["yes","no"]:
                if plane == "yes":
                    print("so lets fly")
                    print("you're in the sky")
                    decision = input("there are birds in front of you do you want to turn right/left ").lower()
                    if decision in ["right","left"]:
                        if decision == "right":
                            print("you lose because you caught in tornedo")
                        else:
                            print("you're going to the next stage")
                            
                    else:
                        print("you lose invalid input")
                else:
                    print("you lose you dont have an plane to fly")
                    
            else:
                print("you lose invalid input")
                
    else:
        print("invalid input")
        
else:
    print("thank you for visting us")
                    