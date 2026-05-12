#Program to simulate a simple library management system with book issue and return operations.
books=["devil","story","comic"]
issued=[]
while True:	
	print("1)Need book?")
	print("2)Return")
	print("3)Isuued books")
	print("4)Exit")
	ch=input("choose:")
	if ch=="1":
		print(books)
		choose=input("Choose the book:")
		if choose in books:
			books.remove(choose)
			issued.append(choose)
		else:
			print("Invalid")
	if ch=="2":
		return_book=input("Enter the book name:")
		if return_book in issued:
			books.append(return_book)
			issued.remove(return_book)
		else:
			print("Invalid!Book alredy exits")
	if ch=="3":
		print(issued)
	if ch=="4":
		print("Thankyou!")
		break
