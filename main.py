import mysql.connector
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
from playsound import playsound
import threading
import names
import random
from datetime import datetime, timedelta
from randomtimestamp import randomtimestamp
from password_generator import PasswordGenerator
import sys

class Signup(QDialog):
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("createacc.ui", self)
        
        # grab button?
        self.signupbutton.clicked.connect(self.get)
        self.backbutton.clicked.connect(self.login)
        self.randombutton.clicked.connect(self.random)
        
        # default (for testing)
        # self.datebox.setInputMask("00-00-0000")
        
    def login(self):
        self.cams = Login()
        self.cams.show()
        self.close()
        
    def random(self):
        sexList = ['male', 'female']
        sex = random.choice(sexList)
        
        first = names.get_first_name(gender=sex)
        middle = names.get_last_name()
        last = names.get_last_name()
        
        NATIONALITIES_list = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan', 'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan', 'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian', 'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu', 'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan', 'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean']
        citizen = random.choice(NATIONALITIES_list)
        
        mail_domains = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@outlook.com', '@facebook.com']
        
        email = str(first + "." + last + random.choice(mail_domains))
        
        pwo = PasswordGenerator()
        passw = pwo.generate()
        
        grade = ['9', '10', '11', '12', '13', '14', '15']
        
        # complex random date generator
        min_year=1900
        max_year=datetime.now().year

        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year+1
        end = start + timedelta(days=365 * years)

        random_date = start + (end - start) * random.random()
        
        datedatedate = randomtimestamp(text=False).strftime("%d/%m/%Y")
        
        self.firstnamebox.setText(first)
        self.middlenamebox.setText(middle)
        self.lastnamebox.setText(last)
        self.genderbox.setText(sex)
        self.datebox.setText(datedatedate)
        self.citizenbox.setText(citizen)
        self.gradebox.setText(random.choice(grade))
        self.trackbox.setText("Programming")
        self.emailbox.setText(email)
        self.passbox.setText(passw)
        
    def get(self):
        print("studio trigger\n")
        print(self.firstnamebox.text())
        print(self.middlenamebox.text())
        print(self.lastnamebox.text())
        print(self.genderbox.text())
        print(self.datebox.text())
        print(self.citizenbox.text())
        print(self.gradebox.text())
        print(self.trackbox.text())
        print(self.emailbox.text())
        print(self.passbox.text())
        
        # connect to database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="new_schema"
        )
        
        mycursor = mydb.cursor()
        
        # check if table 'data' exists
        mycursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = 'data'
        """)
        
        if mycursor.fetchone()[0] != 1:
            mycursor.execute("""CREATE TABLE data (firstname VARCHAR(255), 
                middlename VARCHAR(255), lastname VARCHAR(255), 
                gender VARCHAR(255), birthdate VARCHAR(255), 
                citizenship VARCHAR(255), gradelevel VARCHAR(255), 
                track VARCHAR(255), email VARCHAR(255), 
                password VARCHAR(255))""")

        # send values
        sql = str("INSERT INTO data (firstname, middlename, lastname, " +
            "gender, birthdate, citizenship, gradelevel, track, email, " +
            "password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            
        val = (self.firstnamebox.text(), self.middlenamebox.text(),
            self.lastnamebox.text(), self.genderbox.text(),
            self.datebox.text(), self.citizenbox.text(),
            self.gradebox.text(), self.trackbox.text(),
            self.emailbox.text(), self.passbox.text())
    
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        
        # popup
        self.cams = SignupCmpl()
        self.cams.show()
        self.close()
        
class Login(QDialog):
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("login.ui", self)
        
        # grab button!
        self.createaccbutton.clicked.connect(self.signup)
        self.loginbutton.clicked.connect(self.grab)
        
    def signup(self):
        self.cams = Signup()
        self.cams.show()
        self.close()
        
    def grab(self):
        # connect to database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="new_schema"
        )
        
        mycursor = mydb.cursor()
        
        # temp for logic
        tempmail = ""
        temppass = ""
        
        # check if table 'data' exists
        mycursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = 'data'
        """)
        
        if mycursor.fetchone()[0] != 1:
            mycursor.execute("""CREATE TABLE data (firstname VARCHAR(255), 
                middlename VARCHAR(255), lastname VARCHAR(255), 
                gender VARCHAR(255), birthdate VARCHAR(255), 
                citizenship VARCHAR(255), gradelevel VARCHAR(255), 
                track VARCHAR(255), email VARCHAR(255), 
                password VARCHAR(255))""")
        
        # grab data
        sql_select_Query = "select * from data"
        mycursor.execute(sql_select_Query)
        
        # get all records
        records = mycursor.fetchall()
        print("\nTotal number of rows in table: ", mycursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("email = ", row[8])
            print("pass = ", row[9])
            if row[8] == self.email.text():
                tempmail = row[8]
                temppass = row[9]
        
        if tempmail == "":
            # popup
            self.cams = LoginError()
            self.cams.show()
            self.close()
        elif tempmail == self.email.text() and temppass == self.password.text():
            print("succ")
            currentUser.user = tempmail
            # popup
            self.cams = Profile()
            self.cams.show()
            self.close()
        else:
            # popup
            self.cams = LoginError()
            self.cams.show()
            self.close()
        
class Profile(QDialog):
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("profile.ui", self)
        
        # grab button!
        self.logoutbutton.clicked.connect(self.login)
        self.editbutton.clicked.connect(self.edit)
        self.printbutton.clicked.connect(self.printb)
        
        # connect to database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="new_schema"
        )
        
        mycursor = mydb.cursor()
        sql_select_Query = "select * from data"
        mycursor.execute(sql_select_Query)
        
        # get all records
        records = mycursor.fetchall()
        print("\nTotal number of rows in table: ", mycursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("email = ", row[8])
            print("pass = ", row[9])
            if row[8] == currentUser.user:
                print("found entry")
                
                self.firstnametext_2.setText(row[0])
                self.middlenametext_2.setText(row[1])
                self.lastnametext_2.setText(row[2])
                self.gendertext_2.setText(row[3])
                self.datetext_2.setText(row[4])
                self.citizentext_2.setText(row[5])
                self.gradetext_2.setText(row[6])
                self.tracktext_2.setText(row[7])
                self.emailtext_2.setText(row[8])
                self.passtext_2.setText(row[9])
        
    def login(self):
        self.cams = Login()
        self.cams.show()
        self.close()
        
    def edit(self):
        self.cams = Edit()
        self.cams.show()
        self.close()
        
    def printb(self):
        # selecting file path
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                         "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
 
        # if file path is blank return back
        if filePath == "":
            return
         
        # saving canvas at desired path
        pixmap = self.grab()
        pixmap.save(filePath)
        
class Edit(QDialog):
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("profileedit.ui", self)
        
        # grab button!
        self.cancelbutton.clicked.connect(self.profile)
        self.savebutton.clicked.connect(self.save)
        self.deletebutton.clicked.connect(self.delete)
        
        # connect to database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="new_schema"
        )
        
        mycursor = mydb.cursor()
        sql_select_Query = "select * from data"
        mycursor.execute(sql_select_Query)
        
        # get all records
        records = mycursor.fetchall()
        print("\nTotal number of rows in table: ", mycursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("email = ", row[8])
            print("pass = ", row[9])
            if row[8] == currentUser.user:
                print("found entry")
                self.firstnamebox.setText(row[0])
                self.middlenamebox.setText(row[1])
                self.lastnamebox.setText(row[2])
                self.genderbox.setText(row[3])
                self.datebox.setText(row[4])
                self.citizenbox.setText(row[5])
                self.gradebox.setText(row[6])
                self.trackbox.setText(row[7])
                self.emailbox.setText(row[8])
                self.passbox.setText(row[9])
        
    def profile(self):
        self.cams = Profile()
        self.cams.show()
        self.close()
        
    def save(self):
        # connect to database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="new_schema"
        )
        
        mycursor = mydb.cursor()
        
        sql_select_Query = "select * from data"
        mycursor.execute(sql_select_Query)
        
        # get all records
        records = mycursor.fetchall()
        print("\nTotal number of rows in table: ", mycursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("email = ", row[8])
            print("pass = ", row[9])
            if row[8] == currentUser.user:
                print("found entry")
                
                # SET = NEW, WHERE = OLD
                sql = str("UPDATE data SET firstname = '" + self.firstnamebox.text() + 
                    "', middlename = '" + self.middlenamebox.text() +
                    "', lastname = '" + self.lastnamebox.text() +
                    "', gender = '" + self.genderbox.text() +
                    "', birthdate = '" + self.datebox.text() +
                    "', citizenship = '" + self.citizenbox.text() +
                    "', gradelevel = '" + self.gradebox.text() +
                    "', track = '" + self.trackbox.text() +
                    "', email = '" + self.emailbox.text() +
                    "', password = '" + self.passbox.text() +
                    "' WHERE firstname = '" + row[0] +
                    "'"
                )
                    
                mycursor.execute(sql)
                mydb.commit()
                
                # popup
                self.cams = EditSaved()
                self.cams.show()
                self.close()
        
    def delete(self):
        # connect to database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="new_schema"
        )
        
        mycursor = mydb.cursor()
        
        sql_select_Query = "select * from data"
        mycursor.execute(sql_select_Query)
        
        # get all records
        records = mycursor.fetchall()
        print("\nTotal number of rows in table: ", mycursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("email = ", row[8])
            print("pass = ", row[9])
            if row[8] == currentUser.user:
                print("found entry")
                
                # SET = NEW, WHERE = OLD
                sql = str("DELETE FROM data WHERE firstname = '" + row[0] + "'")
                    
                mycursor.execute(sql)
                mydb.commit()
                
                # popup
                self.cams = EditDeleted()
                self.cams.show()
                self.close()
        
# Popup dialogs
class LoginError(QDialog):
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("loginerr.ui", self)
        
        # grab button!
        self.okbutton.clicked.connect(self.login)
        
    def login(self):
        self.cams = Login()
        self.cams.show()
        self.close()

class EditSaved(QDialog):
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("saved.ui", self)
        
        # grab button!
        self.okbutton.clicked.connect(self.login)
        
    def login(self):
        self.cams = Login()
        self.cams.show()
        self.close()
        
class EditDeleted(QDialog):
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("deleted.ui", self)
        
        # grab button!
        self.okbutton.clicked.connect(self.login)
        
    def login(self):
        self.cams = Login()
        self.cams.show()
        self.close()
        
class SignupCmpl(QDialog):
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("signupcmpl.ui", self)
        
        # grab button!
        self.okbutton.clicked.connect(self.signupcmpl)
        
    def signupcmpl(self):
        self.cams = Login()
        self.cams.show()
        self.close()

# hold current profile
class currentUser:
    user = ""

# public static void main(String[] args)

# loop music code
#def loopSound():
#    while True:
#        playsound('01 reminds me of elevators.mp3', block=True)

# providing a name for the thread improves usefulness of error messages.
#loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
#loopThread.daemon = True # shut down music thread when the rest of the program exits
#loopThread.start()

# main app
app = QApplication([])
window = Login()
window.show()
app.exec()