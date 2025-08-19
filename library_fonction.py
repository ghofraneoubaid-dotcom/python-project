print("Welcome to the Small Library System!")

def get_user_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print("Hello, "+ first_name +" "+ last_name +" Here are the books available in our library: ")

books={"1" :"chicka chika boom boom",
       "2" : "Brown Bear, what do you see?"}

def availble_books():
    print("Availabla Books: ")
    for ID, book_name in books.items():
        """"
        a loop that print the book and the ID 
        """
        print(ID +" : "+ book_name)

information = {"1":{"titre": "chicka chika boom boom",
                "autor":"bill martin jr. and jor=hn archambault",
                "description":"a fun and rhythmic alphabet book.. "}}

def books_details(information):
    chosen_book = input("enter the book ID to get details: ")
    for chosen_ID in information.keys():
        """
        to find the ID choose
        """
        for ID, detail in information[chosen_ID].items():
            """
            print the book chose informations
            """
            print(ID +" : "+ detail)

def library():
    get_user_name()
    availble_books()
    books_details(information)

library()