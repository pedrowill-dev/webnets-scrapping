from selenium.webdriver.common.by import By

class Extract:

    def __init__(self, webdriver):
        self.webdriver = webdriver

    def _get(self, link_content: str):
        self.webdriver.get(link_content)
        
    def _extract_cover_img(self, news):
        src_img_link = news.find_element(By.CSS_SELECTOR, 'a.list-item__img img')
        src_img_link = src_img_link.get_attribute('src')
        return src_img_link
    
    def _extract_title(self, news):
        element_title = news.find_element(By.CSS_SELECTOR, 'a.list-item__link')
        title = element_title.text
        link = element_title.get_attribute('href')
        return title, link
    
    def _extract_source(self, news):
        source = news.get_attribute('outerHTML')
        source = source.split('\n')
        html_source = ''.join([item for item in source if not item in '\n'])
        return html_source

    def _extract_all_img(self, news):
        img_list = news.find_elements(By.CLASS_NAME, 'gallery__img')
        img_list = [img.get_attribute('src') for img in img_list]
        return img_list

    def extract_news_content(self, link_news):
        self._get(link_content=link_news)
        element_news = self.webdriver.find_element(By.CLASS_NAME, 'wrapper main')
        news_content = self._extract_source(news=element_news)
        all_img_list = self._extract_all_img(news=element_news)
        self.webdriver.back()
        return news_content, all_img_list
        


    def _extract(self):
        news_dict = []
        news_session = self.webdriver.find_elements(By.CLASS_NAME, "list-item")
        

        for news in news_session:
            
            title_text_content, link_news = self._extract_title(news=news)
            cover_image_attribute = self._extract_cover_img(news=news)
            page_source_content, images_src_attribute = self.extract_news_content(link_news=link_news)

            
            news_dict.append({
                "title": title_text_content,
                "capa_imagem_src": cover_image_attribute,
                'html': page_source_content,
                'img_list_news': images_src_attribute,
                })
        return news_dict


    def run(self):
        news_collect = []
        for page in range(1, 10+1):
            text_link = f'https://www.araraquara.sp.gov.br/noticias?&pagina={page}'
            self._get(link_content=text_link)
            news_dict = self._extract()
            news_collect.append({
                f"Pagina {page}": news_dict
            })
        return news_collect