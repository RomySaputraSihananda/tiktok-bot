import os
import undetected_chromedriver as uc
from undetected_chromedriver import Chrome
from time import sleep
class Zefoy:
    def __init__(self) -> None:
        self.__url: str = 'https://zefoy.com'
        self.__driver: Chrome = uc.Chrome(driver_executable_path=f"./driver/{os.listdir('./driver')[0]}")
        self.__driver.set_window_size(500, 800)
        self.__sent: int = 1
        self.__videourl: str = None

        self.__selectors: dict = {
                selector: f".row div:nth-child({i + 2}) div button" for i, selector in enumerate(['followers', 'hearts', 'chearts', 'views', 'shares', 'favorites', 'livestream'])                   
            }

    def __wait_element(self, selector: str):
        while True:
            try:
                return self.__driver.find_element("css selector", selector)
            except Exception:
                pass
    
    def __send_bot(self, key: str):
        input_link = self.__wait_element(f'.col-sm-5.col-xs-12.p-1.container.t-{key}-menu div form div input')
        input_link.clear()
        input_link.send_keys(self.__videourl)
        self.__wait_element(f'.col-sm-5.col-xs-12.p-1.container.t-{key}-menu div form div div button').click()
        
                
        self.__wait_element(f'.col-sm-5.col-xs-12.p-1.container.t-{key}-menu div div div div form button').click()

        sleep(3)

        while(True):
            if('READY' in self.__wait_element(f'.col-sm-5.col-xs-12.p-1.container.t-{key}-menu div div span').text): break
            sleep(2)

        print(f"[{self.__sent}] {self.__wait_element(f'.col-sm-5.col-xs-12.p-1.container.t-{key}-menu div div span:last-child').text}")
        self.__sent += 1
        self.__send_bot(key)

    def execute(self):
        self.__driver.get(self.__url)

        self.__wait_element('.card.mb-3.word-load')

        captha = input('Solve the Captha : ') 

        self.__wait_element('.card.mb-3.word-load div input').send_keys(captha)
        self.__wait_element('.card.mb-3.word-load div div button').click()

        self.__wait_element('.row')

        for i, key in enumerate(self.__selectors):
            print(f'[{i + 1}] [ {self.__wait_element(self.__selectors[key]).is_enabled()} ] {key}')

        choice = int(input('Choice : '))
        self.__videourl = input('videourl : ')

        for i, key in enumerate(self.__selectors):
            if(i == choice - 1): 
                self.__wait_element(self.__selectors[key]).click()
                self.__send_bot(key)
                

        self.__wait_element('#test')

# https://vt.tiktok.com/ZSNVHNyVT/
# testing
if(__name__ == '__main__'):
    zefoy: Zefoy = Zefoy()
    zefoy.execute()