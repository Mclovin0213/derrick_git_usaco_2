Sonic’s Speedy Essay Formatter

Sonic the Hedgehog has finally decided to slow down for a moment and write an essay for his “History of Mobius” class. But there’s one problem—typing at supersonic speeds often leaves his formatting all over the place! Luckily, Sonic’s trusty sidekick, Tails, built a word processor that helps Sonic keep everything neat and tidy.

The essay contains N words (1 ≤ N ≤ 100), separated by spaces. Each word is between 1 and 15 characters long and consists only of uppercase or lowercase letters (Tails told Sonic no chili dog emojis allowed!).

However, the professor, Dr. Eggman (who insists on being called Doctor), is very strict about formatting. Each line of Sonic’s essay can contain at most K non-space characters (1 ≤ K ≤ 80). Spaces between words don’t count toward this limit, but there can’t be extra spaces at the end of a line.

Tails’ word processor was supposed to handle this, but Knuckles accidentally punched it into oblivion during a “friendly” arm wrestling match. Now, Sonic needs your help to format his essay correctly!

The formatting works like this:
	•	If Sonic types a word and it can fit on the current line, place it there.
	•	Otherwise, zoom it onto the next line and continue from there.
	•	Words on the same line must be separated by a single space.
	•	No extra space at the end of any line!

Can you help Sonic keep his essay neat so he doesn’t fail the class?

⸻

INPUT FORMAT (file: word.in):
The first line contains two space-separated integers N and K.
The second line contains N words separated by single spaces.
No word will ever be longer than K characters.

⸻

OUTPUT FORMAT (file: word.out):
Sonic’s essay, formatted correctly.

⸻

SAMPLE INPUT:

10 7
gotta go fast with Sonic and save the world today

SAMPLE OUTPUT:

gotta go  
fast  
with  
Sonic  
and save  
the  
world  
today
