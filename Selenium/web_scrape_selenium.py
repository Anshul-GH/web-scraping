from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os

# launch url
url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"

# create a new firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

# after opening the URL above, Selenium clicks the specific agency link
python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33')
python_button.click()

# Selenium hands the page source back to Beautiful Soup
soup_level_1 = BeautifulSoup(driver.page_source, 'lxml')

# empty list
datalist = []

# counter
x = 0

# beautiful Soup finds all the job title links on the agency page and the loop begins
for link in soup_level_1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):

    # Selenium visits each job title page
    python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
    python_button.click() #click link

    # Again Selenium hands off the source of the specific job page to Beautiful Soup
    soup_level_2 = BeautifulSoup(driver.page_source, 'lxml')

    # Beautiful Soup grabs the HTML table on the page
    table = soup_level_2.find_all('table')[0]

    # passing the HTML table to pandas to put it in a dataframe
    df = pd.read_html(str(table), header=0)

    # store the dataframe in a list - list will be a collection of dataframes eventually
    datalist.append(df[0])

    # ask Selenium to click the back button
    driver.execute_script('window.history.go(-1)')

    # increment the counter by 1 before starting over the loop again
    x += 1

    # end of loop

# end the Selenium browser session
driver.quit()

# combine all the pandas dataframe in the list into one big dataframe
result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))], ignore_index=True)

# convert the pandas dataframe to JSON
json_records = result.to_json(orient='records')

# pretty print to CLI with tabulate
print(tabulate(result, headers=["Employee Name","Job Title","Overtime Pay","Total Gross Pay"], tablefmt='psql'))

# get current working directory
path = os.getcwd()

# open, write and close the json file
f = open(path + '/fshu_payroll_data.json', 'w')
f.write(json_records)
f.close()

