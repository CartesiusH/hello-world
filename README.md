# What Each Script Does
## Password Manager
- This script does 2 things:
  - Given a sentence, take the first letter of each word to make a password that has a mix of numbers/letters/special characters. I do this to create my passwords because it creates a varied sequence of seemingly random characters (ie. not an English word with characther subsitutions that's prone to a dictionary attack) that is easier to remember than an actual random sequence.
  - Store the password in a file and encrypt it based off a key derived from a master-password (and decrypt it the same way.) I don't actually use this for anything of importance (and just memorize my passwords) because it only uses base64 encryption, but it was fun to create.

## Gaslaws Calculator
- In chemistry, we learned the equation PV=nRT, and we did a lot of practice converting different units and entering them into the equation.  This program asks for the user to enter 3 of the 4 following: pressure (psi, mm Hg, bar, kPa, atm), volume (L,  mL), mols, and temperature (°F,°C, °K) followed by any of the given  units. The program auto-detects the units, converts them into the right  ones for the equation, and gives the missing value.

## What To Eat
- Gives a list of things to eat based on a healthy-ness level and time of day/week (whether it's breakfast/lunch/dinner and weekday/weekend.) 
- I made two versions of the script, one that stores the list of food options in a .pickle file and another that stores the list in a .json file (just for the sake of expirementation.)

## Hangman Game
- The program choses one of several pre-set words at random and allows the user to guess up to 10 different letters.