import matplotlib.pyplot as plt

bases = ["A", "T", "G", "C"]
counts = [15, 12, 18, 10]

plt.bar(bases,counts)

plt.xlabel("DNA Base")
plt.ylabel("Count")
plt.title("DNA Base Count")


plt.show()

