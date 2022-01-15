from datetime import date
import application.salary as salary
import application.db.people as people


def print_hi():
    user = input(f'Как к вам обращаться?: ')
    local_date = date.today()
    print(f'Hi, {user}. Local data is: {local_date.strftime("%d-%m-%Y")}')


if __name__ == '__main__':
    print_hi()
    salary.calculate_salary()
    people.get_employees()