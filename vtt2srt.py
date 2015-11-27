# -*- coding: utf-8 -*-

import os
import os.path

def handle_vtt(caption):
    try:
        fp = open(caption,'r')
        lines = [line.replace('.',',') for line in fp.readlines()]
        fp.close()
        fp = open(caption,'w')
        fp.writelines(lines[2:])
        fp.close()
    except IOError as e:
        return "some default data"
        raise
    
def vtt_to_srt():
    # path = os.getcwd()
    # dirlist = [ i for i in os.listdir(path) if os.path.isdir(i)]
    # print dirlist
    # videolist = [ i for i in os.listdir(path) if os.path.isfile(i) and i[-4:] == ".mp4"]
    # captionlist = [ i for i in os.listdir(path) if os.path.isfile(i) and i[-4:] == ".vtt"]
    # print videolist,captionlist
    # for video in videolist:
        # for caption in captionlist:
            # if video[0] == caption[0] :
                # handle_vtt(caption)
                # os.rename(path+'\\'+caption,path+'\\'+video[:-4]+".srt")
    # for directory in dirlist:
        # os.chdir(path + '\\' + directory)
        # vtt_to_srt()
    for root,dirs,files in os.walk(os.getcwd()):
        videolist = list(filter(lambda x:x.split('.')[-1] == "srt",files))
        captionlist = list(filter(lambda x:x.split('.')[-1] == "mp4",files))
        

if __name__ == '__main__':
    vtt_to_srt()
