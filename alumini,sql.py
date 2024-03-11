import mysql.connector 
conn=mysql.connector.connect(host='localhost', database='alumuni', user='root', password='shruti@20') 
if conn.is_connected():
  print("Database connected successfully")
from datetime import date
import time

def clear():
  for _ in range(65):
     print()


def made by():
    msg = ''
         Alumuni information system made by     : xyz
         Roll No                                : 1234
         School Name                            : your school name
         Session                                : 2020-2021

         Thanks for evaluating my Project,
    ,,, \n\n\n
    
  for x in msg:
        print(x, end='')
        time.sleep(0.002)
        
    wait = input('Press any key to continue.....')
    



def record_exists(name,fname,dob):

    cursor = conn.cursor()
    sql ='select * from alumni where name ="'+name +'" and fname ="'+fname+'"  and dob ="'+dob+'";'
    cursor.execute(sql)
    record = cursor.fetchone()
    return record

def add_alumni():
  cursor = conn.cursor()
  clear()
  name = input('Enter Alumni Name  : ').upper()
  fname = input('Enter Alumni Father Name  : ').upper()
  dob = input('Enter Alumni Date Of birth(yyyy/mm/dd) : ')
  phone = input('Enter Alumni Phone No  : ')
  email = input('Enter Alumni Email ID  : ')
  stream = input('Enter Alumni Stream(passed)  : ').upper()
  pass_year = input('Enter Alumni Pass Year : ')
  quali = input('Enter Alumni Highest Qualification : ').upper()
  position = input('Enter Alumni Current Position : ')
  city= input('Enter Alumni Current City : ').upper()
  country= input('Enter Alumni Current Country : ').upper()
  employ= input('Enter Alumni Currently employeed/Business : ')

  sql ='insert into alumni(name,fname,phone,email,stream,pass_year,hqualification,\
          current_position,dob,c_city,c_country,employement) values(\
          "'+name+'","'+fname+'","'+phone+'","'+email+'","'+stream+'","'+pass_year+'","'+quali+'","'+position+'","'\
          +dob+'","'+city+ '","'+country+'","'+employ+'");'
  result = record_exists(name,fname,dob)
  if result is None:
    cursor.execute(sql)
    print('\n\n\n Alumni information added successfully.....')
  else:
    print('\n\n\n Record already exist.....................')
  conn.close()
  wait = input('\n\n\n Press any key to continue....')


def modify_alumni():
   
    cursor = conn.cursor()
    while True:
        clear()
        print('ALUMNI INFORMATION MODIFICATION MENU')
        print('*'*100)
        print('1.   Correction In Name')
        print('2.   Correction In Father Name')
        print('3.   Correction In Phone No')
        print('4.   Correction In Email ID')
        print('5.   Correction In Stream')
        print('6.   Correction In Pass Year')
        print('7.   Correction In Highest Qualification')
        print('8.   Correction In Current Position')
        print('9.   Correction In Current City')
        print('10.  Correction In Current Country')
        print('11.   Back to main Menu')
        choice = int(input('\n\nEnter your choice : '))
        field_name =''
        if choice ==1:
            field_name='name'
        if choice == 2:
            field_name = 'fname'
        if choice == 3:
            field_name = 'phone'
        if choice == 4:
            field_name = 'email'
        if choice == 5:
            field_name = 'stream'
        if choice ==6:
            field_name='pass_year'
        if choice ==7:
            field_name='hqualification'
        if choice ==8:
            field_name='current_position'
        if choice == 9:
            field_name = 'c_city'
        if choice == 10:
            field_name = 'c_country'
        if choice == 11:
          conn.close()
          break
        clear()
        print('Change Value for ',field_name)
        print('*'*100)
        idr= input('Enter Alumuni name:')
        value = input('Enter new Value :')
        sql = 'update alumni set '+field_name +'="'+ value +'" where id = '+idr+';' 
        cursor.execute(sql)
        wait = input('\n\n\n Record updated.........Press any key to continue....')
    
    conn.close()
       

