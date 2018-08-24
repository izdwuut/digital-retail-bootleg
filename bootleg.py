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
        config = self.config['cd_key']
        path = config['path']
        pad_x = config['padding_x']
        pad_y = config['padding_y']
        border = config['border']
        bg_color = config['bg_color']

        parent = Frame(self.master)
        cd_key = self.get_cd_key(path)
        text = Text(parent, height=1, width=len(cd_key), bd=border, bg=bg_color, padx=pad_x, pady=pad_y)
        text.pack()
        text.insert(END, cd_key)
        text.config(state=DISABLED)
        parent.place(**self.get_position())

    def get_position(self):
        key = 'cd_key'
        anchor = self.config[key]['anchor']
        position = {}
        if anchor:
            position = self._get_anchor_position(anchor)
        else:
            x = self.config[key]['x']
            y = self.config[key]['y']
            if x:
                position['x'] = int(x)
            if y:
                position['y'] = int(y)
        if not position:
            position = self._get_default_position()
        return position

    def _get_anchor_position(self, anchor):
        positions = {'n': {'anchor': 'n', 'relx': 0.5},
                     's': {'anchor': 's', 'relx': 0.5, 'rely': 1.0},
                     'e': {'anchor': 'e', 'relx': 1.0, 'rely': 0.5},
                     'w': {'anchor': 'w', 'rely': 0.5},
                     'ne': {'anchor': 'ne', 'relx': 1.0, 'rely': 0.5},
                     'se': {'anchor': 'se', 'relx': 1.0, 'rely': 1.0},
                     'sw': {'anchor': 'sw', 'rely': 1.0},
                     'nw': {'anchor': 'nw'},
                     'center': {'anchor': 'center', 'relx': 0.5, 'rely': 0.5}}
        return positions[anchor.lower()]

    def _get_default_position(self):
        return {}

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


if __name__ == "__main__":
    root = Tk()
    root.configure()
    app = Application.with_bg_image(root)
    app.start()
