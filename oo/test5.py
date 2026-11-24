import random


class Student:
    count = 0
    def __init__(self, name, roll, maths, physics, chemistry):
        Student.count += 1
        self.roll = roll
        self.name = name
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

class Group:
    leader=''
    def __init__(self):
        self.members = [ ]

    def add(self, student):
        self.members.append(student)

    def print_members(self):
        for student in self.members:
            print(student.name)

    def remove(self, roll):
        found = False
        for student in self.members:
            if student.roll == roll:
                found = True
        if found:
            self.members.remove(student)
        else:
            print('Student not found')
    def pick_leader(self):
        potential = [ ]
        for student in self.members:
            avg = (student.maths +
                   student.physics +
                   student.chemistry) // 3
            if avg >= 80:
                potential.append(student)
        if len(potential) > 0:
            index = random.randint(0, len(potential) - 1)
            self.leader = potential[index].name
        else:
            self.leader = None


study_group = Group()
study_group.add(Student('Lathika', 1, 80, 80, 80))
study_group.add(Student('Keerthana', 2, 80, 70, 60))
study_group.add(Student('Sourabh', 3, 75, 85, 80))
study_group.add(Student('Nikhil', 4, 100, 79, 59))
study_group.pick_leader()
print(study_group.leader)
try:
    L = [x for x in range(10)]
    f = open('numbers.txt', 'w')
    for x in L:
        f.write(x)
except FileNotFoundError:
    print('File was not found')
except:
    print('This is some other error')
finally:
    print('The file has been closed')
    f.close()