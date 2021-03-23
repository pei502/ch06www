from django.shortcuts import render
from datetime import datetime


def index(request, tvno = 0):
    tv_list = [{'name':'東森', 'tvcode':'R2iMq5LKXco'},
               {'name':'民視', 'tvcode':'XxJKnDLYZz4'},
               {'name':'公視', 'tvcode':'ED4QXd5xAco'},]
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'index.html', locals())


# Create your views here.
