"""
Tuple Practice Exercises
Description: Solutions to tuple exercises covering creation, indexing, slicing,
immutability, unpacking, dictionary keys, and enumerate usage.
"""

# -----------------------------
# Problem 1 — Create a tuple
# -----------------------------
"""
Prompt: 
Create a tuple that contains your name (str), age (int), and favorite color (str). 
Print the tuple and its type.
"""


def problem_1(answer: tuple[str, int, str]) -> tuple[str, int, str]:
    # Unpack the tuple (optional)
    name, age, favorite_color = answer

    print("Problem 1 — Tuple Creation")
    print("Tuple:", answer)
    print("Type:", type(answer))
    print("-" * 40)
    return answer


answer = ("Chris", 38, "Orange")
problem_1(answer=answer)


# -----------------------------
# Problem 2 — Access elements
# -----------------------------
"""
Prompt:
Given the tuple t = (10, 20, 30, 40, 50):
1. Print the first element
2. Print the second element
3. Print elements from index 1 to 3 (slice)
"""

t = (10, 20, 30, 40, 50)
print("Problem 2 — Access Elements")
print("First element:", t[0])
print("Second element:", t[1])
print("Slice from index 1 to 3:", t[1:4])
print("-" * 40)


# -----------------------------
# Problem 3 — Immutability
# -----------------------------
"""
Prompt:
Try to modify the first element of the tuple t. Catch any errors and print a message 
explaining that tuples cannot be modified.
"""

print("Problem 3 — Immutability")
try:
    t[0] = 5
except TypeError as e:
    print("Cannot modify a tuple:", e)
print("-" * 40)


# -----------------------------
# Problem 4 — Tuple unpacking
# -----------------------------
"""
Prompt:
Given the tuple person = ("Bob", 30, "Engineer"):
1. Unpack it into three variables: name, age, profession
2. Print each variable with a descriptive label
"""

person = ("Bob", 30, "Engineer")
name, age, profession = person

print("Problem 4 — Tuple Unpacking")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")
print("-" * 40)


# -----------------------------
# Problem 5 — Tuples as dictionary keys
# -----------------------------
"""
Prompt:
Given two coordinate tuples, point1 = (2, 3) and point2 = (5, 7):
1. Create a dictionary where the keys are the tuples and the values are "A" and "B"
2. Print the dictionary
"""

point1 = (2, 3)
point2 = (5, 7)
points = {point1: "A", point2: "B"}

print("Problem 5 — Tuples as Dictionary Keys")
print("Dictionary of points:", points)
print("-" * 40)


# -----------------------------
# Problem 6 — Enumerate with tuples
# -----------------------------
"""
Prompt:
Given a list of fruits: ["apple", "banana", "cherry"]:
1. Use enumerate() to print each index and fruit in the format: index: fruit
"""

fruits = ["apple", "banana", "cherry"]

print("Problem 6 — Enumerate with Tuples")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
print("-" * 40)
