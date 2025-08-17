from user import User  # Import the parent class

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # inherit first_name and last_name
        self.knowledge = []  # empty list initially

    def learn(self, info):
        # add new knowledge to student's list
        self.knowledge.append(info)

