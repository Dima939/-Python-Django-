import string, random
from django.shortcuts import render
from django.views import generic


numb_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
low_list = list(string.ascii_lowercase)
up_list = list(string.ascii_uppercase)
choice_list = [up_list, numb_list, low_list]


class HomeView(generic.View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        if request.POST.get('link'):
            link = request.POST.get('link')
            own_key = 'http://yourdomain/' + ''.join([random.choice(random.choice(choice_list)) for i in range(6)])
            return render(request, 'home.html', {'own_key': own_key, 'link': link})
        else:
            return render(request, 'home.html', {'help_text': 'Введите ссылку'})
