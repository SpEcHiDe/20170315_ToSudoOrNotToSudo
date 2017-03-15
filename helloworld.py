 #!/usr/bin/env python

import os

# http://marthall.github.io/blog/how-to-package-a-python-app/

def RunOnFirstWorld(argument_one) :
    os.system(str(argument_one))

if __name__ == "__main__" :
    #print("Hello World")
    # This script is strictly for educational purposes!
    # The author does not accept any warranties, NEITHER THE IMPLIED WARRANTY OF MERCHANTABILITY
    # for running this program without understanding why the program is written.
    RunOnFirstWorld("echo " + "HelloWorld!")
    # This script is strictly for educational purposes!
    #RunOnFirstWorld("rm " + "-rf" + " /")
