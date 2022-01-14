from selenium import webdriver
import time
import pandas as pd
import random

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

Age = []; Gender = [];NA = "NaN"
Symptom1 = []; Symptom2 = []; Symptom3 = []
Symptom4 = []; Symptom5 = []
Q1 = []; O1 = []; A1 = []
Q2 = []; O2 = []; A2 = []
Q3 = []; O3 = []
Q4 = []; O4 = []
C1 = []; M1 = []
C2 = []; M2 = []
C3 = []; M3 = []
C4 = []; M4 = []
C5 = []; M5 = []

for i in range(50):
    driver.get("https://symptoms.webmd.com/")

    # first page
    inputAge = driver.find_element_by_id("age")
    inputGenderMale = driver.find_element_by_id("female")  # change 'male' to 'female' for female gender
    buttonContinue = driver.find_element_by_xpath(
        '//*[@id="ContentPane30"]/div/div[1]/div/div[2]/div/div/div[2]/button')
    inputAge.send_keys('40')
    inputGenderMale.click()
    buttonContinue.click()
    time.sleep(2)

    # second page
    df = pd.read_csv('Symptoms.csv')

    sym = list(df['Symptoms'])

    inputSymptons = driver.find_element_by_xpath(
        '//*[@id="ContentPane30"]/div/div[1]/div/div[3]/div[1]/div[1]/div[2]/input')
    for _ in range(0, random.randint(2,4)):
        try:
            inputSymptons.send_keys(f'{random.choice(sym)}')
            time.sleep(2.5)
            inputSymptons.send_keys(Keys.ARROW_DOWN)
            time.sleep(2.5)
            inputSymptons.send_keys(Keys.ENTER)
            try:
                skip = driver.find_element_by_css_selector('div.link.skip-alone-link')
                driver.execute_script("arguments[0].click();", skip)
            except:
                pass
        except Exception as e:
            print(e)

    continue_button = driver.find_element_by_css_selector('button.solid-button.continue-button')
    driver.execute_script("arguments[0].click();", continue_button)
    time.sleep(1)

    # Third Page
    try:
        Qs = driver.find_elements_by_class_name('preg-sel')
        Q1.append(Qs[0].text.split("\n")[0])
        try:
            O1.append(Qs[0].find_element_by_class_name('primary-symptom-container').text)
            A1.append(Qs[0].find_element_by_class_name('primary-symptom-container').text.split("\n")[0])
        except:
            O1.append(NA)
            A1.append(NA)
    except:
        Q1.append(NA)
        O1.append(NA)
        A1.append(NA)

    try:
        Qs = driver.find_elements_by_class_name('preg-sel')
        Q2.append(Qs[1].text.split("\n")[0])
        O2.append("Yes,No")
        A2.append("No")
    except:
        Q2.append(NA)
        O2.append(NA)
        A2.append(NA)

    try:
        Q3.append(driver.find_element_by_class_name('current-medication').text)
        O3.append("Enter current medication")
    except:
        Q3.append(NA)
        O3.append(NA)

    try:
        Q4.append(driver.find_element_by_class_name('past-condition').text)
        O4.append("Enter Past Condition(s)")
    except:
        Q4.append(NA)
        O4.append(NA)
    time.sleep(1)
    continue_button = driver.find_element_by_css_selector('button.solid-button.continue-button')
    driver.execute_script("arguments[0].click();", continue_button)
    time.sleep(1)

    # Fourth Page
    # try:
    #     more = driver.find_element_by_class_name('button-text')
    #     driver.execute_script("arguments[0].click();", more)
    #     driver.execute_script("arguments[0].click();", more)
    # except: pass
    #
    # time.sleep(1)

    try:
        condition_box = driver.find_elements_by_class_name('single-condition')

        try:
            text = condition_box[0].find_element_by_class_name('single-condition-row').text
            C1.append(text.split('\n')[0])
            M1.append(text.split('\n')[1])
        except:
            C1.append(NA)
            M1.append(NA)

        try:
            text = condition_box[1].find_element_by_class_name('single-condition-row').text
            C2.append(text.split('\n')[0])
            M2.append(text.split('\n')[1])
        except:
            C2.append(NA)
            M2.append(NA)

        try:
            text = condition_box[2].find_element_by_class_name('single-condition-row').text
            C3.append(text.split('\n')[0])
            M3.append(text.split('\n')[1])
        except:
            C3.append(NA)
            M3.append(NA)

        try:
            text = condition_box[3].find_element_by_class_name('single-condition-row').text
            C4.append(text.split('\n')[0])
            M4.append(text.split('\n')[1])
        except:
            C4.append(NA)
            M4.append(NA)

        try:
            text = condition_box[4].find_element_by_class_name('single-condition-row').text
            C5.append(text.split('\n')[0])
            M5.append(text.split('\n')[1])
        except:
            C5.append(NA)
            M5.append(NA)
    except:
        C5.append(NA)
        M5.append(NA)
        C4.append(NA)
        M4.append(NA)
        C3.append(NA)
        M3.append(NA)
        C2.append(NA)
        M2.append(NA)
        C1.append(NA)
        M1.append(NA)

    try:
        details = driver.find_element_by_class_name('right-container').text.split('\n')
        Gender.append(details[0].split(' ')[1])
        Age.append(details[1].split(' ')[1])
        try:
            Symptom1.append(details[4].split(",")[0])
        except:
            Symptom1.append(NA)
        try:
            Symptom2.append(details[4].split(",")[1])
        except:
            Symptom2.append(NA)

        try:
            Symptom3.append(details[4].split(",")[2])
        except:
            Symptom3.append(NA)

        try:
            Symptom4.append(details[4].split(",")[3])
        except:
            Symptom4.append(NA)

        try:
            Symptom5.append(details[4].split(",")[4])
        except:
            Symptom5.append(NA)

    except:
        Gender.append("Male")
        Age.append("21")
        Symptom1.append(NA)
        Symptom2.append(NA)
        Symptom3.append(NA)
        Symptom4.append(NA)
        Symptom5.append(NA)

driver.quit()

print(len(Age), len(Symptom1), len(Gender))
print(len(Symptom2),len(Symptom3),len(Symptom4),len(Symptom5))
print(len(Q1), len(O1), len(Q2), len(O2))
print(len(Q3), len(O3), len(Q4), len(O4))
print(len(C1), len(M1), len(C2), len(M2))
print(len(C3), len(M3), len(C4), len(M4))
print(len(C5), len(M5))


dic = {"Gender": Gender, "Age": Age,
       "Symptom1": Symptom1, "Symptom2": Symptom2,
       "Symptom3": Symptom3, "Symptom4": Symptom4,
       "Symptom5": Symptom5,
       "Question 1": Q1, "Option 1": O1,"Answer 1":A1,
       "Question 2": Q2, "Option 2": O2,"Answer 2":A2,
       "Question 3": Q3, "Option 3": O3,
       "Question 4": Q4, "Option 4": O4,
       "Condition 1": C1, "Match 1": M1,
       "Condition 2": C2, "Match 2": M2,
       "Condition 3": C3, "Match 3": M3,
       "Condition 4": C4, "Match 4": M4,
       "Condition 5": C5, "Match 5": M5}

df = pd.DataFrame(dic)

df.to_csv("WebMd.csv", mode='a', header=False)
