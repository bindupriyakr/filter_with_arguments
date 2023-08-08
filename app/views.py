from django.shortcuts import render

# Create your views here.
import datetime
def Built_in_Filters(request):
    dt=datetime.datetime.now()
    d={'data':'Today We are discuess about the Fiters','Filters':'Filters are Two types Built in & User/Custom filet','dt':dt}
    return render(request,'create_a_Built_in_filters.html',d)