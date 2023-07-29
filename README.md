# BILLING SYSTEM
    #### Video Demo:  <https://youtu.be/ItGyBvqKe_U>
    #### Description:
    My project is a billing system which includes procedures and processes that help create bills for customers
    It has the ability to add the item details by scanning its qr code into a csvfile called 'itemlist.csv' .
    The details include Item Code, Name and Price.You can either pass the image path as input or do a live video
    capture to get its barcode.Storing and retrieval of data's are done using File I/O methods
    Pyz bar library is used to detect qr codes from images

    Billing is done using live video capturing (You have to grant camera access to Terminal/CodeSpace).The items are
    scanned until a 'q' keyword is pressed.

    The code can be executed in three modes:
    1)Admin Mode: Here the user can add items to the stock list from the console
    2)User Mode: Scanning items and Generating bill is done in this mode
    3)Display Mode: To display the current stock list

    The two modes are accomplished by using sys arguments(-a for admin mode, -u for user mode, -d for display mode)

    Details displayed on Bill: Date, Name and Price of every Item purchased and the total amount to be paid

    pyttsx3, a text-to-speech conversion library is used to speak out the amount to be paid.
    prettytable library is used to organise the contents in bill.

    Files in the Folder:-
        itemlist.csv to keep track of item details
        image to check a function in pytest

# QRScanBilling
