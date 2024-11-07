import customtkinter as ctk
import tkinter.messagebox as messagebox
import subprocess
import json
import sys
import threading


# filename = ""
# Function to handle form submission
def submit() :
    # global filename

    # Collect the form data
    data = {
        "base_url": base_url_entry.get().strip(),
        "product_name": product_name_entry.get().strip(),
        "cust_name": cust_name_entry.get().strip(),
        "review_title": review_title_entry.get().strip(),
        "rating": rating_entry.get().strip(),
        "comment": comment_entry.get().strip(),
        "filename": filename_entry.get().strip(),
        "from_page": from_page_entry.get().strip(),
        "to_page": to_page_entry.get().strip(),

    }

    # Check if any of the fields are empty
    for key in data :
        if not data[key] :
            messagebox.showerror("Missing Information", "Please fill in all the fields.")
            return

    # Validate "From Page", and "To Page" to ensure they are integers
    try:
        data['from_page'] = int(data['from_page'])
        data['to_page'] = int(data['to_page'])
        if data['from_page'] <= 0 or data['from_page'] > data['to_page'] :
            raise ValueError

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers for 'From Page', and 'To Page'.")
        return  # Exit the function if input is invalid



    # filename = filename_entry.get()
    # Serialize the dictionary into a JSON string
    data_json = json.dumps(data)

    # Disable the Submit Button to prevent multiple submissions
    submit_button.configure(state="disabled")
    submit_button.grid_forget()
    
    # Show the loading indicator
    loading_label.grid(row=10, columnspan=2, pady=30)  # Place loading label in the grid
    progress_bar.grid(row=11, columnspan=2, pady=20)  # Place progress bar in the grid
    progress_bar.start()

    # Create a thread to run the subprocess so it doesn't block the UI
    threading.Thread(target=run_subprocess, args=(data_json,)).start()

# Function to run the subprocess
def run_subprocess(data_json):
    # global filename
    try:
        # Pass the data to another Python script (for example, 'other_script.py')
        result = subprocess.run(
            [sys.executable, 'Gen_Data.py', data_json],
            capture_output=True,  # Capture both stdout and stderr
            text=True  # Return output as text (not bytes)
        )

        # Stop the progress bar after subprocess finishes
        progress_bar.stop()

        # If there was an error in stderr, show the error message in a pop-up
        if result.stderr :
            messagebox.showerror("Error", f"Error in other script: {result.stderr}")
        else :
            resinfo = result.stdout
            messagebox.showinfo("Success", f"Dataset has been Downloaded Successfully.\n{resinfo}")

    except Exception as e:
        # Stop the progress bar in case of an exception
        progress_bar.stop()
        # If there's an exception while running subprocess, show an error message
        messagebox.showerror("Error", f"Error while running the script: {e}")

    finally:
        # Re-enable the Submit button after the subprocess finishes
        submit_button.configure(state="normal")
        submit_button.grid(row=10, columnspan=2, pady=20)
        loading_label.grid_forget()  # Remove loading label from the grid
        progress_bar.grid_forget()  # Remove progress bar from the grid


# Create the main window
app = ctk.CTk()

# Set window title and size
app.title("@https://github.com/joelblr/WST-FKART")
app.geometry("500x600")  # Adjusted height to accommodate the grid

# Set the background color of the main window (not the labels)
app.configure(fg_color="#2C3E50")  # Dark Blue Background for the main window

# Define a color that complements the blue background (light cyan)
text_color = "#A3D0D4"  # Light Cyan

# Create a header label
header_label = ctk.CTkLabel(app, text="Web Scraper Tool: FlipKart", font=("Helvetica", 20, "bold"), text_color=text_color)
header_label.grid(row=0, columnspan=2, pady=20)

# Base URL (first field)
base_url_label = ctk.CTkLabel(app, text="Base URL", font=("Helvetica", 14, "bold"), text_color=text_color)
base_url_label.grid(row=1, column=0, pady=(10, 5), padx=(10, 10), sticky="w")
base_url_entry = ctk.CTkEntry(app, placeholder_text="Enter Base URL", font=("Helvetica", 14))
base_url_entry.grid(row=1, column=1, pady=5, padx=20, sticky="ew")

