print("Welcome to the Small Library System!")
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
print("Hello, "+first_name+" "+last_name+" HEre are the books available in our library: ")
print("Availabla Books: ")
books={1 :"chicka chika boom boom",
       2: "Brown Bear, what do you see?"}
for i, j in books.items():
    """"
    a loop that print the book and the ID 
    """
    print(str(i)+" : "+j)
x=input("enter the book ID to get details: ")
information={1:{"titre": "chicka chika boom boom",
                "autor":"bill martin jr. and jor=hn archambault",
                "description":"a fun and rhythmic alphabet book.. "}}
for k in information.keys():
    """
    to find the ID choose
    """
    for y, z in information[k].items():
        """
        print the book chose informations
        """
        print(y+" : "+j)