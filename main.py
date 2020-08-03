import pymysql
from PIL import Image
from get_twitter_data import *
from test_face import face_rec,face_detect
from result import add_result
from storage import delete_results,count,delete_result_tbl
import sys

db = pymysql.connect(host='localhost',database='test',
                                     user='root',
                                     password='')

cursor = db.cursor()
sql_query = "select * from tbl_img order by imgName DESC limit 1"

try:
    cursor.execute(sql_query)
    record = cursor.fetchall()
    imgname=record[0][0]

    print(imgname)
except:
    db.rollback()

db.close()
print("MySQL connection is closed")


known_img="E:/xampp_installed/htdocs/appupload/uploads/"+imgname+".jpg"



cnt=1
def save_image(imagepath):
    result_path="E:/xampp_installed/htdocs/appupload/results/"
    with Image.open(imagepath) as image:
        image.save(result_path+"rst"+str(cnt)+".jpg")


if face_detect(known_img):
    print("human face detected in given input image")

    try:
        t1=twitter_class()
        t1.twitter_data()
        imgpath_list=t1.img_list
        print(imgpath_list)
    except Exception as e:
        print("Error in downloading twitter images ")
        print(e)
        sys.exit(0)

    if not len(os.listdir("E:/xampp_installed/htdocs/appupload/results")) == 0:
        delete_results()
    if not count()==0:
        delete_result_tbl()
    for twitter_image in imgpath_list:
        if face_rec(known_img,twitter_image):
            print("match found")
            save_image(twitter_image)
            a=imgpath_list.index(twitter_image)
            un=t1.profile_list[a]
            tt=t1.tweet_list[a]
            add_result(cnt,"rst"+str(cnt)+".jpg",un,tt)
            cnt=cnt+1

    print("completed")



else :
    print("no human face detected in given input image")
