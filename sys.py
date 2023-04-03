from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import pymysql
from database import cur, con
import manager

root = Tk()
root.title("SYLLABUS MANAGEMENT SYSTEM")
root.geometry("1500x780+0+0")
root.resizable(False, False)


class StringVarCollection:
    @staticmethod
    def convert_string_var_collection(col):
        return {k: v.get() for k, v in col.__dict__.items()}

    @staticmethod
    def reset_string_var_collection(col):
        for value in col.__dict__.values():
            value.set("")


string_var_collection = StringVarCollection()

logo = Label(root, bd=15, relief=RIDGE, text="SYLLABUS MANAGEMENT SYSTEM", fg="red", bg='#FFEBCD',
             font=("times new roman", 30, "bold"))
logo.pack(side=TOP, fill=X)

# input bolder
Frame(root, bd=20, relief=RIDGE, bg='#FFEBCD').place(x=0, y=80, width=1499, height=700)
Frame(root, bd=10, relief=RIDGE, bg='#FFEBCD').place(x=20, y=100, width=510, height=460)
Frame(root, bd=10, relief=RIDGE, bg='#FFEBCD').place(x=530, y=100, width=949, height=170)
Frame(root, bd=10, relief=RIDGE, bg='#FFEBCD').place(x=530, y=270, width=949, height=290)
button_frame = Frame(root, bd=10, relief=RIDGE, bg='#FFEBCD').place(x=20, y=560, width=1459, height=200)


# Function
def list_courses():
    fetched_data = manager.list_syllabus()
    update_view(fetched_data)


def update_view(fetched_data):
    Syllabus_table.delete(*Syllabus_table.get_children())
    for data in fetched_data:
        print(data)
        Syllabus_table.insert('', END, values=data)


def search():
    fetched_data = manager.search(**StringVarCollection.convert_string_var_collection(string_var_collection))
    Syllabus_table.delete(*Syllabus_table.get_children())
    for data in fetched_data:
        Syllabus_table.insert('', END, values=data)


def add_course():
    all_inputs = StringVarCollection.convert_string_var_collection(string_var_collection)
    for value in all_inputs.values():
        if not value:
            messagebox.showerror('Error', 'All fields are required')
            return
    manager.create_course(**all_inputs)
    con.commit()
    list_courses()


def delete():
    indexing = Syllabus_table.focus()
    print(indexing)
    cont = Syllabus_table.item(indexing)
    cont_id = cont["values"][0]
    manager.delete_course(cont_id)
    messagebox.showinfo('Deleted', f'Course {cont_id} is deleted successfully.')
    list_courses()


def view():
    indexing = Syllabus_table.focus()
    cont = Syllabus_table.item(indexing)
    row = cont['values']

    variables = [
        string_var_collection.id, string_var_collection.major_id, string_var_collection.course_name,
        string_var_collection.credit_points, string_var_collection.background_knowledge, string_var_collection.textbook,
        string_var_collection.reference,
        string_var_collection.course_content, string_var_collection.objectives,
        string_var_collection.lecture, string_var_collection.tutor, string_var_collection.practice,
        string_var_collection.attendance, string_var_collection.exercises, string_var_collection.assignments,
        string_var_collection.reports,
        string_var_collection.midterm, string_var_collection.final,
    ]

    i = 0
    for variable in variables:
        variable.set(row[i])
        i += 1


def update():
    manager.update_course(**StringVarCollection.convert_string_var_collection(string_var_collection))
    list_courses()


# input bolder
string_var_collection.id = tk.StringVar()
string_var_collection.course_name = tk.StringVar()
string_var_collection.major_id = tk.StringVar()
string_var_collection.credit_points = tk.StringVar()
string_var_collection.background_knowledge = tk.StringVar()
string_var_collection.textbook = tk.StringVar()
string_var_collection.reference = tk.StringVar()
string_var_collection.course_content = tk.StringVar()
string_var_collection.objectives = tk.StringVar()
string_var_collection.lecture = tk.StringVar()
string_var_collection.tutor = tk.StringVar()
string_var_collection.practice = tk.StringVar()
string_var_collection.attendance = tk.StringVar()
string_var_collection.exercises = tk.StringVar()
string_var_collection.assignments = tk.StringVar()
string_var_collection.reports = tk.StringVar()
string_var_collection.midterm = tk.StringVar()
string_var_collection.final = tk.StringVar()

LbId = Label(font=("times new roman", 13, "bold"), text="Id:", bg='#FFEBCD').place(x=40, y=115, width=200, height=30)
IpId = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.id).place(x=250, y=115,
                                                                                                width=250,
                                                                                                height=30)

