import tkinter as tk
from tkinter import simpledialog

class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        books = [f"Book: {line.split(',')[0]}, Author: {line.split(',')[1]}" for line in lines]
        return books

    def add_book(self, title, author, release_year, num_pages):
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        return f"{title} has been added to the library."

    def remove_book(self, title_to_remove):
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()

            with open(self.file_name, 'w') as file:
                for line in lines:
                    if title_to_remove.lower() not in line.lower():
                        file.write(line)

            print(f"The expression '{title_to_remove}' has been successfully removed from the file.")
        except FileNotFoundError:
            print(f"File not found: {self.file_name}")
        except Exception as e:
            print(f"An error occurred: {e}")


    def clear_file(self):
        self.file.seek(0)
        self.file.truncate()

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.lib = Library()

        self.label = tk.Label(root, text="*** MENU ***", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.list_button = tk.Button(root, text="List Books", command=self.list_books)
        self.list_button.pack()

        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Book", command=self.remove_book)
        self.remove_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack()

    def list_books(self):
        books = self.lib.list_books()
        result = "\n".join(books)

        # Temizleme
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()

        result_label = tk.Label(self.root, text=result, font=("Helvetica", 12))
        result_label.pack(pady=10)

    def add_book(self):
        title = simpledialog.askstring("Input", "Enter the book title:")
        author = simpledialog.askstring("Input", "Enter the author:")
        release_year = simpledialog.askstring("Input", "Enter the release year:")
        num_pages = simpledialog.askstring("Input", "Enter the number of pages:")

        result = self.lib.add_book(title, author, release_year, num_pages)
        self.show_result(result)

    def remove_book(self):
        title_to_remove = simpledialog.askstring("Input", "Enter the title of the book to remove:")
        self.lib.remove_book(title_to_remove)
        self.show_result(f"{title_to_remove} has been removed from the library.")

    def show_result(self, result):
        result_label = tk.Label(self.root, text=result, font=("Helvetica", 12))
        result_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
