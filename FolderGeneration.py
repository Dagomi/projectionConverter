'''
Create all the folder structure.
@author: David Gomez david.gomez@i2cat.com
'''
#Common Imports
import glob
import os
import shutil

#Internal Imports
import Config

#External Tools
def OutputMainFolders(PremierXml,OutputFileFullPath):
    # create #logger with 'Folder Generation'

    #=============================================================================
    #Create the Main Output Folder and define the log file
    #=============================================================================
    Config.OuputhPath = OutputFileFullPath
    source_xml = os.path.realpath(PremierXml)
    Config.InputhPath = os.path.dirname(PremierXml)
    path_list = source_xml.split(os.sep)
    name_premier_project = path_list[len(path_list)-2]
    name_premier_project = Config.format_filename(name_premier_project)

    Config.PremierProjectName = name_premier_project

    absoluteOutputPath = OutputFileFullPath + "/" +  name_premier_project
    #Allows the videos in MPEG-DASH format: Video-> h264 or h265 and audio in aac.
    # This videos are removed at the end of the encoder process

    #Premier Folder
    if (not(os.path.exists(absoluteOutputPath))):
        os.mkdir(absoluteOutputPath)
        Config.MainPathFolder = absoluteOutputPath

    #Temps Folder
    if (not(os.path.exists(absoluteOutputPath + "/Temp"))):
        os.mkdir(absoluteOutputPath + "/Temp")
        Config.TempFolder = absoluteOutputPath + "/Temp"

    #===========================================================================
    # Create Video output
    #===========================================================================
    #Video Folder
    if (not(os.path.exists(absoluteOutputPath + "/" + "Video"))):
        os.mkdir(absoluteOutputPath + "/" + "Video")
        Config.OutputTransformationFolder = absoluteOutputPath + "/Video"
    
    #===========================================================================
    # Create Config output
    #===========================================================================
    #Video Folder
    if (not(os.path.exists(absoluteOutputPath + "/" + "Config"))):
        os.mkdir(absoluteOutputPath + "/" + "Config")
        Config.ConfigFolder = absoluteOutputPath + "/Config"
 
#===============================================================================
# Remove temporale files and directories
#===============================================================================
def RemoveTempsFolder():
    '''
    Remove the Temp Folders
    '''
    print("Remove temp files:" + Config.TempFolder)
    shutil.rmtree(Config.TempFolder)