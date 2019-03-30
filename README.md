# David Gallagher - Graph Theory Project

The Purpose of this Project is to create a Python script that can build a non-deterministic finite automaton (NFA) from a regular expression and use the NFA to check if the regular expression matches any given string of text.

This repository was developed as part of the Graph Theory Module of 3rd Year Software Development in GMIT.

## Pre-Requesits and Dependencies.
* Python - https://www.python.org/downloads/
* Text Editor - https://code.visualstudio.com/download
* Some understanding of programming is desirable, here's a helpful guide about using Python:
* https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf

## Run The Project
* Clone the repository to your directory: 'git clone https://github.com/d-gallagher/python_GraphTheoryProject'. 
* Change Directory to the project folder and run the 'thompsonsConst_Submision.py' file: 
* ~ python thompsonsConst_Submision.py
* This is the current working file while a GUI is in development on a separate branch.

## Project Design
The current working project is comprised of 4 concise functions, which are commented for readability.
* Shunt
* Compile
* Followes
* Match

#### Shunt Function
* The Shunting Yard Algorithm is used to parse through an infix notation and return the string in postfix notation. For more information on this see: 
* > https://en.wikipedia.org/wiki/Shunting-yard_algorithm
* Infix examples:
* >  a.b -- an 'a' followed by a 'b'
* >  a|b -- an 'a' or a 'b'
* >  a*  -- any number of 'a's, includng 0
* >  a+b  -- one 'a' or more 
* >  a?  -- zero or one 'a's
* Postfix examples:
* >  ab. -- an 'a' followed by a 'b'
* >  ab| -- an 'a' or a 'b'
* >  a*  -- any number of 'a's, includng 0
* >  ab+ -- one 'a' or more 
* >  a?  -- zero or one 'a's
* > A more in depth explanation is found here: www.oxfordmathcenter.com/drupal7/node/628

#### Compile Function
* Transforms a regular expression into an NFA which can then be used to match strings against the regular expression.
* For each of the special operators listed in the Shunt algorithm, Compile will parse the postfix and return an NFA.
* This is based on the Thompsons Constrction algorithm, invented by Ken Thompson.
* A more detailed explanation of that here: https://en.wikipedia.org/wiki/Thompson%27s_construction

#### Followes Function
* Returns the state or set of states which can be reached from a state by following 'E' arrows.
* Read as "Follow E's ".., this function builds a set of states from a given NFA which can be reached by following any 'E' arrow in the NFA.

#### Match Function

    
