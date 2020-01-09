#
# Rule Generator
#
# Peter Turney, October 30, 2019
#
# Read in a list of totalistic life-like rules of the
# form "B37/S236" and generate Golly rule files for 
# playing the Immmigration Game with the given rules.
# The Immigration Game requires odd numbers for birth
# (for example, "B37" but not "B47"), in order to break
# ties between the two colours (red and blue).
#
#
# import regular expressions (re)
#
import re
#
# read in a list of rules from a file
#
# - each line in the file should be one rule
#   of the form "B37/S236"
#
input_rule_file_name = "group3-rules.txt"
output_rule_file_prefix = "Group-3-"
#
input_rule_handle = open(input_rule_file_name, "r")
rule_list = []
#
for rule in input_rule_handle:
  # born numbers must be odd
  born_search = re.search(r'(B[1357]+)/', rule)
  assert born_search
  # survive numbers range from 0 to 8
  survive_search = re.search(r'(S[012345678]+$)', rule)
  assert survive_search
  # if the assertions are true, then add the rule to the list
  born = born_search.group(1)
  survive = survive_search.group(1)
  # replace "/" with "-" because "/" is not legal in a file name
  rule_list.append(born + "-" + survive)
#
input_rule_handle.close()
#
# iterate through the list of rules
#
for rule in rule_list:
  #
  # create a file name for the current rule
  #
  output_rule_file_base = output_rule_file_prefix + rule
  output_rule_file_name = output_rule_file_base + ".rule"
  #
  # open output file for writing
  #
  output_rule_handle = open(output_rule_file_name, "w")
  #
  # write the file header
  #
  output_rule_handle.write("@RULE " + output_rule_file_base + "\n")
  #
  output_rule_handle.write("@TABLE\n" + \
                           "n_states:3\n" + \
                           "neighborhood:Moore\n" + \
                           "symmetries:permute\n" + \
                           "var a={1,2}\n" + \
                           "var b={1,2}\n" + \
                           "var c={1,2}\n" + \
                           "var d={1,2}\n" + \
                           "var e={1,2}\n" + \
                           "var f={1,2}\n" + \
                           "var g={1,2}\n" + \
                           "var h={1,2}\n" + \
                           "var i={1,2}\n")
  #
  # parse the rule into born and survive
  #
  born_search = re.search(r'B([1357]+)-', rule)
  survive_search = re.search(r'S([012345678]+$)', rule)
  born = born_search.group(1)
  survive = survive_search.group(1)
  #
  # write out rules for born
  #
  # - these should all involve odd numbers
  #
  for num in list(born):
    if (num == "1"):
      output_rule_handle.write("# B1\n")
      output_rule_handle.write("0,1,0,0,0,0,0,0,0,1\n")
      output_rule_handle.write("0,2,0,0,0,0,0,0,0,2\n")
    elif (num == "3"):
      output_rule_handle.write("# B3\n")
      output_rule_handle.write("0,a,1,1,0,0,0,0,0,1\n")
      output_rule_handle.write("0,a,2,2,0,0,0,0,0,2\n")
    elif (num == "5"):
      output_rule_handle.write("# B5\n")
      output_rule_handle.write("0,a,b,1,1,1,0,0,0,1\n")
      output_rule_handle.write("0,a,b,2,2,2,0,0,0,2\n")
    else:
      assert num == "7"
      output_rule_handle.write("# B7\n")
      output_rule_handle.write("0,a,b,c,1,1,1,1,0,1\n")
      output_rule_handle.write("0,a,b,c,2,2,2,2,0,2\n")
  #
  # write out the rules for survive
  #
  for num in list(survive):
    if (num == "0"):
      output_rule_handle.write("# S0\n")
      output_rule_handle.write("1,0,0,0,0,0,0,0,0,1\n")
      output_rule_handle.write("2,0,0,0,0,0,0,0,0,2\n")
    elif (num == "1"):
      output_rule_handle.write("# S1\n")
      output_rule_handle.write("1,a,0,0,0,0,0,0,0,1\n")
      output_rule_handle.write("2,a,0,0,0,0,0,0,0,2\n")
    elif (num == "2"):
      output_rule_handle.write("# S2\n")
      output_rule_handle.write("1,a,b,0,0,0,0,0,0,1\n")
      output_rule_handle.write("2,a,b,0,0,0,0,0,0,2\n")
    elif (num == "3"):
      output_rule_handle.write("# S3\n")
      output_rule_handle.write("1,a,b,c,0,0,0,0,0,1\n")
      output_rule_handle.write("2,a,b,c,0,0,0,0,0,2\n")
    elif (num == "4"):
      output_rule_handle.write("# S4\n")
      output_rule_handle.write("1,a,b,c,d,0,0,0,0,1\n")
      output_rule_handle.write("2,a,b,c,d,0,0,0,0,2\n")
    elif (num == "5"):
      output_rule_handle.write("# S5\n")
      output_rule_handle.write("1,a,b,c,d,e,0,0,0,1\n")
      output_rule_handle.write("2,a,b,c,d,e,0,0,0,2\n")
    elif (num == "6"):
      output_rule_handle.write("# S6\n")
      output_rule_handle.write("1,a,b,c,d,e,f,0,0,1\n")
      output_rule_handle.write("2,a,b,c,d,e,f,0,0,2\n")
    elif (num == "7"):
      output_rule_handle.write("# S7\n")
      output_rule_handle.write("1,a,b,c,d,e,f,g,0,1\n")
      output_rule_handle.write("2,a,b,c,d,e,f,g,0,2\n")
    else:
      assert num == "8"
      output_rule_handle.write("# S8\n")
      output_rule_handle.write("1,a,b,c,d,e,f,g,h,1\n")
      output_rule_handle.write("2,a,b,c,d,e,f,g,h,2\n")
  #
  # write out the rules for die
  #
  # - die equals NOT survive
  #
  die = ""
  for i in range(9):
    if (str(i) not in survive):
      die = die + str(i)
  #
  for num in list(die):
    if (num == "0"):
      output_rule_handle.write("# D0\n")
      output_rule_handle.write("a,0,0,0,0,0,0,0,0,0\n")
    elif (num == "1"):
      output_rule_handle.write("# D1\n")
      output_rule_handle.write("a,b,0,0,0,0,0,0,0,0\n")
    elif (num == "2"):
      output_rule_handle.write("# D2\n")
      output_rule_handle.write("a,b,c,0,0,0,0,0,0,0\n")
    elif (num == "3"):
      output_rule_handle.write("# D3\n")
      output_rule_handle.write("a,b,c,d,0,0,0,0,0,0\n")
    elif (num == "4"):
      output_rule_handle.write("# D4\n")
      output_rule_handle.write("a,b,c,d,e,0,0,0,0,0\n")
    elif (num == "5"):
      output_rule_handle.write("# D5\n")
      output_rule_handle.write("a,b,c,d,e,f,0,0,0,0\n")
    elif (num == "6"):
      output_rule_handle.write("# D6\n")
      output_rule_handle.write("a,b,c,d,e,f,g,0,0,0\n")
    elif (num == "7"):
      output_rule_handle.write("# D7\n")
      output_rule_handle.write("a,b,c,d,e,f,g,h,0,0\n")
    else:
      assert num == "8"
      output_rule_handle.write("# D8\n")
      output_rule_handle.write("a,b,c,d,e,f,g,h,i,0\n")
  #
  # set the colours
  #
  output_rule_handle.write("@COLORS\n")
  output_rule_handle.write("0 255 255 255 white\n")
  output_rule_handle.write("1 255 0 0 red\n")
  output_rule_handle.write("2 0 0 255 blue\n")
  #
  # close output file
  #
  output_rule_handle.close()
  #
#
#
#