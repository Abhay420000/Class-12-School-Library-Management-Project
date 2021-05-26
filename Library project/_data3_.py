import mysql.connector as noc
mycon=noc.connect(host="localhost",user="root",passwd="12345",database="abhay")
if mycon.is_connected()==False:
    print('Error connecting to MySQL database')
cursor=mycon.cursor()
def dep():
    print("Book Deposit....")
    n=int(input("Enter the student's Admission no."))
    print("Book details")
    cursor.execute("select * from book where ISAd_no=%s"%(n,))
    data=cursor.fetchall()
    print('Book_no',' '*6,'Book_Name',' '*10,'Author_Name')
    for x in data:
        print(x[0],' '*6,x[1],' '*2,x[2])
    print()
    mycon.commit()
    a=input("Enter the book number: ")
    st="update book set STATUS='{}' where Book_no='{}'".format('Available',a)
    cursor.execute(st)
    mycon.commit()
    st="update book set ISAd_no={} where Book_no='{}'".format('NULL',a)
    cursor.execute(st)
    mycon.commit()
    a=int(input('Book deposited in number of days:'))
    if a<=15:
        print('Fine: Rs.0')
    else:
        b=a-15
        print('Fine: Rs.',b)
    print('Book Deposited Successfully')
    print()
