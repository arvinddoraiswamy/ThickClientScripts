import sys
import re
import os

def read_config_file():
  f=open('config.txt','rU')
  for line in f:
    m=re.search(r'^#',line)
    if not m:
      t1=line.split('=')
      conf[t1[0]] = t1[1]
  f.close()

def search_for_applicable_files():
  dirs=[]
  extensions=[]

  dirs=conf['directories'].split(';')
  extensions=conf['vuln_functions_file_types'].split(';')

  for dirname in dirs:
    dirname.rstrip()
    for root,dirs,filename_list in os.walk(dirname):
      for f1 in filename_list:
        if f1.endswith(".exe") or f1.endswith(".dll") or f1.endswith(".sys"):
	  filelist.append(os.path.join(root,f1))

def write_to_file():
  f=open('C:\data\Exe_file_list.txt','w')
  for filename in filelist:
    f.write(filename+'\n')
  f.close()

conf={}
filelist=[]
read_config_file()
search_for_applicable_files()
write_to_file()
