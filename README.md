# Rock-Paper-Scissors
Revature Project0
I used MongoDB Compass, Pymongo, Python code, and Visual Studio Code
Before coding I imported from tkinter import menu, import pymongo from mongo client
I also connected my databases from mongodb at the beginning
My project is an ultimate game of rock paper scissors. When I first approached trying to create the game, I began with the actual game code.The game code consists of a “while true” statement. In the while true loop it has the different outcomes of when the player writes out their choice, rock paper or scissors. It also has the output that the computer will choose based  on what the player puts in.  Each outcome is numbered, Rock =0, paper=1 and scissors=2, and this is to calculate the score of each win and loss. After writing the code for the game, I was given the idea of giving it an arcade game layout, where when you finish the game, it asks for your- in this case username- and you're put onto the leaderboard with your score. How I approached this idea was to create a menu. The menu is put at the beginning of the code with everything inside. Including the game code. I then gave the options which are my CRUD operations, a new game, where at the end they are prompted to create a username immediately after they quit the game. 2 is to view the leaderboard and see where you are. 3 is to update your username in  case you don’t like the username that you put in after you finished the game. And 4th is to delete yourself from the leaderboard. All of these operations are in the menu loop I was discussing before, so if you don't want to play anymore you can quit the game, and it will break that loop. 
During this project I learned so much, I learned how to connect databases within the code. I learned what a loop was and learned more about defined functions. I also learned how to be more comfortable with the things that we have been learning over the past couple of weeks. And I also learned that  Visual Studio Code can be temperamental.
In the future I hope to make changes, like I would like to be able to give the option of deleting your lowest score rather than deleting you completely out of the system.

--HOW TO RUN THE PROJECT--

  Once you hit run code, you will be prompted immediately with the menu
  It will give you the options of new game (1), View leaderboard(2), update username (3), delete username(4), or quit(0)
  You will type the number of the response you want
  If you choose new game it will bring you to the game, where you follow the directons of typing rock,paper,scissors
  After you choose, it will output if you win or the computer and will give you or computer a point
  It will ask continuously after you win or lose to choose rock/paper/scissors
  Once you are done playing and input "q", it will immediately prompt you to type in a username
  Once submitted it will then add your total score and username to the database
 Then it will show the menu once again
 If you want to see your name on the leaderboard you will insert "2" for "view leaderboard" and the collection from my database will show up
 You will get the menu prompted once again
 if you choose update username, you will enter the username that you inserted earlier, and it will ask for a new username
 You will have the menu pop up and if you want to delete the username, then you can insert your username you want to delete, and it will delete that username from the collection in my database
 Then if you want to completely quit the game you will insert "0" and it will break the loop of the game and quit.
