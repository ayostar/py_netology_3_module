from datetime import date
import application.salary as salary
import application.db.people as people


def print_hi(name):
    local_date = date.today()
    print(f'Hi, {name}. Local data is: {local_date.strftime("%d-%m-%Y")}')


if __name__ == '__main__':
    user = input(f'Как к вам обращаться?: ')
    print_hi(user)
    salary.calculate_salary()
    people.get_employees()