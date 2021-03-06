filename = input('which file do you want to open?\n')
try:
    file = open(filename, "r")
except FileNotFoundError:
    print('File not found.')
    exit()
#here we make sure the users input is a valid filename
count = 0
confidence = 0
#declaring the two variables we'll use to calculate the average confidence
for line in file:
    if not line.startswith('X-DSPAM-Confidence'):
        continue
        #here we ignore every line that does not start with the given string
    else:
        needed_line = line.split(" ")
        #we separate the line into the string component and the number component, which is what we want

        count += 1
        confidence += float(needed_line[1])
        #we add up all the diffrent values for the confidence

print(confidence/count)
#we print the total confidence divided by the number of lines, which is the confidence