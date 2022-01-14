from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

start = time.time()


# Input Name and Location
def Practo(location, name):
    print("\nSearching For : ")
    print(name, "In ", location, "From Practo ")

    driver.get("https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22Ayurveda"
               "%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city=Mumbai")

    if location != "Mumbai":
        location_box = driver.find_element_by_css_selector("input[data-qa-id ='omni-searchbox-locality']")
        location_box.click()

        cross = driver.find_element_by_class_name('c-omni-clear__icon')
        cross.click()
        time.sleep(2)

        location_box.send_keys(f'{location}')
        time.sleep(2)

        # Using Navigation keys, Selecting the location from the drop down list
        location_box.send_keys(Keys.DOWN)
        time.sleep(1)

        location_box.send_keys(Keys.DOWN)
        time.sleep(1)

        location_box.send_keys(Keys.RETURN)
        time.sleep(5)
        # Set the location to the user input location

    if name != "Ayurveda":
        doc_name_box = driver.find_element_by_css_selector("input[data-qa-id ='omni-searchbox-keyword']")
        doc_name_box.click()

        time.sleep(1)

        cross = driver.find_element_by_class_name('c-omni-clear__icon')
        cross.click()

        time.sleep(1)

        # Send the doctor name to the input box
        doc_name_box.send_keys(f'{name}')
        time.sleep(2)

        # Navigation Keys to move through the drop-down list
        doc_name_box.send_keys(Keys.DOWN)
        time.sleep(1)

        doc_name_box.send_keys(Keys.RETURN)
        time.sleep(10)
    print(driver.current_url)
    # Get the Name, Ratings/Votes Of the Fetched Result
    try:
        driver.find_element_by_class_name('listing-doctor-card')
        print("Top Results for ", name, "\n")

        # Change The Range to get More Doctors
        for _ in range(1):
            cards = driver.find_elements_by_class_name('listing-doctor-card')
            for card in cards:
                print("Name : ", card.find_element_by_class_name("doctor-name").text)
                try:
                    rat = card.find_element_by_css_selector("span[data-qa-id ='doctor_recommendation']").text
                except:
                    rat = "NaN"
                spec = card.find_element_by_class_name('u-grey_3-text > div > span').text
                print("Rating : ", rat)
                print("Speciality : ", spec)
                print()
            next = driver.find_element_by_css_selector("a[data-qa-id ='pagination_next']")
            next.click()
            time.sleep(2)
    except:
        try:
            print("Name : ", driver.find_element_by_class_name('c-profile__title').text)
            try:
                percent = driver.find_element_by_css_selector('span.u-green-text.u-bold.u-large-font').text
                votes = driver.find_element_by_css_selector('span.u-smallest-font.u-grey_3-text').text
            except:
                percent = votes = "NaN"
            print(percent, votes)
            try:
                rating = driver.find_element_by_class_name('common__star-rating').text
                print(rating, "stars out of 5")
            except:
                rating = "NaN"
            print("Rating : ", rating)
            spec = driver.find_element_by_css_selector("p[data-qa-id ='doctor-qualifications']").text
            print("Speciality : ", spec)
        except:
            print("No Results")
    print("--------------------------------------------------------------------------")


