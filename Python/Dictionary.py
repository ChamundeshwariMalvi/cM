# dict={
#     "name":"chinki",
#     "CGPA":9.6,
#     "Marks":[95,92,80]
# }
# print(type(dict))


# to find perticular key-----------
# print(dict["name"])

# dict["CGPA"]=8.6

# print(dict)


# add key-pair
# dict["state"]="Karnataka"
# print(dict)


# Nested dic----ry

student={
    "name":"chams",
    "score":{
        "chem":70,
        "phy":80,
         "Maths":40
    }
}

# print(student["score"]["chem"])

# print(student)

dict={
    "name":"chinki",
    "CGPA":9.6,
    "Marks":[95,92,80]
}

# print(student.keys())

# print(student.values())

# print(dict.items())

# print(dict.get("name"))

dict={
    "name":"chinki",
    "name":"Raju",
    "CGPA":9.6,
    "Marks":[95,92,80]
}
new_dict={
    "name":"chams",
    "city":"Bijapur"
}

# dict.update(new_dict)
# print(dict)

print(list(dict.keys()))

# print(dict.keys())