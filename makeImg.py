import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time

def capture_full_page_screenshot_fixed_height(driver, file_path, window_width, window_height):
    # 固定のウィンドウサイズを設定
    driver.set_window_size(window_width, window_height)

    # スクリーンショットを取得して保存
    driver.save_screenshot(file_path)

# 現在のスクリプトのディレクトリを取得
current_directory = os.path.dirname(os.path.abspath(__file__))

# Chromedriverのパス
chromedriver_path = os.path.join(current_directory, 'chromedriver.exe')

# Chromedriverを起動
service = ChromeService(executable_path=chromedriver_path)
chrome_options = Options()
chrome_options.add_argument('--headless')  # ヘッドレスモードで起動（画面を表示しない）
driver = webdriver.Chrome(service=service, options=chrome_options)

# 固定のウィンドウサイズ
window_width = 1000
window_height = 2580

# スクリプトのディレクトリ内のすべてのMHTMLファイルを処理
for filename in os.listdir(current_directory):
    if filename.endswith('.mhtml'):
        mhtml_file_path = os.path.join(current_directory, filename)

        # 画像ファイルのパスを生成
        image_file_path = os.path.splitext(mhtml_file_path)[0] + '.png'

        # MHTMLファイルを開く
        driver.get('file:///' + mhtml_file_path.replace('\\', '/'))

        # ページが読み込まれるまで待機
        time.sleep(2)

        # 固定サイズの全体スクリーンショットを取得
        capture_full_page_screenshot_fixed_height(driver, image_file_path, window_width, window_height)

        print(f"Conversion complete. Image saved at: {image_file_path}")

# WebDriverを終了
driver.quit()
