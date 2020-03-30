import requests
from bs4 import BeautifulSoup
from coronavirus_tracker_hourly import get_current_datetime

def get_url_resp(country="Worldwide"):
    base_url = "https://www.worldometers.info/coronavirus/"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}
    if country =="Worldwide":
        url = base_url
    else:
        url =base_url+"country/"+country+"/"
    response = requests.get(url, headers = headers)
    html = response.text
    return BeautifulSoup(html,"html.parser")

def format_case_numbers(soup,country="Worldwide"):
    if country == "Worldwide":
        soup_selector = soup.select(".col-md-6")
        val = [soup_selector[2].find_all(type="text/javascript")[0],soup_selector[3].find_all(type="text/javascript")[0]]
    else:
        soup_selector = soup.find_all("script")
        new_soup =[]
        for i in range(len(soup_selector)):
            if 'categories' in str(soup_selector[i]):
                new_soup.append(soup_selector[i])
        val = new_soup#[:2]
    return val

def get_right_element(val,Status = "Cases"):
    string1 = f"'Total Coronavirus {Status}'"
    new_soup =[]
    for i in range(len(val)):
        if string1 in str(val[i]):
            new_soup.append(val[i])
    return new_soup

def get_both_elements(val):
    statuses_tuple = ("Cases","Deaths")
    new_soup = []
    for sta in statuses_tuple:
        new_soup.append(get_right_element(val,sta))
    return new_soup

def get_case_numbers_from_soup(val):
    dates = val.get_text().rsplit("categories")[1].split("[")[1].split("]")[0]
    case_num = val.get_text().rsplit("data")[1].split("[")[1].split("]")[0]
    case_num_formatted=case_num.split(',')
    dates_formatted=dates.split(',')
    case_num_lst=[]
    date_lst = []

    for i in range(len(case_num_formatted)):
        if case_num_formatted[i] == "null":
            case_num_input = 0
        else:
            case_num_input = int(case_num_formatted[i])
        case_num_lst.append(case_num_input)

    for i in dates_formatted:
        date_lst.append(i.replace('"',''))
    return zip(date_lst,case_num_lst)

def get_case_dictionary(country="Worldwide"):
    soup = get_url_resp(country)
    new_soup1 = format_case_numbers(soup,country)
    val = get_both_elements(new_soup1)
    statuses_tuple = ("Cases","Deaths")
    statuses = {
        "Cases":0,
        "Deaths":1,
    }
    lst=[]
    for sta in statuses_tuple:
        lst.append(dict(get_case_numbers_from_soup(val[statuses[sta]][0])))
    return lst

Countries = ("Worldwide","China","US","Italy","Spain","Germany","France","UK","India","South-Korea","Iran","Netherlands","Belgium","Switzerland","Turkey","Sweden","Indonesia","Portugal")
statuses_tuple = ("Cases","Deaths")

data=[]
for country in Countries:
    country_data=get_case_dictionary(country=country)
    dates = list(country_data[0].keys())
    latest_date = dates[len(dates)-1]
    data.append(latest_date)
final_data = dict(zip(Countries,data))
current_datetime = get_current_datetime()

# filename="next update tracker.txt"

# with open(filename,"a") as file:
#     csv_writer = 

