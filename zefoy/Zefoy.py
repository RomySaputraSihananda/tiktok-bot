import undetected_chromedriver as uc
from undetected_chromedriver import Chrome
import os

class Zefoy:
    def __init__(self) -> None:
        self.__url: str = 'https://zefoy.com'
        self.__driver: Chrome = uc.Chrome(driver_executable_path=f"./driver/{os.listdir('./driver')[0]}")
        self.__selectors: dict = {
                selector: f".row div:nth-child({i + 2}) div button" for i, selector in enumerate(['followers', 'hearts', 'chearts', 'views', 'shares', 'favorites', 'livestream'])                   
            }

    def __wait_element(self, selector: str):
        while True:
            try:
                return self.__driver.find_element("css selector", selector)
            except Exception:
                pass

    def execute(self):
        self.__driver.get(self.__url)

        self.__wait_element('.card.mb-3.word-load')

        self.__wait_element('.row')

        for i, keys in enumerate(self.__selectors):
            print(f'{i + 1}. [ {self.__wait_element(self.__selectors[keys]).is_enabled()} ] {keys}')

        choice = int(input('Choice : '))

        for i, keys in enumerate(self.__selectors):
            if(i == choice - 1): 
                self.__wait_element(self.__selectors[keys]).click()
                self.__wait_element(f'.col-sm-5.col-xs-12.p-1.container.t-{keys}-menu div form div input').send_keys('hehehehehehe')
            
        self.__wait_element('#test')

# testing
if(__name__ == '__main__'):
    zefoy: Zefoy = Zefoy()
    zefoy.execute()