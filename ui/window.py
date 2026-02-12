import tkinter as tk
from tkinter import filedialog, messagebox
from logic.sorter import get_date, move_photo

class PhotoSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PhotoSort")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f2f5")

        self.selected_files = []
        self.destination_folder = ""

        self.init_ui()

    def init_ui(self):
        # title
        tk.Label(self.root, text="Photo Sort", font=("Arial", 18, "bold"), bg="#f0f2f5").pack(pady=10)

        # button for choosing files
        self.file_frame = tk.Frame(self.root, bd=2, relief="groove", bg="white")
        self.file_frame.pack(pady=20, padx=40, fill="both", expand=True)

        self.file_label = tk.Label(self.file_frame, text="No files selected", bg="white", fg="#666")
        self.file_label.pack(pady=20)

        tk.Button(self.file_frame, text="Browse Files", command=self.browse_files,
                  bg="#007bff", fg="white", font=("Arial", 10, "bold"), padx=10).pack(pady=10)

        # bottom part
        bottom_frame = tk.Frame(self.root, bg="#f0f2f5")
        bottom_frame.pack(side="bottom", fill="x", padx=20, pady=20)

        self.dest_label = tk.Entry(bottom_frame, fg="#666")
        self.dest_label.insert(0, "Select Destination Folder")
        self.dest_label.config(state="readonly")
        self.dest_label.pack(side="left", fill="x", expand=True, padx=(0, 10))

        tk.Button(bottom_frame, text="📁", command=self.select_folder).pack(side="left", padx=(0, 10))

        self.sort_btn = tk.Button(bottom_frame, text="Photo Sort", command=self.start_sort,
                                  bg="#28a745", fg="white", font=("Arial", 10, "bold"), padx=15)
        self.sort_btn.pack(side="right")

    def browse_files(self):
        files = filedialog.askopenfilenames(title="Select Images")

        if files:
            self.selected_files = list(files)
            self.file_label.config(text=f"{len(self.selected_files)} files selected")

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.destination_folder = folder
            self.dest_label.config(state="normal")
            self.dest_label.delete(0, tk.END)
            self.dest_label.insert(0, folder)
            self.dest_label.config(state="readonly")

    def start_sort(self):
        if not self.selected_files or not self.destination_folder:
            messagebox.showwarning("Warning", "Please select files and destination!")
            return

        for file in self.selected_files:
            date = get_date(file)
            move_photo(file, date, self.destination_folder)

        messagebox.showinfo("Success", "Photos have been sorted!")
        self.selected_files = []
        self.file_label.config(text="No files selected")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoSorterApp(root)
    root.mainloop()