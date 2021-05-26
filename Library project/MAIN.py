import mysql.connector as noc,random,_data1_,_data2_,_data3_
mycon=noc.connect(host="localhost",user="root",passwd="12345",database="abhay")
if mycon.is_connected()==False:
    print('Error connecting to MySQL database')
cursor=mycon.cursor()
print()
print(" "*28,"*****||||WELCOME||||*****")
print()
a=['Hope sees the invisible, feels the intangible, and achieves the impossible. –Charles Caleb Colton',
   'Stop competing, and start excelling. No one has to lose for you to win. -Abhay Kr.',
   'Don’t settle for being what you used to be or have been. Keep reaching for what you can yet become. -Saurav Chu.',
   'In the middle of difficulty lies opportunity. –Albert Einstein ',
   'Opportunities are usually disguised as hard work, so most people don’t recognize them. –Ann Landers ']
print(" "*10,a[random.randint(0,len(a)-1)])
print()
cursor.execute("select count(*) from stu")
data=cursor.fetchall()
for x in data:
    print("Total Students:",x[0])
cursor.execute("select count(*) from book")
ta=cursor.fetchall()
for x in ta:  
    print("Number of books:",x[0])
op=0
passw='AY'
while op!=4:
    print("Choose options:")
    print("1.Book Issue")
    print("2.Book Deposit")
    print("3.Administrator Menu")
    print("4.Exit")
    op=int(input("Enter option number:"))
    if op==1:
        _data2_.issue()
        print()
    elif op==2:
        _data3_.dep()
        print()
    elif op==3:
        a=input('Enter password: ')
        if a==passw:
            openi=0
            while openi!=3:
                print()
                print('Choose option')
                print('1.Go to Administrator Menu')
                print('2.Change Password')
                print('3.Exit')
                openi=int(input("Enter option number:"))
                if openi==1:
                   _data1_.Admenue()
                elif openi==2:
                    w=input('Enter new Password:')
                    x=input('Re-Enter your new Password:')
                    while w!=x:
                        print('Password do not match!')
                        w=input('Enter new Password:')
                        x=input('Re-Enter your new Password:')
                    else:
                        passw=w
                        global passsw
                        print('Password Changed!')
                elif openi==3:
                    print("Main Menu")
                else:
                    print('Invalid option')
        else:
            print('Wrong password')
        print()
    elif op==4:
        print("****Thank You****")
    else:
        print("Invalid option,Please choose right option")
