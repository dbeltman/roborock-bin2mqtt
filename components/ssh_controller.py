from distutils.cmd import Command
import paramiko, os
from sys import stdin, stdout
from datetime import datetime

host = os.getenv('ROBOROCKHOST', 'roborock-hostname-or-ip')
username = os.getenv('SSHUSER', 'root')
language=os.getenv('LANGUAGE', 'en')
bin_in_filename="/opt/rockrobo/resources/sounds/"+ language +"/bin_in.wav"
k = paramiko.RSAKey.from_private_key_file("/app/keys/robokey")

def get_metrics():
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, pkey=k)
        command="ls -ltue " + bin_in_filename + " | awk '{print $7\" \"$8\" \"$9\" \"$10}'"
        print("Executing " + command)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
        print("Closing stdin..")
        ssh_stdin.close()
        output=ssh_stdout.read()    
        ssh.close()
        print("Output:")
        rawdate=str(output.decode("utf-8")).strip()
        print(rawdate)        
    # except:
    #     print("Something foobar")
    # finally:

    try:
        emptydate=datetime.strptime(rawdate, "%b %d %H:%M:%S %Y")
        print(emptydate)
        return emptydate
    except ValueError:
        print("Date was not present in command output string..")
        exit(1)
    except:
        print("Something else went wrong parsing date") 
        exit(1)           