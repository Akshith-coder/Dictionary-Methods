#clear- Removes all elements in a dictionary

mydict =	{
  "First Name": "paul",
  "Last Name": "Rudd",
  "year": 1969
}
print(mydict.clear())

#copy- returns a copy of the dictionary

x = mydict.copy()
print(x)

#fromkeys- returns a dictionary with the specified values and keys

x=("a", "b", "c")
y=0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#get- returns a value with the specified key

print(mydict.get("year"))

#items- returns a lost containg a tuple for each key value pair

print(mydict.items())

#keys- returns a list with the dictionaries keys

print(mydict.keys())

#pop- removes the element containing the specified key

mydict.pop("First Name")
print(mydict)

#popitem- removes the last inserted key-value pair

mydict.popitem()
print(mydict)

#setdefault- returns the value of the specified key; If the key doesn't exist, then insert the key with the value

x = mydict.setdefault("Last Name", "Reynolds")
print(x)

#update- updates the dictionary with the specified key-value pairs

mydict.update({"First Name":"Barney"})
print(mydict)

#values- returns a list of all the values in the list

y = mydict.values()
print(y)