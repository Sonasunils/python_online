# ==================================================
# PYTHON STRING
# ==================================================

# 1. STRING INTRODUCTION
# --------------------------------------------------
s = "hello world"
print(s)
print(type(s))

print("\n-----------------------------\n")

# 2. STRING AS ARRAY (INDEXING)
# --------------------------------------------------
s = "python"
print(s[0])
print(s[1])
print(s[-1])

print("\n-----------------------------\n")

# 3. STRING LENGTH
# --------------------------------------------------
s = "hello world"
print(len(s))
print(s.__len__())

print("\n-----------------------------\n")

# 4. STRING CHECK METHODS
# --------------------------------------------------
s = "hello"
print(s.isalpha())  #alpha

s = "908"
print(s.isalnum())   #alpha and numbers

s = "123"
print(s.isdigit())  #num

s = "hello"
print(s.islower())

s = "HELLO"
print(s.isupper())

s = "Hello World"
print(s.istitle())

# print("\n-----------------------------\n")

# # 5. PYTHON STRING SLICING
# # --------------------------------------------------
# s = "hello world"
# print(s[2:5])
# print(s[:5])
# print(s[6:])
# print(s[-5:])
# print(s[::-1])

# print("\n-----------------------------\n")

# # 6. MODIFY STRINGS
# # --------------------------------------------------
# s = "hello world"
# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(s.replace("world", "python"))

# print("\n-----------------------------\n")

# # 7. STRING CONCATENATION
# # --------------------------------------------------
# a = "hello"
# b = "world"
# print(a + " " + b)

# print("\n-----------------------------\n")

# # 8. STRING FORMATTING
# # --------------------------------------------------
# name = "Sona"
# age = 22

# print(f"My name is {name} and my age is {age}")
# print("My name is {} and my age is {}".format(name, age))
# print("My name is %s and my age is %d" % (name, age))

# print("\n-----------------------------\n")

# # 9. STRING METHODS
# # --------------------------------------------------

# # capitalize()
# s = "hello world"
# print(s.capitalize())

# # startswith()
# print(s.startswith("hello"))
# print(s.startswith("hello", 0, 5))

# # endswith()
# print(s.endswith("world"))
# print(s.endswith("world", 6, 11))

# # lower() and islower()
# s = "hello"
# print(s.lower())
# print(s.islower())

# # upper() and isupper()
# s = "HELLO"
# print(s.upper())
# print(s.isupper())

# # find()
# s = "hello world"
# print(s.find("world"))
# print(s.find("world", 0, 11))

# # isalpha()
# s = "hello"
# print(s.isalpha())

# # strip()
# s = " hello world "
# print(s.strip())

# s = "*****hello world*****"
# print(s.strip("*"))

# # replace()
# s = "hello world"
# print(s.replace("world", "python"))

# s = "hello world world"
# print(s.replace("world", "python", 1))

# # zfill()
# s = "45"
# print(s.zfill(5))

# # rjust(), ljust(), center()
# s = "hello"
# print(s.rjust(10, "*"))
# print(s.ljust(10, "*"))
# print(s.center(10, "*"))

# # count()
# s = "hello world world"
# print(s.count("world"))
# print(s.count("world", 6))

# # split()
# s = "hello world"
# print(s.split())

# s = "hello-world-python"
# print(s.split("-"))

# print("\n-----------------------------\n")

# # 10.other important methods
# # --------------------------------------------------

# # join()
# words = ["hello", "world"]
# print(" ".join(words))

# # swapcase()
# s = "Hello World"
# print(s.swapcase())

# # casefold()
# s = "HELLO"
# print(s.casefold())


