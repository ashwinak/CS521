#!/usr/bin/python3
import re
import os
import sys

class stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def dump(self):
         return str(self.items)

def symlink_ctime( syml ):
    return os.lstat(syml).st_ctime

# this function returns the most recent release of a particular branch
def latest_mr( branch ):
    yr = int(re.search('([0-9]{1,2})', branch).group(1))
    relnum = int(re.search('[0-9]{1,2}\.([0-6])', branch).group(1))
    path=os.path.join("/volume/build/junos/", str(yr)+"."+str(relnum)+"/release/")
    result = []
    for d in os.listdir(path):
        branchd = os.path.join(path, d)
        if os.path.isdir(branchd) and re.search(branch+"\.[0-9]+$", branchd): result.append(branchd)
    return max(result, key=symlink_ctime)

mr_dir = latest_mr( branch = sys.argv[1])
mr = os.path.basename(mr_dir)
print("1) Assuming the latest MR in this branch is " + mr)
print("2) MR base directory: " + mr_dir + "/")

yr = int(re.search('([0-9]{1,2})', sys.argv[1]).group(1))
relnum = int(re.search('[0-9]{1,2}\.([0-6])', sys.argv[1]).group(1))
if yr < 16:
    if yr<14:
        ddl_dir = "src/esp-shared/lib/ddl/input"
    else:
        ddl_dir = "src/ui/ddl/input"
else:
    if yr == 16:
        if relnum > 1:
            ddl_dir = "src/junos/ddl/features"
        else:
            ddl_dir = "src/ui/ddl/input"
        #end if
    else:
        ddl_dir = "src/junos/ddl/features"
    #end if
#end if

ddl_dir = os.path.join(mr_dir,ddl_dir)
print("3) Assuming DDL directory should be:" + ddl_dir )

print("4) Looking for DDL files...")
success=0
while not success:
    if os.path.exists(ddl_dir):
        print("    " + mr + " DDL directory found ... [OK]")
        success=1
    else:
#        print("    Cannot find DDL directory for this MR. Trying previous one... " )
        respin = int(re.search('([0-9]{1,}$)', mr).group(1)) - 1
        if respin==0:
            print("    Cannot find DDL directory for any MR of this branch. Try anothe one. Exiting now.\n" )
            quit()
        mr = re.sub('[0-9]{1,}$', str(respin), mr)
        print("    Cannot find DDL directory for this MR. Trying previous one... " + mr )

cmd_desc=""
for top, dirs, files in os.walk(ddl_dir):
    for nm in files:
        if "cmd.dd" in os.path.join(top, nm):
            print('\n------------------\n' + os.path.join(top, nm) + '\n------------------')
            f = open(os.path.join(top, nm))
            s = stack()
            hidden=0
            for line in iter(f):
                if "{" in line:
                    s.push(line)
                    if hidden and cmd_desc:
                        print(" " + cmd_desc.strip())
                        hidden=0
                    #end if
                if "help" in line:
                    cmd_desc = line.replace("help", "description: ")
                if "hidden" in line:
                    if "juniper-command " in s.dump():
                        cmd = s.dump()
#                        print cmd
                        cmd = cmd.replace('\\n', '')
                        cmd = cmd.replace('\\t', '')
                        cmd = re.sub('[,\[\]\{\}\']|(juniper-command)|(command )|(argument )|(choice )|(verbosity )|(type )|(enum )|(int )', '', cmd)
                        cmd = re.sub(' +',' ',cmd)
                        print(cmd.strip())
                        if cmd_desc:
                            print(" " + cmd_desc.strip())
                        else:
                            hidden=1
                        #end if
                    #end if
                if "}" in line:
                    if hidden and cmd_desc:
                        print(" " + cmd_desc.strip())
                        hidden=0
                    #end if
                    cmd_desc = ""
                    s.pop()
                #end if
            f.close()
            cmd_desc=""
        #end if
    #end for
#end for

