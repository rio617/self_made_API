import cv2

# モザイク処理の定義
def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

# モザイク処理の実施
def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst


# OpenCVによるメイン処理
# 画像を読み込む
# 画像に前処理を実施する
# 「顔と思われる部分」を検出する
# 検出した範囲に対してモザイク処理を実施する
# 処理を実施した画像を保存する
def submit_cv():
    # 画像の読み込み
    src = cv2.imread("img/image_processing20200630-1-1rehjtn.jpg")
    
    face_cascade_path ="haarcascades/haarcascade_frontalface_default.xml"
    eye_cascade_path ="haarcascades/haarcascade_eye.xml"
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # 読み込んだ検出器のメソッドdetectMultiScale()で顔や瞳（目）などを検出
    faces = face_cascade.detectMultiScale(src_gray)
    eyes = eye_cascade.detectMultiScale(src_gray)

    for x, y, w, h in faces:
        dst_face = mosaic_area(src, x, y, w, h)
        for x, y, w, h in eyes:
            dst_eyes = mosaic_area(src, x, y, w, h)

    if len(faces) > 0:
        cv2.imwrite("img/kirakira_woman4.png", dst_face)
    elif len(eyes) > 0:
        cv2.imwrite("img/kirakira_woman4.png", dst_eyes)
    else:
        cv2.imwrite("img/kirakira_woman4.png")

# 画面への画像の出力
# cv2.imshow("img/kirakira_woman.png", mosaic(img, ratio=0.1))
submit_cv()
# 画像を表示し続ける
cv2.waitKey()