# Default is World
# Author: Snir Shilderman (sshilderman@gmail.com)
import sys
name = "World"
if len(sys.argv) > 1:
	name = sys.argv[1]
print "Hello,", name 