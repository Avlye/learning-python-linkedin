# Writting
file = open("textfile.txt", "w+")

for i in range(10):
    file.write("This is line " + str(i) + "\r\n")

file.close()

# Appending
file = open("textfile.txt", "a")

for i in range(10):
    file.write("More lines: #" + str(i) + "\r\n")

file.close()

# Reading
file = open("textfile.txt", "r")

if file.mode == "r":
    contents = file.read()
    print(contents)

file.close()

# Using context to open
# Much better overall
with open("textfile.txt", "r") as file:
    print(file.read())