import sys
from PyQt5.QtCore import QUrl, QTimer, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
import pyautogui
import pyperclip
import time
import random

class BrowserTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.browser = QWebEngineView()


        self.browser.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)

    def set_url(self, url):
        self.browser.setUrl(QUrl(url))
        self.browser.loadFinished.connect(self.on_load_finished)


    # ----------------------------------------------------------------------------------------------

    def find_coord_and_click(self, selector, button_type):

        self.button_type = button_type

        print(selector)

        self.browser.page().runJavaScript("""
                                    function getTagCoordinates() {
                                            const element = document.querySelector('""" + selector + """');
                                            const rect = element.getBoundingClientRect();
    
                                            const centerX = rect.left + rect.width / 2;
                                            const centerY = rect.top + rect.height / 2;
                                    
                                            return [centerX, centerY];
                                        }

                                    getTagCoordinates();
                                    """, self.move_cursor_to_coord)

    def move_cursor_to_coord(self, coords):
        print(coords,'\n')

        if coords:
            x, y = coords
            widget_coordinates = self.browser.mapToGlobal(QPoint(int(x), int(y)))

            if self.button_type is None:
                pyautogui.move(widget_coordinates.x(), widget_coordinates.y() )

            elif self.button_type == 'move_left': # radio buttonlar için bunu kullan
                pyautogui.click(widget_coordinates.x() + 30, widget_coordinates.y(), button='left')

            else:
                pyautogui.click(widget_coordinates.x(), widget_coordinates.y(), button=self.button_type)

    # ----------------------------------------------------------------------------------------------


    def on_load_finished(self, ok):
        if ok:

            # QTimer.singleShot(5000, self.auto_click_button)
            QTimer.singleShot(1000, self.auto_click_button)

    def auto_click_button(self):

        # pyautogui.click(x=429, y=468, button='left')
        self.find_coord_and_click( selector = '#username' , button_type='left')


        QTimer.singleShot(1000, self.paste_email)

    def paste_email(self):

        email_address = 'scriptbullet@gmail.com'
        pyperclip.copy(email_address)


        pyautogui.hotkey('ctrl', 'v')
        time.sleep(10)


        QTimer.singleShot(1000, self.submit_form)

    def submit_form(self):

        # pyautogui.click(x=488, y=530, button='left')
        self.find_coord_and_click(selector='.Button-sc-qlcn5g-0.cKYEKO', button_type='left')

        # QTimer.singleShot(5000, self.enter_second_page)
        QTimer.singleShot(1000, self.enter_second_page)

    def enter_second_page(self):

        # pyautogui.click(x=409, y=359, button='left')
        self.find_coord_and_click(selector='#new-password', button_type='left')


        # QTimer.singleShot(5000, self.paste_message)
        QTimer.singleShot(1000, self.paste_message)

    def paste_message(self):

        message = '1234567890' # password
        pyperclip.copy(message)

        pyautogui.hotkey('ctrl', 'v')




        # QTimer.singleShot(5000, self.click_send_button)
        QTimer.singleShot(1000, self.click_send_button)

    def click_send_button(self):

        self.find_coord_and_click(selector='.Button-sc-qlcn5g-0.cKYEKO', button_type='left')
        # pyautogui.click(x=500, y=483, button='left')

        QTimer.singleShot(1000, self.click_username)


    def click_username(self):
        # pyautogui.click(x=474, y=372, button='left')
        self.find_coord_and_click(selector='#displayName', button_type='left')

        # QTimer.singleShot(3000, self.username_sender)
        QTimer.singleShot(1000, self.username_sender)
    def username_sender(self):

        message = 'SCRIPTBULLET'
        pyperclip.copy(message)

        pyautogui.hotkey('ctrl', 'v')


        # QTimer.singleShot(3000, self.day_sender_ankara)
        QTimer.singleShot(1000, self.day_sender_ankara)


    def day_sender_ankara(self):

        # pyautogui.click(x=354, y=493, button='left')
        self.find_coord_and_click(selector='#day', button_type='left')

        QTimer.singleShot(1000, self.input_day)


    def input_day(self):
        day_sayi = random.randint(1, 29)
        day_sayi_str = str(day_sayi)

        # pyperclip.copy(day_sayi_str)
        # pyautogui.hotkey('ctrl', 'v')


        pyautogui.write(day_sayi_str)

        QTimer.singleShot(1000, self.month_sender_ankara)

    def month_sender_ankara(self):

        # pyautogui.click(x=481, y=497, button='left')
        self.find_coord_and_click(selector='#month', button_type='left')

        QTimer.singleShot(1000, self.input_month)

    def input_month(self):

        random_sayi = random.randint(1, 12)


        for _ in range(random_sayi):
            pyautogui.press('down')
            time.sleep(0.1)


        pyautogui.press('return')


        QTimer.singleShot(1000, self.year_sender_ankara)

    def year_sender_ankara(self):
        self.find_coord_and_click(selector='#year', button_type='left')

        # pyautogui.click(x=604, y=497, button='left')
        # pyautogui.click(x=706, y=349, button='right')
        # pyautogui.click(x=604, y=497, button='left')
        QTimer.singleShot(1000, self.input_year)

    def input_year(self):


        random_year = random.randint(1980, 2005)
        random_year_str = str(random_year)

        # pyperclip.copy(random_year_str)
        # pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(random_year_str)


        QTimer.singleShot(1000, self.select_gender)


    def select_gender(self):


        self.find_coord_and_click(selector='#gender_option_male', button_type='move_left')


        QTimer.singleShot(1000, self.scroll_to_end)


    def scroll_to_end(self):
        self.browser.page().runJavaScript("window.scrollTo(0, document.body.scrollHeight);")

        print('page scroll down\n')

        QTimer.singleShot(1000, self.enter_third_page)



    def enter_third_page(self):

        self.find_coord_and_click(selector='.Button-sc-qlcn5g-0.cKYEKO', button_type='left')

        QTimer.singleShot(2000, self.kayit_end)

    def kayit_end(self):

        self.find_coord_and_click(selector='#checkbox-marketing', button_type='left')

        QTimer.singleShot(5000, self.kayit_son_artik)
    def kayit_son_artik(self):
        print("'SIGN UP' butonuna tıklanıyor...")

        self.find_coord_and_click(selector='.Button-sc-qlcn5g-0.cKYEKO', button_type='left')
        QTimer.singleShot(5000, self.clear_cookies)

    def clear_cookies(self):
        cookie_store = self.browser.page().profile().cookieStore()
        cookie_store.deleteAllCookies()

        self.browser.setUrl(QUrl("https://www.spotify.com/tr-tr/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F%3F"))

        self.browser.loadFinished.connect(self.on_load_finished)

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)


        self.add_tab("https://www.spotify.com/tr-tr/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F%3F")
        #self.add_tab("https://www.spotify.com/az-az/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2Fintl-tr")

        self.setWindowTitle("Purple Engine")
        self.setGeometry(100, 100, 800, 600)

    def add_tab(self, url):
        tab = BrowserTab()
        tab.set_url(url)
        self.tabs.addTab(tab, QUrl(url).host())

def main():
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
