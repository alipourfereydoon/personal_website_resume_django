from django.shortcuts import render
from blog_app.models import Article,Category

def home(request):
    article = Article.objects.all()
    recent_article = Article.objects.all().order_by('-created')[:3]
    return render(request,'home_app/index.html', {
        'articles':article , 
        'recent_articles':recent_article,
        })


def sidebar(request):
    categorysid = Category.objects.all()
    context = {'cat':categorysid}
    return render(request,'includes/sidebar.html',context)