'''In order to get the tuples to accept two digit numbers, we first split the input string and then turn it into a tuple,
making a tuple out of the input would not allow for two digit numbers '''



while True:
    ball_one = input('Enter the position and radius of ball one:\n ')
    ball_one = ball_one.split(',')
    ball_one = tuple(ball_one)
    if 'Exit' in ball_one :
        print('Byebye')
        break
    # same process for ball two

    ball_two = input('enter size and radius of ball two:\n ')
    ball_two = ball_two.split(',')
    ball_two = tuple(ball_two)
    if 'Exit' in ball_two:
        print('byebye')
        break
    x1,y1,r1 = ball_one
    x2,y2,r2 = ball_two
    sum_radius = r1 + r2
    sum_distances = x1 + x2+y1+y2
    if sum_radius >= sum_distances:
        print('Colliding')
    else:
        print('Not colliding')