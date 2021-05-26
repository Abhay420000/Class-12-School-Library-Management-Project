import mysql.connector as noc,_data4_
mycon=noc.connect(host="localhost",user="root",passwd="12345",database="abhay")
if mycon.is_connected()==False:
    print('Error connecting to MySQL database')
cursor=mycon.cursor()
def Admenue():
    print("ADMINISTRATOR MENU")
    print()
    pop=0
    while pop!=11:
        print('Choose options:')
        print("1.Create student record")
        print("2.Display all student record")
        print("3.Display student with books")
        print("4.Modify student record")
        print("5.Delete student record")
        print("6.Add books")
        print("7.Display all Books with details")
        print("8.Modify Book record")
        print("9.Delete Book record")
        print("10.Display Students using bar Chart")
        print("11.Back to main menu")
        print()
        pop=int(input("Enter option number(1-11) :"))
        if pop==1:
            a=int(input("Enter Admission number: "))
            b=input("Name of student: ")
            c=int(input("Class:"))
            d=int(input("Roll_no"))
            st="insert into stu(ADM_no,Name,Class,Roll_no) values({},'{}',{},{})".format(a,b,c,d)
            cursor.execute(st)
            mycon.commit()
            print('Student record inserted')
        elif pop==2:
            cursor.execute("select * from stu")
            data=cursor.fetchall()
            print('Adm.no',' ','Name',' ','Class',' ','Roll.no')
            for x in data:
                print('  ',x[0],' '*(3-len(x[0])),x[1],' '*(9-len(x[1])),x[2],' '*4,x[3])
            print()
        elif pop==3:
            st="select * from book where STATUS='%s'"%('ISSUED',)
            cursor.execute(st)
            data=cursor.fetchall()
            if len(data)==0:
                print('There is no student with books')
            else:
                for i in data:
                    a=i[4]
                    st="select * from stu where ADM_no=%s"%(a,)
                    cursor.execute(st)
                    ata=cursor.fetchall()
                    print('Adm.no',' ','Name',' ','Class',' ','Roll.no')
                    for x in ata:
                        print('  ',x[0],' '*2,x[1],' '*(7-len(x[1])),x[2],' '*4,x[3])
            print()
        elif pop==4:
            print("What do you want to modify?")
            print("1.Name")
            print("2.Class")
            print("3.Roll_no")
            opq=int(input("Enter option number"))
            if opq==1:
                h=input("Enter Adm.no")
                q=input("Enter new name:")
                st="update stu set Name='{}' where ADM_no={}".format(q,h)
                cursor.execute(st)
                mycon.commit()
                print('New name Updated!')
            elif opq==2:
                h=input("Enter Adm.no")
                q=input("Enter new class:")
                st="update stu set Class={} where ADM_no={}".format(q,h)
                cursor.execute(st)
                mycon.commit()
                print('Class Updated!')
            elif opq==3:
                h=input("Enter Adm.no")
                q=input("Enter new Roll_no:")
                st="update stu set Roll_no ={} where ADM_no={}".format(q,h)
                cursor.execute(st)
                mycon.commit()
                print('Roll_no Updated!')
            else:
                print('Invalid option!')
            print()
        elif pop==5:
            a=input("Enter ADM_no of student")
            st="delete from stu where ADM_no=%s"%(a,)
            cursor.execute(st)
            print('Record of student deleted')
            mycon.commit()
            print("Task done!")
            print()
        elif pop==6:
            a=input("Enter Book number: ")
            b=input("Name of Book: ")
            c=input("Enter Author name: ")
            st="insert into book(Book_no,Book_Name,Author_Name,STATUS) values('{}','{}','{}','{}')".format(a,b,c,'Available')
            cursor.execute(st)
            mycon.commit()
            print("Task done!")
            print()
        elif pop==7:
            cursor.execute("select * from book")
            data=cursor.fetchall()
            print('Book_No',' '*5,'Book_Name',' '*10,'Author_Name',' '*4,'STATUS')
            for x in data:
                print(x[0],' '*5,x[1],' '*(22-len(x[1])),x[2],' '*(15-len(x[2])),x[3])
            print()
        elif pop==8:
            print("What do you want to modify?")
            print("1.Book Name")
            print("2.Author Name")
            print("3.STATUS")
            opq=int(input("Enter option number"))
            if opq==1:
                h=input("Enter BOOK number: ")
                q=input("Enter new Book name: ")
                st="update book set Book_Name='{}' where Book_no='{}'".format(q,h)
                cursor.execute(st)
                mycon.commit()
                print('New Book name Updated!')
            elif opq==2:
                h=input("Enter BOOK number: ")
                q=input("Enter new Author name: ")
                st="update book set Author_Name='{}' where Book_no='{}'".format(q,h)
                cursor.execute(st)
                mycon.commit()
                print('Author name Updated!')
            else:
                print('Invalid option!')
            print()
        elif pop==9:
            a=input("Enter Book_no of Book :")
            st="delete from book where Book_no='%s'"%(a,)
            cursor.execute(st)
            print('Record deleted')
            mycon.commit()
            print("Task done!")
            print()
        elif pop==10:
            _data4_.chart()
        elif pop==11:
            print("Thankyou**")
        else:
            print("Invalid option,Please choose right option")

    














