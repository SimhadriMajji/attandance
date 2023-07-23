import sqlite3
def create_database_table():
       dbase = sqlite3.connect('datab.sqlite3') # Open a database File
       print('Database opened')

       dbase.execute(''' CREATE TABLE IF NOT EXISTS student(
       username VARCHAR UNIQUE NOT NULL,
       password VARCHAR NOT NULL,
       name TEXT NOT NULL,
       phone INT NOT NULL) ''')

       print('Table created')
       #dbase.execute('''INSERT INTO Student(username,password,name,phone)
       #      VALUES('21241A6737','21241A6737','Navya',7893267846)
       #''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6701','21241A6701','ABBAGONI ROHITH GOUD','8179247671')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6702','21241A6702','ADUPA PARDHU','7386385048')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6703','21241A6703','ALLAM KARTHIK KUMAR','9908346636')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6704','21241A6704','ANUPATI SHIVANI','6303486653')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6705','21241A6705','AVULA ABHIRAM YADAV','9347333344')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6706','21241A6706','B SAI GANESH','9553416924')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6707','21241A6707','BALLA AVINASH MALLESH','7330749830')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6708','21241A6708','BANDARU GEETANJALI','9100965665')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6709','21241A6709','BASWA TARUN','9346963489')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6710','21241A6710','BATTULA SRAVANI','6303486653')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6711','21241A6711','BHUMIREDDY CHANDAN REDDY','8008163112')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6712','21241A6712','BODA PRAVEEN','9392601819')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6713','21241A6713','BOKKA DURGA SRI HARSHITHA','8367532299')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6714','21241A6714','BOMBOTTULA SANNITH GOUD','9398816648')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6715','21241A6715','CHERLA SRISAI KRISHNA','6304657058')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6716','21241A6716','CHERUVU VAMSIKA GAYATHRI','9502217788')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6717','21241A6717','CHINTAKINDI SANDEEP KUMAR','6305389811')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6718','21241A6718','G PRANAVI','9966644281')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6719','21241A6719','GANGAVARAPU VENKATA SRIJAN REDDY','9502575169')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6720','21241A6720','GOLI SAI CHANDANA','6301775285')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6721','21241A6721','JUTTU VARSHITH TEJA','9441597044')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6722','21241A6722','K SHYAM SUNDER RAO','9390018575')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6723','21241A6723','KAIRAMKONDA UDAY KIRAN','7989913344')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6724','21241A6724','KALVA PRANEETH','9110747298')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6725','21241A6725','KANAPALA PRIYADARSHINI','8919258570')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6726','21241A6726','KARISHA MOUNIKA','9391361105')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6727','21241A6727','M A ZUNAID ARBAAZ','8247768107')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6728','21241A6728','M TARUN RAIDU','8185897337')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6729','21241A6729','MACHANNAGARI RUPALI REDDY','8790261148')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6730','21241A6730','MADDI VAISHNAVI','7036310599')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6731','21241A6731','MADIREDDY SRI VAISHNAVI SAMHITA','6304752778')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6732','21241A6732','MAILARAM SHRUTHI','9849918382')
       ''')
       #dbase.execute('''INSERT INTO Student(username,password,name,phone)
       #      VALUES('21241A6733','21241A6733','MAJJI SIMHADRI','7386382324')
       #''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6734','21241A6734','MOHAMMED NAVEED ALI','6302543670')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6735','21241A6735','MUNEENDRA','9392857075')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6736','21241A6736','N ANKITH KUMAR','9490888884')
       ''')
       #dbase.execute('''INSERT INTO Student(username,password,name,phone)
       #      VALUES('21241A6737','21241A6737','NAGULA NAVYA SRI','7893762846')
       #''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6738','21241A6738','NARAKANTI MAHESH','9381396852')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6739','21241A6739','NYALAPATLA VAISHNAVI','7013036346')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6740','21241A6740','PADAKANDLA N V SAI KRISHNA','9515284365')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6741','21241A6741','PAIDI GOUTHAMI','8309867370')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6742','21241A6742','PAMULAPARTHY SOWMYA','9063386929')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6743','21241A6743','PHANNI SAI DASARI','8333071505')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6744','21241A6744','PITTALA VENKATA NIKITH VARMA','9640763350')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6745','21241A6745','SANKALA VARALAXMI','7671093050')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6746','21241A6746','PONNAPU REDDY CHENNA KESAVA REDDY','9346781670')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6747','21241A6747','POSIKA SARAN SRI BHARGAVA','8500794296')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6748','21241A6748','R SAI DEVA HARSHA','9949548246')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6749','21241A6749','RETNENI SAI SUDHAMSH','8143805752')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6750','21241A6750','SAI KRISHNA GODEPALLY','9059721244')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6751','21241A6751','SAMALA SAIVIVEK','6305989133')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6752','21241A6752','SHAIK NAZIR HUSSAIN','8074877486')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6753','21241A6753','SHAIK SHAMEEM','9032404349')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6754','21241A6754','SHIVAM MANDAL','7416904925')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6755','21241A6755','SWETHA S','9063935606')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6756','21241A6756','T NAGA SAI TANUSRI','6302517245')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6757','21241A6757','T GARI VINAYAK REDDY','7893203846')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6758','21241A6758','T VARMA SRIMANDAPATI','9742976644')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6759','21241A6759','TIRUKUTCHU MODHITHA','9849273960')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6760','21241A6760','TIRUMANI PRANAVI','7995378959')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6761','21241A6761','ULLI PRIYANKA RAO','7842539927')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6762','21241A6762','URLANA KISHOR','7780106815')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6763','21241A6763','VIVEK GAJAWADA','9133940218')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6764','21241A6764','VUDARA VIVEK CHANDRA','9392500743')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('21241A6765','21241A6765','Y SESHA SAI VIVEK','9440490000')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('22245A6701','22245A6701','BETHI ANUHYA','8106128064')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('22245A6702','22245A6702','BUSSA SAI KIRAN','9542161466')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('22245A6703','22245A6703','GOPALPUTTI POOJA','7799097624')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('22245A6704','22245A6704','PEDDOJU MADHULITHA','9346460058')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('22245A6705','22245A6705','PULI KALPANA','8341096281')
       ''')
       dbase.execute('''INSERT INTO Student(username,password,name,phone)
              VALUES('22245A6706','22245A6706','VADDE NAVEEN','7093151636')
       ''')

       # Execute the SELECT query
       #cursor.execute('DELETE from Student ')
       #cursor.execute('Update Student set name="Nagula Navya Sri" where username="21241A6737"')
       cursor = dbase.cursor()
       dbase.commit()
       # Fetch all the rows and print them
       cursor.execute('SELECT * from Student')
       rows = cursor.fetchall()
       for row in rows:
       print(row)

       # Close the cursor and the database connection
       cursor.close()
       dbase.close()
       print('Database Closed')
if _name_ == "_main_":
    create_database_table()