# importing necessary modules
import mysql.connector
import time
import matplotlib.pyplot as plt
import winsound



a = input("Enter the password of your mysql server: ") # asking user for password


# creating the database
conn = mysql.connector.Connect(host='localhost', user='root', password=a)
cursor = conn.cursor()
query = "SHOW DATABASES LIKE 'ZUYDTkEyVtL25ZYg';"
cursor.execute(query)
data = cursor.fetchall()
if data == []:
    query2 = "CREATE DATABASE ZUYDTkEyVtL25ZYg;"
    cursor.execute(query2)
    conn.commit()
    query3 = "USE ZUYDTkEyVtL25ZYg;"
    cursor.execute(query3)
    conn.commit()
    query5 = """CREATE TABLE data (Category varchar(30) DEFAULT NULL,Place varchar(50) NOT NULL,
                Literacy_rate float DEFAULT NULL,Sex_ratio int DEFAULT NULL,Cases int DEFAULT NULL,
                PRIMARY KEY (Place))"""
    cursor.execute(query5)
    conn.commit()
    query6 = """INSERT INTO data VALUES ('Union Territory','A & N ISLANDS',86.6,878,115),('State','ANDHRA PRADESH', 67,
    992,30648),('State','ARUNACHAL PRADESH',65.4,920,351),('State','ASSAM',72.2,954,19139),('State','BIHAR',61.8, 916,
    15383),('Union Territory','CHANDIGARH',86,818,432),('State','CHHATTISGARH',70.3,991,6255),('Union Territory',
    'DADRA & NAGAR HAVELI',76.2,775,21),('Union Territory','DAMAN & DIU',87.1,618,15),('State','GOA',88.7,968,488),
    ('State','GUJARAT',78,918,10837),('State','HARYANA',75.6,877,8974),('State','HIMACHAL PRADESH',82.8,974,1517),
    ('State','JAMMU & KASHMIR',67.2,883,3321),('State','JHARKHAND',66.4,947,5972),('State','KARNATAKA',75.4,968, 13914),
    ('State','KERALA',94,1084,11380),('Union Territory','LAKSHADWEEP',91.8,946,4),('State','MADHYA PRADESH', 69.3,930,
    28678),('State','MAHARASHTRA',82.3,925,26693),('State','MANIPUR',76.9,987,337),('State','MEGHALAYA', 74.4,986,388),
    ('State','MIZORAM',91.3,975,258),('State','NAGALAND',79.6,931,67),('Union Territory', 'NCT OF DELHI',86.2,866,15265),
    ('State','ORISSA',72.9,978,14606),('Union Territory','PUDUCHERRY',85.8,1038,77), ('State','PUNJAB',75.8,893,5425),
    ('State','RAJASTHAN',66.1,926,31151),('State','SIKKIM',81.4,889,110),('State', 'TAMIL NADU',80.1,995,6325),('State',
    'TRIPURA',87.2,961,1615),('State','UTTAR PRADESH',67.7,908,38467),('State', 'UTTARAKHAND',78.8,963,1395),('State',
    'WEST BENGAL',76.3,947,38299); """
    cursor.execute(query6)
    conn.commit()
    print("Creating database named ZUYDTkEyVtL25ZYg.................")
    time.sleep(1)
    print("Database Successfully Created !")



# introduction of the program

def intro():
    text = (
        "-----------------------------------------------------------------------------------------------------------\n"
        "                               ~~~WELCOME TO THIS PORTAL FOR CRIME AGAINST WOMEN~~~                        \n"
        "-----------------------------------------------------------------------------------------------------------\n")
    for x in text:
        print(x, end='')
        time.sleep(0.002)
    input('Press Enter to continue.....')
    winsound.Beep(1000, 500)


# Credits
def outro():
    creds = '----------------------------\n' \
            '~Made by Nipun Juneja \n' \
            '~Roll number 43 \n' \
            '~Non Medical stream \n' \
            '----------------------------'
    for x in creds:
        print(x, end='')
        time.sleep(0.002)
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)


# clearing the screen
def clear():
    for _ in range(5):
        print()


# displaying all records at once
def all_records():
    cursor.execute("use ZUYDTkEyVtL25ZYg;")
    cursor.execute('select * from data;')
    data = cursor.fetchall()
    print(
        "----The data in the order: (Category,Name,Literacy Rate,Sex ratio,Total cases against women) ARE AS "
        "FOLLOWS----")
    for row in data:
        print(row)
    print(
        "----ORDER: CATEGORY, NAME, LITERACY RATE, SEX RATIO, "
        "CASES------------------------------------------------------")
    input('Press Enter to continue.....')
    winsound.Beep(1000, 500)


