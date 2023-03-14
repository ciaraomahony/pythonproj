name = input("enter your name:")
print("welcome to the school of computing help desk ", name, " we have 3 courses, first lets find yours")
print("\n")

course_name = input("write course code here:")
ec_subj = ["subj1", "subj2", "subj3", "subj4", "subj5", "subj6", "subj7"]
ca_subj = ['casub1', 'casub2', "casub3", "casub4"]
da_subj = ["dasub1", "dasub2", "dasub3", "dasub4"]
user_subj = []
while True:
    if course_name == "ec":
        print('your course is computers for business')
        user_subj.extend(ec_subj)
        break
    elif course_name == "da":
        print('your course is data analytics')
        user_subj.extend(da_subj)
        break
    elif course_name == "ca":
        print('your course is computer science')
        user_subj.extend(ca_subj)
        course_name == True
        break
    else:
        print("that doesn't seem right, try again it is two letters!")
        course_name = input("write course code here:")
if course_name ==
print("welcome to the calculator lets get started")


class Grade:
    def __init__(self):
        self.name = name

    def get_name(self):
        return "hiiiiii " + self.name
person2 = Grade()
print(person2.get_name())





#dict_1 = {
#    "ec":["subj1", "subj2", "subj3", "subj4", "subj5", "subj6", "subj7"],
#"ca": ['casub1', 'casub2', "casub3", "casub4"],
#"da": ["dasub1", "dasub2", "dasub3", "dasub4"]
#}


#print(course_name())
#class Student:

 #   def __init__(self):
  #      self.name = input("enter module name:")
    #    self.weight = input("enter how many credits:")
      #  self.result = input("enter result in numbers:")

#    def show_ans(self):
 #       return self.name + " is worth " + self.weight + " credits"

#person2 = Student()
# print(person2.show_ans())


