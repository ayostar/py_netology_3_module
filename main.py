from datetime import date
import application.salary as salary
# import application.\320\264\320\270\321\200\320\265\320\272\321\202\320\276\321\200\320\270\321\217 db.people
import application.er.people as people

# import "application/\320\264\320\270\321\200\320\265\320\272\321\202\320\276\321\200\320\270\321\217 db/people.py"

def print_hi(name):
    local_date = date.today()
    print(f'Hi, {name}. Local data is: {local_date.strftime("%d-%m-%Y")}')


if __name__ == '__main__':
    user = input(f'Как к вам обращаться?: ')
    print_hi(user)
    salary.calculate_salary()
    people.get_employees()