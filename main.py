import os
import subprocess

print("copying....")
print("---------------------------")
p = subprocess.Popen('C:/Users/Abhi10/Desktop/log-capture/copy.bat', shell=True, stdout = subprocess.PIPE)
stdout, stderr = p.communicate()
if(p.returncode == 0):
    print("All container files copied successfully!!")


container_list = os.listdir("./containers")

print("containers list")
print("---------------------------")
print(container_list)

print()
container_name = input("Enter Container id: ")

log_file = "containers/"+container_name+"/"+container_name+"-json.log"

print("---------------------------")

with open(log_file, 'r') as f:
    print(f.read())
