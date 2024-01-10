import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook, load_workbook 

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)







        
url = "https://www.ss.com/lv/transport/cars/search/"
driver.get(url)

time.sleep(2)
cenaNo = driver.find_element(By.NAME, value="topt[8][min]")
cenaLidz = driver.find_element(By.NAME, value="topt[8][max]")

TehniskaOpt = driver.find_element(By.NAME, value="opt[223][]")
TehniskaOpt.click()

print("Ievadiet mašīnas cenu no")
cn = input()
print("Ievadiet mašīnas cenu līdz")
cl = input()
cenaNo.send_keys(cn)
cenaLidz.send_keys(cl)


option = driver.find_element(By.XPATH, "//option[@value='Yes']")
option.click()
option.click()

meklet = driver.find_element(By.XPATH, "//input[@value='Meklēt']")
time.sleep(1)
meklet.click()
time.sleep(2)


time.sleep(2)
masinas = driver.find_elements(By.XPATH, "//tr[starts-with(@id, 'tr_')]")
masina_count = len(masinas)

for i in range(masina_count):
    current_masinas = driver.find_elements(By.XPATH, "//tr[starts-with(@id, 'tr_')]")
    current_masinas[i].click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

# webTabula = []
# name=[]

# with open("people.csv", "r") as file:
#     next(file)
#     for line in file:
#         row=line.rstrip().split(",")
#         vards = row[2] + " " + row[3]
#         name.append(vards)
# for n in name:

#     input.clear()
#     input.send_keys(n)



#     output = driver.find_element(By.ID, "output")
#     result = output.get_attribute('value')  
#     webTabula.append(result)
    


# workbook = load_workbook('salary.xlsx')
# sheet = workbook.active
# final = []
  

# for i,code in enumerate(webTabula): 
#     for row in range(2, sheet.max_row + 1):
#         excel_code = sheet.cell(row, 1).value 
#         if excel_code == code:
#             value = sheet.cell(row, 2).value 
#             kopa = name[i] + "  " + str(value)
#             final.append(kopa)

# sum = {}
# for c in final:
#     var, alga = c.strip().split("  ")
#     alga = int(alga)
#     if var in sum:
#         sum[var] += alga
#     else:
#         sum[var] = alga 

# for var, total in sum.items():
#     print(var+ " " + str(total))
            







