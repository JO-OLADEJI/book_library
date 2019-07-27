print('Hi, Welcome to J-devs Library.\nYou can search a book by Name(N), Year published(Y) or Author(A).')
library_name = ['Automate the boring stuff with python', 'A byte of python', 'Introduction to programming using python', 'Getting started with python', 'Python for dummies', 'Rich dad poor dad']
library_year = {2011: ['Rich dad poor dad'],
                2015: ['Python for dummies'],
                2016: ['Automate the boring stuff with python', 'A byte of python'],
                2017: ['Introduction to progamming using python', 'Getting started with python']}
library_author = {'Ai sweigart': ['Automate the boring stuff with python', 'Getting started with python'],
                  'Joshua': ['Python for dummies', 'A byte of python'],
                  'Richard': ['Introduction to progamming using python'],
                  'Robert Kiyosaki': ['Rich dad poor dad']}
books_price = {'Automate the boring stuff with python': 9.99,
               'A byte of python': 7.99,
               'Introduction to programming using python': 14.99,
               'Getting started with python': 4.99,
               'Python for dummies': 6.99,
               'Rich dad poor dad': 2.99}
print('Books available on this Library are published in the Year: ')
for i in library_year.keys():
    print(' ' + str(i))
print('Books avaulable on this Library are published by the Authors: ')
for i in library_author.keys():
    print(' ' + i)
while True:
    book_input = input('N(name), Y(year published) or A(author): ').upper()
    if book_input == 'N' or book_input == 'NAME':
        book_name = input('Enter Name of Book: ').capitalize()
        if book_name in library_name:
            print(book_name + ' is available in this Library')
            break
        else:
            print(book_name + ' is not available in this Library.')
            print('\n')
            continue
    elif book_input == 'Y' or book_input == 'YEAR PUBLISHED':
        book_year = input('Enter Year the Book was pulished: ')
        if int(book_year) in library_year.keys():
            print('The books published in ' + book_year + ' are: ')
            for i in library_year[int(book_year)]:
                print(' ' + i)
            break
        elif int(book_year) not in library_year.keys():
            print('Books published in ' + book_year + ' are not available on this Library.')
            print('\n')
            continue
    elif book_input == 'A' or book_input == 'AUTHOR':
        book_author = input('Enter the name of the Author: ').capitalize()
        if book_author in library_author.keys():
            print('The Books published by ' + book_author + ' are: ')
            for names in library_author[book_author]:
                print(' ' + names)
            break
        elif book_author not in library_author.keys():
            print('Books published by ' + book_author + ' are not available on this Library.')
            print('\n')
            continue
    else:
        print('Error: Invalid Parameter Entered !!!')
        print('\n')
        continue
while True:
    book = input('Which of the Books would you like to Purchase: ').capitalize()
    if book in library_name:
        print('The price of [' + book + '] is ' + '$' + str(books_price[book]))
        print('\n')
        break
    elif book not in library_name:
        print('Invalid Book inputed! Please double-check Input.')
        print('\n')
        continue
print('Input the Addess You book will be shipped to: ')
country = input('Country: ').capitalize()
state = input('State\Province: ').capitalize()
city = input('City/Town: ').capitalize()
street = input('House no. and Street: ').capitalize()
print('$10 Shipping Fee will be charged on your Order.')
total = round(((books_price[book]) + 10.00), 2)
print('Cart: \n ' + book + ': $' + str(books_price[book]) + '\n Shipping Fee: $10.00 \n Total: $' + str(total) + '.')
print('Please Input Debit-card details below: ')
while True:
    card = input('Card Number: ')
    cvv = input('CVV: ')
    exp = input('Expiry Date: ')
    card_name = input('Card holder\'s Name: ').upper()
    if len(card) == 19 and len(cvv) == 3 and len(exp) == 5 and len(card_name) >= 1:
        print('Payment Successful.')
        print('\n')
        break
    else:
        print('Error: Please double-check your details and Try again!!!')
        continue
print('Order Successful. \nStatus: completed \nShipping Address: ' + street + ', ' + city + ', ' + state + '. ' + country + '.')
print('You can track your order by clicking the link below..... \n bit.ly/Qxf67tHlg8rK')
bye = input()
