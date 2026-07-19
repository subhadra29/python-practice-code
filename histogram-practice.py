import matplotlib.pyplot as plt

marks = [45, 55, 60, 62, 70, 75, 80, 82, 85, 90, 95]

students=[1,2,3,4,5,6,7,8,9,10,11]

plt.plot(marks,students, marker="o")

plt.plot(marks,students,linestyle="--")

plt.grid()

plt.show()


plt.hist(marks)

plt.show()



