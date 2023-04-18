import manager
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from ui.textbox import Textbox
from ui.scroll_frame import VerticalScrolledFrame

class StringVarCollection:
    @staticmethod
    def convert_string_var_collection(col):
        return {k: v.get() for k, v in col.__dict__.items()}

    @staticmethod
    def reset_string_var_collection(col):
        for value in col.__dict__.values():
            value.set("")


def create_edit_window(mode: str, course_id: int = None, callback = None):
    def spawn_window():
        window = tk.Toplevel()
        window.title("Create or edit course")
        window.geometry("800x600")
        return window

    def create_string_var_collection():
        string_var_collection = StringVarCollection()
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
        return string_var_collection

    def clear_input():
        StringVarCollection.reset_string_var_collection(string_var_collection)

    def populate():
        input_widgets_data = [
            ("Id", string_var_collection.id, 1),
            ("Course name", string_var_collection.course_name, 1),
            ("Major ID", string_var_collection.major_id, 1),
            ("Credit points", string_var_collection.credit_points, 1),
            ("Background knowledge", string_var_collection.background_knowledge, 8),
            ("Textbook", string_var_collection.textbook, 8),
            ("Reference", string_var_collection.reference, 8),
            ("Course content", string_var_collection.course_content, 8),
            ("Objectives", string_var_collection.objectives, 8),
            ("Lecture", string_var_collection.lecture, 1),
            ("Tutor", string_var_collection.tutor, 1),
            ("Practice", string_var_collection.practice, 1),
            ("Attendance", string_var_collection.attendance, 1),
            ("Exercises", string_var_collection.exercises, 1),
            ("Assignments", string_var_collection.assignments, 1),
            ("Reports", string_var_collection.reports, 1),
            ("Midterm", string_var_collection.midterm, 1),
            ("Final", string_var_collection.final, 1)
        ]

        button_frame = tk.Frame(master=window)
        button_frame.pack(side="top", fill=tk.X)
        if mode == "ADD":
            tk.Button(button_frame, font=("times new roman", 13, "bold"), text="ADD",
                    command=add_course).pack(side=tk.LEFT)
        elif mode == "SEARCH":
            tk.Button(button_frame, font=("times new roman", 13, "bold"), text="SEARCH",
                    command=search).pack(side=tk.LEFT)
        elif mode == "EDIT":
            tk.Button(button_frame, font=("times new roman", 13, "bold"), text="DELETE",
                    command=delete).pack(side=tk.LEFT)
            tk.Button(button_frame, font=("times new roman", 13, "bold"), text="UPDATE",
                    command=update).pack(side=tk.LEFT)
            fill_fields()

        input_frame = VerticalScrolledFrame(master=window)
        input_frame.pack(side="bottom", fill=tk.BOTH, expand=True)

        for data in input_widgets_data:
            frame = tk.Frame(master=input_frame.interior)
            frame.pack(side="top", fill=tk.X)
            tk.Label(frame, width=30, text=data[0]).pack(side="left")
            Textbox(frame, height=data[2], textvariable=data[1]).pack(side="left", fill=tk.X, expand=True)

        

    def exit_window():
        try:
            window.destroy()
        except Exception as e:
            print(e)

    def fill_fields():
        row = manager.get_one_course(course_id)
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

    window = spawn_window()
    string_var_collection = create_string_var_collection()

    def cb(value):
        if callback:
            callback(value)

    def search():
        fetched_data = manager.search(
            **StringVarCollection.convert_string_var_collection(string_var_collection))
        exit_window()
        cb(fetched_data)

    def add_course():
        all_inputs = StringVarCollection.convert_string_var_collection(
            string_var_collection)
        del all_inputs["id"]
        for value in all_inputs.values():
            if not value:
                messagebox.showerror('Error', 'All fields are required')
                return
        manager.create_course(**all_inputs)
        exit_window()
        cb(None)

    def update():
        manager.update_course(
            **StringVarCollection.convert_string_var_collection(string_var_collection))
        exit_window()
        cb(None)

    def delete():
        manager.delete_course(course_id)
        messagebox.showinfo(
            'Deleted', f'Course {course_id} is deleted successfully.')
        cb(None)

    populate()
    window.mainloop()
    exit_window()