import re
import idaapi
import idautils

def search_for_vuln_api():
  #Repeat for list of segments
  for n in xrange(idaapi.get_segm_qty()):
    #Get number of segments
    seg = idaapi.getnseg(n)
    if seg:
      #Get list of functions in that segment
      funcs=idautils.Functions(seg.startEA, seg.endEA)
      #Search for vuln functions inside binary and print occurences to output file. This is NOT to be directly reported; perform manual analysis before doing so.
      if funcs:
        for name in funcs:
  	  each_function_disassembly = list(idautils.FuncItems(name))
  	  for e in each_function_disassembly:
  	    for vulnfunc in vuln_function_list:
  	      pattern=vulnfunc+r'$'
  	      m=re.search(pattern,idc.GetDisasm(e))
  	      if m:
  	        f.write(idc.GetFuncOffset(e)+' --> '+idc.GetDisasm(e)+'\n\n')
      else:
        f.write('Failed to get function names and hence cannot parse stuff\n')

#DPAPI, OpenSSL Blowfish, WinHTTP certificate query - Keep adding as and when you come across an API
vuln_function_list = ['CryptProtectData','CryptUnprotectData','EVP_CIPHER_CTX_init','EVP_EncryptInit_ex','EVP_DecryptInit_ex','EVP_EncryptUpdate','EVP_DecryptUpdate','BF_set_key','WinHTTPQueryOption']
pattern = []
conf = {}

#List of vulnerable functions that are searched for inside the IDB. Add more functions here.
vuln_function_list=['']

#Wait for analysis to complete
idaapi.autoWait()

#Write results to output file
output_dir="C:\data\IDBstore\\"
output_filename=str(GetInputFile())+'.txt'
f=open(output_dir+output_filename,'a')
search_for_vuln_api()

#Close and exit
f.close()
idc.Exit(0)
