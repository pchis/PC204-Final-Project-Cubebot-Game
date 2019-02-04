# PC204-Final-Project-Cubebot-Game
This is the final project for a UCSF class which introduced the basics of object oriented programming through Python. See below for the project requirements, project object/description, accomplishments, future goals, and setup.

Project Requirements (from course website https://www.cgl.ucsf.edu/Outreach/pc204/project.html):
The requirements listed here are intentionally fairly general so as to maximize the flexibility you have. All will be discussed in class prior to the end of the quarter and most have been the topic of homework problems.
Your program may be (i) a script, or (ii) an interactive program with either a command-line interface or a graphical user interface (GUI).
If you choose to implement a script, your program must accept command line arguments specified by the user such as file name(s) and program option flags. Your program must also both read from and write to at least one disk file.
If you choose to implement an interactive command line program, your program must include an event loop that reads from standard input (sys.stdin) and reads from or writes to at least one disk file.
If you choose to implement an interactive GUI program, your program must use Tkinter or Pmw and read from or write to at least one disk file. (If you wish, you may use a different windowing system after getting approval from the course instructors.)
When processing user input, at least some rudimentary error checking should be performed in order to avoid tracebacks caused by simple input errors such as mistyped file names or unreasonable numerical data values.
Your program must define at least two Python classes, possibly more. Your use of class definitions should be done in such a way that they improve the modularity and potential re-usability of your code.
Your program must consist of multiple program modules. A good way to start is to put the main program in one file and library functions and classes in other files. Each module should have some simple means of testing that module independently of the other modules.
Your program must either parse input data and use them in some non-trivial task, or use data generated within your program to update one or more graphical outputs such as a histogram or other plot. Examples of parsing include:
extracting values from an XML file,
reading comma- or tab-separated data files, and
screen-scraping from web sites.
Examples of using data include:
creating objects from input values,
sorting input based on criteria other than alphabetical or simple numerical comparison,
querying web sites or web services by providing input data to them and then utilizing the results,
updating graphical displays such as text or graphics (e.g., plot(s)).
The goal is to demonstrate using Python for some non-trivial task. Simply copying data with minor alterations, such as replacing one string with another, is not sufficient.
Your program modules must have sufficient comments and docstrings embedded in the source code so that someone reading the program can tell what is going on. Complex algorithms should be thoroughly documented.
You need to provide either a separate text or MSWord file, or details in an email message, that describes the problem statement, the objective you're trying to accomplish, the approach you've used, any non-standard Python packages you use (including specific versions of those packages), any needed input files used by your program, and any limitations to your solution. In other words, tell us what you're trying to accomplish and provide us with what we need to successfully duplicate your results.

Object: 
The object of the my final project was to build a game I thought would be both fun and interesting to design and play. I initially conceived the game to be similar to a side scroller like Mario or Meat Boy, but with one small twist: the player doesn't directly control the main character. The main character, who I have dubbed "Cubebot," has a basic AI which tells it to run along the ground until it hits a wall, in which case it turns around, it nears a pit, in which case it jumps, or it hits an enemy or a lethal piece of terrain, in which case it dies. The player has to guide Cubebot around enemies and away from poorly planned jumps by utilizing the player's only ability: to place new pieces of terrain onto the level. 

Accomplishments:
In our consultation, Conrad described my idea as "ambitious," and it did turn out to have quite a few more pitfalls than I originally conceived. In the end I was able to set up a game with multiple levels. It has a character and creatures both moving under their own predictable AI, and the player has the option of placing three types of terrain. The player can also restart a level as well as save his or her exact game state and reload it upon running the program again. The game checks for some common errors and handles exceptions, and I have designed it in such a way that I think it is a foundation on which new levels, creatures, AIs, terrain types, etc. can be easily added. I also kept game calculations and tkinter graphing functions mostly separated so that if I wanted to switch to a different GUI interface in the future it would be possible. 

Future goals:
I want to make a longer and more substantial game with difficult levels and a variety of challenges, but I think there are a couple basic problems I would like to tackle before expanding the game. The first issue is a number of "quality of life" issues:  1) Currently the player receives messages from the console but plays the game on a canvas. I'd like to set it up so that the canvas has graphical or text widgets to help the player navigate the game. 2) It would also be nice to have a starting menu and pause menu to more seamlessly allow the player to navigate various options of the game such as saving. 3) I would also like to make the graphical representation smoother and allow the player to see a shadow of the terrain they're about to place before they place it for more accurate placement.
In addition to these quality of life issues I would also like to stress test the AI a little more. I have tested many basic interactions but I'm sure there are some corner cases where odd things happen.

Program setup and utilization: 
The program is divided between four different files. Mainfile.py starts the program by creating a Gamerunner object from the gamerunner_class.py file. The Gamerunner object keeps track of one Player object from a third file (player_class.py) as well as Terrain, Creature, and Character objects from the fourth file (creature_and_character_classes.py) and both iterates a loop over which these objects interact in a “gamespace” as well as graphing this gamespace to a Tkinter canvas. rungame is the primary function to look at to determine what the game does every “turn.” rungame calls itself after a delay after running so that the game continues to update in parallel with the Tkinter canvas’s mainloop function which allows the player to interact with the game by clicking on the canvas and pressing various keyboard keys. 

Things you need to know:
Other than putting all the files in a place they can be imported, you don’t need any special libraries. Please read the instructions in the console upon running mainfile.py, and be advised if you’re using the save and load functions the game can look frozen for maybe 3-10 seconds, but it should be working. Also, I have some very basic checks for each module which initialize variables, but in general I did my debugging by running everything because so much of each object’s functionality is its relation to other objects. I have left in various print functions commented out with # to show where I used them for debugging purposes.

