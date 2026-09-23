def change_string(s):
    s = "X" + s[1:]
    print("Inside function:", s)


name = "git"

print("Before function:", name)

change_string(name)

print("After function:", name)