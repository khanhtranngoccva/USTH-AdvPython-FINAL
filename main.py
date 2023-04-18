from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from database import cur, con
import manager
from login import login_ui
from ui.ui_root import root
from details import create_edit_window

# if not login_ui():
#     exit(0)

logo = Label(root, bd=15, relief=RIDGE, text="SYLLABUS MANAGEMENT SYSTEM", fg="red", bg='#FFEBCD', font=("times new roman", 30, "bold"))
logo.pack(side=TOP, fill=X)

button_frame = Frame(root, bd=20, relief=RIDGE, bg='#FFEBCD')
button_frame.pack(side="bottom", fill=tk.X)

# input bolder
main_frame = Frame(root, bd=20, relief=RIDGE, bg='#FFEBCD')
main_frame.pack(side="top", fill=tk.BOTH, expand=True)
# Frame(root, bd=10, relief=RIDGE, bg='#FFEBCD').place(x=20, y=560, width=1459, height=200)


# Function
def list_courses():
    fetched_data = manager.list_syllabus()
    update_view(fetched_data)


def update_view(fetched_data):
    Syllabus_table.delete(*Syllabus_table.get_children())
    for data in fetched_data:
        Syllabus_table.insert('', END, values=data)

def view_course():
    indexing = Syllabus_table.focus()
    cont = Syllabus_table.item(indexing)
    row = cont['values']
    create_edit_window("EDIT", row[0], lambda x: list_courses())


# create table
scrollBarX = Scrollbar(main_frame, orient=HORIZONTAL)
scrollBarY = Scrollbar(main_frame, orient=VERTICAL)

Syllabus_table = ttk.Treeview(main_frame, columns=(
    'id', 'major_id', 'course_name', 'credit_points_inECTs', 'background_knowledge', 'textbook', 'ref_literature',
    'course_content', 'objectives', \
    'lecture', 'tutorial', 'practical', 'attendance', 'exercise', 'assignment', 'report', 'midterm', 'final'),
                              xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=Syllabus_table.xview)
scrollBarY.config(command=Syllabus_table.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)
Syllabus_table.pack(side="top", fill=tk.BOTH, expand=True)

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



tk.Button(font=("times new roman", 13, "bold"), text="ADD",
                  command=lambda: create_edit_window("ADD", None, lambda x: list_courses())).pack(side="left")
tk.Button(font=("times new roman", 13, "bold"), text="SEARCH",
                  command=lambda: create_edit_window("SEARCH", None, lambda x: update_view(x))).pack(side="left")
tk.Button(font=("times new roman", 13, "bold"), text="LIST",
                  command=lambda: list_courses()).pack(side="left")
tk.Button(font=("times new roman", 13, "bold"), text="VIEW AND EDIT",
                  command=lambda: view_course()).pack(side="left")


list_courses()
root.mainloop()