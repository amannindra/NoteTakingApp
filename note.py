from flet import (UserControl, TextField, InputBorder, Page, ControlEvent, app)
import time
import threading

class TextEditor(UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.textfield = TextField(
            multiline=True, autofocus=True, border=InputBorder.NONE, min_lines=40, content_padding=30, cursor_color='yellow')
        self.autosave_thread = threading.Thread(target=self.autosave_loop, daemon=True)
        self.autosave_thread.start()
        
    def autosave_loop(self):
        while True:
            time.sleep(5)  # Wait for 5 seconds
            self.save_text(None)  # Save the text
    def save_text(self, e: ControlEvent) -> None:
        print("test")
        with open('save.txt', 'w') as f:
            f.write(self.textfield.value)

    def read_text(self) -> str | None:
        try:
            with open('save.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            self.textfield.hint_text = 'Welcome to the text editor!'

    def build(self) -> TextField:
        self.textfield.value = self.read_text()
        return self.textfield


def main(page: Page) -> None:
    page.title = 'text editor'
    page.scroll = True
    page.add(TextEditor())


if __name__ == '__main__':
    app(target=main)
