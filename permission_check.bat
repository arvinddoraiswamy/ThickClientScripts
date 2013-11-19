#Check permissions on a file or directory.
C:\tools\SysInternals\accesschk.exe "users" "<Directory Name>" -s -w

#Check permissions on a registry key.
C:\tools\SysInternals\accesschk.exe "users" -k "<Registry Key>" -s -w

#Check permissions on a service.
C:\tools\SysInternals\accesschk.exe "users" -c <Service Name>

#Check permissions on a process and all its threads.
C:\tools\SysInternals\accesschk.exe "users" -p <Process Name> -t

#Check permissions on Global objects. You can find these by using WinObj from the SysInternals tool suite
C:\tools\SysInternals\accesschk.exe "users" -wo \BaseNamedObjects\<Object Name>
C:\tools\SysInternals\accesschk.exe "users" -wo \Callback\<Object Name>
C:\tools\SysInternals\accesschk.exe "users" -wo \Device\<Object Name>
C:\tools\SysInternals\accesschk.exe "users" -wo \Driver\<Object Name>
C:\tools\SysInternals\accesschk.exe "users" -wo \FileSystem\<Object Name>
