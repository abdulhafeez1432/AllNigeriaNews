from django.shortcuts import render
from app.models import *
import requests
from bs4 import BeautifulSoup as bf
from django.shortcuts import get_object_or_404, redirect, render
import time
from requests_html import HTMLSession

session = HTMLSession()

def WebPunch(url, name):
    url = session.get('https://punchng.com/topics/sports/').content
    #url = requests.get(url).content
    #print(url)
    soup = bf(url, 'html.parser')
    #print(soup.prettify())
    #print(list(soup.children))
    #print(soup.find_all('p'))
    #data = soup.findAll(class_= name)
    data = soup.findAll(class_=name)
    print(len(data))
    news_title = []
    news_image_url = []
    news_time = []
    news_news = []
    news_url = []
    #.find('img',attrs={'class':'c-image__original'}).get('alt').strip()
   

    for details in data:
        title = details.find(class_='entry-title').text
        news_title.append(title)
        #content.find('div', attrs ={'class':'m-entry-featured-image'}).find('img',attrs={'class':'entry-thumbnail'}).get('src').strip()
        #image_url = details.find('img',attrs={'class':'entry-thumbnail'})
        #image_url = details.find(class_='img-lazy-load').get('data-src')
        #image_url = details.find('div',class_ ='entry-thumbnail-wrapper')
        time = details.find(class_='js-update-timestamp').get('data-default-time')
        news_time.append(time)
        detail = details.find('a').get('href')
        news_url.append(detail)
        news_details = session.get(detail)
        content = bf(news_details.text, 'html.parser')
        news = content.find('div', class_='entry-content').text
        #image_url = content.find('class', class_='entry-featured-image').find('img', class_='entry-thumbnail').get('src').strip()
        #image_url = content.find('picture', attrs={'entry-featured-image'}).find('img').attrs['src']
        a = content.findAll('picture', attrs = {'class': 'entry-featured-image'})
        for i in a:
            image_url = i.img['src']
            news_image_url.append(image_url)
        print(news_image_url)
        news_news.append(news)
    return news_title, news_image_url, news_time, news_news, news_url
    #return news_title, news_url


def PunchSport(request, punch, sport):
    category = get_object_or_404(Category, name=sport)
    site = get_object_or_404(Site, name=punch)
    x,y,z,a,b = WebPunch('https://punchng.com/topics/sports/', 'grid-item')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            break
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, 'index.html')


def PunchNews(request, punch, news):
    category = get_object_or_404(Category, name=news)
    site = get_object_or_404(Site, name=punch)
    x,y,z,a,b = WebPunch('https://punchng.com/topics/news/', 'items')
    print(x,y,z,a,b)
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, 'index.html')


def PunchMetro(request, punch, metro):
    category = get_object_or_404(Category, name=metro)
    site = get_object_or_404(Site, name=punch)
    x,y,z,a,b = WebPunch('https://punchng.com/topics/metro-plus/', 'items')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, 'index.html')



def PunchPolitics(request, punch, politics):
    category = get_object_or_404(Category, name=politics)
    site = get_object_or_404(Site, name=punch)
    x,y,z,a,b = WebPunch('https://punchng.com/topics/politics/', 'items')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, 'index.html')


def PunchBusiness(request, punch, business):
    category = get_object_or_404(Category, name=business)
    site = get_object_or_404(Site, name=punch)
    x,y,z,a,b = WebPunch('https://punchng.com/topics/business/', 'items')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, 'index.html')



def PunchEditorial(request, punch, editorial):
    category = get_object_or_404(Category, name=editorial)
    site = get_object_or_404(Site, name=punch)
    x,y,z,a,b = WebPunch('https://punchng.com/topics/editorial/', 'items')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, 'index.html')


def PunchColumns(request, punch, columns):
    category = get_object_or_404(Category, name=columns)
    site = get_object_or_404(Site, name=punch)
    x,y,z,a,b = WebPunch('https://punchng.com/topics/columns/', 'items')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, 'index.html')


def PunchOpinion(request, punch, opinion):
    category = get_object_or_404(Category, name=opinion)
    site = get_object_or_404(Site, name=punch)
    x,y,z,a,b = WebPunch('https://punchng.com/topics/opinion/', 'items')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, 'index.html')

    



    


def WebPremiumtime(url):
    url = requests.get(url).content
    soup = bf(url, 'html.parser')
    data = soup.findAll(class_= "jeg_post jeg_pl_lg_2 format-standard")
    news_title = []
    news_image_url = []
    news_time = []
    news_content = []
    news_url = []


    for details in data:
        #Getting Post Title
        title = details.find(class_='jeg_post_title').text
        news_title.append(title)
        #Getting Post Image
        image_url = details.find('img').get('data-src')
        news_image_url.append(image_url)
        #Getting Post Date&Time
        time = details.find(class_='jeg_meta_date').text
        news_time.append(time)
        #Getting Post Url
        news_link = details.findAll('h3')
        for link in news_link:
            news_link_link = link.find('a').get('href')
            news_url.append(news_link_link)
        #Getting Post Content
        for c in news_url:
            c_url = requests.get(c).content
            getting_content = bf(c_url, 'html.parser')
            c_data = getting_content.find(class_="content-inner").text
            news_content.append(c_data)
            
    return news_title, news_image_url, news_time, news_content, news_url
     

def PremiumSport(request, premium, sport):
    template_name = "index.html"
    category = get_object_or_404(Category, name=sport)
    site = get_object_or_404(Site, name=premium)
    x,y,z,a,b = WebPremiumtime('https://www.premiumtimesng.com/category/sports/football')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)

def PremiumHeadline(request, premium, headlines):
    template_name = "index.html"
    category = get_object_or_404(Category, name=headlines)
    site = get_object_or_404(Site, name=premium)
    x,y,z,a,b = WebPremiumtime('https://www.premiumtimesng.com/category/news/headlines')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def PremiumTopNews(request, premium, top_news):
    template_name = "index.html"
    category = get_object_or_404(Category, name=top_news)
    site = get_object_or_404(Site, name=premium)
    x,y,z,a,b = WebPremiumtime('https://www.premiumtimesng.com/category/news/top-news')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def PremiumFashion(request, premium, fashion):
    template_name = "index.html"
    category = get_object_or_404(Category, name=fashion)
    site = get_object_or_404(Site, name=premium)
    x,y,z,a,b = WebPremiumtime('https://www.premiumtimesng.com/category/entertainment/naija-fashion')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def PremiumHealth(request, premium, health):
    template_name = "index.html"
    category = get_object_or_404(Category, name=health)
    site = get_object_or_404(Site, name=premium)
    x,y,z,a,b = WebPremiumtime('    https://www.premiumtimesng.com/category/health/health-interviews')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)