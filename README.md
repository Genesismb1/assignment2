# assignment2
Assignment2
In this assignment you will use turtle graphics to create an interactive menu-based drawing application.

The application will initially show an empty drawing screen and present the user with the following main menu:

[L]ine

[A]rc

[T]ext

[S]ettings

[Q]uit



The user selects the menu command by entering the letter (case insensitive). The following prompts will depend on the selected option. For example, the following are the prompts for the Line command:

Line > x1 (default current x coordinate):

Line > y1 (default current y coordinate):

Line > x2:

Line > y2:



After the Line parameters are accepted, the program should draw a line on the drawing screen, store the current x and y coordinates, and return back to the main menu. Use the same approach for other commands.



The Arc command will accept two parameters: radius and angle. It will draw a partial circle with those parameters.



The Text command will accept four parameters: content, size, x and y coordinates. It will write the entered content on the screen with specified size at the specified coordinates.



The Settings command will show the following prompts:

Settings > Pen colour (default no change):

Settings > Pen thickness (default no change):

The entered values will apply to any future drawing commands.



Constraints

You must create a module called easyshape.py that contains at least the following functions:
line(x1, y1, x2, y2)
text(content, size, x, y)
arc(radius, angle)
settings(colour, thickness)
You must also use global variables for the colour and thickness values, as well as the current x and y coordinates.
In your main program, you must import the module easyshape. You must not import any modules other than turtle and your own created modules. 


Your assignment should consist of following tasks.

Task 1

Draw a flowchart of your menu handling algorithm. You can abstract the defined functions using function symbols, but the main flowchart should provide sufficient level of details for the logic of your algorithm.

You can draw the flowcharts with a pen/pencil on a piece of paper and scan it for submission, as long as the handwriting is clear and legible. However, it is strongly recommended to draw flowcharts using a drawing software.

Task 2

Select four sets of test data that will demonstrate the 'normal' operation of your program; that is, test data that will demonstrate what happens when a valid input is entered. Select three sets of test data that will demonstrate the 'abnormal' operation of your program. Please note that for this application, user input includes mouse clicks as well as keyboard button presses.

Set out test results in a tabular form as follows. It is important that the output listings (i.e., screenshots) are not edited in any way.
