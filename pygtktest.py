from gimpfu import *
import pygtk
import gtk

class PyApp:
    def __init__(self):
        self.Window = gtk.Window()
        self.Window.set_title("TESTING")

        self.label = gtk.Label("A LABEL")

        self.Window.add(self.label)

        self.Window.set_size_request(800,600)
        self.Window.set_title("Title")
        self.label.show()
        #self.Window.connect("delete_event", gtk.main_quit())

        self.Window.show()


def Init(img, drw):
    PyApp()
    gtk.main()

register(
        "ratio_info",
        "Shows a window",
        "Pop Up",
        "Me",
        "me",
        "1999",
        "<Image>/Testing/RatioWindow",
        "*",
        [],
        [],
        Init)

main()


