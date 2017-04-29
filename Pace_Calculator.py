from tkinter import *

top = Tk()
top.title("Pace Calculator")

minute_per_kilometer = 1.609344

L1 = Label(top, text="minutes")
L1.grid(row=0, column=0)

E1 = Entry(top, bd=5)
E1.grid(row=1, column=0)


L2 = Label(top, text=" seconds")
L2.grid(row=2, column=0)

E2 = Entry(top, bd=5)
E2.grid(row=3, column=0)


def get_minutes
    print(minutes)
    minutes_to_sec = int(minutes) * 60
    print(minutes_to_sec)
    seconds = E2.get()
    seconds = int(seconds)
    pace_in_seconds = (minutes_to_sec + seconds) * minute_per_kilometer
    pace_in_seconds = int(pace_in_seconds)
    m, s = divmod(pace_in_seconds, 60)
    E3.insert(0, '{}:{}'.format(m, s))

    print(seconds)


def reset():
    E3.delete(0, 'end')


B1 = Button(top, text="Enter", command=get_minutes)
B1.grid(row=4, column=0)

B2 = Button(top, text="Reset", command=reset)
B2.grid(row=4, column=1)

L3 = Label(top, text="min/mile pace")
L3.grid(row=5, column=0)

E3 = Entry(top, bd=5)
E3.grid(row=6, column=0)


top.mainloop()
