class PersonalInfo:
    def __init__(self, name, surname, birth_date, phone_number):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.phone_number = phone_number

    def print_info(self):
        print(
            f"Name: {self.name}, Surname: {self.surname}, Birth Date: {self.birth_date}, Phone Number: {self.phone_number}")


class ProfessionalActivity:
    def __init__(self, last_work_place, work_start_date, hourly_rate):
        self.last_work_place = last_work_place
        self.work_start_date = work_start_date
        self.hourly_rate = hourly_rate

    def print_professional_activity(self):
        print(
            f"Last Work Place: {self.last_work_place}, Work Start Date: {self.work_start_date}, Hourly Rate: {self.hourly_rate}")


class Profession(PersonalInfo, ProfessionalActivity):
    def __init__(self, name, surname, birth_date, phone_number, last_work_place, work_start_date, hourly_rate,
                 technologies):
        PersonalInfo.__init__(self, name, surname, birth_date, phone_number)
        ProfessionalActivity.__init__(self, last_work_place, work_start_date, hourly_rate)
        self.technologies = technologies

    def print_profession_info(self):
        self.print_info()
        self.print_professional_activity()
        print(f"Technologies: {', '.join(self.technologies)}")


# Головна функція
if __name__ == "__main__":
    programmer = Profession("John", "Doe", "1990-01-01", "+123456789", "Tech Company", "2020-01-01", 30,
                            ["Python", "JavaScript", "C++"])
    designer = Profession("Jane", "Smith", "1985-05-15", "+987654321", "Creative Studio", "2018-06-01", 28,
                          ["Adobe Photoshop", "Illustrator", "Figma"])

    print("Programmer Info:")
    programmer.print_profession_info()
    print("\nDesigner Info:")
    designer.print_profession_info()
