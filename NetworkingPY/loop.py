import os
import time
try:
    
    while True:
        print "##Start subscription"
        os.system("./start-automation.sh 15.168.0.2")
        print "##Sleeping 30sec"
        time.sleep(7200)
        print "##Stop subscription"
        os.system("./stop-automation.sh 15.168.0.2")
except KeyboardInterrupt:
    print "User interrupted"