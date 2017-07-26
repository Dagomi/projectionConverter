'''
Created on 24 jul. 2017

@author: Pc
'''

#Path TApp360Converter
WINDOWS_TApp360Convert = "C:/JEM/bin/vc2015/x64/Release/"
LINUX_TApp360Convert = ""

#Gloval variables
source_name = ""

#Absolute Paths
OuputhPath = ""

#Path folders
TempFolder = ""
OutputTransformationFolder = ""
ConfigFolder = ""

#Media
frames = "" #Frames to convert


def format_filename(filename):
    invalid_chars_list = '!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~ \t\n\r\x0b\x0c'
    invalid_chars = u"%s" % (invalid_chars_list)

    keyinvalidDict = {}

    for idx, chr_ in enumerate(invalid_chars):
        keyinvalidDict[chr_] = idx

    
    for k in filename:
        if k in keyinvalidDict.keys():
            filename = filename.replace(k,'_') # I don't like spaces in filenames.                
    return filename