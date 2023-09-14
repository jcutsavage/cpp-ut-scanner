# Author: John Cutsvage
# 9/13/2013

import sys, getopt


def main(argv):
    inputfile = ''
    logfile = ''
    
    try:
        opts, args = getopt.getopt(argv, "hf:l:", ["file=","lfile="])
    except getopt.GetoptError as e:
        print('ERROR: Invalid', str(e))
        print('USAGE: cpp-ut-scanner.py -f <inputfile> -l <logfile>')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print('USAGE: cpp-ut-scanner.py -f <inputfile> -l <logfile>')
            sys.exit()
        elif opt in ("-f", "--file"):
            inputfile = arg
        elif opt in ("-l", "--lfile"):
            logfile = arg
            
    print('Input file is ', inputfile)
    print('Log file is ', logfile)
    
if __name__ == "__main__":
    main(sys.argv[1:])