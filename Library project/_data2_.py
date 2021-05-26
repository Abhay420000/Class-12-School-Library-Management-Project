import mysql.connector as noc
mycon=noc.connect(host="localhost",user="root",passwd="12345",database="abhay")
if mycon.is_connected()==False:
    print('Error connecting to MySQL database')
cursor=mycon.cursor()
def issue():
    print("Book Issue....")
    n=int(input("Enter the student's Admission no.::"))
    print("Please select a book")
    cursor.execute("select * from book")
    data=cursor.fetchall()
    print('Book_no',' '*6,'Book_Name',' '*10,'Author_Name',' '*5,'Status')
    for x in data:
        print(' ',x[0],' '*3,x[1],' '*(23-len(x[1])),x[2],' '*(15-len(x[2])),x[3])
    print()
    mycon.commit()
    a=input("Enter the book number of desired book: ")
    st="update book set STATUS='{}' where Book_no='{}'".format('ISSUED',a)
    cursor.execute(st)
    mycon.commit()
    st="update book set ISAd_no={} where Book_no='{}'".format(n,a)
    cursor.execute(st)
    mycon.commit()
    print('Book Issued Successfully')
    print()
    print('Please Note: Write the Current date in backside oof your book and submit within 15 days fine Rs.1 for each day after 15 days period')

