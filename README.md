# AOC2023

Solutions for Advent of Code 2023


## D01

First part of this day was easy and was solved by using `re.findall("\d", line)` then concatinating the result and converting to an integer.

To solve the second part was surprisingly difficult.  
I knew that the soulution would be to expand the pattern I was matching to also include the numbers spelled out. The first problem I had with this was the inability to remember if I was supposed to use brackets `[]` or parethesies `()`, when building out the pattern. After running it though a regex tester it turns out to be `()` that are used for capture groups.

Now that I'd completed the pattern the next thing to fix was the conversion of the strings to numbers. As I now had spelled out numbers aswell I had to add a dictionary to be able to map those values to numbers and as I was no longer concatinating the numbers I needed to multiply the first number by 10 when adding it to the total.

Here I noticed a flaw of me using `re.findall` for this, it only find non-overlapping matches. This was a problem as for the line `seven3lbcvjxqhhdpzkttqsixjzzjjbclfq1fiveeightwojx` it would find the numbers `["seven", "eigth"]` and not `["seven", "two"]`. To solve this I switched regex package to a third-party one with support for overlapped search. So the final solution was to use `re.findall(pattern, line, overlapped=True)`. Another solution would have been to find matches one by one and then only keep the first and last ones.
