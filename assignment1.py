import random

num_experiments = 1000000

#list of 1000000 lists each of size 2 corresponding to 2 dice throws
both_dice_throws = [[random.randint(1, 6), random.randint(1, 6)] for i in range(num_experiments)]

#counting number of 6 for each throw of 2 dice and summing them up for total number of 6 observed
count_6 = sum(one_throw.count(6) for one_throw in both_dice_throws)

mean_simulated = count_6 / num_experiments
print("The expectation of X using simulations is: " + str(mean_simulated))


#computing expectation of X theoretically to compare it with simulated expectation:

PX0 = 25/36
PX1 = 10/36
PX2 = 1/36

mean_theory = 0*PX0 + 1*PX1 + 2*PX2

print("The expectation of X theoretially is: " + str(mean_theory))