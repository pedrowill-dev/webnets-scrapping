from src.utils.webdriver.chrome import Chrome
from src.use_cases.extract import Extract
from src.use_cases.load import Load

def main():


    chrome = Chrome()
    webdriver = chrome.get_driver

    extract_news = Extract(webdriver=webdriver)
    data_news = extract_news.run()


    for indice, news in enumerate(data_news):
        indice+=1
        load_news = Load(data=news)
        load_news.load_file(file_path=f'news_{indice}.txt', indice_news=indice)

    