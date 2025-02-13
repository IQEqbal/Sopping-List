shopping_list = {}    # Shopping list
print("This is your list. Write something you want to add.")
choice = None

# Geting the initial items for the shopping list
print("if you're done, type (exit) or (Exit)")
while True :
    try:
        item = input("Enter the name of item : ").strip().upper()
        if item == "EXIT" :
            print("The items you wrote have been added to the list.")
            break
        assert len(item)>0
        much = input(f"How many {item} do you need? : ")
        if item not in shopping_list :
            shopping_list[item] = much 
            print()
        else :
            print("This item is already in the list.")
    except AssertionError :
        print("you can't enter an empty input")
    
       
# Function for selecting the options
def select() :
        print("""Choose a number 
                1 = Add thing in the list.
                2 = See your list.
                3 = Remove an item from the list.
                4 = View the file 'list.txt'
                5 = Add the list to file 'list.txt' 
                6 = Exit the program """)
        while True :     
            try:  
                choice = int(input("select a number :"))
                assert 0 < choice < 7
                break
            except AssertionError :
                print("please select a valid number")
            except ValueError :
                print("please enter a number")
        return choice
    
    
while True: 
    if choice == None :    
        choice = select()

    # Adding new items to the shopping list         
    if choice == 1 :
        print("if you're done, type (exit) or (Exit)")
        while True :
            try:
                item = input("Add to the list :").strip().upper()
                if item == "EXIT" :
                    break
                assert len(item)>0 
                much = input(f"How many {item} do you need? : ")
                
                if item not in shopping_list :
                    shopping_list[item] = much
                else:
                    print("This item is already in the list.")
            except AssertionError :
                print("you can't give an empty input")
         
        choice = select()  
        print() 

        
    # Showing the list 
    if choice == 2 :
        for i in shopping_list :
            print(i  ,  shopping_list[i] , sep=":")
        print()
        choice = select()


    # Removing an item from the shopping list
    if choice == 3 :
        print(shopping_list)
        print("if you're done, type (exit) or (Exit)")
        while True :
            try :
                item = input("Entr the item to remove from the list :").strip().upper()
                assert len(item) > 0
                if item == "EXIT":
                    break    
                elif item in shopping_list :
                   print(f"the {item} has been successfully removed from the list")
                   del shopping_list[item]
                else :
                    print("That item is not in the list ")
            except AssertionError :
                print("you can't enter an empty input")
        choice = select()
        print()
      
    # Reading file 'list.txt'       
    if choice == 4 :
        try:
            with open("list.txt","r") as file :
               print(file.read())
        except FileNotFoundError :
            print("The file does not exist.")
            print("if you want to create it. go to option 5 and type 'Yes'")
            
    choice = select()
    
                           
    # Saving the shopping list to the file 'list.txt'           
    if choice == 5 :
        while True :
            try :
                print("Do you want to delete the previous list? (Yes or No)")
                question = input('please write "Yes" or "No" : ').strip().upper()
                assert question == "YES" or question == "NO"
                break
            except AssertionError :
                print("please choose one.")  
                  
        if question == "YES" :
            with open("list.txt" , "w") as file :
                pass
        elif question == "NO" :
            pass
        with open("list.txt" ,"a+") as file :
            for i in shopping_list:
                file.write(f"{i} ---> {shopping_list[i]}\n")
        print("The list has been added to the file 'list.txt'")
        
        choice = select()
        
        
    if  choice == 6 :
        print("Have a nice day.")
        break   