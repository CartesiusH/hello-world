# What Each Script Does
## Video-Scraper
- Given a show name and season, find a list of links to each episode of the show.
- Download the show (which is served as a stream of .ts files not an .mp4 unfortunately) by extracting the 1080.m3u8 file (which has the paths to all the .ts files) and downloading all the .ts files into a folder which can be played by VLC media player.

## Password Manager
- This script does 2 things:
  - Given a sentence, take the first letter of each word to make a password that has a mix of numbers/letters/special characters. I do this to create my passwords because it creates a varied sequence of seemingly random characters (ie. not an English word with characther subsitutions that's prone to a dictionary attack) that is easier to remember than an actual random sequence.
  - Store the password in a file and encrypt it based off a key derived from a master-password (and decrypt it the same way.) I don't actually use this for anything of importance (and just memorize my passwords) because it only uses base64 encryption, but it was fun to create.

## Dinner Decider
- Gives a list of things to eat based on a healthy-ness level and time of day/week (whether it's breakfast/lunch/dinner and weekday/weekend.) 
- I made two versions of the script, one that stores the list of food options in a .pickle file and another that stores the list in a .json file just for the sake of expirementation.




