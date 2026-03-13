import pyautogui as pag
import time

print("3秒後にマウスの座標を取得します。")
print("調べたい場所にマウスを移動させて、そのまま待機してください...")
time.sleep(3)

m_posi_x, m_posi_y = pag.position()
print('現在のマウスカーソル位置 x:', m_posi_x)
print('現在のマウスカーソル位置 y:', m_posi_y)

