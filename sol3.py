def add_entry(s):
    s["course"] = "B.Tech"

def reassign_dict(d):
    d = {"name": "Rahul", "age": 25}
    print("Inside reassign_dict:", d)
    return d


student = {"name": "Rahul"}

print("Original dictionary:", student)

add_entry(student)

print("After add_entry:", student)


print("After reassign_dict:", reassign_dict(student))

