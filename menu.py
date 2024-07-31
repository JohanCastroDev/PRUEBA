#import mysql.connector

#conexion = mysql.connector.connect(user = 'root', password='kevin2306',
                                  #host='localhost',
                                  #database='employees',
                                  #port='3306')
import pymysql

connection = pymysql.connect(user = 'root', password ='kevin2306',
                                  host ='localhost',
                                  database ='employees',

)

cursor = connection.cursor()



print('___________________________________')
print('     empresa xxxxxx S.A')
print('sistema para calculo de vacaciones')
print('___________________________________')

#all the necesary data to make the if's works
employee_name=(input('Ingrese el nombre de el empleado   '))
id_employee=(input("Ingrese su id de empleado  "))
dept_id=int(input('ingrese el ID del departamento en el que labora    '))
service_years=int(input('ingrese la cantidad de años laborados por el empleado    '))

if dept_id == 1: # each department have diferent vacations days
    if service_years == 1 and service_years < 3:
        print('el empleado', employee_name, 'tiene 10 días de Vacaciones')
        vacations = ('10 days')
    elif service_years >= 2 and service_years < 8:
        print ('el empleado', employee_name, 'tiene 22 dias de vacaciones')
        vacations = ('22 days')
    elif service_years >= 8:
        print('el empleado', employee_name, "tiene 1 mes de vacaciones")
        vacations = ('30 days')
    else:
        print('no tiene vacaciones')
        vacations = ('0 days')

if dept_id == 2: 
     if service_years == 1 and service_years < 3:
        print('el empleado', employee_name, 'tiene 12 días de Vacaciones')
        vacations = ('12 days')
     elif service_years >= 2 and service_years < 8:
        print ('el empleado', employee_name, 'tiene 22 dias de vacaciones')
        vacations = ('22 days')
     elif service_years >= 8:
        print('el empleado', employee_name, "tiene 1 mes y medio de de vacaciones")
        vacations = ('45 days')
     else:
        print('no tiene vacaciones')
        vacations = ('0 days')

if dept_id == 3:
     if service_years == 1 and service_years < 3:
        print('el empleado', employee_name, 'tiene 20 días de Vacaciones')
        vacations = ('20 days')
     elif service_years >= 2 and service_years < 8:
        print ('el empleado', employee_name, 'tiene 33 dias de vacaciones')
        vacations = ('33 days')
     elif service_years >= 8:
        print('el empleado', employee_name, "tiene 2 meses de vacaciones")
        vacations = ('60 days')
     else:
        print('no tiene vacaciones') 
        vacations = ('0 days')  


#print (conexion)
print (vacations)
            
sql = "insert into datab (idEmployee, ENames, IDDepartment, vacations) VALUES (%s, %s, %s, %s)"  
values = (id_employee, employee_name, dept_id, vacations)  

cursor.execute(sql, values)

connection.commit()