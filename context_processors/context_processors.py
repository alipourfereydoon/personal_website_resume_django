from blog_app.models import Article

def recent_articels(request):
    recent_articels = Article.objects.order_by('-created')
    return {'recent_article':recent_articels}
    