LbName = Label(font=("times new roman", 13, "bold"), text="Name Course:", bg='#FFEBCD').place(x=40, y=165, width=200,
                                                                                              height=30)
IpName = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.course_name).place(x=250, y=165,
                                                                                                           width=250,
                                                                                                           height=30)

LbMajor = Label(font=("times new roman", 13, "bold"), text="Major:", bg='#FFEBCD').place(x=40, y=215, width=200,
                                                                                         height=30)
IpMajor = ttk.Combobox(font=("times new roman", 13, "bold"), textvariable=string_var_collection.major_id).place(x=250,
                                                                                                                y=215,
                                                                                                                width=250,
                                                                                                                height=30)

LbCredit = Label(font=("times new roman", 13, "bold"), text="Credit Points:", bg='#FFEBCD').place(x=40, y=265,
                                                                                                  width=200, height=30)
IpCredit = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.credit_points).place(x=250,
                                                                                                               y=265,
                                                                                                               width=250,
                                                                                                               height=30)

LbBacK = Label(font=("times new roman", 13, "bold"), text="BackGround Knowledge:", bg='#FFEBCD').place(x=40, y=315,
                                                                                                       width=200,
                                                                                                       height=30)
IpBacK = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.background_knowledge).place(
    x=250, y=315,
    width=250,
    height=30)

LbTexB = Label(font=("times new roman", 13, "bold"), text="TextBook:", bg='#FFEBCD').place(x=40, y=365, width=200,
                                                                                           height=30)
IpTexB = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.textbook).place(x=250, y=365,
                                                                                                        width=250,
                                                                                                        height=30)

LbRefL = Label(font=("times new roman", 13, "bold"), text="Reference Literature:", bg='#FFEBCD').place(x=40, y=415,
                                                                                                       width=200,
                                                                                                       height=30)
IpRefL = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.reference).place(x=250, y=415,
                                                                                                         width=250,
                                                                                                         height=30)

LbCouContent = Label(font=("times new roman", 13, "bold"), text="Course Content:", bg='#FFEBCD').place(x=40, y=465,
                                                                                                       width=200,
                                                                                                       height=30)
IpCouContent = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.course_content).place(
    x=250,
    y=465,
    width=250,
    height=30)

LbObj = Label(font=("times new roman", 13, "bold"), text="Objectives:", bg='#FFEBCD').place(x=40, y=515, width=200,
                                                                                            height=30)
IpObj = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.objectives).place(x=250, y=515,
                                                                                                         width=250,
                                                                                                         height=30)

LbCredit = Label(font=("times new roman", 13, "bold"), text="Time Commitement:", bg='#FFEBCD').place(x=550, y=185,
                                                                                                     width=200,
                                                                                                     height=30)

LbTLecture = Label(font=("times new roman", 13, "bold"), text="Lecture:", bg='#FFEBCD').place(x=770, y=150, width=120,
                                                                                              height=30)
IpTLecture = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.lecture).place(x=900, y=150,
                                                                                                           width=150,
                                                                                                           height=30)

LbTTutor = Label(font=("times new roman", 13, "bold"), text="Tutorial:", bg='#FFEBCD').place(x=770, y=205, width=120,
                                                                                             height=30)
IpTTutor = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.tutor).place(x=900, y=205,
                                                                                                       width=150,
                                                                                                       height=30)

LbTPract = Label(font=("times new roman", 13, "bold"), text="Practical:", bg='#FFEBCD').place(x=1070, y=150, width=120,
                                                                                              height=30)
IpTPract = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.practice).place(x=1200, y=150,
                                                                                                          width=150,
                                                                                                          height=30)

LbAsses = Label(font=("times new roman", 13, "bold"), text="Assessment:", bg='#FFEBCD').place(x=550, y=355, width=200,
                                                                                              height=30)

LbAtten = Label(font=("times new roman", 13, "bold"), text="Attendance:", bg='#FFEBCD').place(x=770, y=300, width=120,
                                                                                              height=30)
IpAtten = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.attendance).place(x=900, y=300,
                                                                                                           width=150,
                                                                                                           height=30)

LbExe = Label(font=("times new roman", 13, "bold"), text="Exercises:", bg='#FFEBCD').place(x=770, y=360, width=120,
                                                                                           height=30)
IpExe = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.exercises).place(x=900, y=360,
                                                                                                        width=150,
                                                                                                        height=30)

LbAssign = Label(font=("times new roman", 13, "bold"), text="Assignments:", bg='#FFEBCD').place(x=770, y=420, width=120,
                                                                                                height=30)
