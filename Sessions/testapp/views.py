from django.shortcuts import render

# Create your views here.
def page_count(request):
    count = request.session.get('count', 0)
    newCount = count + 1
    request.session['count'] = newCount
    return render(request, 'count.html', {'count': newCount})