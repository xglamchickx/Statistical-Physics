import matplotlib.pylab as plt

plt.plot([0,1,2],[3,6,2])
plt.xlabel("Some numbers")
plt.ylabel("Other numbers")
# all other plotting stuff goes here

plt.savefig("example.png")