IpAssign = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.assignments).place(x=900,
                                                                                                             y=420,
                                                                                                             width=150,
                                                                                                             height=30)

LbReports = Label(font=("times new roman", 13, "bold"), text="Reports:", bg='#FFEBCD').place(x=1070, y=300, width=120,
                                                                                             height=30)
IpReports = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.reports).place(x=1200, y=300,
                                                                                                          width=150,
                                                                                                          height=30)

LbMid = Label(font=("times new roman", 13, "bold"), text="Midterm:", bg='#FFEBCD').place(x=1070, y=360, width=120,
                                                                                         height=30)
IpMid = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.midterm).place(x=1200, y=360,
                                                                                                      width=150,
                                                                                                      height=30)

LbFinal = Label(font=("times new roman", 13, "bold"), text="Final:", bg='#FFEBCD').place(x=1070, y=420, width=120,
                                                                                         height=30)
IpFinal = Entry(font=("times new roman", 13, "bold"), textvariable=string_var_collection.final).place(x=1200, y=420,
                                                                                                      width=150,
                                                                                                      height=30)

# creat button
Button(font=("times new roman", 13, "bold"), text="SEARCH", command=search).place(x=580, y=500, width=100)
Button(font=("times new roman", 13, "bold"), text="ADD", command=add_course).place(x=700, y=500, width=100)
Button(font=("times new roman", 13, "bold"), text="DESELECT",
       command=lambda: StringVarCollection.reset_string_var_collection(string_var_collection)).place(x=820, y=500,
                                                                                                       width=100)
Button(font=("times new roman", 13, "bold"), text="DELETE", command=delete).place(x=940, y=500, width=100)
Button(font=("times new roman", 13, "bold"), text="UPDATE", command=update).place(x=1110, y=500, width=100)
Button(font=("times new roman", 13, "bold"), text="VIEW", command=view).place(x=1230, y=500, width=100)
Button(font=("times new roman", 13, "bold"), text="LIST", command=list_courses).place(x=1350, y=500, width=100)

# create table
scrollBarX = Scrollbar(button_frame, orient=HORIZONTAL)
scrollBarY = Scrollbar(button_frame, orient=VERTICAL)

Syllabus_table = ttk.Treeview(button_frame, columns=(
    'id', 'major_id', 'course_name', 'credit_points_inECTs', 'background_knowledge', 'textbook', 'ref_literature',
    'course_content', 'objectives', \
    'lecture', 'tutorial', 'practical', 'attendance', 'exercise', 'assignment', 'report', 'midterm', 'final'),
                              xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

Syllabus_table.place(x=27, y=567, width=1450, height=190)
scrollBarX.config(command=Syllabus_table.xview)
scrollBarY.config(command=Syllabus_table.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

Syllabus_table.heading('id', text='ID')
Syllabus_table.heading('course_name', text='Name Course')
Syllabus_table.heading('major_id', text='Major')
Syllabus_table.heading('credit_points_inECTs', text='Credit points')
Syllabus_table.heading('background_knowledge', text='Background knowledge')
Syllabus_table.heading('textbook', text='TextBook')
Syllabus_table.heading('ref_literature', text='Reference Literature')
Syllabus_table.heading('course_content', text='Course Content')
Syllabus_table.heading('objectives', text='Objectives')
Syllabus_table.heading('lecture', text='Lecture')
Syllabus_table.heading('tutorial', text='Tutorial')
Syllabus_table.heading('practical', text='Practical')
Syllabus_table.heading('attendance', text='Attendance')
Syllabus_table.heading('exercise', text='Exercise')
Syllabus_table.heading('assignment', text='Assignment')
Syllabus_table.heading('report', text='Report')
Syllabus_table.heading('midterm', text='Midterm')
Syllabus_table.heading('final', text='Final')

Syllabus_table.column('id', width=30, anchor=CENTER)
Syllabus_table.column('major_id', width=80, anchor=CENTER)
Syllabus_table.column('credit_points_inECTs', width=80, anchor=CENTER)
Syllabus_table.column('lecture', width=80, anchor=CENTER)
Syllabus_table.column('tutorial', width=80, anchor=CENTER)
Syllabus_table.column('practical', width=80, anchor=CENTER)
Syllabus_table.column('attendance', width=80, anchor=CENTER)
Syllabus_table.column('exercise', width=80, anchor=CENTER)
Syllabus_table.column('assignment', width=80, anchor=CENTER)
Syllabus_table.column('report', width=80, anchor=CENTER)
Syllabus_table.column('midterm', width=80, anchor=CENTER)
Syllabus_table.column('final', width=80, anchor=CENTER)

Syllabus_table.config(show='headings')

root.mainloop()
