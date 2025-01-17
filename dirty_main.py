from application.salary import *    # так нельзя
from application.db.people import * # так нельзя
from datetime import datetime

if __name__ == '__main__':
    calculate_salary('Salare_1 '+str(datetime.now()))
    get_employees('Employ_1 '+str(datetime.now()))