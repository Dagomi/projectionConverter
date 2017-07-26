'''
Created on 24 jul. 2017

@author: Pc
'''
import os
import Config
import sys
import ProgressConversion
from subprocess import Popen, PIPE, STDOUT


def progress(count, total):
    bar_len = 10
    filled_len = int(round(bar_len * count / float(total)))
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    print ('[%s] \r' % (bar)),

    
def status_handler(old, new):
    print "Conversion {0} %".format(old),
    progress(old, 100)
    
    
def mp4_to_yuv(source):
    
    input_source = source
    output_yuv = Config.TempFolder 
    
    cmd = "ffmpeg -i " + input_source + " -c:v rawvideo -pix_fmt yuv420p " + output_yuv + "/" + Config.source_name + ".yuv"
    print cmd
    converter = ProgressConversion.ProgressConversion()
    converter.RunSession(cmd, status_handler=status_handler)
    print ("Conversion {100} %")
    
def equirectangular_to_cubemap():
    
    cmd = Config.WINDOWS_TApp360Convert + "TApp360Convert.exe"
    cmd += " -c " + Config.ConfigFolder + "/" +"equirectangular_2_cubemap_.cfg"
    cmd += " -c " + Config.ConfigFolder + "/" + Config.source_name + ".cfg"
    cmd += " -i " + Config.TempFolder + "/" + Config.source_name + ".yuv"
    cmd += " -o " + Config.TempFolder + "/" + Config.source_name + ".yuv"
    cmd += " -f " + Config.frames
    print cmd
    os.system(cmd)  
    
def yuv_to_mp4():
    
    CodingFaceWidth = 960
    CodingFaceHeight = 960
    
    CubeFaceWidth = str(3 * CodingFaceWidth)
    CubeFaceHeight = str(2 * CodingFaceHeight)
    
    input_source = Config.TempFolder + "/" + Config.source_name + "_" + CubeFaceWidth + "x" + CubeFaceHeight + "x8_cf1"
    output_yuv = Config.OutputTransformationFolder + "/" + Config.source_name + "_cubemap32"
    
    cmd = " ffmpeg -f rawvideo"
    cmd += " -s:v %sx%s" % (CubeFaceWidth,CubeFaceHeight) 
    cmd += " -r 25" 
    cmd += " -i %s.yuv" % input_source 
    cmd += " -c:v libx264"
    cmd += " %s.mp4" % output_yuv

    print cmd
    converter = ProgressConversion.ProgressConversion()
    converter.RunSession(cmd, status_handler=status_handler)
    print ("Conversion {100} %")