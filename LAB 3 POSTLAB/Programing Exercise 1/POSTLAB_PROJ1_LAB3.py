class Student(object):

    def __init__(self, name, num):

        self.name = name
        self.scores = []
        for count in range(num):
            self.scores.append(0)
            
    def getName(self):
        return self.name 

    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]

    def getAverage(self):
        return sum(self.scores) / len(self._scores)

    def getHighScore(self):
         return max(self.scores)

    def __eq__(self,student):
        return self.name == student.name

    def __ge__(self,student):
        return self.name == student.name or self.name>student.name

 
    def __lt__(self,student):
        return self.name<student.name

    def __str__(self):
        return f"Name: {self.name}\nScores: {' '.join(map(str, self.scores))}"

 
def main():

    student1 = Student("Vince", 5)
    student2 = Student("Kyla", 5)
    student3 = Student("Jesher", 3)
    
    print(student1 == student2)
    print(student1 == student3)
    
    print(student1 < student2) 
    print(student1 < student3)  
    
    print(student1 >= student2) 
    print(student1 >= student3)


if __name__ == "__main__":
    main()