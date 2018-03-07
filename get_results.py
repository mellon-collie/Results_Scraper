from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
count = 0
for i in range(1,490):
    driver.get("https://www.pesuacademy.com/Academy/r/results")
    if(i<100):
        i = '{0:03}'.format(i)  # to get 001, 002, 003 etc      
    usn = '01FB16ECS'+str(i)
    usn_wait = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"usn"))) #to handle ElementNotFoundException
    usn_box = driver.find_element_by_name("usn")
    usn_box.send_keys(usn) #enter usn in text field
    driver.implicitly_wait(10)
    capche_wait = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"capche")))
    capcha = driver.find_element_by_id("capche")
    expression = capcha.text
    values = [int(s) for s in expression.split() if s.isdigit()] #extract operands from expression
    answer = 0
    if '+' in expression:
        answer = values[0]+values[1]
    elif '-' in expression:
        answer = values[0]-values[1]
    elif '*' in expression:
        answer = values[0]*values[1] 
    elif '/' in expression:
        answer = int(values[0]/values[1])  
    

    capche_val_wait = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"capcheVal")))
    capcha_box = driver.find_element_by_name("capcheVal")
    capcha_box.send_keys(answer) #enter the capcha answer in the text field
    driver.find_element_by_css_selector("button.btn.btn-primary").click()
    table = driver.find_element_by_css_selector("table.table-condensed.table-bordered")
    for i in range(0,len(table.find_elements_by_css_selector("tbody tr"))):
        row = table.find_elements_by_css_selector("tbody tr")[i]
        grades = row.find_elements_by_css_selector("td")
        if grades[0].text == "SGPA":
            sgpa = grades[1].text
            if(sgpa!="TAL"):
                if(float(sgpa)>=9.22):
                    count = count + 1
                    print(count)
                    print(sgpa)