# Input Name and Location
def JustDial(location, name):
    # User Input of the location and Name
    # Just Hit Enter during Input to Use the default values
    print("\nSearching For : ")
    print(name, "in ", location, "From JustDial ")

    driver.get('https://www.justdial.com/Mumbai/search?q=Ayurvedic-Doctors')

    srch_box = driver.find_element_by_id('srchbx')
    srch_box_cross = driver.find_element_by_id('cross_S')
    driver.execute_script('arguments[0].click();', srch_box)
    driver.execute_script('arguments[0].click();', srch_box_cross)

    time.sleep(0.5)

    if location != "Mumbai":
        city_box = driver.find_element_by_id('city')
        driver.execute_script('arguments[0].click();', city_box)

        time.sleep(0.5)

        city_box.send_keys(location)
        time.sleep(1)

        city_box.send_keys(Keys.DOWN)
        time.sleep(1)

        city_box.send_keys(Keys.RETURN)
        time.sleep(1)

    # area = input("(Optional Hit Enter to Skip) Enter area : ")
    # if len(area) > 0:
    #     insrch_box = driver.find_element_by_id('insrch')
    #     insrch_box_cross = driver.find_element_by_id('cross')
    #     driver.execute_script('arguments[0].click();', insrch_box_cross)
    #
    #     insrch_box.send_keys(area)
    #     time.sleep(1)
    #     insrch_box.send_keys(Keys.DOWN)
    #     time.sleep(1)
    #     insrch_box.send_keys(Keys.RETURN)
    #     time.sleep(1)
    #     srch_box.send_keys(name)

    if name != "Ayurveda":
        driver.execute_script('arguments[0].click();', srch_box_cross)
        srch_box.send_keys(name)
        time.sleep(1)
        srch_box.send_keys(Keys.DOWN)
        time.sleep(1)
    srch_box.send_keys(Keys.RETURN)
    time.sleep(5)
    print(driver.current_url)
    try:
        print("Here are the top Results ")
        driver.find_element_by_class_name('cntanr')
        cards = driver.find_elements_by_class_name('cntanr')
        for card in cards:
            name = card.find_element_by_class_name('store-name').text.rstrip(".")
            try:
                rating = card.find_element_by_class_name('green-box').text
            except:
                rating = "NaN"
            spec = card.find_element_by_class_name('lng_commn').text
            print("Name : ", name)
            print("Rating : ", rating)
            print("Speciality : ", spec)
            print()
        print("-----------------------------------------------------------------")
    except:
        try:
            name = driver.find_element_by_class_name('fn').text
            try:
                rating = driver.find_element_by_class_name('rating').text
            except:
                rating = "NaN"
            spec = driver.find_element_by_css_selector('span.comp-text.also-list.more').text
            print("Name : ", name)
            print("Rating : ", rating)
            print("Speciality : ", spec)
        except:
            print("No doctors found ")
        print("--------------------------------------------------------------------")


# Input Just the Location and Choose Speciality
def Doctors360(location, chc):
    # User Input of the location and Name
    # Just Hit Enter during Input to Use the default values
    if chc == '2':
        speciality = "homeopath"
    else:
        speciality = "ayurveda"

    url = "https://www.doctor360.in/" + location.lower() + "/" + speciality
    print("Searching For ", speciality, " in ", location, "From Doctors360.in ")
    print(url)
    driver.get(url)

    print("Top ",speciality.capitalize()," doctors in ",location)
    # Change the range to get more pages
    for i in range(2):
        try:
            time.sleep(3)
            driver.find_element_by_css_selector('div.listing-item.text-left')
            cards = driver.find_elements_by_css_selector('div.listing-item.text-left')

            for card in cards:
                try:
                    name = card.find_element_by_class_name('docName').text
                    spec = card.find_element_by_class_name('specs').text
                    rats = len(card.find_elements_by_css_selector('i.flaticon.flaticon-star'))
                    print("Name : ", name)
                    print("Speciality : ", spec)
                    print("Rating : ", rats)
                    print()
                except:
                    break
            next = driver.find_elements_by_class_name('css-1gm22n8')[1]
            driver.execute_script('arguments[0].click();', next)
        except:
            print("No Doctors Found ")
    print("-----------------------------------------------------------------")


# ---(Check Error)----
# Input Location And Choose Speciality
def onemg(location, chc):
    if chc == '1':
        url = "https://www.1mg.com/doctors/homeopaths-in-" + location + "/SPC-7r017"
        print("Searching For Homeopathy in ", location, "From 1mg ")
    else:
        url = "https://www.1mg.com/doctors/ayurvedic-doctors-in-" + location + "/SPC-zodxj"
        print("Searching For Ayurveda in ", location, "From 1mg ")
    driver.get(url)
    print(driver.current_url)
    time.sleep(2)

    try:
        driver.find_element_by_css_selector('div.col.s12.hide-on-large-only')
        cards = driver.find_elements_by_class_name('DoctorName__name___2fjjE > a')
        names = [c.text for c in cards[::2]]
        cards = [c.get_attribute("href") for c in cards[::2]]

        for i in range(len(cards)):
            driver.get(cards[i])
            time.sleep(1.5)
            print("Name : ", names[i])
            print("Rating : ", driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div/div/div/div[2]/'
                    'div[3]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div[2]/span').text)
    except:
        print("No doctors found")
    print("---------------------------------------------------------------------------------")


