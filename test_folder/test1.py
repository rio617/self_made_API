import cv2

# 画像の読み込み
img=cv2.imread("img/kirakira_woman.png")

# モザイク処理を行う関数
def mosaic(img, ratio):
   # いったん画像を10分の1のサイズに縮小    (INTER_NEAREST – 最近傍補間)最近傍補間法では、「追加したい画素」を「その画素に一番近い画素と同じ」と仮定して画素を補う補間法
   small = cv2.resize(img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
   # 縮小された画像を元の大きさに戻し、mosaic関数の戻り値を返す仕組み
   return cv2.resize(small, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

# 画面への画像の出力
cv2.imshow("img/kirakira_woman.png", mosaic(img, ratio=0.1))
# 画像を表示し続ける
cv2.waitKey()