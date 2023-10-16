import cv2
import tkinter as tk

# モザイク処理を行う関数
def face_mosaic(src,ratio=0.05):
    # 画像を10分の1のサイズに縮小    (INTER_NEAREST – 最近傍補間)最近傍補間法では、「追加したい画素」を「その画素に一番近い画素と同じ」と仮定して画素を補う補間法
    f_small = cv2.resize(src[y: y + h, x: x + w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    # 縮小された画像を元の大きさに戻す
    src[y: y + h, x: x + w] = cv2.resize(f_small, (w, h), interpolation=cv2.INTER_NEAREST)
    feces=src[y: y + h, x: x + w]
    return feces


# 画像ファイルを読み込んで顔検出・瞳検出を行う
face_cascade_path ="haarcascades/haarcascade_frontalface_default.xml"
facesmile_cascade_path ="haarcascades/haarcascade_smile.xml"
eye_cascade_path = "haarcascades/haarcascade_eye.xml"

# パスを指定してxmlファイルを読み込む
face_cascade = cv2.CascadeClassifier(face_cascade_path)
facesmile_cascade = cv2.CascadeClassifier(facesmile_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# 画像を読み込む
src = cv2.imread("img/kirakira_woman.png")
# カラー画像からグレースケール（白黒）画像への変換
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 読み込んだ検出器のメソッドdetectMultiScale()で顔や瞳（目）などを検出
faces = face_cascade.detectMultiScale(src_gray)

# モザイクの割合の設定
ratio = 0.05

# 顔
for x, y, w, h in faces:
    # # 画像を10分の1のサイズに縮小    (INTER_NEAREST – 最近傍補間)最近傍補間法では、「追加したい画素」を「その画素に一番近い画素と同じ」と仮定して画素を補う補間法
    # f_small = cv2.resize(src[y: y + h, x: x + w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    # # 縮小された画像を元の大きさに戻す
    # src[y: y + h, x: x + w] = cv2.resize(f_small, (w, h), interpolation=cv2.INTER_NEAREST)

# 目
# 読み込んだ検出器のメソッドdetectMultiScale()で顔や瞳（目）などを検出
eyes = eye_cascade.detectMultiScale(src_gray)
for (ex, ey, ew, eh) in eyes:
    # 画像を10分の1のサイズに縮小    (INTER_NEAREST – 最近傍補間)最近傍補間法では、「追加したい画素」を「その画素に一番近い画素と同じ」と仮定して画素を補う補間法
    e_small = cv2.resize(src[ey: ey + eh, ex: ex + ew], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    # 縮小された画像を元の大きさに戻す
    src[ey: ey + eh, ex: ex + ew] = cv2.resize(e_small, (ew, eh), interpolation=cv2.INTER_NEAREST)

# 笑顔
# 読み込んだ検出器のメソッドdetectMultiScale()で顔や瞳（目）などを検出
smile = facesmile_cascade.detectMultiScale(src_gray)
for (sx, sy, sw, sh) in smile:
    # 画像を10分の1のサイズに縮小    (INTER_NEAREST – 最近傍補間)最近傍補間法では、「追加したい画素」を「その画素に一番近い画素と同じ」と仮定して画素を補う補間法
    s_small = cv2.resize(src[sy: sy + sh, sx: sx + sw], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    # 縮小された画像を元の大きさに戻す
    src[sy: sy + sh, sx: sx + sw] = cv2.resize(s_small, (sw, sh), interpolation=cv2.INTER_NEAREST)

# 処理を実施した画像を保存する
cv2.imwrite("img/kirakira_woman_mosaic1.png", src)