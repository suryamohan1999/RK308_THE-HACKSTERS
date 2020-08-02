import pymysql
import os

'''
# Open database connection
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()'''


def create_result():
    
    db = pymysql.connect("localhost","testuser","test123","TESTDB" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Drop table if it already exist using execute() method.
    # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # Create table as per requirement
    sql = """CREATE TABLE RESULT (
       ID  INT(11) NOT NULL,
       IMAGENAME  VARCHAR(20),
       USERNAME VARCHAR(20),  
       TWEET VARCHAR(100),
       PRIMARY KEY(ID))"""

    cursor.execute(sql)

    # disconnect from server
    db.close()

#create_result()

def delete_result_tbl():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "testdb")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to DELETE required records
    sql = "DELETE FROM result"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        print("error")
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()

def count():
    # Open database connection
    db = pymysql.connect("localhost", "testuser", "test123", "testdb")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to DELETE required records
    sql = "SELECT COUNT(*) FROM result"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        data = cursor.fetchone()
        #print(data[0])
    except:
        print("error")
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()
    return data[0]

def delete_tbl_img():

    db = pymysql.connect("localhost","root","","test" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to DELETE required records
    sql = "DELETE FROM tbl_image"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        print("error")
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()



def delete_results():
    path="E:/xampp_installed/htdocs/appupload/results/"
    file_list = os.listdir(path)
    #print(file_list)
    for file in file_list:
        os.remove(path+file)


def del_twitter_imgs():
    path="C:/Users/Surya Mohan/Desktop/test_rfrs/twitter_images/"
    file_list = os.listdir(path)
    #print(file_list)
    for file in file_list:
        os.remove(path+file)

def del_uploads():
    path="E:/xampp_installed/htdocs/appupload/uploads/"
    file_list = os.listdir(path)
    print(file_list)
    for file in file_list:
        os.remove(path+file)

#delete_tbl_img()
#del_uploads()
#delete_result_tbl()
#del_twitter_imgs()
#delete_results()
#count()

