import json
import urllib2

def GetCity():
    city = raw_input("Please enter the name or zip code of the city:")
    city = "https://api.apixu.com/v1/current.json?key=3ee5513ffea04a0ca2a00402172404&q=" + city
    return city


def main():
    url = GetCity()
    jsontxt = urllib2.urlopen(url).read()
    weather = json.loads(jsontxt)
    print 'Here is the weather for ' + weather['location']['name'] + ', ' + weather['location']['region']
    print weather['current']['condition']['text'] + " and " + str(weather['current']['temp_f']) + " degrees Farenheit"
    print 'it actually feels like ' + str(weather['current']['feelslike_f']) + ' degrees Farenheit'
    
main()