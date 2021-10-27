from django.shortcuts import render
from app.models import *
import requests
from bs4 import BeautifulSoup as bf
from django.shortcuts import get_object_or_404, redirect, render
import time
from requests_html import HTMLSession

session = HTMLSession()

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
     

def WebPunch(url, name):
    #url = session.get(url).content
    url = requests.get(url).content
    soup = bf(url, 'html.parser')
    data = soup.findAll(class_=name)
    news_title = []
    news_image_url = []
    news_time = []
    news_content = []
    news_url = []
   

    for details in data:
        #Getting Post Title
        t = details.find('h3', class_="entry-title").text
        news_title.append(t)

        #Getting Post Image
        image_url = details.find('img').get('data-src')
        news_image_url.append(image_url)

        #Getting Post Url
        news_link = details.find('a').get('href')
        news_url.append(news_link)

        #Getting Post Date & Time
        time = details.find(class_="meta-time").text
        news_time.append(time)

        #Getting Post Content
        for c in news_url:
            c_url = requests.get(c).content
            getting_content = bf(c_url, 'html.parser')
            c_data = getting_content.find(class_="entry-content").text
            news_content.append(c_data)
    return news_title, news_image_url, news_time, news_content, news_url
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
    x,y,z,a,b = WebPunch('https://punchng.com/topics/news/', 'grid-item')
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
    x,y,z,a,b = WebPunch('https://punchng.com/topics/metro-plus/', 'grid-item')
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
    x,y,z,a,b = WebPunch('https://punchng.com/topics/politics/', 'grid-item')
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
    x,y,z,a,b = WebPunch('https://punchng.com/topics/business/', 'grid-item')
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
    x,y,z,a,b = WebPunch('https://punchng.com/topics/editorial/', 'grid-item')
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
    x,y,z,a,b = WebPunch('https://punchng.com/topics/columns/', 'grid-item')
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
    x,y,z,a,b = WebPunch('https://punchng.com/topics/opinion/', 'grid-item')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, 'index.html')




def PremiumSport(request, premium, sport):
    template_name = "index.html"
    category = get_object_or_404(Category, name=sport)
    site = get_object_or_404(Site, name=premium)
    x,y,z,a,b = WebPremiumtime('https://www.premiumtimesng.com/category/sports/football/')
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
    x,y,z,a,b = WebPremiumtime('https://www.premiumtimesng.com/category/news/headlines/')
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
    x,y,z,a,b = WebPremiumtime('https://www.premiumtimesng.com/category/news/top-news/')
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
    x,y,z,a,b = WebPremiumtime('https://www.premiumtimesng.com/category/entertainment/naija-fashion/')
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
    x,y,z,a,b = WebPremiumtime('https://www.premiumtimesng.com/category/health/health-interviews/')
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)

def WebTribune(url):
    url = requests.get(url).content
    soup = bf(url, 'html.parser')
    data = soup.findAll(class_= "col-md-12 col-sm-12 col-xs-12 pt-cv-content-item pt-cv-2-col")
    news_title = []
    news_image_url = []
    news_time = []
    news_content = []
    news_url = []


    for details in data:
        #Getting Post Title
        t = details.find(class_='pt-cv-title').text
        news_title.append(t)

        #Getting Post Image
        image_url = details.find('img').get('data-src')
        news_image_url.append(image_url)

        #Getting Post Url
        news_link = details.findAll(class_='pt-cv-title')
        for l in news_link:
            link = l.find('a').get('href')
            news_url.append(link)

        #Getting Post Content, Date & Time
        for c in news_url:
            c_url = requests.get(c).content
            getting_content = bf(c_url, 'html.parser')
            c_data = getting_content.find(class_="entry-content clearfix single-post-content").text
            news_content.append(c_data)
            time = getting_content.find('time').text
            news_time.append(time)
    return news_title, news_image_url, news_time, news_content, news_url


