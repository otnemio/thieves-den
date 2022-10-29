import sys
import gi
import yaml, os, common

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(800, 600)
        self.set_title("GST Dash")

        # Main layout containers
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_child(self.box1)  # Horizontal box to window
        self.box1.append(self.box2)  # Put vert box in that box
        self.box1.append(self.box3)  # And another one, empty for now

        
        for g in common.readConfig('gst'):
            for i in g:
                self.button = Gtk.Button(label=i)
                self.button.connect('clicked', self.hello)
                self.box2.append(self.button)  # But button in the first of the two vertical boxes

        # Add a check button
        self.check = Gtk.CheckButton(label="And goodbye?")
        self.box2.append(self.check)

        # Add a box containing a switch and label
        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.switch_box.set_spacing(5)

        self.switch = Gtk.Switch()
        self.switch.set_active(True)  # Let's default it to on
        self.switch.connect("state-set", self.switch_switched)  # Lets trigger a function on state change

        self.label = Gtk.Label(label="A switch")

        self.switch_box.append(self.switch)
        self.switch_box.append(self.label)
        self.box2.append(self.switch_box)

        self.scrldwin = Gtk.ScrolledWindow(hexpand=True,vexpand=True)
    
        self.lstbox = Gtk.ListBox()
        self.scrldwin.set_child(self.lstbox)
        for i in range(100):
            self.label = Gtk.Label(label=i)
            self.lstbox.append(self.label)
        self.box3.append(self.scrldwin)

    def switch_switched(self, switch, state):
        print(f"The switch has been switched {'on' if state else 'off'}")

    def hello(self, button):
        print(f"Hello world {button.get_label()}")
        if self.check.get_active():
            print("Goodbye world!")
            self.close()


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = MyApp(application_id="com.github.otnemio.GSTDash")
app.run(sys.argv)