#!/usr/bin/python

import os
import glob
from os.path import expanduser
import sys, getopt
import time

def main(argv):
    inputfile = ''
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
    except getopt.GetoptError:
      print 'signature_installer.py -i <inputfile>'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print 'signature_installer.py -i <inputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
    print 'Input file is "', inputfile

    home = expanduser("~")  # Get users home folder

    # Test to see which signature folder to use, depending on OS version
    if os.path.exists('{}/Library/Mail/V4/MailData/Signatures/'.format(home)):
      signatures_folder = ('/Library/Mail/V4/MailData/Signatures/')
    elif os.path.exists('{}/Library/Mail/V3/MailData/Signatures/'.format(home)):
      signatures_folder = ('/Library/Mail/V3/MailData/Signatures/')
    elif os.path.exists('{}/Library/Mail/V2/MailData/Signatures/'.format(home)):
      signatures_folder = ('/Library/Mail/V2/MailData/Signatures/')
    else:
      print("No Mail Signature folder found! Something is wrong...")
      sys.exit(2)

    list_of_files = glob.glob('{}{}*.mailsignature'.format(home, signatures_folder))  # Get list of files in signature directory
    latest_signature = max(list_of_files, key=os.path.getctime)  # Get last edited file in signatures folder
    print(latest_signature)

    #Get html signature from input file
    f = open(inputfile, 'r')
    html_signature = f.read()
    f.close()

    #Create backup of current mail signature
    f = open(latest_signature, 'r')
    current_signature = f.read()
    f.close()
    f = open('{}.{}.old'.format(latest_signature, time.strftime("%Y.%m.%d.%H%M%S")), 'w')
    f.write(current_signature)
    f.close()

    #Read first 5 lines of current signature from mail directory
    with open(latest_signature) as myfile:
       new_signature = [next(myfile) for x in xrange(5)]
    new_signature = ''.join(map(str, new_signature)) #Create string from list of first 5 lines read from file
    new_signature = new_signature + '\n' + html_signature #Append html for first 5 lines of signature
    print(new_signature)

    #Write new signature to disk
    wr = open(latest_signature, 'w')
    wr.write(new_signature)
    wr.close()

    os.system("chflags uchg {}".format(latest_signature))

if __name__ == "__main__":
   main(sys.argv[1:])




