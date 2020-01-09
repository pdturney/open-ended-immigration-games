#
# Classification Parmeters
#
# Peter Turney, October 29, 2019
#
# Set various parameters for running experiments
#
#
#
# path to log file for recording statistics
#
log_path = "group3-classes.txt"
#
# name of file containing B/S rules
#
rule_file_name = "group3-rules.txt"
#
# density range for initial random matrix
#
density_range = [0.1, 0.9]
#
# width and height for initial random square matrix
# of boolean values
#
initial_size = 16
#
# number of steps for given run of simulation
#
num_steps = 200
#
# number of trials to evaluate for each rule
#
num_trials = 1000
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
margins = [0.2, 0.8, 1.25, 5.0]
#
# screen magnification for Golly
#
screen_mag = 2 # mag 3 = ratio 1:8
#