# Input Location And Choose Between Speciality or Searching By Name
def lybrate(location, lybrate_name):
    driver.get('https://www.lybrate.com/search?find=Ayurvedic%20Doctor&near=&cityName=Mumbai')

    if location != 'Mumbai':
        location_cross = driver.find_element_by_id('clearCityIcon')
        driver.execute_script('arguments[0].click();', location_cross)
        location_box = driver.find_element_by_id('ex1_value')

        driver.execute_script('arguments[0].click();', location_box)
        location_box.send_keys(location)
        time.sleep(2)
        srch_btn = driver.find_element_by_css_selector('div.primary.flat')
        driver.execute_script('arguments[0].click();', srch_btn)
        time.sleep(2)

    chc = lybrate_name[0]

    if chc == '2':
        print("Searching For Homeopathy in ", location, "From lybrate ")
        name_box = driver.find_element_by_id('ex3_value')
        name_cross = driver.find_element_by_id('clearSpecialityIcon')
        driver.execute_script('arguments[0].click();', name_cross)
        name_box.send_keys("Homeopath")
        srch_btn = driver.find_element_by_css_selector('div.primary.flat')
        driver.execute_script('arguments[0].click();', srch_btn)
        time.sleep(1)

        print(driver.current_url)

    elif chc == "3":
        name = lybrate_name[1]
        print("Searching For", name, " in ", location, "From lybrate ")
        time.sleep(5)
        name_box = driver.find_element_by_id('ex3_value')
        name_cross = driver.find_element_by_id('clearSpecialityIcon')
        driver.execute_script('arguments[0].click();', name_cross)
        name_box.send_keys(name)
        time.sleep(3)
        name_box.send_keys(Keys.DOWN)
        time.sleep(2)
        name_box.send_keys(Keys.RETURN)
        time.sleep(10)

        print(driver.current_url)
        try:
            name = driver.find_element_by_css_selector("h1[itemprop ='name']").text
            spec = driver.find_element_by_css_selector("span[itemprop ='medicalSpecialty']").text
            try:
                rats = driver.find_element_by_css_selector("span[itemprop ='aggregateRating']").text
            except:
                rats = "No Rating"
            print("Name : ", name)
            print("Speciality : ", spec)
            print("Rating : ", rats)
        except:
            print("No Doctors Found")
        print("-------------------------------------------------------")
        return

    else:
        print("Searching for Ayurveda in ", location, "From lybrate ")
        print(driver.current_url)

    time.sleep(5)

    try:
        driver.find_element_by_class_name("ly-doctor")

        print("Here are the top results : ")
        cards = driver.find_elements_by_class_name("ly-doctor")

        for card in cards:
            try:
                name = card.find_element_by_class_name('ly-doctor__name').text
                spec = card.find_element_by_css_selector("div[ng-if ='ctrl.profile.specialityName']").text
                try:
                    rating = card.find_element_by_class_name('lybText--green').text
                except:
                    rating = "No Rating"
                print("Name : ", name)
                print("Speciality : ", spec)
                print("Rating : ", rating)
                print()
            except:
                continue
    except:
        print("No Doctors Found")
    print("---------------------------------------------------------")


options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.maximize_window()

# User Input of the location and Name
# Just Hit Enter during Input to Use the default values
location = input("Enter the Location : ")
if len(location) == 0:
    location = "Mumbai"

chc = input("Press 1 to Search For Ayurveda\n"
            "Press 2 to Search For Homeopathy\n"
            "Press 3 to Search By Doctor Name (For all websites except Docs360 and 1mg)\n"
            "-> ")

if chc == "2":
    practo_name = "Homeopathy"
    justd_name = "Homeopathy"
    docs360_name = "2"
    onemg_name = "1"
    lybrate_name = ("2",None)
elif chc == "3":
    name = input("Enter Doctor's Name : ")
    if len(name) == 0:
        name = "Rajshree Chavan"
    practo_name = name
    justd_name = name
    docs360_name = "1"
    onemg_name = "2"
    lybrate_name = ("3",name)
else:
    practo_name = "Ayurveda"
    justd_name = "Ayurveda"
    docs360_name = "1"
    onemg_name = "2"
    lybrate_name = ("1", None)

print("--------------------------------------------------------------")

# Created Functions for each website.
# Uncomment the function as per the website needed

try:
    Practo(location.capitalize(), practo_name)
except Exception as e:
    print("Practo Error ", e)

try:
    JustDial(location.capitalize(), justd_name)
except Exception as e:
    print("JustDial Error ", e)

try:
    Doctors360(location.lower(), docs360_name)
except Exception as e:
    print("Doctors360 Error ", e)

# Error, *Check*
try:
    onemg(location.lower(), onemg_name)
except Exception as e:
    print("Onemg Error ", e)

try:
    lybrate(location.capitalize(), lybrate_name)
except Exception as e:
    print("Lybrate Error ", e)

stop = time.time()
print("Total Time Taken = ", stop - start)

driver.quit()