# searching for individual records
def search():
    a = input("Enter the name of the state/ut whose data you would like to see (Telangana doesn't exist in this): ")
    cursor.execute('use ZUYDTkEyVtL25ZYg;')
    cursor.execute(f"select * from data where place like '%{a}%';")
    data2 = cursor.fetchall()
    print("The data is as follows: ")
    print(f"Category: {data2[0][0]}\n"
          f"Name: {data2[0][1]}\n"
          f"Literacy Rate: {data2[0][2]}\n"
          f"Sex Ratio: {data2[0][3]}\n"
          f"Total Cases against women: {data2[0][4]}")
    input('Press Enter to continue.....')
    winsound.Beep(1000, 500)
    clear()


# viewing graph
def graph():
    cursor.execute('use ZUYDTkEyVtL25ZYg;')
    cursor.execute('select * from data;')
    data = cursor.fetchall()
    lst_lr = []
    for row in data:
        lst_lr.append(row[2])
    lst_name = []
    for row in data:
        lst_name.append(row[1])
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.barh(lst_name, lst_lr)
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)
    ax.grid(b=True, color='grey',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)
    ax.invert_yaxis()
    for i in ax.patches:
        plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
                 str(round((i.get_width()), 2)),
                 fontsize=10, fontweight='bold',
                 color='grey')
    ax.set_title('Literacy Rate of different states/UTs',
                 loc='left', )
    plt.xlabel("Literacy Rate")
    plt.ylabel("Name of States/UTs")
    plt.show()


# updating the database
def update():
    cursor.execute('use ZUYDTkEyVtL25ZYg;')
    field = ''
    print('Welcome to the Modify section. Here you can update the currently fed data.')
    print('1-Literacy Rate')
    print('2-Sex Ratio')
    print('3-Number of cases')
    a = int(input("What would you like to update? Please give the number: "))
    if a == 1:
        field = 'Literacy_rate'
    if a == 2:
        field = 'Sex_ratio'
    if a == 3:
        field = 'Cases'

    name = input('Enter the name of the state for which you would like to update the data: ')
    new_data = (input('Enter the new data that will be replaced with older data: '))
    st = f"update data set {field} = {new_data} where Place = '{name}';"
    cursor.execute(st)
    conn.commit()
    print("~~Records updated successfully~~")
    input('Press Enter to continue.....')
    winsound.Beep(100, 500)


# Random facts about women safety
def miscellaneous_facts():
    print("HEY!\n"
          "Welcome to this random miscellaneous fact generator!\n"
          "Pick a number between 1-10 and I'll show a random fact regarding women safety!")
    a = int(input("Enter the number: "))
    if a == 1:
        print(
            "~~'80 percent of Delhi teenagers replied they hadn't experienced sexual harassment in their life when "
            "asked in an survey.'~~")
    if a == 2:
        print(
            "~~'42 percent of Delhi teenagers think that Indian women are extremely likely to fall prey to a crime "
            "when asked in a survey.'~~")
    if a == 3:
        print(
            "~~'58 percent of Delhi teenagers believe that direct death penalty should be given to sex offenders when "
            "asked in a survey.'~~")
    if a == 4:
        print(
            "~~'58 percent of Delhi teenagers believe that women are more safe in the cities as compared to villages "
            "when asked in a survey.'~~")
    if a == 5:
        print("~~'Every 1 out of 3 women have been subjected to violence at some point in their life globally.'~~")
    if a == 6:
        print("~~'15 million adolescent girls worldwide (aged 15-19) have experienced forced sex.'~~")
    if a == 7:
        print("~~'In 2019, one in five women, aged 20–24 years, were married before the age of 18.'~~")
    if a == 8:
        print("~~'Fewer than 40 per cent of the women who experience violence seek help of any sort.'~~")
    if a == 9:
        print("~~'One hundred thirty-seven women are killed by a member of their family every day'~~")
    if a == 10:
        print("~~'200 million women and girls have experienced female genital mutilation/cutting (FGM/C)'~~")
    clear()


# Main menu of the program
def main_menu():
    intro()

    while True:
        clear()
        print('~---P O R T A L    F O R     C R I M E    A G A I N S T    W O M E N---~')
        print('*' * 100)
        print("\n1. Show All records")
        print("\n2. Search for records")
        print("\n3. Update records")
        print("\n4. Miscellaneous facts")
        print("\n5. Graph")
        print("\n6. Quit")
        choice = int(input("What would you like to do?: "))

        if choice == 1:
            all_records()
        if choice == 2:
            search()
        if choice == 3:
            update()
        if choice == 4:
            miscellaneous_facts()
        if choice == 5:
            graph()
        if choice == 6:
            break
    outro()


# Running the program
if __name__ == "__main__":
    main_menu()
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
