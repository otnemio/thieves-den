import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class GSTApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        builder = Gtk.Builder.new_from_file('github/thieves-den/gtk_builder.ui')
        self.win = builder.get_object('GSTDash')
        self.win.present()
        app.add_window(self.win)

app = GSTApp(application_id="com.github.otnemio.GSTDash")
app.run(sys.argv)