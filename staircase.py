# Print a staircase of height N
# that consists of # symbols and spaces.
# For example for N=6, here's a staircase of that height:
#       #
#      ##
#     ###
#    ####
#   #####
#  ######

def staircase(x):
    for i in range(x):
        print " " * (x - (i+1)) + "#" * (i+1)

def main():
    staircase(6)

if __name__ == '__main__':
    main()
