#dictionary and set
a ={
    "harry" : "40",
    "rohan" : "45",
    "skillf" : "50"

}
print(a["harry"])
#methods in dictionary
print(a.items)
print(a.keys)
print(a.values)
a.update({"harry" : 33})
print(a)


print(a.get("harry"))#it will not give error if we try to access a key which is not present in the dictionary
print(a["harry"])

#sets
a = {1,2,3,4,5}
e=set()
#to make aempty set
#we cant, repaate values in set

#methondes in set
a.add(6)
#union set1.union(set2)
#intersection set1.intersection(set2)
#difference set1.difference(set2)
