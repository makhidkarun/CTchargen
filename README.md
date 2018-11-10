# CTchargen

chargen.py
Classic Traveller character generator
v0.3, April 9th, 2018
By Omer Golan-Joel, golan2072@gmail.com
This code is open-source

Version History

0.5, November 10th, 2018
Fixed bugs with "-1 SOC" or "+2 INT" appearing as possessions or skills
Guns and blades are now selected per existing weapon skills (if any)
Increased probability for material mustering out benefits
Increased probability for female characters to be "Ms." rather than "Mrs.".

0.4, April 12th, 2018
All careers added
Rank skills added

0.3, April 9th, 2018
Cascade skills added
"Cascade" equipment added (gun and melee types)
Noble title are now by sex

0.2, April 9th, 2018
Army career finalized
Mustering out benefits added

0.15, April 6th, 2018
Improved the chargen loop and skill acquision
Implemented the Marines career
Implemented a more traditional character output format
Characters now have names and surnames randomly chosen from an external file
Implemented noble titles

0.1, April 6th, 2018
Returned to dictionaries for the career data structure, works perfectly.
Baseline career loop created. It still lacks mustering out and only uses the Service skill table, but starts generating something remotely resembling a Traveller character,
Careers are mock-up; all use Navy stats except for their names. To be changed later.

0.03, April 6th, 2018
Implemented the Named Tuple career data structure.

0.02, April 5th, 2018
Still extremely partial, but improved the data structure. The character will now be an object; I'll later add the careers as Named Tuples.

0.01, March 30th, 2018
Very early and very partial code. Includes several relevant functions, the career and character data structures, and the very beginning of the character object and the main character generation function.
