import love_bomb


from tkinter import *
window = Tk()
window.geometry('100x100')
def send():
  love_bomb.mail()
  window.destroy()
btn = Button(window, text = 'Love Bomb!',width='100', height='25',bd = '25', command=send)
btn.pack(side='top')
window.mainloop()