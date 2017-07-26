'''
Created on 24 jul. 2017

@author: Pc
'''
#===============================================================================
# Obtain media information to the source imput
#===============================================================================
import json
import os
import Config
def GenerateJson(mediaFile):
    comand = "ffprobe %s -v quiet -print_format json -show_format -show_streams" % mediaFile
    jsonString = os.popen(comand).read()
    jsonDatatry = json.loads(jsonString)
    return jsonDatatry

def ObtainFormatParamaeters(mediaFile, parameter):
    jsonDatatry = GenerateJson(mediaFile)
    #frame rate
    if parameter == 'duration':
        duration = []
        #Video duration
        duration_unformated = jsonDatatry['format']['duration']
        time = (duration_unformated.split('.'))
        #minutes
        duration.append(str(((int(time[0]))/60)))
        #seconds
        duration.append(str(((float(time[1]))/100000)))
        return duration
    param = jsonDatatry['format'][parameter]
    
    return param

def ObtainStreamsParamaeters(mediaFile, parameter):
    jsonDatatry = GenerateJson(mediaFile)
    if parameter == 'frame_rate':
        frame_rate = jsonDatatry['streams'][0]['r_frame_rate']
        frame_rate_split = (frame_rate.split('/'))
        '''TODO: Change a dynamic fps in a future, fix the origin lecture'''
        frame_rate_split[0] = "25"
        return frame_rate_split[0]
        
    if parameter == 'language':
        try:
            language = jsonDatatry['streams'][0]['tags']['language']
            return language
        except KeyError:
            return "und"
    if parameter == 'time_base':
        time_base = jsonDatatry['streams'][0]['time_base']
        time_base_split = (time_base.split('/'))
        return time_base_split[1]
    param = jsonDatatry['streams'][0][parameter]
    return param
