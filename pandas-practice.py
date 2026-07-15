import pandas as pd

data = {
    "Student" : ["A" ,"B" , "C" , "D"],
    "Marks" : [85 ,62 ,91 ,48]
}


data1= pd.DataFrame(data)

print(data1.head())
print(data1.tail())
print(data1.info())
print(data1.describe())


print(data1[data1["Marks"] > 70] )

data1["passed"] = True

#print genes that,s expression is greater than 10

data2={
    "Gene" : ["TP53" , "BRCA1" , "EGFR" , "MYC" , "KRAS"],
    "Expression" : [15, 8 , 25 ,6 , 18]
}

data3= pd.DataFrame(data2)

print(data3[data3["Expression"] > 10])