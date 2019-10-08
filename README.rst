Dungeon Run
============

**New working branch web**


**Summary**

Dungeon Run is a text-based adventure game for one player.
It is played by making choices in menus which contains different options.
You choose what kind of hero you want to play, and then explore one map
with random content in search of treasures. But watch out
for monsters! The goal is collecting as much treasures as possible
and finding your way out with your life intact.

This is sonsofbjorn's implementation of the game as described by the assignment.
The game is written i Python 3.7 and compiled to a windows binary.
It runs in console and takes text inputs.

game.dungeon module
-------------------
	
	The Dungeon module handles the map and things on it as well as helper
	functions and debug tools.
	It contains the map class itself and classes that populate it.

game.main module
----------------
	
	Main function to follow python standards to initiate the game.
	
game.view module
----------------
	
	This Class handles every console input/output of the game
	and passes it to forward to controller.
	This Class exists to isolate the disorder of long strings and prints
	from other classes, to keep every other class as clean as possible.
	
game.player module
------------------
	
	Makes a player object. Takes name, class, start room and score
	Name is a string, class is one of the classes below and start room
	is a room object.
	
game.controller module
----------------------
	
	This class handles several key features which are:
	Starting the main game.
	This class calls other classes to make use of their functions.
	Handles every aspect of saving and reading to player.txt.
	Creates a dungeon and a player object depending on user choices.
	Handles movement for both player and AI.
	Handles combat and loot.
	Rolls a dice to decide initiative for players.
	
