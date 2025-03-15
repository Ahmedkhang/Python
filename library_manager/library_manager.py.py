# declaring an empty arr to store books
total_books = []
# defining a func which will take input from user and it will add the book in 'total_books'
def add():
    try:
        while True:
            title = input("Enter the book title: ")
            if not title.isdigit():
                break
            print('Please enter a String (a-z) or (A-Z)')

        while True:
            author = input("Enter the Author Name: ")
            if not author.isdigit():
                break
            print('Please enter a String (a-z) or (A-Z)')

        while True:
            year = input("Enter the publish year: ")
            if year.isdigit():
                break
            print("please enter integer (0-9):")

        while True:
            genre = input("Enter the Genre: ")
            if not genre.isdigit():
                break
            print('Please enter a String (a-z) or (A-Z)')

        while True:
            status = input("Have you read this book? (Y/N): ").upper()
            if status in ('Y', 'N'):
                break
            print('Please Enter Y or N!')
    except ValueError:
        print('Please enter a valid number (1-6)')

    book = {
        "title": title,
        "author": author,
        'year': int(year),
        'genre': genre,
        'status': status
    }

    total_books.append(book)
    print(f'Book: {title} by {author} ({year}) - {genre} has been added')
    return   
# defining a func which will take input from user and it will remove the book from 'total_books'
def remove():
    title = input("Enter the book title to remove: ")
    for book in total_books:
        if book['title'].lower() == title.lower():
            total_books.remove(book)
            print(f'{book["title"]} has been removed')
            break
    else:
        print(f'Book titled "{title}" not found')
    return
# defining a func which will take input from user and it will display all the book in 'total_books'
def display_all_Books():
    for book in total_books:
        print(f'Book: {book["title"]}\nAuthor: {book["author"]}\nYear: {book["year"]}\nGenre: {book["genre"]}\nStatus: {book["status"]}\n')
# defining a function which will search a book in 'total book'
def search_book():

    title = input('Search a book with book title: ')
    for book in total_books:
        if title.lower() == book['title'].lower():
            print(f'This book "{book["title"]}" is available')
            break
    else:
        print(f'Your book titled "{title}" does not exist in the library')
# defining a func which will show all the statistics
def statistics():

    total = len(total_books)
    if total == 0:
       print('\nNo stats available')
       return
    
    read_books = sum(1 for book in total_books if book['status'] == 'Y')
    unread_books = total - read_books
    genres = {book['genre'] for book in total_books}
    print('--------- Your Stats ----------\n\n')  
    print(f'Total Books : {total}')
    print(f'Read Books : {read_books}')
    print(f'Reading Percentage : {read_books / total * 100}%')
    print(f'Unread Books : {unread_books}')
    print(f'Unique Genres :{', '.join(genres)}')

                
             
print("\n---------------- Menu ------------------")

# initializing while loop and taking input to perform operation

while True:
  
  operation = int(input('\n1-Add a book\n2-Remove a book\n3-Search for a book\n4-Display all books\n5-statistics\n6-Exit\n\n'))
  
  if operation == 1:
     add()
  elif operation == 2:
     remove()
  elif operation == 3:
      
      search_book()
     
  elif operation == 4:
      print('------------ Your Books ------------')
      display_all_Books()   
  
  elif operation == 5:
      statistics() 
  elif operation == 6:
      print("Thank You for using library management system.Good bye!")
      break 
  else :
      print("Please enter a valid number!")
