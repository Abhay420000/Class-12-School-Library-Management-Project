import matplotlib.pyplot as plt,mysql.connector as noc
mycon=noc.connect(host="localhost",user="root",passwd="12345",database="abhay")
if mycon.is_connected()==False:
    print('Error connecting to MySQL database')
cursor=mycon.cursor()
#####SQL Class Student Count
def chart():
    cursor.execute("select count(*) from stu where Class=12")
    data=cursor.fetchall()
    i12=data[0][0]
    cursor.execute("select count(*) from stu where Class=11")
    data=cursor.fetchall()
    i11=data[0][0]
    cursor.execute("select count(*) from stu where Class=10")
    data=cursor.fetchall()
    i10=data[0][0]
    cursor.execute("select count(*) from stu where Class=9")
    data=cursor.fetchall()
    i9=data[0][0]
    cursor.execute("select count(*) from stu where Class=8")
    data=cursor.fetchall()
    i8=data[0][0]
    cursor.execute("select count(*) from stu where Class=7")
    data=cursor.fetchall()
    i7=data[0][0]
    cursor.execute("select count(*) from stu where Class=6")
    data=cursor.fetchall()
    i6=data[0][0]
    #####Bar Chart
    classes=[6,7,8,9,10,11,12]
    students=[i6,i7,i8,i9,i10,i11,i12]
    plt.bar(classes,students,color=['b','g','r','m','y','k','c'])
    plt.title('Registered Students')
    plt.xlabel('Class')
    plt.ylabel('Number of Students')
    plt.show()



























