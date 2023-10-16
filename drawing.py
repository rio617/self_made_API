# 画像ファイルを読み込んで顔検出・瞳検出を行う
import cv2

face_cascade_path ='haarcascades/haarcascade_frontalface_default.xml'
eye_cascade_path = 'haarcascades/haarcascade_eye.xml'

# パスを指定してxmlファイルを読み込む
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# 画像を読み込む
src = cv2.imread("img/kirakira_woman.png")
# カラー画像からグレースケール（白黒）画像への変換
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 読み込んだ検出器のメソッドdetectMultiScale()で顔や瞳（目）などを検出
faces = face_cascade.detectMultiScale(src_gray)

for x, y, w, h in faces:
    # rectangle()で検出した領域の枠を描画
    cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
    face = src[y: y + h, x: x + w]
    face_gray = src_gray[y: y + h, x: x + w]
    eyes = eye_cascade.detectMultiScale(face_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# 処理を実施した画像を保存する
cv2.imwrite("img/kirakira_woman_copy1.jpg", src)