import tkinter
import json

class Textbox(tkinter.Text):
    def __init__(self, parent=None, *args, textvariable: tkinter.StringVar=None, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._textvariable = textvariable
        self._refresh()
        self._textvariable.trace_add("write", self._refresh)
        self.bind("<KeyRelease>", lambda _: self._update())

    def _update(self):
        data = self.get("0.0", tkinter.END+"-1c") # Newline removal
        self._textvariable.set(data)

    def _refresh(self, *args):
        last_index = self.index("insert")
        self.delete("0.0", tkinter.END)
        self.insert(tkinter.END, self._textvariable.get())
        self.mark_set("insert", last_index)

if __name__ == "__main__":
    Textbox()