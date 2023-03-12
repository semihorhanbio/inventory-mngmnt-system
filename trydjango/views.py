from django.http import HttpResponse

from articles.models import Article

def home_view(request):
    article_obj = Article.objects.get(id=1)
    html = f'''
        <h1>{article_obj.title}</h1>
        <p>{article_obj.content}</p>
    '''
    return HttpResponse(html)