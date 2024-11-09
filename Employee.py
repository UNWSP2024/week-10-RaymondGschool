# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employee:
    def __init__(self, name: str, ID: int, department: str, job_title: str) -> None:
        self.__name: str = name
        self.__ID: int = ID
        self.__department: str = department
        self.__job_title: str = job_title

    def __str__(self) -> str:
        return f"{self.__name}\t\t{self.__ID}\t\t{self.__department}\t\t{self.__job_title}"
    

if __name__ == "__main__":
    employee1: Employee = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    employee2: Employee = Employee("Mark Jones", 39119, "IT", "Programmer")
    employee3: Employee = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    all_employees = [employee1, employee2, employee3]

    print("Name\t\t\tID\t\tDepartment\t\tJob Title")
    for employee in all_employees:
        print(employee)