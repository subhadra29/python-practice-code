import matplotlib.pyplot as plt
import pandas as pd

csv= pd.read_csv("student2.csv")

print(csv)

plt.pie(
    csv["Marks"],
    labels=csv["Student"],
    autopct="%1.1f%%"
)

plt.title("Result")

plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()

plt.show()
