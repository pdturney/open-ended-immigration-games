

README file for Universal Rules

Peter Turney
October 28, 2019


(1) Group 1 Rules
- the following URL gives a list of Turing-complete totalistic cellular 
  automata rules:
- https://conwaylife.com/forums/viewtopic.php?f=11&t=2597
- this list contains 30 universal rules
- this list was last updated on October 27, 2017
- we are interested in rules that can play the Immigration Game, which
  requires odd numbers in the "born" part of the rule
- there are 13 such rules in the above list
- the 13 odd-born rules are in the file "group1-rules.txt"
- B35/S236 is particularly interesting because it is Turing-complete yet 
  it does not belong in Wolfram's Class 4:
- https://www.ics.uci.edu/~eppstein/ca/b35s236/

(2) Group 2 Rules
- this group is a list of 13 rules randomly selected from all 2**18 possible
  totalistic cellular automata rules

(3) Group 3 Rules
- this group is a list of 13 rules randomly selected from all 2**18 possible
  totalistic cellular automata rules that satisfy the constraints given here:
- https://www.ics.uci.edu/~eppstein/ca/wolfram.html
- (I) Contraction impossible: If a rule includes B1, any pattern expands to infinity 
  in all directions, no gliders can exist, and the question of whether a pattern 
  lives or dies can not be universal.
- (II) Expansion impossible: If a rule does not include B2 or B3, any pattern 
  remains within its initial bounding box, no gliders can exist, and again the 
  question of whether a pattern lives or dies is not universal (it can be solved 
  in at most exponential time).
- (III) Both expansion and contraction possible: Only in the remaining cases can 
  gliders exist. Our investigations show that a large fraction of the remaining 
  cases do indeed support gliders; much more work would be required to show that 
  they are universal.

