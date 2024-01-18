# SS.com Tehniskās apskates meklētājs ar Selenium

# Video ar skripta palaišanu
https://youtu.be/h6C2nKghh50



## Programmas uzdevums
Programma atver ss.com automašīnas meklēšanas lapu un dod iespēju lietotājam perosnalizēt savu meklēšanu un programma piedāvā lietotājam ievadīt tehniskās apskates termiņu (ss.com tādas opcijas nav). Pēc Teh. apsk termiņa ievadīšanas, programma iziet cauri katram sludinājumam un pārbauda vai termiņš atbilst lietotāja vēlamajam. Kad tiek iziets cauri visiem sluidinājumiem, visi atbilstošie sludinājumi tiek saglabāti excel failā, kas ir pievienots šajā repository. Programma dod iespēju šo excel dokumentu saglabāt.

## Bilbliotēkas skaidrojums

### Selenium ir bibliotēka, kas piedāvā iespēju automatizēt tīmekļa pārlūkprogrammas darbību. To izmanto, lai iegūtu informāciju no tīmekļa vietnēm.
    from selenium import webdriver

###  Selenium bibliotēkas daļa, kas piedāvā dažādus pārlūkprogrammu vadītājus, piemēram, Chrome, Firefox u.c. Šajā programmā tiek izmantots Chrome vadītājs (webdriver.Chrome).
    from selenium.webdriver.chrome.service import Service

###  Chrome pārlūkprogrammas serviss, kas tiek izmantots, lai inicializētu Chrome vadītāju.
    from selenium.webdriver.chrome.service import Service

###  "By" ir daļa no Selenium. Izmanto lai identificētu HTML elementus pēc to atribūtiem, piemēram, pēc ID, klases vai teksta.
    from selenium.webdriver.common.by import By

###  Time izmanto, lai iepauzētu programmas darbības. Šajā programmā izmanto, lai mājaslapa paspētu inicilizēties pirms nākamās programmas darbības.
        import time

### openpyxl dod iespēju apstrādāt Excel failus.
    from openpyxl import Workbook, load_workbook

### NoSuchElementException ir daļa no Selenium un tiek izmantota, lai apstrādātu izņēmumus, kas saistīti ar HTML elementu meklēšanu, kad elements nav atrasts.
    from selenium.common.exceptions import NoSuchElementException

###  ScrollOrigin un ActionChains dod iespēju patīt lapu
    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

### date un datetime piedāvā laika manipulācijas iespējas. Šajā programmā tiek izmantots, lai iegūtu pašreizējo datumu un izrēķinātu tehniskās apskates termiņu.
    from datetime import date





## Koda skaidrojums

### Inicializē Selenium servisu un opcijas
    service = Service()
    option = webdriver.ChromeOptions()
### Izveido Chrome pārlūkprogrammas vadītāju
    driver = webdriver.Chrome(service=service, options=option)

### Ielādē esošo Excel darba grāmatu un aktīvo lapu
    workbook = load_workbook('AtrastāsMašīnas.xlsx') 
    sheet = workbook.active

### Nosaka pašreizējo rindu, kur ievietot jaunos datus
    current_row = sheet.max_row + 1

### Nosaka šodienas datumu
    today = date.today()
    sodiena = today.strftime("%m/%Y")
    print("Today's date:", sodiena)

### Iestata mājaslapu
    url = "https://www.ss.com/lv/transport/cars/search/"
    driver.get(url)

### Apstādina programmu uz 2 sekundēm, lai lapai pilnībā ielādētos
    time.sleep(2)

### Atrast un iegūt cenas diapazona ievades laukus
    cenaNo = driver.find_element(By.NAME, value="topt[8][min]")
    cenaLidz = driver.find_element(By.NAME, value="topt[8][max]")

### Atver "Tehniskā apskate" izvēlni
    TehniskaOpt = driver.find_element(By.NAME, value="opt[223][]")
    TehniskaOpt.click()

### Lietotājam jāievada automašīnas cenas diapazons
    print("Ievadiet mašīnas cenu no")
    cn = input()
    print("Ievadiet mašīnas cenu līdz")
    cl = input()
    cenaNo.send_keys(cn)
    cenaLidz.send_keys(cl)

### Lietotājam jāievada vēlamo tehniskās apskates ilgumu mēnešos
    print("Ievadiet vēlamo tehniskās apskates ilgumu (mēnešos)")
    men = input()
    menTeh = int(men)

