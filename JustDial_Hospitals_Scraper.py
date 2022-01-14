from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

link = []
Type = []
Name = []
Photo = []
About = []
Phone = []
Address = []
City = []
State = []
Country = []
Discipline = []
Timings = []
Amenites = []
Pay = []
Rating = []
Votes = []
Verified = []
Year = []
Website = []
FB = []

NA = "NaN"
# '<span class="lng_cont_name">Hcg Ics Khubchandani Cancer..</span>'


def strings_to_num(ph):
    switcher = {
        'dc': '+',
        'fe': '(',
        'hg': ')',
        'ba': '-',
        'acb': '0',
        'yz': '1',
        'wx': '2',
        'vu': '3',
        'ts': '4',
        'rq': '5',
        'po': '6',
        'nm': '7',
        'lk': '8',
        'ji': '9'
    }
    num = ""
    for p in ph:
        num += switcher[p.get_attribute('class').split('-')[1]]
    return num


for i in range(50,51):
    # url = 'https://www.justdial.com/Mumbai/Public-Hospitals/nct-10393816/page-' + str(i)
    # url = 'https://www.justdial.com/Mumbai/Chemists/nct-10096237'
    # url = 'https://www.justdial.com/Pune/Public-Hospitals/nct-10393816'
    # url = 'https://www.justdial.com/Pune/Chemists/nct-10096237'
    url = 'https://www.justdial.com/Pune/Pathology-Labs/nct-10356131'
    driver.get(url)
    time.sleep(10)

    store = driver.find_elements_by_class_name('cntanr')

    for s in store:
        link.append(s.find_element_by_class_name('jcn > a').get_attribute('href'))
        ph = s.find_elements_by_class_name('mobilesv')
        number = strings_to_num(ph)
        try:Photo.append(s.find_element_by_class_name('altImgcls').get_attribute('src'))
        except:Photo.append(NA)
        Phone.append(number)

for l in link:
    print(link.index(l) + 1, '\t', l)
    driver.get(l)
    time.sleep(1)
    City.append("Pune")
    State.append("Maharashtra")
    Country.append("India")
    Type.append("Pathology Labs")
    Discipline.append("Pathology Labs, CT scan centers , Pathology Sevices")

    try:
        bt = driver.find_element_by_id("vhall")
        driver.execute_script("arguments[0].click();", bt)
        time.sleep(1)
        open = ','.join([str(elem) for elem in driver.find_element_by_id("mhd").text.split(")")[1].split("\n")])
        Timings.append(open)
    except:
        Timings.append(NA)

    try:
        Name.append(driver.find_element_by_class_name("rstotle > span > span").text)
    except:
        Name.append(NA)

    try:
        Rating.append(driver.find_element_by_class_name("total-rate > span").text)
    except:
        Rating.append(NA)

    try:
        Votes.append(driver.find_element_by_class_name("rtngsval > span").text)
    except:
        Votes.append(NA)

    try:
        driver.find_element_by_class_name("jd_verified")
        Verified.append("Y")
    except:
        Verified.append("N")

    try:
        Address.append(driver.find_element_by_id("fulladdress").text)
    except:
        Address.append(NA)

    try:
        web = driver.find_elements_by_class_name("mreinfp.comp-text > a")
        web = ' , '.join([str(elem) for elem in [w.get_attribute("href") for w in web if w.get_attribute("href")]])
        Website.append(web)
    except:
        Website.append(NA)

    try:
        amn = ','.join([str(elem) for elem in driver.find_element_by_id("qckinf").text.split("Quick Information")[1].split('\n')])
        Amenites.append(amn)
    except:
        Amenites.append(NA)

    try:
        Pay.append(','.join([str(elem.text) for elem in driver.find_elements_by_class_name('lng_mdpay')]))
    except:
        Pay.append(NA)

    try:
        try:
            year = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/div[1]/div[8]/ul/li').text
        except:
            year = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/div[1]/div[6]/ul/li').text
        Year.append(year)
    except:
        Year.append(NA)

    try:
        FB.append(driver.find_element_by_class_name("social_media_icons > a").get_attribute("href"))
    except: FB.append(NA)

    try:
        About.append(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/div[2]/div[7]/span/p[4]').text.split(".")[0])
    except:About.append(NA)

print("\n-------------------------------------------\n")
print(len(Name))
print(len(About))
print(len(Photo))
print(len(Phone))
print(len(Address))
print(len(City))
print(len(Discipline))
print(len(Timings))
print(len(Amenites))
print(len(Rating))
print(len(Pay))
print(len(Timings))
print(len(Votes))
print(len(Year))
print(len(Website))
print(len(FB))
print(len(link))


dic = {"Name": Name, "Photo": Photo,
       "About": About, "Phone": Phone,
       "City": City, "Address": Address,
       "State": State, "Website": Website,
       "Year Established": Year, "Country": Country,
       "Rating": Rating, "Discipline": Discipline, "Timings": Timings,
       "Amenities": Amenites, "Mode of Payment": Pay,
       "Votes": Votes, "Link": link, "Facebook": FB,
       "Verified": Verified, "Type": Type}

df = pd.DataFrame(dic)
# df.to_csv("USA_Docs.csv")
df.to_csv("Pune_Hospitals.csv", mode="a", header=False)

driver.quit()
