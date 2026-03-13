import cv2
import mediapipe as mp
import pyautogui as pg
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# ウェブ内蔵カメラのサイズ設定
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
cap.set(cv2.CAP_PROP_FPS, 2)

# 手の認識度の設定
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read()
        image_width, image_height = image.shape[1], image.shape[0]

        if not success:
            print("Ignoring empty camera frame.")
            continue

        # BGR画像をRGBに変換し反転
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # 人差し指の指先(8)と第二関節(6)の座標取得
                index_finger_aip_y = int(hand_landmarks.landmark[8].y * image_height)
                index_finger_bip_y = int(hand_landmarks.landmark[6].y * image_height)

                # 人差し指(第二関節)が人差し指(指先)を上回ったとき作動
                if index_finger_aip_y > index_finger_bip_y:
                    pg.PAUSE = 1.5
                
                    
                    pg.doubleClick(x=640, y=880, interval=2) # 1. PowerPointのアイコン
                    pg.press('enter')
                    pg.doubleClick(x=413, y=294, interval=1) # 2. 新しいプレゼンテーション
                    pg.press('enter')
                    pg.doubleClick(x=193, y=85, interval=1)  # 3. 「挿入」タブ
                    pg.press('enter')
                    pg.click(x=235, y=132, interval=0.5)     # 4. 「画像」ボタン
                    pg.click(x=218, y=262, interval=0.5)     # 5. 「このデバイス」
                    pg.click(x=124, y=348, interval=0.5)     # 6. カメラロール等のフォルダ
                    pg.click(x=357, y=276, interval=0.5)     # 7. 挿入したい画像
                    pg.click(x=691, y=664, interval=0.5)     # 8. 「挿入」決定ボタン
                    
                    pg.alert('終了しました')
                else:
                    pass

        # 内蔵カメラを起動
        cv2.imshow('MediaPipe Hands', image)
        
        # qキーで終了
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
