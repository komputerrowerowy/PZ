from kivy.app import App
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.core.window import Window
from jnius import autoclass
import sqlite3
import sys


class ZoneList():

    ListaNazw = []
    ListaId = []


    activity = autoclass("org.renpy.android.PythonActivity").mActivity
    Grupy = autoclass("android.provider.ContactsContract$Groups")
    content_resolver = activity.getApplicationContext()
    resolver = content_resolver.getContentResolver()

    grupa = resolver.query(Grupy.CONTENT_URI, None, None, None, None)
    group = grupa

    ListaNazw.append("Numery spoza grup*")
    ListaId.append('999')

    while (grupa.moveToNext()):

        g = group.getString(group.getColumnIndex("TITLE"))
        id = group.getString(group.getColumnIndex("_id"))

        if g not in ListaNazw:
            ListaNazw.append(g)
            ListaId.append(id)

    grupa.close()

    conn = sqlite3.connect('baza.db')
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS Grupy (ID_GRUPY INTEGER, REAKCJA INTEGER)")
    c.execute("SELECT * FROM Grupy")
    baza = c.fetchall()

    if baza == []:
        for x in xrange(0, len(ListaNazw)):
            c.execute("INSERT INTO Grupy VALUES (?, ?)", (ListaId[x], 0))

    else:
        c.execute("SELECT ID_GRUPY FROM Grupy")
        idBaza = c.fetchall()
        c.execute("SELECT REAKCJA FROM Grupy")
        reakcjaBaza = c.fetchall()
        c.execute("DELETE FROM Grupy")

        for x in ListaId:
            c.execute("INSERT INTO Grupy VALUES (?, ?)", (x, 0))

            if unicode(x) in unicode(idBaza):
                for y in xrange(0, len(idBaza)):
                    if "("+x+",)" == str(idBaza[y]):
                        if str(reakcjaBaza[y]) == "(1,)":
                            c.execute("UPDATE Grupy SET REAKCJA=? WHERE ID_GRUPY=?", (1, x))
                            break


    conn.commit()
    conn.close()


class ZoneElements(GridLayout):
    pass


class ZoneCheckBoxes(GridLayout):
    _instance_count = -1
    _zoneNames = ZoneList.ListaNazw
    
    Window.clearcolor = (1, 1, 1, 1)
    
    def __init__(self, **kwargs):
        super(ZoneCheckBoxes, self).__init__(**kwargs)
        ZoneCheckBoxes._instance_count += 1

        conn = sqlite3.connect('baza.db')
        c = conn.cursor()

        c.execute("SELECT REAKCJA FROM Grupy")
        dane = c.fetchall()

        if dane[ZoneCheckBoxes._instance_count] == (0,):
            ZoneCheckBoxes.odrzuc = True
            ZoneCheckBoxes.decyduj = False

        elif dane[ZoneCheckBoxes._instance_count] == (1,):
            ZoneCheckBoxes.odrzuc = False
            ZoneCheckBoxes.decyduj = True

        conn.commit()
        conn.close()

    def odrzucenie(self, x):

        conn = sqlite3.connect('baza.db')
        c = conn.cursor()
        for i in range(0, len(ZoneList.ListaNazw)):
            if ZoneList.ListaNazw[i] == x[5:len(x)]:
                c.execute("UPDATE Grupy SET REAKCJA=? WHERE ID_GRUPY=?", (0, ZoneList.ListaId[i]))

        conn.commit()
        conn.close()

    def decyzja(self, x):

        conn = sqlite3.connect('baza.db')
        c = conn.cursor()
        for i in range(0, len(ZoneList.ListaNazw)):
            if ZoneList.ListaNazw[i] == x[5:len(x)]:
                c.execute("UPDATE Grupy SET REAKCJA=? WHERE ID_GRUPY=?", (1, ZoneList.ListaId[i]))

        conn.commit()
        conn.close()


class ZoneButton(Button):
    _instance_count = -1
    _zoneNames = ZoneList.ListaNazw
    
    def __init__(self, **kwargs):
        super(ZoneButton, self).__init__(**kwargs)
        ZoneButton._instance_count += 1


class ZoneLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ZoneLayout, self).__init__(**kwargs)

        for i in range(len(ZoneList.ListaNazw)):
            self.add_widget(ZoneElements())


class Grupy(App):
    pass


def main():
    Grupy().run()
    
    return 0

if __name__ == '__main__':
    main()
