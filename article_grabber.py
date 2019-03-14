from newspaper import Article as NA

def load_info(article):
    '''
    Handles grabbing the articles information from the link
    '''
    url = article.url
    A = NA(url)
    A.download()
    A.parse()
    A.nlp()
    return A.text, A.authors, A.summary
    