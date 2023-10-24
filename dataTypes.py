# what is the datatype a data type is a classification or category that specifies which type of value a variable
# can hold or which operations can be performed on those values.
number = 100  # int
second = 56.78  # float
text = "Hello there"  # str
isPythonInteresting = True  # bool

# storing multiple values in a variable

cars = ["toyota", "nissan", "vw", 50]  # list
fruits = ("banana", "oranges", "Apples")  # Tuple
countries = {"Kenya", "tanzania", "tunisia"}  # set
detailes = {
    "firstname": "Meshack",
    "age": 34,
    "course": "web development",
    "nationarity": "kenya"
}  # Dictionary

print(second)
print(text)
print(cars)
print(countries)
print(detailes["firstname"])
print(detailes["age"])
print(detailes.get("age"))

# Determine the datatype

print(type(number))
print(type(second))
print(type(text))
print(type(isPythonInteresting))
print(type(cars))
print(type(fruits))
print(type(countries))
print(type(detailes))


# typecasting

# this is the process of converting one datatype to another

print(float(number))
print(int(round(second)))
