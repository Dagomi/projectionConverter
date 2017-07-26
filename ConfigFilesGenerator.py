'''
Created on 21 jul. 2017

@author: Pc
'''
import io
import MediaInfo
import Config
LevelProfile_264 = {'720p': '3.1', '1080p': '4', '2k': '4.2','4k': '5.1','8k': '6'}

def create_config_input(InputFile, FramesToBeEncoded):
    '''
    #======== File I/O ===============
    InputFile                     : midterm_1.yuv
    InputBitDepth                 : 8           # Input bitdepth
    InputChromaFormat             : 420         # Ratio of luminance to chrominance samples
    FrameRate                     : 25          # Frame Rate per second
    FrameSkip                     : 0           # Number of frames to be skipped in input
    SourceWidth                   : 2048         # Input  frame width
    SourceHeight                  : 1024         # Input  frame height
    FramesToBeEncoded             : 15390         # Number of frames to be coded
    Level                         : 5    '''

    InputBitDepth = MediaInfo.ObtainStreamsParamaeters(InputFile, "bits_per_raw_sample")
    FrameRate = MediaInfo.ObtainStreamsParamaeters(InputFile, "frame_rate")
    SourceWidth = MediaInfo.ObtainStreamsParamaeters(InputFile, "width")
    SourceHeight = MediaInfo.ObtainStreamsParamaeters(InputFile, "height")

    if FramesToBeEncoded == "0":
        FramesToBeEncoded_var = MediaInfo.ObtainStreamsParamaeters(InputFile, "nb_frames")
    else:
        FramesToBeEncoded_var = FramesToBeEncoded
    
    Config.frames = FramesToBeEncoded_var
    profile = h264LevelProfile(SourceWidth)
    
    with io.FileIO(Config.ConfigFolder + "/" + Config.source_name + ".cfg", "w") as file:
        file.write("#======== File I/O ===============\n")
        file.write("InputFile                     : %s.yuv\n" % Config.source_name)
        file.write("InputBitDepth                 : %s\n" % InputBitDepth)
        file.write("InputChromaFormat             : 420\n")
        file.write("FrameRate                     : %s\n" %FrameRate)
        file.write("FrameSkip                     : 0\n")
        file.write("SourceWidth                   : %s\n" % SourceWidth)
        file.write("SourceHeight                  : %s\n" % SourceHeight)
        file.write("FramesToBeEncoded             : %s\n" % FramesToBeEncoded_var)
        file.write("\n")
        file.write("Level             : %s\n" % profile)
        
        
def CreatetConfigCubemapTransform():

    '''
    #======== File I/O =====================
    OutputFile                    : conv.yuv
    #RefFile                       : reference_file_name
    #======== Unit definition ================
    FaceSizeAlignment             : 1           # face size alignment;
    
    #=========== Misc. ============
    InternalBitDepth              : 8          # codec operating bit-depth
    
    #============ 360 video settings ======================
    InputGeometryType                 : 0                                   # 0: equirectangular; 1: cubemap; 2: equalarea; this should be in the cfg of per sequence.
    SourceFPStructure                 : 1 1   0 0                           # frame packing order: numRows numCols Row0Idx0 ROT Row0Idx1 ROT ... Row1...
                                                                            # rotation degrees[0, 90, 180, 270] is anti-clockwise;
    CodingGeometryType                : 1
    CodingFPStructure                 : 2 3   4 0 0 0 5 0   3 180 1 270 2 0  # frame packing order: numRows numCols Row0Idx0 ROT Row0Idx1 ROT ... Row1...
                                                                            # rotation degrees[0, 90, 180] is anti-clockwise;
    SVideoRotation                    : 0 0 0                               # rotation along X, Y, Z;                 
    CodingFaceWidth                   : 960                                   # 0: automatic calculation;
    CodingFaceHeight                  : 960                                   # 0: automatic calculation;
    #ViewPortSettings                  : 80.0 80.0  -90.0  0.0               # view port settings: horizontal FOV [0,360], vertical FOV [0, 180], yaw [-180, 180], pitch [-90, 90]
    SphFile                           : sphere_655362.txt
    
    ### DO NOT ADD ANYTHING BELOW THIS LINE ###
    ### DO NOT DELETE THE EMPTY LINE BELOW ###
    '''
    with io.FileIO(Config.ConfigFolder + "/"  + "equirectangular_2_cubemap_.cfg", "w") as file:
        file.write("#======== File I/O ===============\n")
        file.write("OutputFile                    : conv.yuv\n")
        file.write("#RefFile                       : reference_file_name\n")
        file.write("\n")
        file.write("#======== Unit definition ================\n")
        file.write("FaceSizeAlignment             : 1 \n")
        file.write("\n")
        file.write("#=========== Misc. ============\n")
        file.write("InternalBitDepth              : 8\n")
        file.write("\n")
        file.write("#============ 360 video settings ======================\n")
        file.write("InputGeometryType                 : 0\n")
        file.write("SourceFPStructure                 : 1 1   0 0\n")
        file.write("\n")
        file.write("CodingGeometryType                : 1\n")
        file.write("CodingFPStructure                 : 2 3   4 0 0 0 5 0   3 180 1 270 2 0\n")
        file.write("SVideoRotation                    : 0 0 0\n")
        file.write("\n")
        file.write("CodingFaceWidth                   : 960\n")
        file.write("CodingFaceHeight                  : 960\n")
        file.write("#ViewPortSettings                  : 80.0 80.0  -90.0  0.0\n")
        file.write("SphFile                           : sphere_655362.txt\n")
        file.write("\n")
        file.write("### DO NOT ADD ANYTHING BELOW THIS LINE ###\n")
        file.write("### DO NOT DELETE THE EMPTY LINE BELOW ###\n")
        file.write("\n")

def h264LevelProfile (width):
    if 1 <= width <= 1919:
        return LevelProfile_264['720p']
    if 1920 <= width <= 2047:
        return LevelProfile_264['1080p']
    if 2048 <= width <= 3839:
        return LevelProfile_264['2k']
    if 3840 <= width <= 4095:
        return LevelProfile_264['4k']
    if 4096 <= width <= 8192:
        return LevelProfile_264['8k']
    