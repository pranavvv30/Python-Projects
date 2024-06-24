import tkinter as tk
import random
from tkinter import ttk
from tkinter import filedialog
import pandas
import openpyxl
import csv


def func2():
    def chatbot():
        user_input = chatbot_entry.get()
        if "movie" in user_input:
            return ("I recommend IMBD website for reviews and description of the movie you are looking for. If there's "
                    "anything else please let me know.")
        elif "news" in user_input:
            return ("There are many websites like CNN, NBC News, etc., which will provide you with the latest news "
                    "updated around the world. If there's anything else please let me know.")
        elif "weather" in user_input:
            return ("I think you can find daily weather updates on popular websites such as Weather.com or the Daily "
                    "broadcast.If there's anything else please let me know.")
        elif "joke" in user_input:
            return "Why don't scientists trust atoms? Because they make everything up."
        else:
            return random.choice(responses)

    def send_button():
        user_input = chatbot_entry.get()
        text_area.insert(tk.END, f"User: {user_input}\n")
        text_area.insert(tk.END, f"Chatbot: {chatbot()}\n")
        chatbot_entry.delete(0, tk.END)

    google_form = []

    def submit():
        name = name_entry.get()
        selected_gender = selected.get()
        dob = dob_entry.get()
        qualification = dropdown.get()
        google_form.insert(-1, [name, selected_gender, dob, qualification])
        with open(r'C:/Users/jaspreet/PycharmProjects/pythonProject1/WRITE.txt', 'w') as file:
            file.write(f"Name:{name}\nGender:{selected_gender}\nDate Of Birth:{dob}\nQualification:{qualification}\n\n")
        print(google_form)
        print("Your form has been submitted successfully. Thank You for your cooperation.")

    def open_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                textarea.delete("1.0", tk.END)
                textarea.insert(tk.END, content)

    def openfile():
        filepath = filedialog.askopenfilename()
        if filepath:
            try:
                df = pd.read_excel(filepath)
                textarea2.delete("1.0", tk.END)
                textarea2.insert(tk.END, df.to_string())
                print("Data successfully read from the file")
            except Exception as e:
                print(f"An error occurred while reading the file :{e}")

    def sort_numbers():
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                numbers = list(map(int, content.split()))
                n = len(numbers)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if numbers[j] > numbers[j + 1]:
                            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                            sorted_content = "\n".join(map(str, numbers))
                with open(file_path, 'w') as file2:
                    file2.write(sorted_content)
                    text_area2.delete("1.0", tk.END)
                    text_area2.insert(tk.END, sorted_content)

    def sortlines():
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()

                def extract_number(line):
                    number = int(line.split("-")[0].strip())
                    return number

                lines = content.splitlines()
                sorted_lines = sorted(lines, key=extract_number)
                sorted_content = "\n".join(sorted_lines)
                with open(file_path, 'w') as file2:
                    file2.write(sorted_content)
                    text_area2.delete("1.0", tk.END)
                    text_area2.insert(tk.END, sorted_content)

    def cleanlines():
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                lines = file.readlines()
                cleanedlines = []
                for line in lines:
                    parts = line.split()
                    if parts:
                        cleaned_parts = " ".join(parts)
                        cleanedlines.append(cleaned_parts)
                        cleaned_content = "\n".join(cleanedlines)
                        with open(file_path, "w") as file2:
                            file2.write(cleaned_content)
                            text_area2.delete("1.0", tk.END)
                            text_area2.insert(tk.END, cleaned_content)

    def append_data():
        def write_to_excel(data):
            df = pd.DataFrame(data, columns=["Name", "Age", "Country"])
            df.to_excel(r'/Users/pranav/Desktop/Book2.xlsx', index=False)

        name = name2_entry.get()
        age = age_entry.get()
        country = country_entry.get()
        if name and age and country:
            data2.append([name, age, country])
            write_to_excel(data2)
            print("Your Data has been successfully written into your excel file.")



    frame_2 = tk.Tk()
    frame_2.geometry("1000x1000")
    notebook = ttk.Notebook(frame_2)
    chatbot_tab = ttk.Frame(frame_2)
    form_tab = ttk.Notebook(frame_2)
    txtreader_tab = ttk.Frame(frame_2)
    excelreader_tab = ttk.Frame(frame_2)
    write_to_excel_tab = ttk.Frame(frame_2)
    tree_tab = ttk.Frame(frame_2)
    sorter_tab = ttk.Frame(frame_2)
    xlstotxt_tab = ttk.Frame(frame_2)
    notebook.add(chatbot_tab, text="Chatbot")
    notebook.add(form_tab, text="Form")
    notebook.add(txtreader_tab, text="TXT Reader")
    notebook.add(excelreader_tab, text="Excel File Reader")
    notebook.add(write_to_excel_tab, text="Write to Excel")
    notebook.add(tree_tab, text="Tree")
    notebook.add(sorter_tab, text="Sorter")
    notebook.pack(expand=True, fill="both")

    data = [("John", 25, "Engineer"),
            ("Aalia", 18, "Student"),
            ("Arshia", 19, "Fashion")]

    data2 = []

    #CHATBOT TAB
    label_chatbot = tk.Label(chatbot_tab,
                             text="Hey I am your personal chatbot. Type in the given below space to talk to me",
                             padx=10, pady=10, relief="raised", bg="#1E90FF", fg="#FFFFFF", bd=5)
    label_chatbot.place(x=150, y=30)

    chatbot_entry = tk.Entry(chatbot_tab)
    chatbot_entry.place(x=10, y=500)
    send_button = tk.Button(chatbot_tab, text="Send", command=send_button)
    send_button.place(x=150, y=500)
    text_area = tk.Text(chatbot_tab)
    text_area.place(x=10, y=100)
    responses = ["Hello! How can I help you today?", "Anything I can help you with today?", "How can I assist you?"]

    #FORM TAB
    lab12 = tk.Label(form_tab, text="Name (Full Name)")
    lab12.place(x=50, y=10)
    name_entry = tk.Entry(form_tab)
    name_entry.place(x=200, y=10)
    selected = tk.StringVar()
    gender_label = tk.Label(form_tab, text="Select you gender")
    gender_label.place(x=50, y=50)
    radiobutton = ttk.Radiobutton(form_tab, text="Male", value="Male", variable=selected)
    radiobutton_2 = ttk.Radiobutton(form_tab, text="Female", value="Female", variable=selected)
    radiobutton_3 = ttk.Radiobutton(form_tab, text="Prefer not to say", value="Prefer not to say", variable=selected)
    radiobutton.place(x=50, y=80)
    radiobutton_2.place(x=50, y=110)
    radiobutton_3.place(x=50, y=140)
    dob_label = tk.Label(form_tab, text="Date of birth (DD/MM/YYYY)")
    dob_label.place(x=50, y=170)
    dob_entry = tk.Entry(form_tab)
    dob_entry.place(x=250, y=170)
    qualification_label = tk.Label(form_tab, text="Qualification")
    qualification_label.place(x=50, y=200)
    options = ["Senior Secondary Education", "Undergraduate", "Graduate"]
    dropdown = ttk.Combobox(form_tab, values=options)
    dropdown.set("Select an option")
    dropdown.place(x=50, y=240)
    submit_button = tk.Button(form_tab, text="Submit", command=submit)
    submit_button.place(x=50, y=280)
    form_label = tk.Label(form_tab, text="This form stores the data entered by you in a .TXT file.", padx=10, pady=10,
                          relief="raised", bg="#1E90FF", fg="#FFFFFF", bd=5)
    form_label.place(x=100, y=350)

    #TXT READER TAB
    textarea = tk.Text(txtreader_tab)
    textarea.place(x=10, y=40)
    openfile_button = tk.Button(txtreader_tab, text="Open File", command=open_file)
    openfile_button.place(x=400, y=500)
    txtreader_label = tk.Label(txtreader_tab, text="This Tab reads the desired .TXT file selected by the user and "
                                                   "displays its contents in the given text area.", padx=10, pady=10,
                               relief="raised", bg="#1E90FF", fg="#FFFFFF", bd=5)
    txtreader_label.place(x=100, y=600)

    #EXCEL FILE READER TAB
    textarea2 = tk.Text(excelreader_tab)
    textarea2.place(x=10, y=40)
    openfile_button2 = tk.Button(excelreader_tab, text="Open File", command=openfile)
    openfile_button2.place(x=400, y=500)
    excelreader_label = tk.Label(excelreader_tab, text="This Tab reads the desired .xlsx file selected by the user and "
                                                       "displays its contents in the given text area.", padx=10,
                                 pady=10, relief="raised", bg="#1E90FF", fg="#FFFFFF", bd=5)
    excelreader_label.place(x=100, y=600)

    #WRITE TO EXCEL FILE TAB
    name2_label = tk.Label(write_to_excel_tab, text="Name")
    name2_label.place(x=50, y=100)
    name2_entry = tk.Entry(write_to_excel_tab)
    name2_entry.place(x=120, y=100)
    age_label = tk.Label(write_to_excel_tab, text="Age")
    age_label.place(x=50, y=150)
    age_entry = tk.Entry(write_to_excel_tab)
    age_entry.place(x=120, y=150)
    country_label = tk.Label(write_to_excel_tab, text="Country")
    country_label.place(x=50, y=200)
    country_entry = tk.Entry(write_to_excel_tab)
    country_entry.place(x=120, y=200)
    submit2_button = tk.Button(write_to_excel_tab, text="Submit", command=append_data)
    submit2_button.place(x=100, y=250)
    write_to_excel_label = tk.Label(write_to_excel_tab, text="This tab stores and writes the data entered by the user  "
                                                             " in a .xlsx file.", padx=10, pady=10, relief="raised",
                                    bg="#1E90FF", fg="#FFFFFF", bd=5)
    write_to_excel_label.place(x=100, y=500)

    #TREEVIEW TAB
    tree = ttk.Treeview(tree_tab, columns=("Name", "Age", "Profession"), show="headings")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")
    tree.heading("Profession", text="Profession")

    for row in data:
        tree.insert("", "end", values=row)
        tree.pack(expand=True, fill="both")
    tree_label = tk.Label(tree_tab, text="This tab displays the values stored in a variable in table form.", padx=10,
                          pady=10, relief="raised", bg="#1E90FF", fg="#FFFFFF", bd=5)
    tree_label.place(x=100, y=500)

    #SORTER TAB
    sortnumbers_button = tk.Button(sorter_tab, text="Sort Numbers", command=sort_numbers)
    sortnumbers_button.place(x=10, y=450)
    sortlines_button = tk.Button(sorter_tab, text="Sort Lines", command=sortlines)
    sortlines_button.place(x=150, y=450)
    cleandata_button = tk.Button(sorter_tab, text="Clean Data", command=cleanlines)
    cleandata_button.place(x=290, y=450)

    text_area2 = tk.Text(sorter_tab)
    text_area2.place(x=100, y=100)
    sorter_1=tk.Label(sorter_tab, text="The SORT NUMBERS button sorts numbers given in a .txt file.", padx=10,
             pady=10, relief="raised", bg="#1E90FF", fg="#FFFFFF", bd=5)
    sorter_2 = tk.Label(sorter_tab,
                        text="This SORT LINES button sorts the lines of a selected file based on numerical values extracted from "
                             "the beginning of each line.",
                        padx=10,
                        pady=10, relief="raised", bg="#1E90FF", fg="#FFFFFF", bd=5)
    sorter_3 = tk.Label(sorter_tab,
                        text="This CLEAN DATA button cleans up a selected file by removing extra spaces and rewriting the" 
                              "file with cleaned lines.",padx=10,
                        pady=10, relief="raised", bg="#1E90FF", fg="#FFFFFF", bd=5)


    sorter_1.place(x=10, y=500)
    sorter_2.place(x=10, y=560)
    sorter_3.place(x=10,y=630)

    frame_2.mainloop()


