from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
link = []

# XPATH Reference
# '''.//div[@class='print-list-item']/div/a/h3/span'''

for i in range(1,13):
    # url = "https://doctors.beaumont.org/search?sort=networks%2Crelevance&unified=Physician&page=" + str(i)
    # url = "https://doctors.beaumont.org/search?alias_term=Family%20Medicine&sort=networks%2Crelevance&specialty_synonym=Family%20Medicine.*&page=" + str(i)
    # url = "https://doctors.beaumont.org/search?alias_term=Cardiology&sort=networks%2Crelevance&specialty_synonym=Cardiology.*&page=" + str(i)
    # url = 'https://doctors.beaumont.org/search?alias_term=Pediatrics&sort=networks%2Crelevance&specialty_synonym=Pediatrics.*&page=' + str(i)
    url = 'https://doctors.beaumont.org/search?sort=networks%2Crelevance&unified=dermatology&page=' + str(i)
    # url = 'https://doctors.beaumont.org/search?alias_term=Neurology&sort=networks%2Crelevance&specialty_synonym=Neurology.*&page=' + str(i)
    driver.get(url)
    docs = driver.find_elements_by_class_name("css-tirmoe-ProviderInfo > h2 > a")
    for doc in docs:
        link.append(doc.get_attribute("href"))

NA = "NaN"
Photo = []
Name = []
Speciality = []
Address = []
Clinics = []
Contact_Details = []
Years_of_practice = []
About = []
Languages_Spoken = []
Age_Groups = []
Certifications = []
Rating = []
Consult_Online = []
Online_Visit = []
Email = []
Timings = []
Link = []

for l in link:
    driver.get(l)
    time.sleep(1)
    Link.append(l)
    Email.append(NA)
    Timings.append(NA)
    try:
        photo = driver.find_element_by_class_name("provider-image-lg").get_attribute("src")
        Photo.append(photo)
    except:
        Photo.append(NA)

    try:
        speciality = driver.find_element_by_id("specialty-list").text
        Speciality.append(speciality)
    except:
        Speciality.append(NA)

    try:
        name = driver.find_element_by_id("provider-name").text
        Name.append(name)
    except:
        Name.append(NA)

    try:
        addr = driver.find_element_by_css_selector(".col-xs-10.col-sm-10").text
        address = addr.split("Get Directions")[0]
        Address.append(address.rstrip("\n"))
        phone = addr.split("Get Directions")[1]
        Contact_Details.append(phone.lstrip("\n"))
    except:
        Address.append(NA)
        Contact_Details.append(NA)

    try:
        cli = driver.find_elements_by_id("about-panel-network_affiliations.name")
        clinics = '\n'.join([str(elem) for elem in cli[0].text.split("\n")[1:]])
        Clinics.append(clinics)
    except:
        Clinics.append(NA)

    try:
        practice = driver.find_element_by_id("about-panel-years_in_practice").text.split("\n")[1]
        Years_of_practice.append(practice)
    except:
        Years_of_practice.append(NA)

    try:
        gender = driver.find_element_by_id("about-panel-gender").text.split("\n")[1]
        education = '\n'.join([str(elem) for elem in driver.find_element_by_id("experience-training").text.split("\n")[1:]])
        About.append(gender + ",\nEducation :" + education)
    except:
        About.append(NA)

    try:
        languages = ','.join([str(elem) for elem in driver.find_element_by_id("about-panel-languages.language").text.split("\n")[1:]])
        Languages_Spoken.append(languages)
    except:
        Languages_Spoken.append(NA)

    try:
        age_groups = ','.join([str(elem) for elem in driver.find_element_by_id("about-panel-age_groups_seen.name").text.split("\n")[1:]])
        Age_Groups.append(age_groups)
    except:
        Age_Groups.append(NA)

    # try:
    #     ehr = ','.join([str(elem) for elem in driver.find_element_by_id("about-panel-ehr_platform").text.split("\n")[1:]])
    #     EHR.append(ehr)
    # except:
    #     EHR.append(NA)

    # try:
    #     practice_url = driver.find_element_by_id("about-panel-provider_practice_url").text.split("\n")[1]
    #     Practice_URL.append(practice_url)
    # except:
    #     Practice_URL.append(NA)

    # try:
    #     education = '\n'.join([str(elem) for elem in driver.find_element_by_id("experience-training").text.split("\n")[1:]])
    #     Education.append(education)
    # except:
    #     Education.append(NA)

    try:
        certifications = '\n'.join([str(elem) for elem in driver.find_element_by_id("experience-board_certifications").text.split("\n")[1:]])
        Certifications.append(certifications)
    except:
        Certifications.append(NA)

    try:
        rating = driver.find_element_by_class_name("css-63uvus-StyledAverageRating").text + \
                 " from\n" + driver.find_element_by_class_name("review-count").text
        Rating.append(rating)
    except:
        Rating.append(NA)

    # try:
    #     comment = driver.find_element_by_class_name("review-response").text
    #     Comment.append(comment)
    # except:
    #     Comment.append(NA)

    try:
        video_visit = driver.find_elements_by_css_selector("span.label.provider-badge.kyruus-config-tertiary-color")
        flag = 0
        for i in video_visit:
            if i.text == "OFFERING VIDEO VISITS":
                flag = 1
        if flag == 1:
            Consult_Online.append("Y")
        else:
            Consult_Online.append("N")
    except:
        Consult_Online.append("N")

    try:
        online_visit = driver.find_element_by_class_name("online-booking")
        print(online_visit.text)
        Online_Visit.append("Y")
    except:
        Online_Visit.append("N")

dic = {"Name": Name, "Photo": Photo, "About": About,
        "Degree": Certifications, "Phone": Contact_Details,
        "Email": Email, "Address": Address,
        "Specialization": Speciality,
        "Years of Experience": Years_of_practice, "Language": Languages_Spoken,
        "Rating": Rating, "Clinic Name": Clinics, "Timings": Timings,
        "Online Booking": Online_Visit, "Consult Online": Consult_Online,
        "Age Groups Treated": Age_Groups, "Link": Link}

print(len(Name))
print(len(Photo))
print(len(About))
print(len(Certifications))
print(len(Contact_Details))
print(len(Email))
print(len(Address))
print(len(Speciality))
print(len(Years_of_practice))
print(len(Languages_Spoken))
print(len(Link))
print(len(Rating))
print(len(Clinics))
print(len(Timings))
print(len(Online_Visit))
print(len(Consult_Online))
print(len(Age_Groups))

df = pd.DataFrame(dic)
# df.to_csv("USA_Docs.csv")
df.to_csv("USA_Docs.csv" , mode="a" , header= False)

driver.quit()
