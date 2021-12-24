import datetime
from facebook_scraper import get_posts
from requests import cookies 
from rfeed import Extension, Image, Item,Feed,Guid,ItemImage

list_sourses = [
                '3OmarTaha','SymbianSyMoh',
                'ShaDiAbdulhafeZ','doctor.virus11',
                'Aly.Medad',"ITIchannel","ITIMansoura",
                'mohamed.hamedhammad','www.kfs.edu.eg',
                'StateOfEcom'
                ]
list_groubs = ['1596832580575937','172338516139198']


lst_items = []


for source in list_groubs:
    for post in get_posts(source,pages=2,cookies="from_browser"):#
        item  = Item(
                    link=post['post_url'],
                    guid=Guid(post['post_url']),
                    author=post['header'],
                    pubDate=post['time'],
                    description=str(post["header"]+'\n\n\n\n' + post["text"] +'\n\n'+post["post_url"]+'\n\n'+str(post["images"])+'\n'),
                    title="",
                )
        lst_items.append(item)
for source in list_sourses:
    for post in get_posts(source,pages=2,cookies="from_browser"):#
        item  = Item(
                    link=post['post_url'],
                    guid=Guid(post['post_url']),
                    author=post['username'],
                    pubDate=post['time'],
                    description=str(post["username"]+'\n\n\n\n'+post["text"]+'\n\n'+post["post_url"]+'\n\n'+str(post["images"])+'\n'),
                    title="",
                )
        lst_items.append(item)

feed = Feed(
    title = "facebook",
    link = "facebook.com",
    description = "facebook feed for my following list",
    language = "ar-SA",
    lastBuildDate = datetime.datetime.now(),
    items = [item for item in lst_items])
print(feed.rss())