def TribuneNews(request, tribune, news):
    template_name = "index.html"
    category = get_object_or_404(Category, name=news)
    site = get_object_or_404(Site, name=tribune)
    x,y,z,a,b = WebTribune("https://tribuneonlineng.com/news/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def TribuneHealth(request, tribune, health):
    template_name = "index.html"
    category = get_object_or_404(Category, name=health)
    site = get_object_or_404(Site, name=tribune)
    x,y,z,a,b = WebTribune("https://tribuneonlineng.com/health/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def TribunePolitics(request, tribune, politics):
    template_name = "index.html"
    category = get_object_or_404(Category, name=politics)
    site = get_object_or_404(Site, name=tribune)
    x,y,z,a,b = WebTribune("https://tribuneonlineng.com/politics/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)



def TribuneEntertainment(request, tribune, entertainment):
    template_name = "index.html"
    category = get_object_or_404(Category, name=entertainment)
    site = get_object_or_404(Site, name=tribune)
    x,y,z,a,b = WebTribune("https://tribuneonlineng.com/entertainment/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)



def TribuneBusiness(request, tribune, business):
    template_name = "index.html"
    category = get_object_or_404(Category, name=business)
    site = get_object_or_404(Site, name=tribune)
    x,y,z,a,b = WebTribune("https://tribuneonlineng.com/business/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def WebDailyPost(url):
    url = requests.get(url).content
    soup = bf(url, 'html.parser')
    data = soup.findAll(class_= "mvp-blog-story-wrap left relative infinite-post")
    news_title = []
    news_image_url = []
    news_time = []
    news_content = []
    news_url = []


    for details in data:
        #Getting Post Title
        t = details.find('h2').text
        news_title.append(t)

        #Getting Post Image
        image_url = details.find('img').get('src')
        news_image_url.append(image_url)

        #Getting Post Url
        link = details.find('a').get('href')
        news_url.append(link)

        #Getting Post Time
        time = details.find(class_="mvp-cd-date left relative").text
        news_time.append(time)

        #Getting Post Content, Date & Time
    for c in news_url:
        c_url = requests.get(c).content
        getting_content = bf(c_url, 'html.parser')
        c_data = getting_content.find('div', {"id": "mvp-content-main"}).text
        news_content.append(c_data)
    return news_title, news_image_url, news_time, news_content, news_url


def DailpostNews(request, dailypost, news):
    template_name = "index.html"
    category = get_object_or_404(Category, name=news)
    site = get_object_or_404(Site, name=dailypost)
    x,y,z,a,b = WebTribune("https://dailypost.ng/hot-news/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def DailpostSport(request, dailypost, sport):
    template_name = "index.html"
    category = get_object_or_404(Category, name=sport)
    site = get_object_or_404(Site, name=dailypost)
    x,y,z,a,b = WebTribune("https://dailypost.ng/sport-news/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def DailpostEntertainment(request, dailypost, entertainment):
    template_name = "index.html"
    category = get_object_or_404(Category, name=entertainment)
    site = get_object_or_404(Site, name=dailypost)
    x,y,z,a,b = WebTribune("https://dailypost.ng/entertainment/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def DailpostMetro(request, dailypost, metro):
    template_name = "index.html"
    category = get_object_or_404(Category, name=metro)
    site = get_object_or_404(Site, name=dailypost)
    x,y,z,a,b = WebTribune("https://dailypost.ng/metro/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def DailpostPolitics(request, dailypost, politics):
    template_name = "index.html"
    category = get_object_or_404(Category, name=politics)
    site = get_object_or_404(Site, name=dailypost)
    x,y,z,a,b = WebTribune("https://dailypost.ng/politics/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)



def WebDailyNation(url):
    url = requests.get(url).content
    soup = bf(url, 'html.parser')
    data = soup.findAll(class_= "td-block-span6")
    news_title = []
    news_image_url = []
    news_time = []
    news_content = []
    news_url = []


    for details in data:

        #Getting Post Title
        t = details.find(class_="entry-title td-module-title").text
        news_title.append(t)
        
        #Getting Post Image
        image_url = details.find('img').get('src')
        news_image_url.append(image_url)

        #Getting Post Url
        link = details.find('a').get('href')
        news_url.append(link)
        #Getting Post Time
        time = details.find("time").text
        news_time.append(time)


    #Getting Post Content, Date & Time
    for c in news_url:
        c_url = requests.get(c).content
        getting_content = bf(c_url, 'html.parser')
        c_data = getting_content.findAll(class_="td_block_wrap tdb_single_content tdi_85 td-pb-border-top td_block_template_1 td-post-content tagdiv-type")
        for con in c_data:
            content = con.find(class_="tdb-block-inner td-fix-index").text
            news_content.append(content)
    return news_title, news_image_url, news_time, news_content, news_url


def DailyNationNews(request, dailynation, news):
    template_name = "index.html"
    category = get_object_or_404(Category, name=news)
    site = get_object_or_404(Site, name=dailynation)
    x,y,z,a,b = WebDailyNation("https://dailynigerian.com/category/nation/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def DailyNationPolitics(request, dailynation, politics):
    template_name = "index.html"
    category = get_object_or_404(Category, name=politics)
    site = get_object_or_404(Site, name=dailynation)
    x,y,z,a,b = WebDailyNation("https://dailynigerian.com/category/politics/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def DailyNationEntertainment(request, dailynation, entertainment):
    template_name = "index.html"
    category = get_object_or_404(Category, name=entertainment)
    site = get_object_or_404(Site, name=dailynation)
    x,y,z,a,b = WebDailyNation("https://dailynigerian.com/category/entertainment/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)


def DailyNationBusiness(request, dailynation, business):
    template_name = "index.html"
    category = get_object_or_404(Category, name=business)
    site = get_object_or_404(Site, name=dailynation)
    x,y,z,a,b = WebDailyNation("https://dailynigerian.com/category/business/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)



def DailyNationOpinion(request, dailynation, opinion):
    template_name = "index.html"
    category = get_object_or_404(Category, name=opinion)
    site = get_object_or_404(Site, name=dailynation)
    x,y,z,a,b = WebDailyNation("https://dailynigerian.com/category/opinion/")
    for x, y, z, a, b in zip(x,y,z,a,b):
        if NewsDetails.objects.filter(url=b).exists():
            pass
        else:
            news = NewsDetails(title=x, image_url=y, content=a, category=category, site=site, url=b, uploaded=z)
            news.save()
    return render(request, template_name)