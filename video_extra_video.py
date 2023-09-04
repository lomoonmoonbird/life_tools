# -*- coding: UTF-8 -*-

import os
import re
import subprocess
import shlex

def strQ2B(ustring):

    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                              #全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring

def FullToHalf(s):
    n = []
    s = s
    for char in s:
        num = ord(char)
        if num == 0x3000:
            num = 32
        elif 0xFF01 <= num <= 0xFF5E:
            num -= 0xfee0
        num = chr(num)
        n.append(num)
    return ''.join(n)

def change_file_name(dir):

    for root,b,files in os.walk(dir):
        for file in files:
            name, suffix = os.path.splitext(file)
            if suffix == '.flv' and re.match('[0-1]', name):
                replace_name = re.sub(r' ', '', FullToHalf(name))
                origin_path = os.path.join(root, file)
                # print(origin_path)
                new_path = os.path.join(root, replace_name+suffix)
                os.rename(origin_path, new_path)
                mp3_file = os.path.join(root, replace_name+'.mp3')
                convert_from_flv_to_mp3(origin_path, "/Users/moonmoonbird/"+replace_name+'.mp3')

def convert_from_flv_to_mp3(src, dest):
    # command = shlex.split("ffmpeg -i "+src+"  -vn -acodec libmp3lame "+dest)
    command = shlex.split("ffmpeg -i "+src+" -c copy -bsf:a aac_adtstoasc "+ dest)
    subprocess.run(command)


change_file_name("/Volumes/Player")