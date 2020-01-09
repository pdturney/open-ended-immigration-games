#
# Classification Main
#
# Peter Turney, October 29, 2019
#
# Find a way to score the 2**18 possible outer-totalistic 
# automata rules, such that the Game of Life (and hopefully
# other universal cellular automata) gets a high score.
#
# https://www.conwaylife.com/wiki/List_of_Life-like_cellular_automata
#
import golly as g
import numpy as np
import random as rand
import classification_functions as cfuncs
import classification_parameters as cparams
#
# make a list of B/S rules (born/survive -- outer-totalistic)
#
rule_file_name = cparams.rule_file_name
rule_list = cfuncs.txt_BS_rules(rule_file_name)
#
# density range for initial random matrix
#
density_range = cparams.density_range
#
# width and height for initial random square matrix
#
initial_size = cparams.initial_size
#
# number of steps for given run of simulation
#
num_steps = cparams.num_steps
#
# number of random trials to evaluate
#
num_trials = cparams.num_trials
#
# margins for calculating die / shrink / stable /expand / explode
#
# - margins are defined as fractions of the initial population
#
# - e.g.:   margins = [0.2, 0.8, 1.25, 5.0]
#
#           final pop < 0.2 * initial pop   --> die
#           final pop < 0.8 * initial pop   --> shrink
#           final pop < 1.25 * initial pop  --> stable
#           final pop < 5.0 * initial pop   --> expand
#           else                            --> explode
#
margins = cparams.margins
#
# Golly screen magnification
#
screen_mag = cparams.screen_mag
#
# initialize Golly
#
g.setalgo("QuickLife") # select the algorithm for Golly
g.autoupdate(False) # do not update the view unless requested
g.new("Classification") # create a new, empty universe and set the window title
g.setmag(screen_mag) # screen magnification
#
# prepare log file for recording statistics
#
# - use option 0 so that log file writes immediately (no buffer), 
#   in case of forced exit (crash)
#
log_path = cparams.log_path
log_handle = open(log_path, "w", 0)
#
# show parameter settings in the log file
#
parameter_settings = cfuncs.show_parameters()
log_handle.write("\nParameter Settings\n\n")
for setting in parameter_settings:
  log_handle.write(setting + "\n")
log_handle.write("\n")
#
# write a header line for the list of results
#
#                "rule  die  shrink  stable expand  explode"
log_handle.write("rule\tdie\tshrink\tstable\texpand\texplode\n")
#
# -------------------------------------------------
# main loop: iterate through the list of rules
# -------------------------------------------------
#
for rule in rule_list:
  #
  # initialize die / shrink / stable /expand / explode
  #
  die_sum = 0.0
  shrink_sum = 0.0
  stable_sum = 0.0
  expand_sum = 0.0
  explode_sum = 0.0
  #
  for trial in range(num_trials):
    #
    # show the rule and the trial number in the Golly header
    #
    g.show(rule + " -- trial " + str(trial + 1))
    #
    # initialize a random matrix
    #
    prob_one = rand.uniform(density_range[0], density_range[1]) 
    initial_matrix = np.zeros((initial_size, initial_size), dtype=np.int)
    initial_pop_count = 0
    for x in range(initial_size):
      for y in range(initial_size):
        if (rand.uniform(0, 1) <= prob_one):
          initial_matrix[x][y] = 1
          initial_pop_count = initial_pop_count + 1
    #
    # initialize Golly
    #
    g.new("Classification") # make a new, empty Golly universe
    g.setmag(screen_mag) # screen magnification
    g.setrule(rule) # set the rule that Golly will use
    offset = int(initial_size / 2) # this centers the matrix in the display
    # write initial matrix into the Golly universe
    for x in range(initial_size):
      for y in range(initial_size):
        g.setcell(x - offset, y - offset, initial_matrix[x][y])
    #
    # run Golly for num_steps
    #
    g.run(num_steps) 
    g.update() # update the Golly display
    #
    # read the updated matrix from the Golly universe
    #
    # - with each step, the matrix size increases by two
    #   new outer columns and two new outer rows
    #
    expanded_size = initial_size + (2 * num_steps)
    updated_matrix = np.zeros((expanded_size, expanded_size), dtype=np.int)
    offset = int(expanded_size / 2) # this centers the matrix in the display
    final_pop_count = 0
    for x in range(expanded_size):
      for y in range(expanded_size):
        if (g.getcell(x - offset, y - offset) == 1):
          updated_matrix[x][y] = 1
          final_pop_count = final_pop_count + 1
    #
    # update die / shrink / stable /expand / explode
    #
    if (final_pop_count < (initial_pop_count * margins[0])):
      die_sum = die_sum + 1
    elif (final_pop_count < (initial_pop_count * margins[1])):
      shrink_sum = shrink_sum + 1
    elif (final_pop_count < (initial_pop_count * margins[2])):
      stable_sum = stable_sum + 1
    elif (final_pop_count < (initial_pop_count * margins[3])):
      expand_sum = expand_sum + 1
    else:
      explode_sum = explode_sum + 1
    #
    # end of trial loop
    #
  #
  # report some statistics
  #
  die_pct = float(die_sum) / num_trials
  shrink_pct = float(shrink_sum) / num_trials
  stable_pct = float(stable_sum) / num_trials
  expand_pct = float(expand_sum) / num_trials
  explode_pct = float(explode_sum) / num_trials
  #
  log_handle.write(rule + "\t" + \
    str(die_pct) + "\t" + \
    str(shrink_pct) + "\t" + \
    str(stable_pct) + "\t" + \
    str(expand_pct) + "\t" + \
    str(explode_pct) + "\n")
  #
  # end of rule loop
  #
#
# close log file
#
log_handle.write("\nDone.\n")
log_handle.close()
# 
#