# Create your views here.
from django.shortcuts import render_to_response
from article.models import List
from article.models import Item 

def news_report(request):
 article_listing = []
 for article_list in List.objects.all():
   article_dict = {}
   article_dict['news_object'] = article_list
   article_dict['item_count'] = article_list.item_set.count()
   article_dict['items_title'] = article_list.title
   article_listing.append(article_dict)
 return render_to_response('show_report.html', { 'article_listing': article_listing })


def news_article(request):
 article_listing = []
 for article_list in Item.objects.all():
   article_dict = {}
   article_dict['news_object'] = article_list
   article_dict['article_list'] = article_list.article_list
   article_dict['items_id'] = article_list.id
   article_dict['items_title'] = article_list.title
   article_dict['items_content'] = article_list.content
   article_dict['created_date'] = article_list.created_date
   article_listing.append(article_dict)
 return render_to_response('show_list.html', { 'article_listing': article_listing })

def news_aid(request, aid):
 article_listing = {}
 article = Item.objects.get( id = aid )
 if article:
  article_listing['items_title'] = article.title
  article_listing['items_content'] = article.content
  article_listing['created_date'] = article.created_date
 return render_to_response('show_article.html', { 'article_listing': article_listing })
