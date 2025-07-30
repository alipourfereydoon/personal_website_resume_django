from django.shortcuts import render,get_object_or_404
from . models import Article,Category,Comment
from django.core.paginator import Paginator


def article_detail(request,pk):
    articles = get_object_or_404(Article,id = pk)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(article = articles , user = request.user , body = body , parent_id= parent_id)
        

    
    comments = get_object_or_404(Comment,id = pk)
    return render(request,'blog_app/article_detail.html',context={'article':articles , 'comment':comments})



def allpost(request):
    articles = Article.objects.all()
    paginator = Paginator(articles,1)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    recents = Article.objects.order_by('-created')[:3]
    return render(request,'blog_app/article_list.html',
                  {'articles':object_list,
                   'recent_post':recents
                   })


def category_detail(request,pk=None):
    category = get_object_or_404(Category,id=pk)
    articles = category.articles.all()
    return render(request,'blog_app/article_list.html',{'articles':articles})

def search(request):
    q = request.GET.get('q')
    article = Article.objects.filter(title__icontains = q)
    paginator = Paginator(article,1)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    return render(request,'blog_app/article_list.html',{'articles':object_list})
