import idaapi
import idautils

def get_all_strings():
  #Get a list of strings stored in that segment
  list_of_strings = idautils.Strings()
  for string in list_of_strings:
    f.write(str(string)+'\n')

#Wait for analysis to complete
idaapi.autoWait()

#Write results to output file
output_dir="C:\data\IDBstore\Strings_output\\"
output_filename='strings_'+str(GetInputFile())+'.txt'
f=open(output_dir+output_filename,'a')
get_all_strings()

#Close and exit
f.close()
idc.Exit(0)
