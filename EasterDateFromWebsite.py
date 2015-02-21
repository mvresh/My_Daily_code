from urllib import request
import bs4,time
year = raw_input('Easter date for??')
def EasterYear(year):
    opener = request.build_opener()
    opener.add_headers = [('UserAgent','Mozilla 5.0')] #websites prefer web browsers and so
    response = opener.open('http://www.wheniseastersunday.com/year/' + str(year) + '/') #specifying the url we need
    read_response = bs4.BeautifulSoup(response.read()) #parsing HTML
    print read_response.select('.easterdate')[0].get_text() #selecting the one we need from the collected response
    
