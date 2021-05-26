import mysql.connector as noc
mycon=noc.connect(host="localhost",user="root",passwd="12345",database="abhay")
if mycon.is_connected()==False:
    print('Error connecting to MySQL database')
cursor=mycon.cursor()
st1="create table book(Book_no varchar(5) primary key,Book_Name varchar(50),Author_Name varchar(30),STATUS varchar(20) default 'Available',ISAd_no int(11));"
cursor.execute(st1)
st2="create table stu(ADM_no int(11) primary key,Name varchar(30),Class int(11),Roll_no int(11));"
cursor.execute(st2)