### Izvēlas "Jā" opciju tehniskajai apskatei
    option = driver.find_element(By.XPATH, "//option[@value='Yes']")
    option.click()
    option.click()

### Atrast un noklikšķināt uz "Meklēt" pogas
    meklet = driver.find_element(By.XPATH, "//input[@value='Meklēt']")
    time.sleep(1)
    meklet.click()
    time.sleep(2)

### Patin lapu uz leju, lai iegūtu visu automašīnu ierakstu informāciju
    scroll_origin = ScrollOrigin.from_viewport(10, 10)
    ActionChains(driver)\
        .scroll_from_origin(scroll_origin, 0, 99999)\
        .perform()
    time.sleep(2)

### Atrast un iegūt visus automašīnu ierakstus
    masinas = driver.find_elements(By.XPATH, "//tr[starts-with(@id, 'tr_')]")
    masina_count = len(masinas)
    time.sleep(1)

### Pirmo lappas pusi maina uz 2. lappaspusi
    page_number = 2

### Atrod un noklikšķina uz nākamās lapas pogas
     button = driver.find_element(By.XPATH, "//a[contains(@href, 'page" + str(page_number) + ".html')]")
        
### Atver katru automašīu sludinājumu pašreizējā lapā
    for i in range(masina_count-1):
                try:
                    ### Noklikšķina uz konkrētās automašīnas
                    time.sleep(1)
                    current_masinas = driver.find_elements(By.XPATH, "//tr[starts-with(@id, 'tr_')]")
                    time.sleep(1)
                    current_masinas[i].click()
                    time.sleep(1)
 ### Iegūst un pārbauda tehniskās apskates datumu
     tehniska = driver.find_element(By.ID, "tdo_223")
                    print(tehniska.text)
                    datums = datetime.strptime(tehniska.text, "%m.%Y").date()
                    if datums.year == 2023:
                        difference = 0
                    elif datums.year > 2024:
                        diffrence = 999
                        
     else:
     difference = datums.month - today.month

### Ja tehniskā apskate ir pietiekami ilga, tad saglabā datus
       if difference >= menTeh: 
                        print("OK")
                        marka = driver.find_element(By.ID, "tdo_31")
                        markaText = marka.text
                        gads = driver.find_element(By.ID, "tdo_18")
                        gadsText = gads.text
                        motors = driver.find_element(By.ID, "tdo_15")
                        motorsText = motors.text
                        nobraukums = driver.find_element(By.ID, "tdo_16")
                        nobraukumsText = nobraukums.text
                        teha = driver.find_element(By.ID, "tdo_223")
                        tehaText = teha.text 
                        
     links = driver.current_url

 ### Ievieto datus Excel failā
     sheet.cell(row=current_row, column=1, value=markaText)
                        sheet.cell(row=current_row, column=2, value=gadsText)
                        sheet.cell(row=current_row, column=3, value=motorsText)
                        sheet.cell(row=current_row, column=4, value=nobraukumsText)
                        sheet.cell(row=current_row, column=5, value=tehaText)
                        sheet.cell(row=current_row, column=6, value=links)
### Pārvieto nākamo rindu Excel failā                   
      current_row += 1
    
### Atgriežas atpakaļ uz iepriekšējo lapu
      driver.back()

 ### Patin lapu uz leju, lai iegūtu visu automašīnu ierakstu informāciju
       scroll_origin = ScrollOrigin.from_viewport(10, 10)
                    ActionChains(driver)\
                    .scroll_from_origin(scroll_origin, 0, 200)\
                    .perform()

  
   
      except NoSuchElementException:
                    print("Tehniskā nav ierakstīta")
                    driver.back()
                    continue

### Atrod un noklikšķina uz nākamās lapas pogas
    button = driver.find_element(By.XPATH, "//a[contains(@href, 'page" + str(page_number) + ".html')]")
            button.click()
            page_number += 1
### Ja nākamā lapa netiek atrasta, tad programma iziet for loopam vēlreiz vai vienreiz
     except NoSuchElementException:
            print("Nav papildus lapu")
            .... tas pats for loop vēlreiz
### Dod izvēli saglabāt Excel lapu ar jaunajiem datiem
    saglabat = input("Vai vēlaties saglabāt excel file? (Y/N) ") 
    if saglabat == "Y":
        workbook.save('AtrastāsMašīnas.xlsx')
        driver.quit()
    else:
        driver.quit()
