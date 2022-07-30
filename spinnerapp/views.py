from datetime import datetime
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import random
from .models import *
from random import randint
# Create your views here.

def home(request):
      
    try:
    # Python 2
        from itertools import izip_longest
        zip_longest = izip_longest
    except ImportError:
    # Python 3
        from itertools import zip_longest
    
    
    try:
        value = randint(1,100)
        list12=[]
        list34=[]
        list45=[]
        list78=[]
        
        wheels = Wheel.objects.all()
        for wheel in wheels:
            list12.append(wheel.starting_point) 
            list34.append(wheel.ending_point)
            list45.append(wheel.name) 
            list78.append(wheel.img)
            print(list78)
        try:
            wheel_data = dict(zip(list45, zip(list12, list34)))
            a =list(wheel_data.keys())[0]
            b = list(wheel_data.keys())[1]
            c=list(wheel_data.keys())[2]
            d =list(wheel_data.keys())[3]
            e =list(wheel_data.keys())[4]
            f =list(wheel_data.keys())[5]
            print(value)
            result = ''
        except Exception as e:
            return HttpResponse(f"Error!!! {e} Kindly Refresh it, Thanks")
      
          
        try:
            timestamp = str(datetime.now())
            if value >= wheel_data[a][0] and value <= wheel_data[a][1]:
                print("Item#1 is True")
                result = a
                img = list78[0]
                timestamp = str(datetime.now())
                history_log = History(name=result,timestamp=timestamp)
                history_log.save()
                        
                        
            elif value >= wheel_data[b][0] and value <= wheel_data[b][1]:
                print("Item#2 is True")
                result = b
                img = list78[1]
                history_log = History(name=result,timestamp=timestamp)
                history_log.save()
                            
            elif value >= wheel_data[c][0] and value <= wheel_data[c][1]:
                print("Item#3 is True")
                result = c
                img = list78[2]
                history_log = History(name=result,timestamp=timestamp)
                history_log.save()
                    
            elif value >= wheel_data[d][0] and value <= wheel_data[d][1]:
                print("Item#4 is True")
                result = d
                img = list78[3]
                history_log = History(name=result,timestamp=timestamp)
                history_log.save()
                            
            elif value >= wheel_data[e][0] and value <= wheel_data[e][1]:
                print("Item#5 is True")
                result = e
                img = list78[4]
                history_log = History(name=result,timestamp=timestamp)
                history_log.save()      
                        
            elif value >= wheel_data[f][0] and value <= wheel_data[f][1]:
                print("Item#6 is True")
                result = f 
                img = list78[5]
                history_log = History(name=result,timestamp=timestamp)
                history_log.save()
                        
            else:
                result = "Item not found"
        except Exception as e:
            return HttpResponse(f"Error!!! {e} Kindly Refresh it, Thanks")
        
        return render(request,'home.html',{'wheels':wheels,'value':result,'img':img})

      
        
        
    except Exception as e:
        return HttpResponse(f"Error!!! {e} Kindly Refresh it, Thanks")
    