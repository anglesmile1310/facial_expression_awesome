import mistune
from bs4 import BeautifulSoup
import re

class MarkdownParser(object):
    def __gen_html(self, document):
        markdown = mistune.Markdown()
        html_doc = markdown(document)
        return html_doc

    def __html_parser(self, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        for tag in soup.find_all(['pre']):
            tag.replace_with('')
        for tag in soup.find_all(['img']):
            tag.replace_with('')
        for tag in soup.find_all(['a']):
            tag.replace_with('')
            
        text = soup.text
        text = text.replace('\n', ' ')
        text = re.sub(r'[^\w\s]',' ',text)
        text = text.lower()
        text = text.strip()
        
        return text

    def __remove_emoji(self, text):
        RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
        return RE_EMOJI.sub(r'', text)

    def pure_text(self, document):
        html_doc = self.__gen_html(document)
        text = self.__html_parser(html_doc)
        return self.__remove_emoji(text)