# Product Name (new field)
product_name_label = ctk.CTkLabel(app, text="Product Name", font=("Helvetica", 14, "bold"), text_color=text_color)
product_name_label.grid(row=2, column=0, pady=(10, 5), padx=(10, 10), sticky="w")
product_name_entry = ctk.CTkEntry(app, placeholder_text="Enter Product Name", font=("Helvetica", 14))
product_name_entry.grid(row=2, column=1, pady=5, padx=20, sticky="ew")

# Customer Name
cust_name_label = ctk.CTkLabel(app, text="Customer Name", font=("Helvetica", 14, "bold"), text_color=text_color)
cust_name_label.grid(row=3, column=0, pady=(10, 5), padx=(10, 10), sticky="w")
cust_name_entry = ctk.CTkEntry(app, placeholder_text="Enter Customer-Name Class-Id", font=("Helvetica", 14))
cust_name_entry.grid(row=3, column=1, pady=5, padx=20, sticky="ew")

# Review Title
review_title_label = ctk.CTkLabel(app, text="Review Title", font=("Helvetica", 14, "bold"), text_color=text_color)
review_title_label.grid(row=4, column=0, pady=(10, 5), padx=(10, 10), sticky="w")
review_title_entry = ctk.CTkEntry(app, placeholder_text="Enter Review-Title Class-Id", font=("Helvetica", 14))
review_title_entry.grid(row=4, column=1, pady=5, padx=20, sticky="ew")

# Rating
rating_label = ctk.CTkLabel(app, text="Rating", font=("Helvetica", 14, "bold"), text_color=text_color)
rating_label.grid(row=5, column=0, pady=(10, 5), padx=(10, 10), sticky="w")
rating_entry = ctk.CTkEntry(app, placeholder_text="Enter Rating Class-Id", font=("Helvetica", 14))
rating_entry.grid(row=5, column=1, pady=5, padx=20, sticky="ew")

# Comment
comment_label = ctk.CTkLabel(app, text="Comment", font=("Helvetica", 14, "bold"), text_color=text_color)
comment_label.grid(row=6, column=0, pady=(10, 5), padx=(10, 10), sticky="w")
comment_entry = ctk.CTkEntry(app, placeholder_text="Enter Comment Class-Id", font=("Helvetica", 14))
comment_entry.grid(row=6, column=1, pady=5, padx=20, sticky="ew")

# From Page (new field)
from_page_label = ctk.CTkLabel(app, text="From Page", font=("Helvetica", 14, "bold"), text_color=text_color)
from_page_label.grid(row=7, column=0, pady=(10, 5), padx=(10, 10), sticky="w")
from_page_entry = ctk.CTkEntry(app, placeholder_text="Enter From Page", font=("Helvetica", 14))
from_page_entry.grid(row=7, column=1, pady=5, padx=20, sticky="ew")

# To Page (new field)
to_page_label = ctk.CTkLabel(app, text="To Page", font=("Helvetica", 14, "bold"), text_color=text_color)
to_page_label.grid(row=8, column=0, pady=(10, 5), padx=(10, 10), sticky="w")
to_page_entry = ctk.CTkEntry(app, placeholder_text="Enter To Page", font=("Helvetica", 14))
to_page_entry.grid(row=8, column=1, pady=5, padx=20, sticky="ew")


# Filename
filename_label = ctk.CTkLabel(app, text="Save-As", font=("Helvetica", 14, "bold"), text_color=text_color)
filename_label.grid(row=9, column=0, pady=(10, 5), padx=(10, 10), sticky="w")
filename_entry = ctk.CTkEntry(app, placeholder_text="Filename.csv", font=("Helvetica", 14))
filename_entry.grid(row=9, column=1, pady=5, padx=20, sticky="ew")


# Submit Button
submit_button = ctk.CTkButton(app, text="Generate", font=("Helvetica", 16, "bold"), fg_color="#2980B9", text_color="white", command=submit)
submit_button.grid(row=10, columnspan=2, pady=20)

# Create the loading label and progress bar, but do not show them initially
loading_label = ctk.CTkLabel(app, text="Processing...", font=("Helvetica", 16, "bold"), text_color="white", anchor="center")
progress_bar = ctk.CTkProgressBar(app, mode='indeterminate', width=300)

# Make the grid columns expandable to fit the window
app.grid_columnconfigure(1, weight=1)

# Run the app
app.mainloop()
