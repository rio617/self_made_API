import cv2
import os
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np


def imread2Byte(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


def imwrite2Byte(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode="w+b") as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def replace_faces(input_path, replacement_path, output_folder):
    # 画像読み込み
    image = imread2Byte(input_path)
    replacement_image = imread2Byte(replacement_path)

    # Haarcascadesを使用して顔検出器を初期化
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # 顔検出
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    if len(faces) == 0:
        messagebox.showinfo("Info", "顔が検出されませんでした。")
        return

    # 置き換え処理
    for x, y, w, h in faces:
        resized_replacement = cv2.resize(replacement_image, (w, h))
        image[y : y + h, x : x + w] = resized_replacement

    # 出力ファイル名を作成
    output_filename = (
        os.path.splitext(os.path.basename(input_path))[0]
        + "_"
        + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        + ".png"
    )
    output_path = os.path.join(output_folder, output_filename)

    # 画像保存
    imwrite2Byte(output_path, image)

    messagebox.showinfo("Info", "置き換えが完了し、画像が保存されました。")


def select_image(title):
    file_path = filedialog.askopenfilename(
        title=title, filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    return file_path


def main():
    root = tk.Tk()
    root.withdraw()  # ルートウィンドウを非表示にする

    input_image_path = select_image("変換したい画像を選択")
    if not input_image_path:
        return

    replacement_image_path = select_image("顔を隠す画像を選択")
    if not replacement_image_path:
        return

    output_folder = os.path.dirname(input_image_path)

    replace_faces(input_image_path, replacement_image_path, output_folder)


if __name__ == "__main__":
    main()
