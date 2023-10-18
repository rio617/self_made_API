import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import mosaic
import mosaiccopy


# 画像選択
def image_select():
    img_path = filedialog.askopenfilename(
        title="画像を選択",
        initialdir="\Downloads",
        filetypes=[("Image File", "*.png;*.jpg")],
    )

    mosaic.select_img = img_path
    change_image(img_path)


# 画像読み込み・画像変更
def change_image(img_path):
    global label
    # Pillowで画像読み込み
    pil_img = Image.open(img_path)
    w = pil_img.width  # 画像の横幅を取得
    h = pil_img.height  # 画像の縦幅を取得
    # 読み込んだ画像を半分にする
    pil_img = pil_img.resize((int(w / 2), int(h / 2)))
    # Pillowで読み込んだ画像をtkinterで使えるように変換
    tk_img = ImageTk.PhotoImage(pil_img)
    # ラベルウィジェットの画像変更
    label.configure(image=tk_img)
    label.image = tk_img


# 顔　モザイク処理後　画面に出す
def push_face_mosaic():
    mosaic_path = mosaic.face_mosaic()
    print(mosaic_path)
    change_image(mosaic_path)


# 目　モザイク処理後　画面に出す
def push_eye_mosaic():
    mosaic_path = mosaic.eye_mosaic()
    print(mosaic_path)
    change_image(mosaic_path)


# 笑顔　モザイク処理後　画面に出す
def push_smile_mosaic():
    mosaic_path = mosaic.smile_mosaic()
    print(mosaic_path)
    change_image(mosaic_path)


# 顔隠し
def push_replace_face():
    replace_path = mosaiccopy.replace_faces()
    print(replace_path)


# tkinterでウィンドウ用意
root = tk.Tk()
root.geometry("750x750")

title = tk.Label(text="画像にモザイクをかけるアプリ", font=60)
title.pack()

# フレーム作成
entry_frame = tk.Frame(root)
button_frame = tk.Frame(root)
image_frame = tk.Frame(root)
image_frame.pack()


# ファイル選択欄
entry = tk.Entry(entry_frame)
entry_button = tk.Button(entry_frame, text="画像を選択", command=image_select)

# 画面表示
entry_frame.pack()
entry.grid(row=0, column=0)
entry_button.grid(row=0, column=1)

# 各種ボタン
face_button = tk.Button(button_frame, text="顔をモザイク", font=30, command=push_face_mosaic)
eye_button = tk.Button(button_frame, text="瞳をモザイク", font=30, command=push_eye_mosaic)
smile_button = tk.Button(
    button_frame, text="笑顔をモザイク", font=30, command=push_smile_mosaic
)
replace_button = tk.Button(button_frame, text="顔隠し", font=30, command=push_replace_face)

# 画面表示
button_frame.pack(pady=20)
face_button.grid(row=0, column=0)
eye_button.grid(row=0, column=1)
smile_button.grid(row=0, column=2)
replace_button.grid(row=0, column=3)

# tkinterでラベル用意、画面表示
label = tk.Label(image_frame)
label.pack()

root.mainloop()
