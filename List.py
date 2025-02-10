_list = {}    # shopping list
print("This is your lsit write something you want ")
chose = 0


# for get first things
print("if it's enough write (exit) or (Exit)")
while True :
    try:
        thing = input("name of thing : ")
        thing = thing.upper()
        thing = thing.strip()
        if thing == "EXIT" :
            break
        assert len(thing)>0
        much = input(f"how many {thing} you need : ")
        
        
        if thing not in _list :
            _list[thing] = much 
        else :
            print("already this thing added in the list ")
            
    except :
        print("you can't give an empty input")
    
    
      
# function for select the options
def select() :
        print("""chose one number 
                1 = add thing in the list
                2 = see yuar list
                3 = remove thing of list
                4 = adding list in file'list.txt' 
                5 = exit in list """)
        while True :     
            try:  
                chose = int(input("select a number :"))
                assert chose > 0 
                assert chose < 6
                break
            except:
                print("try agin")
        return chose
    
    
while True: 
    if chose == 0 :    
        chose = select()

 # add to the list           
    if chose == 1 :
        print("if it's enough write (exit) or (Exit)")
        while True :
            try:
                thing = input("add in the list :")
                thing = thing.upper()
                thing = thing.strip()
                if thing == "EXIT" :
                    break
                assert len(thing)>0 
                much = input(f"how many {thing} you need : ")
                
                if thing not in _list :
                    _list[thing] = much
                else:
                    print("already this thing added in the list ")
            except :
                print("you can't give an empty input")
         
        chose = select()  
        print()
        print()
        
 # show the list 
    if chose == 2 :
        print(_list)
        print("""
              """)
        chose = select()


 # lowering from the list 
    if chose == 3 :
        print(_list)
        print("if it's enough write (exit) or (Exit)")
        while True :
            try :
                thing = input("intr thing to remove in list :")
                thing = thing.upper()
                thing = thing.strip()
                assert len(thing)>0
                if thing == "EXIT":
                    break    
                elif thing in _list :
                   print(f"the {thing} is successfully removed from the list")
                   del _list[thing]
                else :
                    print("that is not in list ")
            except :
                print("you can't give an empty input")
        chose = select()
        print("""
              """)
             
    #  adding list in the file           
    if chose == 4 :
        with open("list.txt" , "w") as file :
            pass
        with open("list.txt" ,"a+") as file :
            for i in _list:
                file.write(f"{i} ---> {_list[i]}\n")
        print("added list in the file'list.txt'")
                
        chose = select()
        
        
    if  chose == 5 :
        print("have a nice day!")
        break
    
    
    
    
