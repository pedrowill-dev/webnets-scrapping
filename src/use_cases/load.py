class Load:

    def __init__(self, data: dict):
        self.data = data
    
    def load_file(self, file_path: str, indice_news) -> None:
        
        content_news = ''
        data = self.data[f'Pagina {indice_news}']
        for item in data:
            content_news += item['title'] + '\n'
            content_news += item['capa_imagem_src'] + '\n'
            content_news += item['html'] + '\n'
            content_news += '\n'.join(item['img_list_news'])

            with open(f'src/news/{file_path}', 'a', encoding="utf8") as file:
                file.write(content_news)
