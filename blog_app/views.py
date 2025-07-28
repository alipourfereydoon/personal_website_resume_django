from django.shortcuts import render,get_object_or_404
from . models import Article


def article_detail(request,pk):
    article = get_object_or_404(Article,id = pk)
    return render(request,'blog_app/article_detail.html',context={'article':article})



def allpost(request):
    articles = Article.objects.all()
    recents = Article.objects.order_by('-created')[:3]
    return render(request,'blog_app/article_list.html',
                  {'articles':articles,
                   'recent_post':recents
                   })


