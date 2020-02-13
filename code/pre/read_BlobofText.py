import sys
import json
import os

pageset=set()
max_l=0

def read_one(filename):
    global max_l
    with open(filename,'r',encoding='utf-8') as f:
        jobj=json.load(f)
        text_buffer=[]
        for page in jobj:
            text_buffer.append(jobj[page])
            pageset.add(page)
        text_buffer='\n'.join(text_buffer)
        max_l=max(max_l,len(text_buffer.split()))
    return text_buffer

def read_all(input_dir):
    files=os.listdir(input_dir)
    for file in files:
        file=os.path.join(input_dir,file,'AggregatedBlobofText',
                          os.listdir(os.path.join(input_dir,file,'AggregatedBlobofText'))[0])
        read_one(file)


read_all(sys.argv[1])