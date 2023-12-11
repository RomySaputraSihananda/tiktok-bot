import undetected_chromedriver as uc
from undetected_chromedriver import Chrome
import os

class Zefoy:
    def __init__(self) -> None:
        self.__url: str = 'https://zefoy.com'
        self.__driver: Chrome = uc.Chrome(driver_executable_path=f"./driver/{os.listdir('./driver')[0]}")

    def __wait_element(self, selector: str):
        while True:
            try:
                f = self.__driver.find_element('xpath', selector)
                return True
            except Exception:
                pass

    def execute(self):
        self.__driver.get(self.__url)

        self.__wait_element('/html/body/div[5]/div[2]/form/div/div')

# testing
if(__name__ == '__main__'):
    zefoy: Zefoy = Zefoy()
    zefoy.execute()