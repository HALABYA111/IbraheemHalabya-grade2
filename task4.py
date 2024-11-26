#"Library Book Borrowing Analysis"

input_books = input("Enter borrowed books in the format 'Book Title - Days Borrowed', separated by commas:\n")

book_records = input_books.split(", ")

book_borrowed_days = {}

for record in book_records:
    try:
        title, days = record.split(" - ")
        days = int(days)  
        
        if title in book_borrowed_days:
            book_borrowed_days[title] += days
        else:
            book_borrowed_days[title] = days
    except ValueError:
        print(f"Invalid record format: {record}. Skipping.")

unique_titles = set(book_borrowed_days.keys())

most_borrowed = max(book_borrowed_days.items(), key=lambda x: x[1])
least_borrowed = min(book_borrowed_days.items(), key=lambda x: x[1])

total_days = sum(book_borrowed_days.values())
average_days = total_days / len(book_borrowed_days)

sorted_books = sorted(book_borrowed_days.items(), key=lambda x: x[1], reverse=True)

print("\nLibrary Borrowing Analysis:")
print(f"Unique Titles Borrowed: {unique_titles}")
print(f"Most Borrowed Book: {most_borrowed[0]} ({most_borrowed[1]} days)")
print(f"Least Borrowed Book: {least_borrowed[0]} ({least_borrowed[1]} days)")
print(f"Average Borrowing Duration: {round(average_days, 2)} days")
print("Books Sorted by Borrowing Duration (Descending):")
for title, days in sorted_books:
    print(f"  {title}: {days} days")
