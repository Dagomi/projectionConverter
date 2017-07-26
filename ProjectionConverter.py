'''
This is the main core of the Project Conversion tool,the orchestrator of all the sctipt
@author: David Gomez david.gomez@i2cat.com
'''

import argparse
import time

#Internal Inports
import os
import Config
import MediaInfo
import FolderGeneration
import ConfigFilesGenerator
import VideoConversion
import time


#===============================================================================
# CLI inputs
#===============================================================================

parser = argparse.ArgumentParser(description='IMMERSIATV Projection Converter',epilog='david.gomez@i2cat')
##InputFileFullPath: Path of the Premiere Xml file
parser.add_argument('-i','--InputFileFullPath')
##OutputFileFullPath: Output of the Dasher\n
parser.add_argument('-o','--OutputFileFullPath')
##JobId: Id of the job (webserver variable)\n
parser.add_argument('-f','--FramesToBeEncoded')

args = parser.parse_args()

class ProjectionConverter:
    '''
    Main Procces of the Dasher
    '''
    if __name__ == '__main__':
        
        source_xml = os.path.realpath(args.InputFileFullPath)
        path_list = source_xml.split(os.sep)
        Config.source_name = Config.format_filename(path_list[len(path_list)-2])
        
        startTime = time.time()
        
        print("-> Creating folder structure")
        FolderGeneration.OutputMainFolders(args.InputFileFullPath,args.OutputFileFullPath)
         
        print("-> Creating config files")
        ConfigFilesGenerator.create_config_input( args.InputFileFullPath, args.FramesToBeEncoded)
        ConfigFilesGenerator.CreatetConfigCubemapTransform()
         
        print("-> Converting video to YUV420")
        VideoConversion.mp4_to_yuv(args.InputFileFullPath)
        elapsedTime = time.time() - startTime
        print("-> Conversion done in: " + time.strftime('%H:%M:%S', time.gmtime(elapsedTime)))
         
        VideoConversion.equirectangular_to_cubemap()
        elapsedTime = time.time() - startTime
        print("-> Transformation done in: " + time.strftime('%H:%M:%S', time.gmtime(elapsedTime)))
        
        VideoConversion.yuv_to_mp4()
        elapsedTime = time.time() - startTime
        print("-> Transformation yuv_to_mp4 done" )
        print("-> Total time elapsed: " + time.strftime('%H:%M:%S', time.gmtime(elapsedTime)))