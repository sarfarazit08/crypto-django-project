from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):

    # Crypto news data
    api_req = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_req.content)

    return render(request, 'home.html', {'api' : api })

# Create your views here.
def prices(request):

    symbols = "BTC,ETH,BNB,DOGE,XRP,YFI,BCH,LTC"
    # Crypto price data
    price_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ symbols +"&tsyms=USD,EUR,INR")
    prices = json.loads(price_req.content)

    return render(request, 'prices.html', {'prices' : prices})

# Create your views here.
def weather(request):

    # Weather data
    weather_req = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=22.5697&lon=88.3697&units=metric&appid=e84701b1dd761787ba28ce7e7c358ca9")
    weather = json.loads(weather_req.content)

    headers = {   'accept': 'application/json',}
    params = (    ('language', 'en'),)

    # Quote of the day API
    qod_req = requests.get('https://quotes.rest/qod', headers=headers, params=params)
    qod = json.loads(qod_req.content)


    return render(request, 'weather.html', {'weather' : weather, 'qod' : qod})

# Create your views here.
def wiki(request):
    if request.method == "POST":

        article = request.POST['article']

        # Wiki search
        wiki_req = requests.get("https://en.wikipedia.org/w/api.php?action=query&list=search&origin=*&format=json&srlimit=50&srsearch=" + article)
        wiki = json.loads(wiki_req.content)

        return render(request, 'wiki.html', {'wiki' : wiki})

    else:

        return render(request, 'wiki.html', {'notfound' : "No data yet... search again!"})

# Create your views here.
def covid(request):

    # Crypto news data
    covid_req = requests.get("https://api.covid19api.com/country/india?from=2021-05-10T00:00:00Z&to=2021-05-11T00:00:00Z")
    covid = json.loads(covid_req.content)

    return render(request, 'covid.html', {'covid' : covid })


