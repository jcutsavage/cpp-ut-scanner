# Author: John Cutsvage
# 9/13/2013

import sys, getopt
import subprocess
import glob
from os import path

global repo_path

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
            print('This script must be run within a Git repository.')
            print('USAGE: cpp-ut-scanner.py -f <inputfile> -l <logfile>')
            sys.exit()
        elif opt in ("-f", "--file"):
            inputfile = arg
        elif opt in ("-l", "--lfile"):
            logfile = arg
    
    cmd = "git rev-parse --show-toplevel"
    
    result = subprocess.run([cmd], shell=True, capture_output=True, text=True)
    
    repo_path = result.stdout
    err = result.stderr
    
    if(err != ''):
        print(err)
        sys.exit(-1)
    
    print()
    print('Repo root: ', repo_path)
    
    findstr = repo_path.rstrip() + '/**/*' + inputfile.rstrip() + '*'
    
    print('Searching for files matching', inputfile, ' in', findstr, '...')
    print()
    
    
    files = glob.glob(findstr.rstrip(), recursive=True)
    
    if all(False for _ in files):
        print("File not found!")
        sys.exit(1)
    
    scan_file = chooseFileToScan(files)
        
    file_name, file_extension = path.splitext(scan_file)
            
    if(file_extension != ".cpp" and file_extension != ".h"):
        print('Chosen path is not a C++ file')
        sys.exit(1)
        
        
def chooseFileToScan(filelist):
    
    print('Please select the file you would like to scan:')
    
    count = 1
    
    fileselector = {}
    
    for f in filelist:
        filedict = {str(count): f}
        fileselector.update(filedict)
        print(str(count) + ')', f)
        
    usrselection = input('Enter a number from the list: ')
    
    validselection = False
    
    while(validselection == False):
        if usrselection in fileselector :
          print('You have selected:', fileselector.get(usrselection))
          affirmation = input('Is this correct? [y/n]: ')
          if(affirmation.lower() == "y" or affirmation == ''):
              validselection = True
          else:
              usrselection = input('Please make another selection: ')
        else:
            usrselection = input('Please select a valid number: ')
            
    return fileselector.get(usrselection)
    
    
if __name__ == "__main__":
    main(sys.argv[1:])