import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib


class NotificationServer(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName(
            "org.freedesktop.Notifications", bus=dbus.SessionBus()
        )
        dbus.service.Object.__init__(self, bus_name, "/org/freedesktop/Notifications")

    @dbus.service.method(
        "org.freedesktop.Notifications", in_signature="susssasa{ss}i", out_signature="u"
    )
    def Notify(
        self, app_name, replaces_id, app_icon, summary, body, actions, hints, timeout
    ):
        print("Recieved Notification")
        print("\t App Name:", app_name)
        print("\t Replace ID:", replaces_id)
        print("\t App Icon:", app_icon)
        print("\t summary:", summary)
        print("\t Body:", body)
        print("\t Actions:", actions)
        print("\t Hints:", hints)
        print("\t Timeout:", timeout)
        return 0

    @dbus.service.method("org.freedesktop.Notifications", out_signature="ssss")
    def GetServerInformation(self):
        return ("Custome Notification Server", "ExampleNS", "1.0", "1.2")


DBusGMainLoop(set_as_default=True)

if __name__ == "__main__":
    server = NotificationServer()
    mainloop = GLib.MainLoop()
    mainloop.run()
