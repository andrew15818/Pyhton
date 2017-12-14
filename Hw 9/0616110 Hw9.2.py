'''In order to get the tuples to accept two digit numbers, we first split the input string and then turn it into a tuple,
ma0king a tuple out of the input would not allow for two digit numbers '''

import math
#we import the math module to be able to find the distance of the centers

while True:
    '''to get the values into a tuple, we first receive the input as a string, 
    then turn it into a list by splitting the string in every comma, then turn the list into
    a tuple, and repeat the process for the second ball'''
    ball_one = input('Enter the position and radius of ball one:\n ')
    ball_one = ball_one.split(',')
    ball_one = tuple(ball_one)
    if 'Exit' in ball_one:
        print('Byebye')
        break
    # same process for ball two

    ball_two = input('enter size and radius of ball two:\n ')
    ball_two = ball_two.split(',')
    ball_two = tuple(ball_two)
    if 'Exit' in ball_two:
        print('Thank you. byebye')
        break

    x1, y1, r1 = ball_one
    x2, y2, r2 = ball_two

    '''the values in the tuple are strings, so we convert every value into 
    an integer'''
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    r1 = int(r1)
    r2 = int(r2)


    sum_radius = r1 + r2
    '''To get the distance between the centers, we use the distance formula,
    and compare it to the sum of the radii'''
    sum_distances = math.sqrt(((x1-x2)**2) + ((y1-y2)**2))
    #print('sum of distances: ', sum_distances)
    #print('sum of radius: ', sum_radius)
    #comparing the length of the two raddi and the distance between the centers
    if sum_radius >= sum_distances:
        print('Colliding')
    else:
        print('Not Colliding')