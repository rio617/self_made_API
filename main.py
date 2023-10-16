import tkinter as tk
from PIL import Image,ImageTk

root=tk.Tk()
root.geometry("650x650")

# フレーム作成
entry_frame=tk.Frame(root)
button_frame=tk.Frame(root)

# ファイル選択欄
entry=tk.Entry(entry_frame)
entry_button=tk.Button(entry_frame,text="ボタン")

# 画面表示
entry_frame.pack()
entry.grid(row=0,column=0)
entry_button.grid(row=0,column=1)

# 各種ボタン
face_button=tk.Button(button_frame,text="顔",font=30)
eye_button=tk.Button(button_frame,text="目",font=30)
smile_button=tk.Button(button_frame,text="笑顔",font=30)

# 画面表示
button_frame.pack()
face_button.grid(row=0,column=0)
eye_button.grid(row=0,column=1)
smile_button.grid(row=0,column=2)

# 1. Pillowで画像読み込み**
# 2. Pillowで読み込んだ画像をtkinterで使えるように変換**
pil_img = Image.open("image.png")
tk_img = ImageTk.PhotoImage(pil_img)


root.mainloop()