#
# Group 3 Rules
#
# Peter Turney, October 29, 2019
#
# Make a list of all totalistic life-like rules that can be 
# adapated to play the Immigration Game and meet the three
# conditions given by Eppstein. A rule of the form 
# "Babc/Sxyz" can be adapated to play the Immigration Game 
# if all of the "born" numbers are odd (a, b, c = 1, 3, 5, .., 7).
# The Eppstein conditions forbid "B1..." and require either "B2..."\
# or "B3...". Since "B2..." is not compatible with the Immigration
# Game, we require every rule to have the form "B3...".
# Randomly sample some rules from the list.
#
# import classification_functions for random sampling
# and for rule generation
#
import classification_functions as cfuncs
#
# import regular expressions (re)
#
import re
#
# output file with list of totalistic life-like 
# CAs that are suitable for the Immigration Game
# and meet Eppstein's conditions.
#
output_rule_file_name = "group3-rules.txt"
#
# desired number of rules in the final list
#
num_desired = 13
#
# make a list of all possible rules
#
complete_rule_list = cfuncs.all_BS_rules()
#
# select the subset of rules that can be adapted to play
# the Immigration Game
#
candidate_rule_list = []
#
for rule in complete_rule_list:
  born_search = re.search(r'(B3[57]*/)', rule)
  survive_search = re.search(r'(S[012345678]+$)', rule)
  if born_search and survive_search: 
    born = born_search.group(1)
    survive = survive_search.group(1)
    candidate_rule_list.append(born + survive)
#
# randomly sample from candidate_rule_list
#
sample_rule_list = cfuncs.random_sample(candidate_rule_list, num_desired)
#
# write the sample list to the output file
#
output_rule_handle = open(output_rule_file_name, "w")
#
for rule in sample_rule_list:
  output_rule_handle.write(rule + "\n")
#
output_rule_handle.close()
#
#