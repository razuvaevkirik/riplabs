from datetime import datetime
from django.shortcuts import render
from django.views import View


def main(request):
    return render(request, 'main.html')


def tickets(request):
    return render(request, 'tickets.html')

def hello(request):
    return render(request, 'hello.html')


def concerts(request, id):
    name = ['BMTH_info', 'CTE_info']
    BMTH_info = 'BMTH bla bla'
    CTE_info = 'Crown the empire bla bla'
    info = [BMTH_info, CTE_info]
    data1 = {'concert': {'id': id}}
    data2 = {'concerts': [{'id': '1', 'concert_name': 'Bring Me The Horizon', 'info': BMTH_info},
                       {'id': '2', 'concert_name': 'Crown The Empire', 'info': CTE_info}]}
    return render(request, 'concerts.html', locals())

class TicketsView(View):
    def get(self, request):
        #variable = 'Django'
        today_date = datetime.now()
        data = {
            'tickets': [
                {'title': 'Первый билет', 'id': 1},
                {'title': 'Второй билет', 'id': 2}
            ]
        }
        return render(request, 'tickets.html', locals())


class TicketView(View):
    def get(self, request, id):
        #variable = 'Django'
        today_date = datetime.now()
        data = {
            'ticket': {
                'id': id
            }
        }
        return render(request, 'ticket.html', locals())

