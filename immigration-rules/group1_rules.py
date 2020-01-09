#
# Group 1 Rules
#
# Peter Turney, October 28, 2019
#
# Make a list of all Turing-complete totalistic life-like CAs
# that can be adapated to play the Immigration Game. A rule
# of the form "Babc/Sxyz" can be adapated to play the Immigration
# Game if all of the "born" numbers are odd (a, b, c = 1, 3, 5, .., 7).
#
# There should be 13 such rules, given the Turing-complete totalistic 
# life-like CAs here: 
#
# - https://conwaylife.com/forums/viewtopic.php?f=11&t=2597
# - "turing-complete-totalistic-CA.txt"
#
# import regular expressions (re)
#
import re
#
# input file with list of all known Turing-complete totalistic 
# life-like CAs
#
input_rule_file_name = "turing-complete-totalistic-CA.txt"
#
# output file with list of Turing-complete totalistic life-like 
# CAs that are suitable for the Immigration Game
#
output_rule_file_name = "group1-rules.txt"
#
# read input file and extract rules with odd "born" numbers 
# from the input file
#
input_rule_handle = open(input_rule_file_name, "r")
output_rule_handle = open(output_rule_file_name, "w")
#
for rule in input_rule_handle:
  born_search = re.search(r'(B[1357]+/)', rule)
  survive_search = re.search(r'(S[012345678]+$)', rule)
  if born_search and survive_search: 
    born = born_search.group(1)
    survive = survive_search.group(1)
    output_rule_handle.write(born + survive + "\n")
#
input_rule_handle.close()
output_rule_handle.close()
#
#