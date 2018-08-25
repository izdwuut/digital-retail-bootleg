from tkinter import *
from configparser import ConfigParser


class Application(Frame):
    config_path = "config.ini"
    config = ConfigParser()
    config.read(config_path)

    def __init__(self, master=None, bg_image=None):
        super().__init__(master)
        self.bg_image = bg_image

    def start(self):
        self.configure_window()
        self.create_widgets()
        self.mainloop()

    def create_widgets(self):
        self.show_cd_key()

    @staticmethod
    def get_cd_key(filename):
        cd_key = ""
        with open(filename) as f:
            cd_key = f.read()
        return cd_key

    def show_cd_key(self):
        text = self.get_text_widget()
        label = self.get_label()
        self.set_position(text, label)

    def set_position(self, text, label=None):
        config = self.config['cd_key']
        anchor = config['anchor']
        params = {'text': {'widget': text, 'row': 2, 'column': 1, 'stick': W}}
        if label:
            params['label'] = {'widget': label, 'row': 1, 'column': 1, 'stick': W}
        if anchor:
            Config.set_anchor_position(anchor, self.master)
        else:
            Config.set_absolute_position(config['x'], config['y'], self.master)
        for p in params:
            widget = params[p].pop('widget')
            widget.grid(**params[p])

    def get_text_widget(self):
        config = self.config['cd_key']
        path = config['path']
        pad_x = config['padding_x']
        pad_y = config['padding_y']
        border = config['border']
        bg_color = config['bg_color']

        cd_key = self.get_cd_key(path)
        text = Text(self.master, height=1, width=len(cd_key), bd=border, bg=bg_color, padx=pad_x, pady=pad_y)
        text.insert(END, cd_key)
        text.config(state=DISABLED)
        return text

    def get_label(self):
        label = self.config['cd_key']['label']
        if label:
            return Label(self.master, text=label)
        return None

    @classmethod
    def with_bg_image(cls, master=None):
        src = cls.config['bg_image']['path']

        bg_image = PhotoImage(file=src)
        x = Label(image=bg_image)
        x.anchor("center")
        x.place(x=0, y=0, relwidth=1, relheight=1)
        return cls(master, bg_image)

    def configure_window(self):
        config = self.config['title_bar']
        title = config['title']
        icon = config['icon']

        self.center_window()
        self.configure_title_bar(title, icon)
        self.master.resizable(0, 0)
        self.set_window_size()

    def set_window_size(self):
        size = self.get_bg_image_size()
        self.master.minsize(width=size['x'], height=size['y'])

    def configure_title_bar(self, title="", icon=""):
        if title:
            self.show_title(title)
        if icon:
            self.show_icon(icon)

    def show_title(self, title):
        self.master.title(title)

    def get_bg_image_size(self):
        size = {'x': 0, 'y': 0}
        if self.bg_image:
            size['x'] = self.bg_image.width()
            size['y'] = self.bg_image.height()
        return size

    # Thanks to Yagisanatode.com for an article on centering a window :)
    # https://yagisanatode.com/2018/02/24/how-to-center-the-main-window-on-the-screen-in-tkinter-with-python-3/
    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        image_size = self.get_bg_image_size()
        position_right = int((screen_width - image_size['x']) / 2)
        position_down = int((screen_height - image_size['y']) / 2)
        self.master.geometry("+{}+{}".format(position_right, position_down))

    def show_icon(self, path):
        self.master.iconbitmap(path)


class Config:
    @staticmethod
    def set_anchor_position(anchor, parent):
        anchor = anchor.lower()
        if 'n' not in anchor or anchor == 'center':
            parent.grid_rowconfigure(0, weight=1)
        if 's' not in anchor:
            parent.grid_rowconfigure(3, weight=1)
        if 'e' not in anchor or anchor == 'center':
            parent.grid_columnconfigure(2, weight=1)
        if 'w' not in anchor:
            parent.grid_columnconfigure(0, weight=1)

    @staticmethod
    def set_absolute_position(x, y, parent):
        position = {}
        if x:
            # position['padx'] =
            root.grid_columnconfigure(0, minsize=int(x))
        if y:
            # position['pady'] =
            root.grid_rowconfigure(0, minsize=int(y))


if __name__ == "__main__":
    root = Tk()
    root.configure()
    app = Application.with_bg_image(root)
    app.start()
