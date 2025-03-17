import cv2

vc = cv2.VideoCapture('02_Video/00_Scenery.mp4')

# 检查是否打开正确

if vc.isOpened():
    open_, frame = vc.read()
else:
    open_ = False

while open_:
    ret, frame = vc.read()
    if frame is None:
        break

    if ret:  # 将每帧是视频都转为灰度图
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)

        # 这里的waitKey越小，视频播放的就越快
        # 意思是每灰度渲染完一帧后等待的时间
        if cv2.waitKey(10) & 0xFF == 27:  # 0xFF == 27 的意思是按Esc就退出循环(Esc的ASCII码就是27)
            break
vc.release()
cv2.destroyAllWindows()
