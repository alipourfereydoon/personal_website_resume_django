from django.shortcuts import render,get_object_or_404,redirect
from . models import Article,Category,Comment,Message
from django.core.paginator import Paginator
from . forms import ContactusForm,MessageForm

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

def contactus(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            Message.objects.create(title = title , text = text , email = email)
            return redirect('home:home')
    else:    
        form = MessageForm()
    return render(request,'blog_app/contact_us.html',{'form':form})



