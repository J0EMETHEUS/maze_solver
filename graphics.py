from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # create root widget and set the root's title property
        self.__root = Tk()
        self.__root.title("Maze Solver")

        # https://tkinter-docs.readthedocs.io/en/latest/widgets/canvas.html#
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        # https://docs.python.org/3/library/tkinter.html#the-packer
        self.__canvas.pack(fill=BOTH, expand=1)
        
        self.__running = False

        # https://wiki.tcl-lang.org/page/wm+protocol
        # https://tkdocs.com/tutorial/windows.html
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False