filename = input('Please enter name of file\n')
try:
    file = open(filename, "r")
except FileNotFoundError:
    print('File not found')
    exit()
    # opening the file requested by the user
times = dict()
hola = 0
for line in file:
    if not line.startswith("From "):
        continue
    else:
        '''This loop is a little complicated, maybe there's an easier way to do multiple splits
        however, it splits it until we have only the hour left, and all the hours from all the lines are stored in 
        the times dictionary'''
        hola += 1
        cool = line.split(" ")
        final = cool[-2]
        casi = final.split(":")
        hours = casi[0]
        times[hola] = int(hours)
track = 0
new_times = dict()
''''This loop keeps track of how many times every number has appeared,
and stores it into a new dictionary'''
for key, value in times.items():
    if value not in new_times:
        track = 1
        new_times[value] = track
    else:
        new_times[value] += 1

'''finally we sort this dictionary into a new dictionary '''

final_list = list(sorted([(v, k) for (k, v) in new_times.items()], reverse=True))
'''This function sorts our function so that the keys and values are switched'''
for keys, values in final_list:
    print(values, keys)
    '''because we already sorted our dictionary, our keys and values are in the correct order,
    they are ranked by appearances,
    so we can now just print them off'''
