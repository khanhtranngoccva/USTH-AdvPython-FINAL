import tkinter

class Textbox(tkinter.Text):
    def __init__(self, parent=None, *args, textvariable: tkinter.StringVar=None, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._textvariable = textvariable
        self._refresh()
        self._textvariable.trace_add("write", self._refresh)
        self.bind("<KeyRelease>", lambda _: self._update())

    def _update(self):
        self._textvariable.set(self.get("1.0", "end"))

    def _refresh(self, *args):
        last_index = self.index("insert")
        self.delete("1.0", tkinter.END)
        self.insert(tkinter.END, self._textvariable.get())
        self.mark_set("insert", last_index)

if __name__ == "__main__":
    Textbox()