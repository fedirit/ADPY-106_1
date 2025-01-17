from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    calculate_salary('Salare_1 '+str(datetime.now()))
    get_employees('Employ_1 '+str(datetime.now()))