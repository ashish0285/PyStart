#!/usr/bin/python3
import sys, getopt
def main(argv):
 inputfile = ''
 outputfile = ''
 try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
 except getopt.GetoptError:
    print ('app.py -i <inputfile> -o <outputfile>')
    sys.exit(2)
 for opt, arg in opts:
    if opt == '-h':
        print ('app.py -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg
 print ('Input file is "', inputfile)
 print ('Output file is "', outputfile)
if __name__ == "__main__":
 main(sys.argv[1:])
"""  getopt.getopt(args, options, [long_options]) 
Here is the detail of the parameters-
 args: This is the argument list to be parsed.
 options: This is the string of option letters that the script wants to recognize, with
options that require an argument should be followed by a colon (:).
 long_options: This is an optional parameter and if specified, must be a list of
strings with the names of the long options, which should be supported. Long
options, which require an argument should be followed by an equal sign ('='). To
accept only long options, options should be an empty string.
 This method returns a value consisting of two elements- the first is a list
of (option, value) pairs, the second is a list of program arguments left after the
option list was stripped. 
Each option-and-value pair returned has the option as its first element, prefixed
with a hyphen for short options (e.g., '-x') or two hyphens for long options (e.g., '-
-long-option').
usage: app.py -i <inputfile> -o <outputfile>
$ app.py -h
usage: app.py -i <inputfile> -o <outputfile>
$ app.py -i BMP -o
usage: app.py -i <inputfile> -o <outputfile>
$ app.py -i inputfile -o outputfile
Input file is " inputfile
Output file is " outputfile
"""
