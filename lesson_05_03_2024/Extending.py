class Person:
    def __init__(self, name, birth_date, phone_number, address):
        self.name = name
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.address = address

    def setName(self, name):
        self.name = name

    def setBirthDate(self, birth_date):
        self.birth_date = birth_date

    def setPhoneNumber(self, phone_number):
        self.phone_number = phone_number

    def setAddress(self, address):
        self.address = address

    def print_information_about_person(self):
        print(f"name: {self.name}, \n"
              f"birth date: {self.birth_date}, \n"
              f"phone number: {self.phone_number}, \n"
              f"address: {self.address}\n")

class Student(Person):
    def __init__(self, name, birth_date, phone_number, address, group_number):
        super().__init__(name, birth_date, phone_number, address)
        self.group_number = group_number

    def setGroupNumber(self, group_number):
        self.group_number = group_number

    def print_information_about_student(self):
        super().print_information_about_person()
        print(f"group number: {self.group_number}\n")


person = Person("John Doe", "01-01-1990", "+380123456789", "Some Street 123")
person.print_information_about_person()


person.setAddress("New Address 456")
person.setPhoneNumber("+380987654321")
person.print_information_about_person()


student = Student("Jane Doe", "02-02-1995", "+380987654321", "University Street 1", "CS101")
student.print_information_about_student()


student.setGroupNumber("CS102")
student.setPhoneNumber("+380123456789")
student.print_information_about_student()
