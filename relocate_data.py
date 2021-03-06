import os
import paramiko 
from os import listdir

myHostname = 
myUsername =
myPassword =

def get_remote_path(sftp):
    files = sftp.listdir()
    output = []

    for f in files:
        if "CSD17" in f and "log" not in f:
            output.append(f)
        #emd
    #end

    return output
#end

def already_converted(name):
    #Checks if the file has already been converted
    files = listdir("data/")
    
    if name+".fastq" in files:
        return True
    #end
    return False
#end

def download():
    #Downloads csd17 files and converts to vector representation

    #Connect to big data server and change working directory
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(myHostname, username=myUsername, password=myPassword)
    sftp = ssh.open_sftp()
    sftp.chdir('../../data5/camdaNonC/')

    #Get files
    paths = get_remote_path(sftp)

    
    for path in paths:
        if not already_converted(path[-1-12:-1-5]):
            print("Moving "+ str(path[-1-12:-1-5]))

            #Download file
            localpath = 'data/'+str(path[-1-12:-1-5])+".fastq"
            
            sftp.get(path,localpath)
        #end
    #end

    sftp.close()
    ssh.close()  
#end

if __name__ == '__main__':
    download()
#end