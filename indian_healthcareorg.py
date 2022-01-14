from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

NA = "NaN"
Name = []; Photo = []; Address = []
Landline = []; Mobile = []; email = []
Website = []; TotalBeds = []; ICUBeds = []
Operatingrooms = []; Intlarr = []
NABH = []; NABL = []; ISO = []
AppointmentLink = []; Language = []
Room = []; Payment=[]; Link = []
i = 0

url = 'https://www.indiahealthcare.org/?speciality=Cardiology'

driver.get(url)
time.sleep(10)
# print(driver.current_window_handle)
names = driver.find_elements_by_class_name("hospital-name")

for name in names:
    driver.execute_script("arguments[0].click();", name)
    i += 1
    time.sleep(1)
    Name.append(name.text)
    driver.switch_to.window(driver.window_handles[i])
    time.sleep(1)
    # print(driver.current_window_handle)

    try:
        Link.append(driver.current_url)
    except:Link.append(NA)

    try:
        address = driver.find_element_by_class_name("hospital-content").text
        Address.append(address.split('ADDRESS')[1].lstrip('\n'))
    except:Address.append(NA)

    try:
        Photo.append(driver.find_element_by_id('banner_image').get_attribute('src'))
    except:Photo.append(NA)

    try:
        TotalBeds.append(driver.find_element_by_id('beds_count').text)
    except:TotalBeds.append(NA)

    try:
        ICUBeds.append(driver.find_element_by_id('icu_beds').text)
    except:ICUBeds.append(NA)

    try:
        Operatingrooms.append(driver.find_element_by_id('operating_rooms').text)
    except:Operatingrooms.append(NA)

    try:
        Intlarr.append(driver.find_element_by_id('intl_patients').text)
    except:Intlarr.append(NA)

    try:
        Landline.append(driver.find_element_by_xpath('/html/body/section/hospital-data/div/div/div[2]/div[3]/div[1]/p[2]').text)
    except:Landline.append(NA)

    try:
        Mobile.append(driver.find_element_by_xpath('/html/body/section/hospital-data/div/div/div[2]/div[3]/div[2]/p[2]').text)
    except:Mobile.append(NA)

    try:
        Website.append(driver.find_element_by_xpath('/html/body/section/hospital-data/div/div/div[2]/div[3]/div[3]/p[2]/b/a').text)
    except:Website.append(NA)

    try:
        email.append(driver.find_element_by_xpath('/html/body/section/hospital-data/div/div/div[2]/div[3]/div[4]/p[2]/b').text)
    except:email.append(NA)

    # Accreditions Photo
    try:
        cert = [c.text for c in driver.find_elements_by_class_name('mr-4')]
        if "NABH" in cert:
            NABH.append("https://www.indiahealthcare.org/static/images2/NABH%202.png")
        else:
            NABH.append("N")
        if "NABL" in cert:
            NABL.append("https://www.indiahealthcare.org/static/images2/NABL.jpeg")
        else:
            NABL.append("N")
        if "ISO" in cert:
            ISO.append("https://www.indiahealthcare.org/static/images2/ISO.png")
        else:
            ISO.append("N")
    except:
        NABH.append("N")
        NABL.append("N")
        ISO.append("N")

    try:
        items = driver.find_elements_by_class_name('hospital-item-card')
        app_count = 0
        lang_count = 0
        room_count = 0
        pay_count = 0

        for item in items:
            if item.find_element_by_class_name('hospital-item-card_heading').text == 'APPOINTMENT LINK':
                AppointmentLink.append(item.find_element_by_class_name('hospital-item-card_value').text)
                app_count = 1
            if item.find_element_by_class_name('hospital-item-card_heading').text == 'LANGUAGES':
                Language.append(",".join(item.find_element_by_class_name('hospital-item-card_value').text.split("\n*")).lstrip("*"))
                lang_count = 1
            if item.find_element_by_class_name('hospital-item-card_heading').text == 'ROOMS':
                Room.append(",".join(item.find_element_by_class_name('hospital-item-card_value').text.split("\n*")).lstrip("*"))
                room_count = 1
            if item.find_element_by_class_name('hospital-item-card_heading').text == 'PAYMENT MODES':
                Payment.append(",".join(item.find_element_by_class_name('hospital-item-card_value').text.split("\n*")).lstrip("*"))
                pay_count = 1
        if app_count == 0:
            AppointmentLink.append("NaN")
        if lang_count == 0:
            Language.append("NaN")
        if room_count == 0:
            Room.append("NA")
        if pay_count == 0:
            Payment.append("NA")
    except:
        AppointmentLink.append("NaN")
        Language.append("NaN")
        Room.append("NA")
        Payment.append("NA")

    driver.switch_to.window(driver.window_handles[0])

dic = {"Name": Name, "Address": Address,
       "Phone Landline": Landline, "Phone Mobile": Mobile,
       "Email": email, "Languages Spoken": Language,
       "Rooms":Room,"Payment Methods": Payment,
       "Total Beds in Hospital": TotalBeds,"ICU Beds in Hospital": ICUBeds,
       "Operating Rooms in Hospital": Operatingrooms,
       "International arrivals per year": Intlarr,"NABH Certified":NABH,
       "NABL Certified": NABL,"ISO Certified":ISO,
       "Appointment Link":AppointmentLink,"Website": Website,"Link":Link
       }

df = pd.DataFrame(dic)
df.to_csv("Hospitals.csv", mode="a", header=False)
driver.quit()
