import cv2
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import numpy as np

select_img = None


# 顔隠し
def imread2Byte(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


def replace_faces(select_img):
    # 画像読み込み
    src = imread2Byte(select_img)

    # 画像ファイルを読み込んで顔検出・瞳検出を行う
    face_cascade_path = "haarcascades/haarcascade_frontalface_default.xml"
    # パスを指定してxmlファイルを読み込む
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    # 読み込んだ検出器のメソッドdetectMultiScale()で顔や瞳（目）などを検出
    faces = face_cascade.detectMultiScale(src_gray)

    # 顔検出
    # カラー画像からグレースケール（白黒）画像への変換
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        src_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    if len(faces) == 0:
        messagebox.showinfo("Info", "顔が検出されませんでした。")
        return

    # 置き換え処理
    for x, y, w, h in faces:
        resized_replacement = cv2.resize(src, (w, h))
        src[y : y + h, x : x + w] = resized_replacement

    # ファイル名を付けて保存
    filename = filedialog.asksaveasfilename(
        title="ファイル名を付けて画像を保存",
        filetypes=[
            ("PNG", ".png"),
            ("JPEG", ".jpg"),
        ],
        initialdir="./",
        defaultextension="",
    )

    # 画像保存
    cv2.imwrite(filename, src)
    return filename

    messagebox.showinfo("Info", "置き換えが完了し、画像が保存されました。")


# 顔を検出してモザイク処理
def face_mosaic(ratio=0.05):
    # 画像を読み込む
    src = cv2.imread(select_img)
    # カラー画像からグレースケール（白黒）画像への変換
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # 画像ファイルを読み込んで顔検出・瞳検出を行う
    face_cascade_path = "haarcascades/haarcascade_frontalface_default.xml"
    # パスを指定してxmlファイルを読み込む
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    # 読み込んだ検出器のメソッドdetectMultiScale()で顔や瞳（目）などを検出
    faces = face_cascade.detectMultiScale(src_gray)
    for x, y, w, h in faces:
        # 画像を10分の1のサイズに縮小 (INTER_NEAREST – 最近傍補間)最近傍補間法では、「追加したい画素」を「その画素に一番近い画素と同じ」と仮定して画素を補う補間法
        f_small = cv2.resize(
            src[y : y + h, x : x + w],
            None,
            fx=ratio,
            fy=ratio,
            interpolation=cv2.INTER_NEAREST,
        )
        # 縮小された画像を元の大きさに戻す
        src[y : y + h, x : x + w] = cv2.resize(
            f_small, (w, h), interpolation=cv2.INTER_NEAREST
        )

    # ファイル名を付けて保存
    # filename = simpledialog.askstring("入力案", "入力欄")
    filename = filedialog.asksaveasfilename(
        title="ファイル名を付けて画像を保存",
        filetypes=[
            ("PNG", ".png"),
            ("JPEG", ".jpg"),
        ],
        initialdir="./",
        defaultextension="",
    )

    # 画像を保存
    cv2.imwrite(filename, src)
    return filename


# 瞳を検出してモザイク処理
def eye_mosaic(ratio=0.05):
    # 画像を読み込む
    src = cv2.imread(select_img)
    # カラー画像からグレースケール（白黒）画像への変換
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # 画像ファイルを読み込んで顔検出・瞳検出を行う
    eye_cascade_path = "haarcascades/haarcascade_eye.xml"
    # パスを指定してxmlファイルを読み込む
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
    # 読み込んだ検出器のメソッドdetectMultiScale()で顔や瞳（目）などを検出
    eyes = eye_cascade.detectMultiScale(src_gray)
    for ex, ey, ew, eh in eyes:
        # 画像を10分の1のサイズに縮小    (INTER_NEAREST – 最近傍補間)最近傍補間法では、「追加したい画素」を「その画素に一番近い画素と同じ」と仮定して画素を補う補間法
        e_small = cv2.resize(
            src[ey : ey + eh, ex : ex + ew],
            None,
            fx=ratio,
            fy=ratio,
            interpolation=cv2.INTER_NEAREST,
        )
        # 縮小された画像を元の大きさに戻す
        src[ey : ey + eh, ex : ex + ew] = cv2.resize(
            e_small, (ew, eh), interpolation=cv2.INTER_NEAREST
        )

    # ファイル名を付けて保存
    filename = filedialog.asksaveasfilename(
        title="ファイル名を付けて画像を保存",
        filetypes=[
            ("PNG", ".png"),
            ("JPEG", ".jpg"),
        ],
        initialdir="./",
        defaultextension="",
    )

    # 画像を保存
    cv2.imwrite(filename, src)
    return filename


# 笑顔を検出してモザイク処理
def smile_mosaic(ratio=0.05):
    # 画像を読み込む
    src = cv2.imread(select_img)
    # カラー画像からグレースケール（白黒）画像への変換
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # 画像ファイルを読み込んで顔検出・瞳検出を行う
    facesmile_cascade_path = "haarcascades/haarcascade_smile.xml"
    # パスを指定してxmlファイルを読み込む
    facesmile_cascade = cv2.CascadeClassifier(facesmile_cascade_path)

    # 読み込んだ検出器のメソッドdetectMultiScale()で顔や瞳（目）などを検出
    smile = facesmile_cascade.detectMultiScale(src_gray)
    for sx, sy, sw, sh in smile:
        # 画像を10分の1のサイズに縮小    (INTER_NEAREST – 最近傍補間)最近傍補間法では、「追加したい画素」を「その画素に一番近い画素と同じ」と仮定して画素を補う補間法
        s_small = cv2.resize(
            src[sy : sy + sh, sx : sx + sw],
            None,
            fx=ratio,
            fy=ratio,
            interpolation=cv2.INTER_NEAREST,
        )
        # 縮小された画像を元の大きさに戻す
        src[sy : sy + sh, sx : sx + sw] = cv2.resize(
            s_small, (sw, sh), interpolation=cv2.INTER_NEAREST
        )

    # ファイル名を付けて保存
    filename = filedialog.asksaveasfilename(
        title="ファイル名を付けて画像を保存",
        filetypes=[
            ("PNG", ".png"),
            ("JPEG", ".jpg"),
        ],
        initialdir="./",
        defaultextension="",
    )

    # 画像を保存
    cv2.imwrite(filename, src)
    return filename


# モザイク処理を行う関数
# def mosaic(src, ratio=0.05):
#     # 画像を10分の1のサイズに縮小    (INTER_NEAREST – 最近傍補間)最近傍補間法では、「追加したい画素」を「その画素に一番近い画素と同じ」と仮定して画素を補う補間法
#     f_small = cv2.resize(
#         src[y : y + h, x : x + w],
#         None,
#         fx=ratio,
#         fy=ratio,
#         interpolation=cv2.INTER_NEAREST,
#     )
#     # 縮小された画像を元の大きさに戻す
#     src[y : y + h, x : x + w] = cv2.resize(
#         f_small, (w, h), interpolation=cv2.INTER_NEAREST
#     )
#     feces = src[y : y + h, x : x + w]
#     return feces


# 画像ファイルを読み込んで顔検出・瞳検出を行う
# face_cascade_path ="haarcascades/haarcascade_frontalface_default.xml"
# facesmile_cascade_path ="haarcascades/haarcascade_smile.xml"
# eye_cascade_path = "haarcascades/haarcascade_eye.xml"

# パスを指定してxmlファイルを読み込む
# face_cascade = cv2.CascadeClassifier(face_cascade_path)
# facesmile_cascade = cv2.CascadeClassifier(facesmile_cascade_path)
# eye_cascade = cv2.CascadeClassifier(eye_cascade_path)


# 読み込んだ検出器のメソッドdetectMultiScale()で顔や瞳（目）などを検出
# faces = face_cascade.detectMultiScale(src_gray)


# 顔
# for x, y, w, h in faces:
# # 画像を10分の1のサイズに縮小    (INTER_NEAREST – 最近傍補間)最近傍補間法では、「追加したい画素」を「その画素に一番近い画素と同じ」と仮定して画素を補う補間法
# f_small = cv2.resize(src[y: y + h, x: x + w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
# # 縮小された画像を元の大きさに戻す
# src[y: y + h, x: x + w] = cv2.resize(f_small, (w, h), interpolation=cv2.INTER_NEAREST)

# 目
# 読み込んだ検出器のメソッドdetectMultiScale()で顔や瞳（目）などを検出
# eyes = eye_cascade.detectMultiScale(src_gray)
# for (ex, ey, ew, eh) in eyes:
#     # 画像を10分の1のサイズに縮小    (INTER_NEAREST – 最近傍補間)最近傍補間法では、「追加したい画素」を「その画素に一番近い画素と同じ」と仮定して画素を補う補間法
#     e_small = cv2.resize(src[ey: ey + eh, ex: ex + ew], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
#     # 縮小された画像を元の大きさに戻す
#     src[ey: ey + eh, ex: ex + ew] = cv2.resize(e_small, (ew, eh), interpolation=cv2.INTER_NEAREST)

# 笑顔
# 読み込んだ検出器のメソッドdetectMultiScale()で顔や瞳（目）などを検出
# smile = facesmile_cascade.detectMultiScale(src_gray)
# for sx, sy, sw, sh in smile:
#     # 画像を10分の1のサイズに縮小    (INTER_NEAREST – 最近傍補間)最近傍補間法では、「追加したい画素」を「その画素に一番近い画素と同じ」と仮定して画素を補う補間法
#     s_small = cv2.resize(
#         src[sy : sy + sh, sx : sx + sw],
#         None,
#         fx=ratio,
#         fy=ratio,
#         interpolation=cv2.INTER_NEAREST,
#     )
#     # 縮小された画像を元の大きさに戻す
#     src[sy : sy + sh, sx : sx + sw] = cv2.resize(
#         s_small, (sw, sh), interpolation=cv2.INTER_NEAREST
#     )

# 処理を実施した画像を保存する
# cv2.imwrite("img/kirakira_woman_mosaic1.png", src)
