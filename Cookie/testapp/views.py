from django.shortcuts import render

# Create your views here.
def countview(request):
    if 'count' in request.COOKIES:
        newCount = int(request.COOKIES['count']) + 1
        response = render(request, 'testapp/Count.html', {'count': newCount})
        response.set_cookie('count', newCount)
    else:
        newCount = 1
        response = render(request, 'testapp/Count.html', {'count': newCount})
        response.set_cookie('count', newCount)
        
        
    return response
