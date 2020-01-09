"""
Classification Functions

Peter Turney, October 29, 2019
"""
import golly as g
import numpy as np
import random as rand
import csv
import classification_parameters as cparams
#
# all_BS_rules() -- returns a list of all possible B/S rules (born/survive)
#
def all_BS_rules():
  """
  Make a list of all possible B/S rules (born/survive)
  - https://www.conwaylife.com/wiki/Rulestring#B.2FS_notation
  - there are 2^18 = 262,144 possible B/S rules
  - the Game of Life is "B3/S23" (born if 3 live neighbours / survive if 2 or 3)
  - the null rule "B/S" is legal, as is "B1/S" or "B/S1"
  - Golly supports all 262,144 of these rules
  """
  #
  num_rules = 2 ** 18
  rule_list = []
  #
  for rule_num in range(num_rules):
    # convert rule_num to a binary string with 18 characters
    # e.g. 14 --> '000000000000001110'
    binary_string = format(rule_num, '018b')
    # the binary string '111111111111111111' yields the rule
    # 'B012345678/S012345678' -- if there are any 0 values
    # in the binary string, then we delete the corresponding
    # number from the rule 'B012345678/S012345678'
    born = binary_string[0:9] # first 9 bits in binary_string
    survive = binary_string[9:18] # last 9 bits in binary_string
    # born
    rule = "B"
    for pos in range(9):
      if (born[pos] == '1'):
        rule = rule + str(pos)
    # survive
    rule = rule + "/S"
    for pos in range(9):
      if (survive[pos] == '1'):
        rule = rule + str(pos)
    # append the new rule to rule_list
    rule_list.append(rule)
  #
  return rule_list
#
# tsv_BS_rules(rule_file_name) -- load B/S rules from a tsv file
#
def tsv_BS_rules(rule_file_name):
  """
  Load a list of B/S rules from a file. We assume the file is a
  tab-separated value (tsv) file with the B/S rule in the second
  column (column number 1, starting from 0).
  """
  #
  rule_list = []
  #
  with open(rule_file_name) as tsvfile:
    reader = csv.reader(tsvfile, delimiter = '\t')
    for row in reader:
      rule = row[1] # extract second column from row
      rule_list.append(rule) 
  #
  return rule_list
#
# txt_BS_rules(rule_file_name) -- load B/S rules from a txt file
#
def txt_BS_rules(rule_file_name):
  """
  Load a list of B/S rules from a file. We assume the file is a
  plain text file with one B/S rule in each line.
  """
  #
  rule_list = []
  rule_handle = open(rule_file_name, "r")
  #
  for rule in rule_handle:
    rule_list.append(rule.strip()) # strip() removes newline character
  #
  return rule_list
#
# show_parameters() -- returns a list of parameters and values
#
def show_parameters():
  """
  Make a list of the parameters in cparams and show
  the value of each parameter.
  """
  parameter_names = sorted(dir(cparams))
  display_list = []
  #
  for name in parameter_names:
    # skip over system names
    # - system names have the form "__file__"
    if (name[0] != "_"): 
      value = str(getattr(cparams, name))
      display_list.append(name + " = " + value)
  #
  return display_list
#
# random_sample(rule_list, sample_size) -- returns sample_list
#
def random_sample(rule_list, sample_size):
  """
  Get a random sample of sample_size rules from the rule list.
  """
  #
  # To avoid duplicates in the sample, randomize the order of the
  # rule list and then take the first sample_size rules
  # from the randomized list.
  #
  total_size = len(rule_list)
  assert total_size > sample_size
  assert sample_size > 0
  # attach a random number to each rule in the rule list
  randomized_rule_list = []
  for i in range(total_size):
    # item = [random real number between 0 and 1, the i-th rule]
    item = [rand.uniform(0, 1), rule_list[i]]
    randomized_rule_list.append(item)
  # sort randomized_rule_list in order of the attached random numbers
  randomized_rule_list.sort(key = lambda x: x[0]) # sort by random number
  # take the top sample_size items from randomized_rule_list and
  # remove their attached random numbers
  sample_list = []
  for i in range(sample_size):
    sample_list.append(randomized_rule_list[i][1]) # drop random number
  # return the cleaned-up list of sample_size rules
  return sample_list
#
#
#
