from sys import stdin, stdout
from datetime import datetime
import paramiko, os

host = os.getenv('ROBOROCKHOST', 'roborock-hostname-or-ip')
username = os.getenv('SSHUSER', 'root')
language=os.getenv('LANGUAGE', 'en')

bin_in_filename="/opt/rockrobo/resources/sounds/"+ language +"/bin_in.wav"

ssh = paramiko.SSHClient()
k = paramiko.RSAKey.from_private_key_file("/app/keys/robokey")
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=username, pkey=k)

try:
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls -ltue " + bin_in_filename + " | awk '{print $7\" \"$8\" \"$9\" \"$10}'")

except:
    print("Something foobar")
finally:
    print("Closing Connection..")
    ssh_stdin.close()
    output=ssh_stdout.read()    
    ssh.close()
    print("Output:")
    commandoutput=str(output.decode("utf-8")).strip()
    print(commandoutput)

try:
    emptydate=datetime.strptime(commandoutput, "%b %d %H:%M:%S %Y")
    print(emptydate)
except ValueError:
    print("Date was not present in command output string..")
except:
    print("Something else went wrong parsing date")
