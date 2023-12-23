# AOC2023

Solutions for Advent of Code 2023


## D01

First part of this day was easy and was solved by using `re.findall("\d", line)` then concatinating the result and converting to an integer.

To solve the second part was surprisingly difficult.  
I knew that the soulution would be to expand the pattern I was matching to also include the numbers spelled out. The first problem I had with this was the inability to remember if I was supposed to use brackets `[]` or parethesies `()`, when building out the pattern. After running it though a regex tester it turns out to be `()` that are used for capture groups.

Now that I'd completed the pattern the next thing to fix was the conversion of the strings to numbers. As I now had spelled out numbers aswell I had to add a dictionary to be able to map those values to numbers and as I was no longer concatinating the numbers I needed to multiply the first number by 10 when adding it to the total.

Here I noticed a flaw of me using `re.findall` for this, it only find non-overlapping matches. This was a problem as for the line `seven3lbcvjxqhhdpzkttqsixjzzjjbclfq1fiveeightwojx` it would find the numbers `["seven", "eigth"]` and not `["seven", "two"]`. To solve this I switched regex package to a third-party one with support for overlapped search. So the final solution was to use `re.findall(pattern, line, overlapped=True)`. Another solution would have been to find matches one by one and then only keep the first and last ones.

## D02

### P1

Solved by splitting the line down so I could iterate over each played round and then using a regex to match the numbers and which color they were. The resulting list of matches was checked against a dict of the known limits for each color, when a limit was found it raises a `StopIteration` and continues with the next game.

### P2

What was changed from p1 was that for each round it would iterate over the drawn cubes and add them back to a dict incase they were larger than the previous round. At the end of each game the product of the values was calculated and added back to the total sum.

## D03

### P1

First I create a matrix of the input to be able to get locations on previous and next rows. Then when iterating over each row in the matrix i find all numbers using a regex function. I then use the start and end position to get the surroundings and concatinate that to a new string where I replace all everything matching `r"\d+|\."` and also strip the text to get rid of newlines. If the remaining string is not empty the number of the part gets added to the total sum.

### P2

For part 2 I had to switch my approach from finding numbers and checking if there was a symbol touching, to checking for symbols and testing if they were touching exactly two numbers. So now I use a different regex to find symbols and then I also get the numbers on the previous line, same line, and next line. Then for each symbol I check if there are numbers that intersect the area surrounding the symbol.

### Reflection

I could have made the solution easier if I had collected all symbols and numbers and just matched intersections where used symbols and numbers are removed after they are used.  
Another solution might have been to do everything during the first pass over the file where I create a matrix, that might have involved a more difficult management of the loop so it was not something I wanted to try initially.

## D04

### P1

Very straightforward challenge using a simple regex to find all numbers after splitting the line at the separator. Then transforming the results to sets and checking for the length of the intersection and if there was one adding $(2^{len-1})$ to the total.

### P2

To keep track of the number of copies of each scratchcard I used a simple list of ints that where I initialize each number to 1. Then I add the number of copies to following cards if there are winning numbers. And finally add the number of copies of the current card to the total.
