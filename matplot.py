from matplotlib import pyplot as plt
x=[0,1,2,3,4,5]
y=[5,10,15,20,25,30]
plt.plot(x,y)
plt.title("xyz graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x,y,marker="d",ms=5,mec="r",mfc="b",ls="dotted",lw=10,c="y")
plt.grid(axis="y")
plt.show()