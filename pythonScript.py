import serial 
import MySQLdb
import time

dbConn = MySQLdb.connect("localhost","root","","bpmsp02new") or die("could not connect to database")

cursor = dbConn.cursor()

device = 'COM4'
try:
    print ("Trying ....")
    arduino = serial.Serial(device,115200)
except:
    print ("Failed to connect on")


try :
    time.sleep(1)
    data= arduino.readline()
    print (data)
    pieces= str(data).split(" ")
#   print(pieces)
    try:
        print("inserting data in dbms")
        cursor.execute("INSERT INTO dht11 (heartRate,validHeartRate,spo2,validSPO2) values(%s,%s,%s,%s)",(pieces[0][2:],pieces[1],pieces[2],pieces[3][:-5]))
        dbConn.commit()
        cursor.close()
    except MySQLdb.IntegrityError:
        print ("fail to insert data")
except:
    print("failed to get data from arduino")
    
    
    
    
    
    
    
    
    