#LOGIN AND SIGNUP TABS
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    if username in credentials and credentials[username] == password:
        login_tab.destroy()
        func2()

    else:
        pass


def sign_up():
    def sign_up2():
        username1 = username__entry.get()
        password1 = pass_entry.get()
        confirm_pass = confirmpass_entry.get()
        if password1 == confirm_pass:
            credentials.update({username1: password1})
            print(credentials)
            signup_tab.destroy()
        else:
            raise ValueError("Both the passwords do not match. Please try again.")

    signup_tab = tk.Tk()
    signup_tab.config(bg="lightblue")
    signup_tab.title("Sign Up")
    signup_tab.geometry("1000x1000")
    username__label = tk.Label(signup_tab, text="Username", bg="black", fg="white", font=("Garamond", 12, "bold"))
    username__label.place(x=350, y=400)
    username__entry = tk.Entry(signup_tab)
    username__entry.place(x=450, y=400)
    pass_label = tk.Label(signup_tab, text="Password", bg="black", fg="white", font=("Garamond", 12, "bold"))
    pass_label.place(x=350, y=450)
    pass_entry = tk.Entry(signup_tab, show="*")
    pass_entry.place(x=450, y=450)
    confirmpass_label = tk.Label(signup_tab, text="Confirm Password", bg="black", fg="white",
                                 font=("Garamond", 12, "bold"))
    confirmpass_label.place(x=300, y=500)
    confirmpass_entry = tk.Entry(signup_tab, show="*")
    confirmpass_entry.place(x=450, y=500)
    signup_button2 = tk.Button(signup_tab, text="Sign up", command=sign_up2, bg="black", fg="white",
                               font=("Garamond", 12, "bold"))
    signup_button2.place(x=420, y=600)
    signup_tab.mainloop()


login_tab = tk.Tk()
login_tab.config(bg="lightblue")
login_tab.geometry("1000x1000")
credentials = {"Pranav": "Pranav3008", "A": "123"}
username_label = tk.Label(login_tab, text="Username", bg="black", fg="white", font=("Garamond", 12, "bold"))
password_label = tk.Label(login_tab, text="Password", bg="black", fg="white", font=("Garamond", 12, "bold"))
username_label.place(x=350, y=350)
password_label.place(x=350, y=400)

username_entry = tk.Entry(login_tab)
password_entry = tk.Entry(login_tab, show="*")
username_entry.place(x=450, y=350)
password_entry.place(x=450, y=400)
login_button = tk.Button(login_tab, text="Login", command=check_login, font=("Garamond", 12, "bold"))
login_button.place(x=400, y=500)

signup_button = tk.Button(login_tab, text="Signup", command=sign_up, font=("Garamond", 12, "bold"))
signup_button.place(x=500, y=500)

login_tab.mainloop()
