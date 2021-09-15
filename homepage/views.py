from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import feedparser
import re

def striphtml(data):
        p = re.compile(r'<\/?(?!p)(?!em)\w*\b[^>]*>')
        return p.sub('', data)
    
rssURL = 'https://shawnleemilitary.wordpress.com/feed/'


# Create your views here.
def HomeView(request):
    feed = feedparser.parse(rssURL)
    entries = [{"title" : a["title"], 
                "link" : a["link"], 
                "published": str(a["published_parsed"][0]) + "/" + str(a["published_parsed"][1]) + "/" + str(a["published_parsed"][2]),
                "summary" : re.sub('<span.*?</span>','',a["summary"], flags=re.DOTALL),
                "short_contents" : striphtml(a["content"][0]["value"])[0:500] + "...",
                "full_contents" : a["content"][0]["value"],
               } for a in feed.entries]
    return render(request, "homepage/home.html", {"entries" : entries})


def AboutView(request):
    return render(request, "homepage/about.html")

def BlogView(request):
    feed = feedparser.parse(rssURL)
    entries = [{"title" : a["title"], 
                "link" : a["link"], 
                "published": str(a["published_parsed"][0]) + "/" + str(a["published_parsed"][1]) + "/" + str(a["published_parsed"][2]),
                "summary" : re.sub('<span.*?</span>','',a["summary"], flags=re.DOTALL),
                "short_contents" : striphtml(a["content"][0]["value"])[0:500] + "...",
                "full_contents" : a["content"][0]["value"],
               } for a in feed.entries]
    return render(request, "homepage/blog.html", {"entries" : entries})