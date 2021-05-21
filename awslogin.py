import os
import sys

os.system("ssh -i mgcklwz-210519-1217.pem ec2-user@" + str(sys.argv[1]))