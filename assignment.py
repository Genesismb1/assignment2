import turtle
import easyshape # Importing the custom module easyshape.py

def main(): #defining the main module
    turtle.hideturtle() #Hiding turtle

    #Inputting the menu option
    menu_input=input('Enter the desired menu option: \n [L] ine \n [A] arc \n [T] ext \n [S] ettings \n [Q] uit \n') 

    while menu_input!= 'q': #Ensuring that the loop does not run if menu_input=q
        if (menu_input=='Q'): #Ensuring that the loop breaks if menu_input=Q
            break


        #This section runs if input = l or L
        elif (menu_input=='L' or menu_input=='l'): 
            print("\nEnter the line parameters: ")
            
            repeat='y' #Ensuring that the while loop executes the first time
            #The while loop runs until repeat==y or Y. It also allows user to select the default value of x1 if
            #select_default==Y/y, else enter their own value. If exception occurs when entering the value, users can repeat the process
            while (repeat=='y' or repeat=='Y'):
                try:
                    select_default=input("Press Y/y to use default value for x1 or press any other key to enter your own value: ")
                    if select_default == 'y' or select_default == 'Y':
                        print('Using default value for x1')
                        x1=easyshape.current_x #Assigning current,default value of x to x1
                    else:
                        x1=float(input("Line > x1: "))
                    repeat='n'#Breaking the while loop if the correct value is entered
                except ValueError:
                    print("Enter numeric value")
                    repeat=str(input('Repeat? (Y/N) '))
                    
            repeat='y'
            #The while loop runs until repeat==y or Y. It also allows user to select the default value of y1 if
            #select_default==Y/y, else enter their own value. If exception occurs when entering the value, users can repeat the process
            while (repeat=='y' or repeat=='Y'):
                try:
                    select_default=input("Press Y/y to use default value for y1 or press any other key to enter your own value: ")
                    if select_default == 'y' or select_default == 'Y':
                        print('Using default value for y1')
                        y1=easyshape.current_y #Assigning current,default value of y to y1
                    else:
                        y1=float(input("Line > y1: "))
                    repeat='n'
                except ValueError:
                    print("Enter numeric value")
                    repeat=str(input('Repeat? (Y/N) '))
                    
            repeat='y'
            #The while loop runs until repeat==y or Y. If exception occurs when entering the value of x2, users can repeat the process
            while (repeat=='y' or repeat=='Y'):
                try:
                    x2=float(input("Line > x2: "))
                    repeat='n'
                except ValueError:
                    print('Enter numeric value!')
                    repeat=str(input('Repeat? (Y/N) '))
                    
            repeat='y'
            #The while loop runs until repeat==y or Y. If exception occurs when entering the value of y2, users can repeat the process
            while (repeat=='y' or repeat=='Y'): 
                try:
                    y2=float(input("Line > y2: "))
                    repeat='n'
                except ValueError:
                    print('Enter numeric value!')
                    repeat=str(input('Repeat? (Y/N) '))

            #Calling the line function of the easyshape module by passing x1,y1,x2,y2 as arguments
            easyshape.line(x1, y1, x2, y2)

            
        #This section runs if input = a or A
        elif (menu_input=='A' or menu_input=='a'): 
            print("\nEnter the arc parameters: ")
            
            repeat='y'
            #The while loop runs until repeat==y or Y. If exception occurs when entering the value of radius, users can repeat the process
            while (repeat=='y' or repeat=='Y'): 
                try:
                    radius=float(input("Radius: "))
                    repeat='n'
                except ValueError:
                    print('Enter numeric value!')
                    repeat=str(input('Repeat? (Y/N) '))
                    
            repeat='y'
            #The while loop runs until repeat==y or Y. If exception occurs when entering the value of angle, users can repeat the process
            while (repeat=='y' or repeat=='Y'): 
                try:
                    angle=float(input("Angle: "))
                    repeat='n'
                except ValueError:
                    print('Enter numeric value!')
                    repeat=str(input('Repeat? (Y/N) '))

            #Calling the arc function of the easyshape module by passing radius and angle as arguments
            easyshape.arc(radius, angle)


        #This section runs if input = t or T    
        elif (menu_input=='T' or menu_input=='t'): 
            print("\nEnter the text parameters: ")
            
            content=str(input("Input the content for the text: ")) #Entering the content for the text
            
            repeat='y'
            #The while loop runs until repeat==y or Y. If exception occurs when entering the value of size, users can repeat the process
            #Even if exception does not occur, input process is repeated until size is positive
            while (repeat=='y' or repeat=='Y'): 
                try:
                    size=int(input("Input the size of the text: "))
                    while size <= 0:
                        print("Size should be positive!")
                        size=int(input("Input the size of the text: "))
                    repeat='n'
                except ValueError:
                    print('Enter numeric value!')
                    repeat=str(input('Repeat? (Y/N) '))
                    
            repeat='y'
            #The while loop runs until repeat==y or Y. It also allows user to select the default value of x coordinate if
            # select_default==Y/y, else enter their own value. If exception occurs when entering the value, users can repeat the process
            while (repeat=='y' or repeat=='Y'): 
                try:
                    select_default=input("Press Y to use default value for x coordinate or press any other key to enter your own value: ")
                    if select_default == 'y' or select_default == 'Y':
                        print('Using default value for x')
                        x3=easyshape.current_x #Assigning current,default value of x to x3
                    else:
                        x3=float(input("Input the x coordinate for the text: "))
                    repeat='n'
                except ValueError:
                    print("Enter numeric value")
                    repeat=str(input('Repeat? (Y/N) '))
                    
            repeat='y'
            #The while loop runs until repeat==y or Y. It also allows user to select the default value of y coordinate if
            #select_default==Y/y, else enter their own value. If exception occurs when entering the value, users can repeat the process
            while (repeat=='y' or repeat=='Y'): 
                try:
                    select_default=input("Press Y to use default value for y coordinate or press any other key to enter your own value: ")
                    if select_default == 'y' or select_default == 'Y':
                        print('Using default value for y')
                        y3=easyshape.current_y #Assigning current,default value of y to y3
                    else:
                        y3=float(input("Input the y coordinate for the text: "))
                    repeat='n'
                except ValueError:
                    print("Enter numeric value")
                    repeat=str(input('Repeat? (Y/N) '))

            #Calling the text function of the easyshape module by passing content, size, x3 and y3 as arguments
            easyshape.text(content, size, x3, y3)

        #This section runs if input = s or S    
        elif (menu_input=='S' or menu_input=='s'):
            print("\nSet the colour and thickness of the pen:")
            
            repeat='y'
            #The while loop runs until repeat==y or Y. It also allows user to select the default value of colour if
            #select_default==Y/y, else enter their own value. If exception occurs when entering invalid colour, users can repeat the process
            while (repeat=='y' or repeat=='Y'): 
                try:
                    select_default=input("Press Y to use default value for Colour or press any other key to enter your own value: ")
                    if select_default == 'y' or select_default == 'Y':
                        print('Using default value for colour')
                        set_colour=easyshape.colour #Assigning current,default value of colour to set_colour
                    else:
                        set_colour=str(input("Colour of the pen: "))
                        turtle.color(set_colour) #Incorrect value of colour raises a turtle exception
                    repeat='n'
                except:
                    print('Enter a valid colour!')
                    repeat=str(input('Repeat? (Y/N) '))
                    
            repeat='y'
            #The while loop runs until repeat==y or Y. It also allows user to select the default value of thickness if
            #select_default==Y/y, else enter their own value. If exception occurs when entering set_thickness value, users can repeat the process
            #if negative value is entered then users are asked to enter the value again
            while (repeat=='y' or repeat=='Y'): 
                try:
                    select_default=input("Press Y to use default value for Thickness or press any other key to enter your own value: ")
                    if select_default == 'y' or select_default == 'Y':
                        print('Using default value for thickness')
                        set_thickness=easyshape.thickness #Assigning current,default value of thickness to set_thickness
                    else:
                        set_thickness=float(input("Thickness of the pen: "))
                        while set_thickness <= 0:
                            print("Thickness should be positive!")
                            set_thickness=float(input("Thickness of the pen: "))
                    repeat='n'
                except ValueError:
                    print("Enter numeric value")
                    repeat=str(input('Repeat? (Y/N) '))

            #Calling the text function of the easyshape module by passing set_colour and set_thickness as arguments
            easyshape.settings(set_colour, set_thickness)
            
        else:
            print("The input is invalid")

        #Entering values continously until user chooses to quit
        menu_input=input('\nEnter the desired menu option: \n [L] ine \n [A] arc \n [T] ext \n [S] ettings \n [Q] uit \n')
    return
main()