def search_menu():
   
    cursor = conn.cursor()
    while True:
      clear()
      print(' S E A R C H    M E N U')
      print('*'*100)
      print("\n1.   ID")
      print('\n2.   Name')
      print('\n3.   Father Name')
      print('\n4.   Phone No')
      print('\n5.   Email')
      print('\n6.   stream')
      print('\n7.   pass year')
      print('\n8.   Qualification')
      print('\n9.   Position')
      print('\n10.  City')
      print('\n11.  Country')
      print('\n12.  Employment')
      print('\n13.  Back to Main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      field_name=''
   
      if choice == 1:
        field_name ='id'
      if choice == 2:
        field_name ='name'
      if choice == 3:
        field_name = 'fname'
      if choice == 4:
        field_name = 'phone'
      if choice == 5:
        field_name = 'email'
      if choice == 6:
        field_name = 'stream'
      if choice == 7:
        field_name = 'pass_year'
      if choice == 8:
        field_name = 'hqualification'
      if choice == 9:
        field_name = 'current_position'
      if choice == 10:
        field_name = 'c_city'
      if choice == 11:
        field_name = 'c_country'
      if choice == 12:
        field_name = 'employement'
      if choice == 13:
        break
      msg ='Enter '+field_name+': '
      value = input(msg)
      if field_name=='id':
        sql = 'select * from alumni where '+field_name + ' = '+value+';'
      else:
        sql = 'select * from alumni where '+field_name +' like "%'+value+'%";'
      #print(sql)
      cursor.execute(sql)
      records = cursor.fetchall()
      n = len(records)
      clear()
      print('Search Result for ', field_name, ' ',value)
      #print('-'*120)
      for record in records:
       print(record[0], record[1], record[2], record[3],
             record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12])
      if(n <= 0):
        print(field_name, ' ', value, ' does not exist')
      wait = input('\n\n\n Press any key to continue....')

    conn.close()
    wait=input('\n\n\n Press any key to continue....')


#def report_alumni_list():
    #conn = mysql.connector.connect(
        #host='localhost', database='alumni', user='root', password='')
    #cursor = conn.cursor()
    #sql ="select * from alumni"
    #cursor.execute(sql)
    #records = cursor.fetchall()
    #clear()
    #print('Alumni List')
    #print('_'*140)
    #print('{:10s} {:30s} {:30s} {:15s} {:30s} {:20s}'.format(
        #'ID', 'Name', 'Father Name','Email','Phone','Position'))
    #print('_'*140)
    #for record in records:
      #print('{:010d} {:30s} {:30s} {:15s} {:30s} {:20s}'.format(
          #record[0], record[1], record[2], record[4],record[3],record[8]))

    #print('_'*140)

    #conn.close()
    #wait=input('\n\n\n Press any key to continue....')

def year_wise_alumni():
    #conn = mysql.connector.connect(
        #host='localhost', database='alumni', user='root', password='')
    cursor = conn.cursor()
    year1 = input(' Enter passout year :')
    sql = 'select * from alumni where pass_year like "%'+ year1 +'%";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni List Passout Year : ',year1)
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Phone', 'Position'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[4], record[8]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def alumni_email_list():
   
    cursor = conn.cursor()
    year1 = input(' Enter passout year :')
    sql = 'select * from alumni;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni Email List')
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email','Position'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[8]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def alumni_phone_list():
    
    cursor = conn.cursor()
    sql = 'select * from alumni;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni Phone Numbers List')
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email','Phone','Position'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[4],record[3] ,record[8]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def city_wise_alumni_list():
    
    cursor = conn.cursor()
    city = input(' Enter city Name :')
    sql = 'select * from alumni where c_city="'+city+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni City Wise List :',city )
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Position','City'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[8],record[10]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def country_wise_alumni_list():
  
    cntry = input(' Enter country Name :')
    sql = 'select * from alumni where c_country="'+cntry+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni City Wise List :',cntry )
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Position','Country'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[8],record[11]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def position_wise_alumni_list():
    
    pos = input(' Enter position Name :')
    sql = 'select * from alumni where position="'+pos+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni position List :',pos )
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Position','Country'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[8],record[11]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def education_wise_alumni_list():
    
    cursor = conn.cursor()
    edu = input(' Enter education Name :')
    sql = 'select * from alumni where heducation="'+edu+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Alumni Education List :',edu )
    print('_'*130)
    print('{:10s} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
        'ID', 'Name', 'Father Name', 'Email', 'Education','Country'))
    print('_'*130)
    for record in records:
      print('{:010d} {:30s} {:30s} {:15s} {:20s} {:20s} {:20s}'.format(
          record[0], record[1], record[2], record[3], record[7],record[11]))

    print('_'*130)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')




def main_menu():
    clear()
   
    while True:
      clear()
      print(' A L U M N I   I N F O R M A T I O N   S Y S T E M')
      print('*'*100)
      print("\n1.  Add New alumni Account")
      print('\n2.  Modify Alumni Information')
      print('\n3.  Search Alumni Menu')
      print('\n4.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        add_alumni()
      if choice == 2:
        modify_alumni()
      if choice ==3 :
        search_menu()
     
      if choice ==4:
        break
    made_by()

if _name_ == "_main_":
    main_menu()
