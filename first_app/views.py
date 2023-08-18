from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# cookie ---
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'rahim')
    # response.set_cookie('name', 'karim', max_age=60*3)  # max age diye cookie koto khon thake setar time save kore rakhe second peramitar e
    response.set_cookie('name', 'karim', expires=datetime.utcnow()+timedelta(days=7))
    return response
def get_cookie(request): # get ar set ekoi html file korte parbo na . tai ei kgane get korar jonno get_cookie.html file create korechi. ar set er jonno home.html
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name':name})

def delete_cookie(request):  # delete korar jonno alada templet dorkar
    response = render(request, 'del.html')
    response.delete_cookie('name')
    return response

# Django Session
# session vs cookie
#session website er data base information save kore rakhe ar cookie brower er database save kore rakhe
#session er jonno migration  command dite hoy

def set_session(request):
    # data = {
    #     'name' : 'rahim',
    #     'age' : 23,
    #     'language' : 'Bangla'
    #  }
    # print(request.session.get_session_cookie_age()) #get_session_cookie_age ei functon nidharon kore web er database info koto din save thakbe
    # print(request.session.get_expiry_date())
    # request.session.update(data)
    request.session['name'] = 'Karim'
    return render(request,'home.html')

def get_session(request):
    #data = request.session
    #print(data)
    #return render(request,'get_session.html' ,{'data' : data})
#--------------------------------------------------------------------------
    # name = request.session.get('name', 'Guest')  #('name', 'Guest') ei khane guest deoyar karon holo name jodi  delete hoy tahole defult hisabe guest bosbe
    # return render(request,'get_session.html' ,{'name' : name})
    if 'name' in request.session:   # eita diye web er session time contron korbo. setting.py file SESSION_COOKIE_AGE eita use korbo
        name = request.session.get('name', 'Guest')
        request.session.modified = True # eita 10 second er modhe relod dile auto 5 second add korbe
        return render(request,'get_session.html' ,{'name' : name})
    else:
        return HttpResponse("Your session has been expired.Login again")

def delete_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request,'del.html')

