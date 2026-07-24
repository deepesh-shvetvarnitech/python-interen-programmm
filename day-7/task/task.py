class Book:
    def __init__(self,book_name,quantity):
     self.book_name = book_name
     self.quantity = quantity
    def check_availablity(self):
       if self.quantity >= 1:
          return "available"
       else:
          return "not available"
available_books = 0
for i in range(1,6):
    print(f"====================book{i}====================")
    book_name = input("enter book name :")
    quantity = int(input("enter quantity"))
    book = Book(book_name,quantity)
    status = book.check_availablity()

    if status == "available":
       available_books+=1
       #display book report
       print(f"Book Name  : {book.book_name}")
       print(f"Book Quantity  : {book.quantity}")
       print(f"Status  : {status}")
       print("============================================")
#final summary 
print(f"====================library summary=================")
print(f"Total Books : {5}")
print(f"Available Books : {available_books}") 
print(f"Not Available Books : {5-available_books}") 
print("======================================================")

print(f"=========================book{i}=====================")
                
