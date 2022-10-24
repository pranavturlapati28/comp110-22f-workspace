schools: dict[str, int]

schools = dict()

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150


#print(schools)

#Lookup value

#print(f"UNC has {schools['UNC']} students")

schools.pop("Duke")

#print(f"Duke is present: {'Duke' in schools}")

schools = {}
#print(schools)
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26500}
#print(schools)

for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

print("-----------")

schools["UNCC"] = 26150

for school in schools:
    print(type(schools[school]))
    print(f"Key: {school} -> Value: {schools[school]}")