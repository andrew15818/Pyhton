filename = input('Please enter name of the file:\n')
try:
    file = open(filename, "r")
except FileNotFoundError:
    print('File not found')
#asking the user for the filename
'''I want to go through each line in the file and look for lines that have \in\ or not
and then further split it to get the information we want'''
for line in file:
    if line.startswith("Subject: [sakai] svn commit:"):
        '''For each line, if there is \in\ inside the string, then it will go 
        to the first for loop, else to the second one'''
        if "in" in line:
            line = line.split('in')
            #print('Line with in : ', line)
            revision = line[0].split(":", 2)
            '''For revision and place, we are trying to get those strings by themselves,
            so we have to split the string multiple times'''
            place = line[1].split("/")
            final_rev = revision[2].replace("-", "")
            #here we just replace the final - so it looks the same as the other ouptuts
            print(final_rev, place[0])
        #we use a very similar process if the string does not have "in"
        elif "in" not in line:
            line = line.split('-')
            revision = line[0].split(":")
            place = line[1].split('/')
            #these strings do not have the "-" at the end, so no further modification is necessary
            print(revision[2], place[0])
            #just printing the stripped down information
    else:
        continue
