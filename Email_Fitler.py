
#################################################
#  Created by Ting Xie on 14-07-05.
#  Copyright (c) 2014 Ting Xie. All rights reserved.
#  This small program can helps you filter the email in a text and store the 
#  result to file. There are 2 args at most.
#  The first is the directory of target file it's mandatory.
#  The second is the directory you give. It's optional. Defaultly the ouput file is in the 
#  same directory as input file.
#################################################
import re
import sys
if sys.argv[1][0]=="~":
	filename="/Users/Justin"+sys.argv[1][1:]
else:
	filename=sys.argv[1]
#filename="/Users/Justin/Desktop/input4"
try:
	filestream=open(filename,"r")
except Exception:
	print "can not find file"
	sys.exit(1)

text=filestream.read()

# Justin made a update on test revert branch
# Justin made a second update on test revert branch
# Justin made a third update on test revert branch

#find_email=re.compile(r"([0-9a-zA-Z_.]+@\w+\.\w+)")
find_email=re.compile(r"([0-9a-zA-Z_.]+@[0-9a-zA-Z_.]+)")

m=re.findall(find_email,text)
#m=re.findall(r"^\w+([-+.]\w+)*@nyu.edu$",text)
if m:
	if len(sys.argv) == 3:
		if sys.argv[2][0]=="~":
			output_file_name="/Users/Justin"+sys.argv[2][1:]
		else:
			output_file_name=sys.argv[2]
		
	else:
		output_file_name=filename+"_output"

	try:
		outputfile=open(output_file_name,"w+")
	except Exception:
		print "no such file or dictory"
		sys.exit(1)
		
	for email in m:
		outputfile.write(email)
		outputfile.write("\n")
	outputfile.close()
else:
	print "no email address found"
filestream.close()