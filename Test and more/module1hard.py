grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# creating dictionary
dict_GPA = {}  # Grade Point Average

# convert an unordered sequence of a 'set' into an ordered 'tuple' sorted alphabetically
students = tuple(sorted(students))

# calculate the gpa of each student using the formula and indexes
# gpa_student = sum(grades[0]) / len(grades[0])

# fill the dictionary using the same indexes in the list and tuple
# dict_GPA[students[0]] = sum(grades[0]) / len(grades[0])
# dict_GPA[students[1]] = sum(grades[1]) / len(grades[1])
# dict_GPA[students[2]] = sum(grades[2]) / len(grades[2])
# dict_GPA[students[3]] = sum(grades[3]) / len(grades[3])
# dict_GPA[students[4]] = sum(grades[4]) / len(grades[4])



test = {}
uniq = [1,2,3,4,5]
fifa = ['a','b','c','d','e']
test = dict(zip(uniq, fifa))
print(test)

for i in range(0, len(students)):
    dict_GPA[students[i]] = sum(grades[i]) / len(grades[i])
print(dict_GPA)

dict_ = {}
grades = (
    sum(grades[0]) / len(grades[0]),
    sum(grades[1]) / len(grades[1]),
    sum(grades[2]) / len(grades[2]),
    sum(grades[3]) / len(grades[3]),
    sum(grades[4]) / len(grades[4]),
)
print(grades)

dict_ = dict(zip(students, grades))
print(dict_)

