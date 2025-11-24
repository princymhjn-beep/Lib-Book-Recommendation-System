import tkinter as tk
from tkinter import ttk, messagebox

# Book Database

books = [
    #Programming/CS 
    {"title": "Python Crash Course", "author": "Eric Matthes", "genre": "Programming"},
    {"title": "Clean Code", "author": "Robert Martin", "genre": "Programming"},
    {"title": "Introduction to Algorithms", "author": "Cormen", "genre": "Programming"},
    {"title": "Data Structures in Python", "author": "Karumanchi", "genre": "Programming"},
    {"title": "Head First Java", "author": "Kathy Sierra", "genre": "Programming"},
    {"title": "Java: Complete Reference", "author": "Herbert Schildt", "genre": "Programming"},
    {"title": "Operating System Concepts", "author": "Silberschatz", "genre": "Programming"},
    {"title": "Database System Concepts", "author": "Silberschatz", "genre": "Programming"},
    {"title": "Computer Networks", "author": "Tanenbaum", "genre": "Programming"},
    {"title": "Artificial Intelligence: A Modern Approach", "author": "Stuart Russell", "genre": "Programming"},
    {"title": "Machine Learning", "author": "Tom Mitchell", "genre": "Programming"},
    {"title": "Deep Learning", "author": "Ian Goodfellow", "genre": "Programming"},
    {"title": "Let Us C", "author": "Yashavant Kanetkar", "genre": "Programming"},
    {"title": "C in Depth", "author": "Shrivastava", "genre": "Programming"},
    {"title": "JavaScript: The Good Parts", "author": "Douglas Crockford", "genre": "Programming"},
    {"title": "Programming in ANSI C", "author": "E. Balagurusamy", "genre": "Programming"},
    {"title": "Computer Organization", "author": "Carl Hamacher", "genre": "Programming"},

    #Fiction
    {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction"},
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "genre": "Fiction"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fiction"},
    {"title": "The Fault in Our Stars", "author": "John Green", "genre": "Fiction"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Fiction"},
    {"title": "1984", "author": "George Orwell", "genre": "Fiction"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction"},

    #Self Help
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self Help"},
    {"title": "Deep Work", "author": "Cal Newport", "genre": "Self Help"},
    {"title": "The Power of Habit", "author": "Charles Duhigg", "genre": "Self Help"},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "genre": "Self Help"},
    {"title": "How to Win Friends and Influence People", "author": "Dale Carnegie", "genre": "Self Help"},
    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "genre": "Self Help"},

    #Finance
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "genre": "Finance"},
    {"title": "The Intelligent Investor", "author": "Benjamin Graham", "genre": "Finance"},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "genre": "Finance"},
    {"title": "Psychology of Money", "author": "Morgan Housel", "genre": "Finance"},

    #Engineering/Science
    {"title": "Basic Electrical Engineering", "author": "Nagrath", "genre": "Engineering"},
    {"title": "Engineering Physics", "author": "HK Malik", "genre": "Engineering"},
    {"title": "Engineering Mathematics", "author": "Erwin Kreyszig", "genre": "Engineering"},
    {"title": "Digital Logic and Computer Design", "author": "Morris Mano", "genre": "Engineering"},
    {"title": "Signals and Systems", "author": "Oppenheim", "genre": "Engineering"},
    {"title": "Discrete Mathematics", "author": "Rosen", "genre": "Engineering"},
    {"title": "Linear Algebra", "author": "Gilbert Strang", "genre": "Engineering"},

    #General Knowledge/Non-fiction
    {"title": "Sapiens", "author": "Yuval Noah Harari", "genre": "Non Fiction"},
    {"title": "Ikigai", "author": "Héctor García", "genre": "Non Fiction"},
    {"title": "The Psychology of Money", "author": "Morgan Housel", "genre": "Non Fiction"},
    {"title": "Wings of Fire", "author": "A.P.J. Abdul Kalam", "genre": "Non Fiction"},
    {"title": "You Can Win", "author": "Shiv Khera", "genre": "Non Fiction"},
    {"title": "The 5 AM Club", "author": "Robin Sharma", "genre": "Non Fiction"},
]
# Show all genres when search is empty
def show_all_genres():
    result_list.delete(*result_list.get_children())

    genres = sorted(list(set([b["genre"] for b in books])))

    for g in genres:
        result_list.insert("", "end", values=("—", "—", g))

# Search Function

def search_book():
    query = search_entry.get().lower().strip()

    # If search is empty → show genre list
    if query == "":
        show_all_genres()
        return

    result_list.delete(*result_list.get_children())

    found = False

    for book in books:
        if query in book["title"].lower() or query in book["genre"].lower() or query in book["author"].lower():
            result_list.insert("", "end", values=(book["title"], book["author"], book["genre"]))
            found = True

    if not found:
        messagebox.showinfo("No Result", "No matching books found!")

# Recommendation Function
def recommend_books():
    selected = result_list.focus()

    if selected == "":
        messagebox.showwarning("Select Book", "Please select a book first!")
        return

    values = result_list.item(selected)["values"]
    selected_genre = values[2]

    # Ignore genre list rows ("—")
    if selected_genre == "—":
        messagebox.showwarning("Genre Selected", "Please select an actual book, not a genre!")
        return

    rec_list = [b["title"] for b in books if b["genre"] == selected_genre and b["title"] != values[0]]

    if rec_list:
        messagebox.showinfo("Recommendations", "\n".join(rec_list))
    else:
        messagebox.showinfo("Recommendations", "No similar books found!")

# GUI Window
root = tk.Tk()
root.title("Book Recommendation System")
root.geometry("600x420")

# Title
title_label = tk.Label(root, text="Book Recommendation System", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Search Bar
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, width=40, font=("Arial", 12))
search_entry.pack(side=tk.LEFT, padx=5)

search_btn = tk.Button(search_frame, text="Search", command=search_book, bg="lightblue")
search_btn.pack(side=tk.LEFT)

# Table
columns = ("Title", "Author", "Genre")
result_list = ttk.Treeview(root, columns=columns, show="headings", height=10)

for col in columns:
    result_list.heading(col, text=col)
    result_list.column(col, width=180)

result_list.pack(pady=10)

# Recommendation Button
rec_btn = tk.Button(root, text="Recommend Similar Books", command=recommend_books, bg="lightgreen")
rec_btn.pack(pady=10)

root.mainloop()
