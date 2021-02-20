import matplotlib.pyplot as plt
import random as rand

IN = 0
ALL = 4000

ax = plt.subplots()

plt.fill([0, 4, 4, 6, 6, 8, 0, 0, 1, 1, 0], [0, 0, 2, 2, 0, 0, 8, 5, 5, 4, 4], 'b')

plt.title("Monte-Carlo's method")
plt.grid(True)

for i in range(0, ALL):
    xEx = ((rand.randrange(0, 8 * (10 ** 9)))) / (10 ** 9)  #diapazon X
    yEx = ((rand.randrange(0, 8 * (10 ** 9)))) / (10 ** 9)  #diapazon Y
    # print('x=',xEx,'y=',yEx)

    if ((xEx + yEx <= 8) and not (
            (xEx >= 0 and xEx <= 1 and yEx >= 4 and yEx <= 5) or (xEx >= 4 and xEx <= 6 and yEx >= 0 and yEx <= 2))):
        IN += 1
        plt.scatter(xEx, yEx, c='g', zorder=10)
    else:
        plt.scatter(xEx, yEx, c='r', zorder=10)

S = 64 * (IN / ALL)
print('S=', S)
# S fig= S kv * IN / H*W


plt.show()
