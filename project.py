import cv2,csv,pyttsx3,sys
from datetime import date
from pyzbar.pyzbar import decode
from prettytable import from_csv,PrettyTable

cap = cv2.VideoCapture(0)
cap.set(3, 340)
cap.set(4, 480)
table = PrettyTable()

amount = 0
def main():
    if len(sys.argv) != 2 or not validatearg(sys.argv[1])   :
        sys.exit("Invalid usage\nusage: project.py [-a][-u][-d] \n-a   --To add items to the stock list\n-u   --Scan QR codes and generate Bill\n-d   --Display the current itemlist")
    if (sys.argv[1]=='-a'):
        read()
    elif (sys.argv[1]=='-u'):
        table.title = f'Bill       Date:  {date.today()}'
        table.field_names = ['Item Name', 'Price']
        bill()
        table.add_row(['------------','-----------'])
        table.add_row(["Total: ", "%.2f"%amount])
        print(table)
        Say(f"Please pay {amount}")
    elif (sys.argv[1]=='-d'):
        printitems()

def validatearg(arg):
    if arg not in ('-a','-u','-d'):
        return False
    else:
        return True
def printitems():
    c = open('itemlist.csv')
    x = from_csv(c)
    print(x)

def getcode(img):
    if isinstance(img, str):
        img = cv2.imread(img)
    try:
        if decode(img):
                for b in decode(img):
                    return b.data.decode('utf-8')
    except (ValueError):
        return ('Cannot Read image')

def gbarcode():
    while True:
        if(cv2.waitKey(1) & 0xFF==ord('q')):
            break
        succes, img = cap.read()
        if decode(img):
            return getcode(img)
        cv2.imshow('Barcode Scanner', img)

def check(a):
    global table
    with open("itemlist.csv", 'r') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            if a == row['Item Code']:
                return int(row['Price'])
        return False

def read():
    n = int(input('How many items would you like to read? '))
    for i in range(n):
        print('Scanning  Item', i+1)
        with open('itemlist.csv', 'a') as file:
            writer = csv.writer(file)
            x=gbarcode()
            if not check(x):
                writer.writerow([x, input('Item Name: '), int(input('Item Price: '))])
            else:
                print('Item already found')

def bill():
    global amount
    global table
    while True:
        if(cv2.waitKey(100) & 0xFF==ord('q')):
            break
        succes, img = cap.read()
        if decode(img):
            a=getcode(img)

            price= check(a)
            if price:
                print('Scanned')
                with open("itemlist.csv", 'r') as f:
                    csvreader = csv.DictReader(f)
                    for row in csvreader:
                        if a == row['Item Code']:
                            table.add_row( [ row['Name'],row['Price'] ] )
                amount+=price
                input('Press any key to continue')
            else:
                print('Invalid Barcode or Item not Found')
        cv2.imshow('Barcode Scanner', img)

def Say(m):
  engine=pyttsx3.init()
  engine.say(m)
  engine.runAndWait()

if __name__ == '__main__':
    main()


