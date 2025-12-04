from django.shortcuts import render
import requests
from datetime import datetime

# Create your views here.
def homepage_view(request):
    api_key = "a39f8ea7337d4bf0895122450251710"
    city = "Gujarat"
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&aqi=yes"
    response = requests.get(url)
    data = response.json()

    day_data = data['forecast']['forecastday'][0]['day']

    temps_by_hour = {}
    for hour_data in data['forecast']['forecastday'][0]['hour']:
        hour = hour_data['time'].split(' ')[1][:2]  # '2025-10-17 12:00' -> '12'
        temp = hour_data['temp_c']
        temps_by_hour[hour] = temp


    now = datetime.now()

    context = {
        'city': data['location']['name'],
        'country': data['location']['country'],
        'temp_c': data['current']['temp_c'],
        'condition': data['current']['condition']['text'],
        'wind_kph': data['current']['wind_kph'],
        'humidity': data['current']['humidity'],
        'high':day_data['maxtemp_c'],
        'low': day_data['mintemp_c'],
        'hourly_temps': {
            '12AM': temps_by_hour.get('0'),
            '3AM': temps_by_hour.get('3'),
            '6AM': temps_by_hour.get('6'),
            '9AM': temps_by_hour.get('9'),
            '12PM': temps_by_hour.get('12'),
            '3PM': temps_by_hour.get('15'),
            '6PM': temps_by_hour.get('18'),
            '9PM': temps_by_hour.get('21'),
        },
    }

    return render(request, 'HomePage.html', context)

def hourly_view(request):
    return render(request, 'Hourly.html')

def tenDaysDetail(request):
    return render(request, 'TenDaysDetail.html')

def news(request):
    return render(request, 'News.html')

def newsDetail(request):
    return render(request, 'NewsDetail.html')

