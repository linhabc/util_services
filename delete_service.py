import subprocess
from os.path import isdir, join
from os import listdir
import sys
from datetime import datetime, timedelta

d = datetime.today() - timedelta(days=90)
print("Foler path: "+sys.argv[1])
filename = "filesave=" + d.strftime("%Y%m%d%H")
print("Delete from date: " + d.strftime("%Y%m%d%H"))


onlyfiles = [f for f in listdir(sys.argv[1]) if isdir(join(sys.argv[1], f))]

for file in onlyfiles:
    if(file < filename and file != "delete_service.py"):
        print("delete: "+file)

val = raw_input("Delete these files [Y]yes/[N]no: ")

if (val == "Y"):
    for file in onlyfiles:
        if(file < filename and file != "delete_service.py"):
            out = subprocess.Popen(
                ['rm', '-rf', file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            print("delete: "+file)
            stdout, stderr = out.communicate()
            print(stdout)
elif (val == "N"):
    print("Exit")
