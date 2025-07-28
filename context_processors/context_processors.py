from blog_app.models import Article,Category

def recent_articels(request):
    recent_articels = Article.objects.order_by('-created')
    category = Category.objects.all()
    return {'recent_article':recent_articels , 'categories':category}
    

# def category(request):
#     category = Category.objects.all()
#     return {'categories':category}