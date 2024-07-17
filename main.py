
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


firebase_config={
  "type": "service_account",
  "project_id": "stockmarket-61d33",
  "private_key_id": "9d5c58989b3e4f20b554156f5e1d934f0aa576aa",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDRhpD2tP6DXx5+\nRtnaJfIo9WcLz7Tue/+SYz2Li9wPoOchvOdMj8rqqrewet1xBuGCIrN2CxLDTXZd\nacbGVc4YtwxQy2nAfXQnkvLqKhFvMqDAxeMLoa7E0SrAiof5/u2De99e59+juR2P\n6+PfGCoJMBdGnuU3M21JtqTs8sUKSOUKZHUJTMZzLAn2eURPkHcKcmbtaW9mL3kj\n621DkQKCN+QRm9Jh8KJ2YjSLXdy3sGwnAxCXts6XZYyNGoxBSalDBqIphbII2UBm\nMnx8OICvEMGLCNBwA8VITV4PuNML5fgCjg4e2WN92aDcOW31eAAqPBPbhq3+MCrB\nGgk/fRi/AgMBAAECggEAASbsVP1G4YbdZaTDdyA4Ww6tRF7gNCXUvJnNBVAGYYaD\npozfjn7mqj24Z7ygyzXR2scMRkAopX5CyLGrcCADjOoiiVajVH5yKc+/cnQ7GxF8\nIGB2Kw7TNz96fDdugO8dJJbCzuV4dCbC1JMh4JWZFZJUz4kCMcXIM7TeAO/MyQBf\nDfP44Y6tw3P7eTR32MnZy3w23LHJWJRzmuxmM/t2r2hPE9LL8RmPpsPo8YuyIqTm\nHOxu5JhNWK5pzT2rktdKpAZdsY30UZZYDGksv6MzV4LMQI89+qGYo6vUrgoOjDu7\ndpJ9w2tMc5Uq6zA9YYsDDXRiABRgjO2xMBml61IQoQKBgQD0GdyXCUOogQqIBnvc\naPrw1nr8HKOmRiy4dW5rEfkYA5+O2Y5e40s0o4s8xtU/ZU0iNAqPb3f2B4RIrUqF\nu+WQnOtiVI9Cdne11bY2fW0LLUxA0LIBfL9EMxrhCEA5VuPfdmg5dxjCCDyvx/rG\nmSqxKtWAsxn399tvGSB+Lt7N2QKBgQDbvTz/dIQWZ6evJkTgqcA5wJODpbwnYGMk\nSrsePe6aswxzNUBT92FtyaVxz0AVUIa2pg1cHxE5XSUGe+UBNZmf0oQN3T960sep\nPPYiPVlKU5zjE6x2HSqQpQ5f3xDNrkr4riJCtpQWhRJ3ztQTmSs5y1PzsWRgCp3/\nBm57I6PEVwKBgCZxIDVFBzu1PsRXSRBYFBTzoiCsHfWknYxbKg2AohrvDyS/DFXT\nM9fRXa8vnQvD11bonTUjl9/OJT4Q1GilQ6z3mXY93OXZpFallnGUZSTaeGTIuQ/U\n5oZGChigZQTiszZQ/m72W5bLF0uTkeHO41NNbJw9GHzdstgXO+/DT+FZAoGAXIpF\ntg+L0SO2Kr0jJLpYifngJgEWTD77gb03MHVEl0HwbFRw0uvLzECvvE5b3p4bHbCw\nz6sFxfLENQbYWroICJbPpkcXBNLf4xYZUjIj+HleCQOwDc4aru/ULevzV6ufRzuO\nkinyE8nXDT29csN+wMgwguCiNRBDmbNLs/A+d+ECgYANIN0YBchlOuv0ibo/OPVm\nCf3+fbKFja62SJWvZ+8/BpGkbEZqT8++Ie6aQOoYLus+nfbts8oh6EkaO4u8F2IN\nEhtJuk8rfSelPCDTVjjBfDaQoJL0mraLsBuVaAOm+8NUJMoiUvsmZIowX8X5X7pN\nlcyEIqLhi85kljDEI7ddyg==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-j9050@stockmarket-61d33.iam.gserviceaccount.com",
  "client_id": "114547067395647550109",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-j9050%40stockmarket-61d33.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
cred = credentials.Certificate(firebasse_config)
firebase_admin.initialize_app(cred)
db=firestore.client()



chrome_driver_path="/Users/ujjwalpatel/Desktop/chromedriver/chromedriver"





chr_options = Options()
chr_options.add_argument('--headless=new')



chr_options.add_experimental_option("detach", True)


service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service,options=chr_options)



newlist=[]
net_profit_list=[]
year_list=[]
year_profit_list ={}
buy_or_not=""
growth_time=""
count = 1

year_net_profit_dict={}
growth_amount=0.0

def growth(cuurent,previous):
    if cuurent>0 and previous>0:
        return ((cuurent-previous)/previous)*100
    elif cuurent<0 and previous<0:
        return ((cuurent-previous)/previous*-1)*100
    elif cuurent==0 and previous==0:
        return 0.0
    elif cuurent==0 and previous<0:
        return 100.0
    elif cuurent>0 and previous<0:
        return ((cuurent-previous)/previous*-1)*100
    elif cuurent>0 and previous==0:
        return 100





def return_arrays(arr,n):
    increasing = []
    decreasing = []
    new_arr = []
    for i,elem in enumerate(arr):
        # print("i:"+str(i))
        # print("elem:"+str(elem))
        if len(new_arr)>1:
            # print("new_Arr"+str(new_arr))
            # print(list(new_arr[0].keys())[0])
            if new_arr[0][list(new_arr[0].keys())[0]]-new_arr[-1][list(new_arr[-1].keys())[0]]>=0:
                # Decreasing
                if new_arr[-1][list(new_arr[-1].keys())[0]]>=year_net_profit_dict[elem]:
                    new_arr.append({elem:year_net_profit_dict[elem]})
                else:
                    if len(new_arr)>=n:
                        decreasing.append(new_arr)
                    new_arr = [new_arr[-1],{elem:year_net_profit_dict[elem]}]

            else:
                # Increasing
                if new_arr[-1][list(new_arr[-1].keys())[0]] <= year_net_profit_dict[elem]:
                    new_arr.append({elem:year_net_profit_dict[elem]})
                else:
                    if len(new_arr)>=n:
                        increasing.append(new_arr)
                    new_arr = [new_arr[-1],{elem:year_net_profit_dict[elem]}]
        else:
            new_arr.append({elem:year_net_profit_dict[elem]})
            # print("n"+str(new_arr))
        if i==len(arr)-1:
            if len(new_arr)>=n:
                if new_arr[0][list(new_arr[0].keys())[0]]-new_arr[-1][list(new_arr[-1].keys())[0]]>=0:
                    decreasing.append(new_arr)
                else:
                    increasing.append(new_arr)
    return increasing


for k in range(1,5):
    driver.get(f"https://www.screener.in/company/CNX100/?page={k}")
    stock_list = driver.find_elements(By.CSS_SELECTOR, "div table tbody tr td a")
    for item in stock_list:
        print(item.text)
        newlist.append(str(item.text))



  # midcap


for k in range(1,5):
    driver.get(f"https://www.screener.in/company/CNXMIDCAP/?page={k}")
    stock_list = driver.find_elements(By.CSS_SELECTOR, "div table tbody tr td a")
    for item in stock_list:
        # print(item.text)
        newlist.append(str(item.text))

# smallcap
for k in range(1,5):
    driver.get(f"https://www.screener.in/company/CNXSMALLCA/?page={k}")
    stock_list = driver.find_elements(By.CSS_SELECTOR, "div table tbody tr td a")
    for item in stock_list:
        # print(item.text)
        newlist.append(str(item.text))






driver.get("https://www.screener.in/")
search=driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/input")
for index,i in enumerate(newlist):
    print(i)
    search = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/input")
    search.send_keys(i)
    time.sleep(3)
    search.send_keys(Keys.ENTER)

    # getting all csg and cp
    try:
        s_ttm=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[1]/tbody/tr[5]/td[2]").text[:1]))
    except:
        try:
            s_ttm = int(str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[5]/td[2]").text[:1]))
        except:
            s_ttm=0
    try:
        p_ttm=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[2]/tbody/tr[5]/td[2]").text[:1]))
    except:
        try:
            p_ttm = int(str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[5]/td[2]").text[:1]))
        except:
            p_ttm=0

    try:
        csg10=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[1]/tbody/tr[2]/td[2]").text)[:-1])
    except:
        try:
            csg10 = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[2]/td[2]").text)[
                :-1])
        except:
            csg10=0

    try:
        csg5=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[1]/tbody/tr[3]/td[2]").text)[:-1])
    except:
        try:
            csg5 = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[3]/td[2]").text)[
                :-1])
        except:
            csg5=0

    try:
        csg3=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[1]/tbody/tr[4]/td[2]").text)[:-1])
    except:
        try:
            csg3 = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[4]/td[2]").text)[
                :-1])
        except:
            csg3 = 0

    try:
        cp10=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[2]/tbody/tr[2]/td[2]").text)[:-1])
    except:
        try:
            cp10 = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[2]/td[2]").text)[
                :-1])
        except:
            cp10=0

    try:
        cp5=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[2]/tbody/tr[3]/td[2]").text)[:-1])
    except:
        try:
            cp5 = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[3]/td[2]").text)[
                :-1])
        except:
            cp5 = 0

    try:
        cp3=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[2]/tbody/tr[4]/td[2]").text)[:-1])
    except:
        try:
            cp3 = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[4]/td[2]").text)[
                :-1])
        except:
           cp3=0

    # median pe ratio
    time.sleep(0.5)
    pe_ratio_button=driver.find_element(By.XPATH,"/html/body/main/section[1]/div[1]/div[2]/div/button[2]")
    pe_ratio_button.click()
    time.sleep(1)
    median_pe = driver.find_element(By.XPATH,"/html/body/main/section[1]/div[3]/label[2]/span").text
    if((median_pe.replace('Median PE =', '')).replace(" ", "")!="None"):
        median_pe_val=float((median_pe.replace('Median PE =', '')).replace(" ", ""))
    else:
        median_pe_val="None"

    # getting current price
    # print(i)
    current_price_element=str(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[2]/span[2]/span").text)
    if "," in  current_price_element:
        current_price=current_price_element.replace(",","")
        current_price=float(current_price)

    else:
        current_price=float(current_price_element)

    # getting highest
    highest_price_element = str(
        driver.find_element(By.XPATH, "/html/body/main/div[3]/div[3]/div[2]/ul/li[3]/span[2]/span[1]").text)
    if "," in highest_price_element:
        highest_price=highest_price_element.replace(",", "")
        highest_price = float(highest_price)

    else:
        highest_price = float(highest_price_element)

    # getting lowest price
    lowest_price_element = str(
        driver.find_element(By.XPATH, "/html/body/main/div[3]/div[3]/div[2]/ul/li[3]/span[2]/span[2]").text)
    if "," in lowest_price_element:
        lowest_price=lowest_price_element.replace(",", "")
        lowest_price = float(lowest_price)

    else:
        lowest_price = float(lowest_price_element)


    # get roe
    try:
        roe=float(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[8]/span[2]/span").text)
    except:
        roe=0.0


    # get roce
    try:
        roce=float(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[7]/span[2]/span").text)
    except:
        roce=0.0


    # get pe

    try:
        pe=float(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[4]/span[2]/span").text)
    except:
        pe=0.0


    # net profit

    try:
        for j in range(2,14):
            net_profit_element=driver.find_element(By.XPATH,f"/html/body/main/section[5]/div[3]/table/tbody/tr[10]/td[{j}]").text
            if "," in net_profit_element:
                net_profit=net_profit_element.replace(",","")
                net_profit=float(net_profit)
            else:
                net_profit=float(net_profit_element)

            net_profit_list.append(net_profit)

    except:
        try:
            for r in range(2, 14):
                net_profit_element = driver.find_element(By.XPATH,
                                                         f"/html/body/main/section[5]/div[2]/table/tbody/tr[10]/td[{r}]").text
                if "," in net_profit_element:
                    net_profit = net_profit_element.replace(",", "")
                    net_profit = float(net_profit)
                else:
                    net_profit = float(net_profit_element)

                net_profit_list.append(net_profit)
        except:
            net_profit_list.append("end")

    if net_profit_list[-1]=="end":
        net_profit_list.remove("end")

    # print("net_profit_list:"+" "+str(net_profit_list))


    # year list
    try:
        for h in range(2,14):
            year=int(str(driver.find_element(By.XPATH,f"/html/body/main/section[5]/div[3]/table/thead/tr/th[{h}]").text)[-4:])
            year_list.append(year)
    except:
        try:
            for p in range(2, 14):
                year = int(str(driver.find_element(By.XPATH,
                                                   f"/html/body/main/section[5]/div[2]/table/thead/tr/th[{p}]").text)[
                           -4:])
                year_list.append(year)
        except:
            year_list.append("end")

    if year_list[-1]=="end":
        year_list.remove("end")

    # print("year list:"+" "+str(year_list))

    # dict of year and net profit
    for length in range(0,len(year_list)):
        year_net_profit_dict[year_list[length]]=net_profit_list[length]

    # print("year_profit_dict"+str(year_net_profit_dict))


    # buy or not

    if net_profit_list[-1] >= max(net_profit_list) and highest_price > current_price:
        buy_or_not="buy"

    else:
        buy_or_not="sell"

    # check growth time
    array_of_profit=return_arrays(year_net_profit_dict,4)


    # print("array_of_profit"+" "+str(array_of_profit))
    if len(array_of_profit)==0:
        growth_amount=0.0
        year_profit_list["startyear"] = 0
        year_profit_list["endyear"] = 0
        year_profit_list["growth"] = growth_amount
        # print("yeaar_profit_list:" + " " + str(year_profit_list))




    else:
        growth_amount=growth(float(array_of_profit[-1][-1][list(array_of_profit[-1][-1].keys())[0]]),float(array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]]))
        print(growth_amount)
        # growth_amount=  ((float(array_of_profit[-1][-1][list(array_of_profit[-1][-1].keys())[0]])-float(array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]]))/abs(float(array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]])))*100
        year_profit_list["startyear"] = [list(array_of_profit[-1][0].keys())[0]]
        year_profit_list["endyear"] = [list(array_of_profit[-1][-1].keys())[0]]
        year_profit_list["growth"] = growth_amount
        # print("yeaar_profit_list:" + " " + str(year_profit_list))

    # diff from highest price
    highest_diff_percentage=((highest_price-current_price)/current_price)*100

    # diff from lowest price
    lowest_diff_percentage=((current_price-lowest_price)/lowest_price)*100
    print(i)

    jsonObject = {
        "name":i,
        "index":index+1,
        "medianPe":median_pe_val,
        "currentPrice":current_price,
        "highestPrice":highest_price,
        "lowestPrice":lowest_price,
        "pe":pe,
        "roce":roce,
        "roe":roe,
        "buyOrNot":buy_or_not,
        "growthPeriod":year_profit_list,
        "csg10":csg10,
        "csg5":csg5,
        "csg3":csg3,
        "cp10":cp10,
        "cp5":cp5,
        "cp3":cp3,
        "netProfitList":net_profit_list,
        "highestDiffPercentage":highest_diff_percentage,
        "lowestDiffPercentage":lowest_diff_percentage,
        "pttm":p_ttm,
        "sttm":s_ttm,
        "growthrate":year_profit_list["growth"],
    }

    if index<=99:
        doc_ref = db.collection('stocks').document(f'stock{index + 1}')
        doc = doc_ref.get()
        if doc.exists:
            db.collection("stocks").document(f"stock{index + 1}").set(jsonObject, merge=True)
        else:
            db.collection("stocks").document(f"stock{index + 1}").set(jsonObject)
        print("finished")
    elif 99<index<=199:
        doc_ref = db.collection('stocksMidCAP').document(f'stock{index + 1}')
        doc = doc_ref.get()
        if doc.exists:
            db.collection("stocksMidCAP").document(f"stock{index + 1}").set(jsonObject, merge=True)
        else:
            db.collection("stocksMidCAP").document(f"stock{index + 1}").set(jsonObject)
        print("finished")
    elif 199<index<=299:
        doc_ref = db.collection('stocksSmallCAP').document(f'stock{index + 1}')
        doc = doc_ref.get()
        if doc.exists:
            db.collection("stocksSmallCAP").document(f"stock{index + 1}").set(jsonObject, merge=True)
        else:
            db.collection("stocksSmallCAP").document(f"stock{index + 1}").set(jsonObject)



    jsonObject={}
    newlist = []
    net_profit_list = []
    year_list = []
    year_profit_list = {}
    buy_or_not = ""
    growth_time = ""
    count=1
    year_net_profit_dict = {}
    growth_amount = 0.0

    driver.get("https://www.screener.in/")
    time.sleep(3)

driver.close()



















# driver.get("https://www.screener.in/")
# search=driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/input")
# for index,i in enumerate(newlist):
#     search = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/input")
#     search.send_keys(i)
#     time.sleep(3)
#     search.send_keys(Keys.ENTER)
#
#     # getting all csg and cp
#     try:
#         s_ttm=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[1]/tbody/tr[5]/td[2]").text[:1]))
#     except:
#         try:
#             s_ttm = int(str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[5]/td[2]").text[:1]))
#         except:
#             s_ttm=0
#     try:
#         p_ttm=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[2]/tbody/tr[5]/td[2]").text[:1]))
#     except:
#         try:
#             p_ttm = int(str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[5]/td[2]").text[:1]))
#         except:
#             p_ttm=0
#
#     try:
#         csg10=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[1]/tbody/tr[2]/td[2]").text)[:-1])
#     except:
#         try:
#             csg10 = int(
#                 str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[2]/td[2]").text)[
#                 :-1])
#         except:
#             csg10=0
#
#     try:
#         csg5=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[1]/tbody/tr[3]/td[2]").text)[:-1])
#     except:
#         try:
#             csg5 = int(
#                 str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[3]/td[2]").text)[
#                 :-1])
#         except:
#             csg5=0
#
#     try:
#         csg3=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[1]/tbody/tr[4]/td[2]").text)[:-1])
#     except:
#         try:
#             csg3 = int(
#                 str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[4]/td[2]").text)[
#                 :-1])
#         except:
#             csg3 = 0
#
#     try:
#         cp10=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[2]/tbody/tr[2]/td[2]").text)[:-1])
#     except:
#         try:
#             cp10 = int(
#                 str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[2]/td[2]").text)[
#                 :-1])
#         except:
#             cp10=0
#
#     try:
#         cp5=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[2]/tbody/tr[3]/td[2]").text)[:-1])
#     except:
#         try:
#             cp5 = int(
#                 str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[3]/td[2]").text)[
#                 :-1])
#         except:
#             cp5 = 0
#
#     try:
#         cp3=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[2]/tbody/tr[4]/td[2]").text)[:-1])
#     except:
#         try:
#             cp3 = int(
#                 str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[4]/td[2]").text)[
#                 :-1])
#         except:
#            cp3=0
#
#     # getting current price
#     # print(i)
#     current_price_element=str(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[2]/span[2]/span").text)
#     if "," in  current_price_element:
#         current_price=current_price_element.replace(",","")
#         current_price=float(current_price)
#
#     else:
#         current_price=float(current_price_element)
#
#     # getting highest
#     highest_price_element = str(
#         driver.find_element(By.XPATH, "/html/body/main/div[3]/div[3]/div[2]/ul/li[3]/span[2]/span[1]").text)
#     if "," in highest_price_element:
#         highest_price=highest_price_element.replace(",", "")
#         highest_price = float(highest_price)
#
#     else:
#         highest_price = float(highest_price_element)
#
#     # getting lowest price
#     lowest_price_element = str(
#         driver.find_element(By.XPATH, "/html/body/main/div[3]/div[3]/div[2]/ul/li[3]/span[2]/span[2]").text)
#     if "," in lowest_price_element:
#         lowest_price=lowest_price_element.replace(",", "")
#         lowest_price = float(lowest_price)
#
#     else:
#         lowest_price = float(lowest_price_element)
#
#
#     # get roe
#     try:
#         roe=float(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[8]/span[2]/span").text)
#     except:
#         roe=0.0
#
#
#     # get roce
#     try:
#         roce=float(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[7]/span[2]/span").text)
#     except:
#         roce=0.0
#
#
#     # get pe
#
#     try:
#         pe=float(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[4]/span[2]/span").text)
#     except:
#         pe=0.0
#
#
#     # net profit
#
#     try:
#         for j in range(2,14):
#             net_profit_element=driver.find_element(By.XPATH,f"/html/body/main/section[5]/div[3]/table/tbody/tr[10]/td[{j}]").text
#             if "," in net_profit_element:
#                 net_profit=net_profit_element.replace(",","")
#                 net_profit=float(net_profit)
#             else:
#                 net_profit=float(net_profit_element)
#
#             net_profit_list.append(net_profit)
#
#     except:
#         try:
#             for r in range(2, 14):
#                 net_profit_element = driver.find_element(By.XPATH,
#                                                          f"/html/body/main/section[5]/div[2]/table/tbody/tr[10]/td[{r}]").text
#                 if "," in net_profit_element:
#                     net_profit = net_profit_element.replace(",", "")
#                     net_profit = float(net_profit)
#                 else:
#                     net_profit = float(net_profit_element)
#
#                 net_profit_list.append(net_profit)
#         except:
#             net_profit_list.append("end")
#
#     if net_profit_list[-1]=="end":
#         net_profit_list.remove("end")
#
#     # print("net_profit_list:"+" "+str(net_profit_list))
#
#
#     # year list
#     try:
#         for h in range(2,14):
#             year=int(str(driver.find_element(By.XPATH,f"/html/body/main/section[5]/div[3]/table/thead/tr/th[{h}]").text)[-4:])
#             year_list.append(year)
#     except:
#         try:
#             for p in range(2, 14):
#                 year = int(str(driver.find_element(By.XPATH,
#                                                    f"/html/body/main/section[5]/div[2]/table/thead/tr/th[{p}]").text)[
#                            -4:])
#                 year_list.append(year)
#         except:
#             year_list.append("end")
#
#     if year_list[-1]=="end":
#         year_list.remove("end")
#
#     # print("year list:"+" "+str(year_list))
#
#     # dict of year and net profit
#     for length in range(0,len(year_list)):
#         year_net_profit_dict[year_list[length]]=net_profit_list[length]
#
#     # print("year_profit_dict"+str(year_net_profit_dict))
#
#
#     # buy or not
#
#     if net_profit_list[-1] >= max(net_profit_list) and highest_price > current_price:
#         buy_or_not="buy"
#
#     else:
#         buy_or_not="sell"
#
#     # check growth time
#     array_of_profit=return_arrays(year_net_profit_dict,4)
#
#
#     # print("array_of_profit"+" "+str(array_of_profit))
#     if len(array_of_profit)==0:
#         growth_amount=0.0
#         year_profit_list["startyear"] = 0
#         year_profit_list["endyear"] = 0
#         year_profit_list["growth"] = growth_amount
#         # print("yeaar_profit_list:" + " " + str(year_profit_list))
#
#
#
#
#     else:
#         growth_amount = growth(float(array_of_profit[-1][-1][list(array_of_profit[-1][-1].keys())[0]]),
#                                float(array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]]))
#         print(growth_amount)
#         # growth_amount=  ((float(array_of_profit[-1][-1][list(array_of_profit[-1][-1].keys())[0]])-float(array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]]))/abs(float(array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]])))*100
#         year_profit_list["startyear"] = [list(array_of_profit[-1][0].keys())[0]]
#         year_profit_list["endyear"] = [list(array_of_profit[-1][-1].keys())[0]]
#         year_profit_list["growth"] = growth_amount
#         # print("yeaar_profit_list:" + " " + str(year_profit_list))
#
#     # diff from highest price
#     highest_diff_percentage=((highest_price-current_price)/current_price)*100
#
#     # diff from lowest price
#     lowest_diff_percentage=((current_price-lowest_price)/lowest_price)*100
#
#     jsonObject = {
#         "name":i,
#         "index":index+1,
#         "currentPrice":current_price,
#         "highestPrice":highest_price,
#         "lowestPrice":lowest_price,
#         "pe":pe,
#         "roce":roce,
#         "roe":roe,
#         "buyOrNot":buy_or_not,
#         "growthPeriod":year_profit_list,
#         "csg10":csg10,
#         "csg5":csg5,
#         "csg3":csg3,
#         "cp10":cp10,
#         "cp5":cp5,
#         "cp3":cp3,
#         "netProfitList":net_profit_list,
#         "highestDiffPercentage":highest_diff_percentage,
#         "lowestDiffPercentage":lowest_diff_percentage,
#         "pttm":p_ttm,
#         "sttm":s_ttm,
#         "growthrate":year_profit_list["growth"],
#     }
#
#     doc_ref = db.collection('stocksMidCAP').document(f'stock{index + 1}')
#     doc = doc_ref.get()
#     if doc.exists:
#         db.collection("stocksMidCAP").document(f"stock{index + 1}").set(jsonObject, merge=True)
#     else:
#         db.collection("stocksMidCAP").document(f"stock{index + 1}").set(jsonObject)
#
#
#     jsonObject={}
#     newlist = []
#     net_profit_list = []
#     year_list = []
#     year_profit_list = {}
#     buy_or_not = ""
#     growth_time = ""
#     count=1
#     year_net_profit_dict = {}
#     growth_amount = 0.0
#
#     driver.get("https://www.screener.in/")
#     time.sleep(3)
#
#
#
#
#
#
#
#
#
#
#
#
#
# driver.get("https://www.screener.in/")
# search=driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/input")
# for index,i in enumerate(newlist):
#     search = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/input")
#     search.send_keys(i)
#     time.sleep(3)
#     search.send_keys(Keys.ENTER)
#
#     # getting all csg and cp
#     try:
#         s_ttm=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[1]/tbody/tr[5]/td[2]").text[:1]))
#     except:
#         try:
#             s_ttm = int(str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[5]/td[2]").text[:1]))
#         except:
#             s_ttm=0
#     try:
#         p_ttm=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[2]/tbody/tr[5]/td[2]").text[:1]))
#     except:
#         try:
#             p_ttm = int(str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[5]/td[2]").text[:1]))
#         except:
#             p_ttm=0
#
#     try:
#         csg10=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[1]/tbody/tr[2]/td[2]").text)[:-1])
#     except:
#         try:
#             csg10 = int(
#                 str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[2]/td[2]").text)[
#                 :-1])
#         except:
#             csg10=0
#
#     try:
#         csg5=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[1]/tbody/tr[3]/td[2]").text)[:-1])
#     except:
#         try:
#             csg5 = int(
#                 str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[3]/td[2]").text)[
#                 :-1])
#         except:
#             csg5=0
#
#     try:
#         csg3=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[1]/tbody/tr[4]/td[2]").text)[:-1])
#     except:
#         try:
#             csg3 = int(
#                 str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[4]/td[2]").text)[
#                 :-1])
#         except:
#             csg3 = 0
#
#     try:
#         cp10=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[2]/tbody/tr[2]/td[2]").text)[:-1])
#     except:
#         try:
#             cp10 = int(
#                 str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[2]/td[2]").text)[
#                 :-1])
#         except:
#             cp10=0
#
#     try:
#         cp5=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[2]/tbody/tr[3]/td[2]").text)[:-1])
#     except:
#         try:
#             cp5 = int(
#                 str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[3]/td[2]").text)[
#                 :-1])
#         except:
#             cp5 = 0
#
#     try:
#         cp3=int(str(driver.find_element(By.XPATH,"/html/body/main/section[5]/div[4]/table[2]/tbody/tr[4]/td[2]").text)[:-1])
#     except:
#         try:
#             cp3 = int(
#                 str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[4]/td[2]").text)[
#                 :-1])
#         except:
#            cp3=0
#
#     # getting current price
#     # print(i)
#     current_price_element=str(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[2]/span[2]/span").text)
#     if "," in  current_price_element:
#         current_price=current_price_element.replace(",","")
#         current_price=float(current_price)
#
#     else:
#         current_price=float(current_price_element)
#
#     # getting highest
#     highest_price_element = str(
#         driver.find_element(By.XPATH, "/html/body/main/div[3]/div[3]/div[2]/ul/li[3]/span[2]/span[1]").text)
#     if "," in highest_price_element:
#         highest_price=highest_price_element.replace(",", "")
#         highest_price = float(highest_price)
#
#     else:
#         highest_price = float(highest_price_element)
#
#     # getting lowest price
#     lowest_price_element = str(
#         driver.find_element(By.XPATH, "/html/body/main/div[3]/div[3]/div[2]/ul/li[3]/span[2]/span[2]").text)
#     if "," in lowest_price_element:
#         lowest_price=lowest_price_element.replace(",", "")
#         lowest_price = float(lowest_price)
#
#     else:
#         lowest_price = float(lowest_price_element)
#
#
#     # get roe
#     try:
#         roe=float(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[8]/span[2]/span").text)
#     except:
#         roe=0.0
#
#
#     # get roce
#     try:
#         roce=float(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[7]/span[2]/span").text)
#     except:
#         roce=0.0
#
#
#     # get pe
#
#     try:
#         pe=float(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[4]/span[2]/span").text)
#     except:
#         pe=0.0
#
#
#     # net profit
#
#     try:
#         for j in range(2,14):
#             net_profit_element=driver.find_element(By.XPATH,f"/html/body/main/section[5]/div[3]/table/tbody/tr[10]/td[{j}]").text
#             if "," in net_profit_element:
#                 net_profit=net_profit_element.replace(",","")
#                 net_profit=float(net_profit)
#             else:
#                 net_profit=float(net_profit_element)
#
#             net_profit_list.append(net_profit)
#
#     except:
#         try:
#             for r in range(2, 14):
#                 net_profit_element = driver.find_element(By.XPATH,
#                                                          f"/html/body/main/section[5]/div[2]/table/tbody/tr[10]/td[{r}]").text
#                 if "," in net_profit_element:
#                     net_profit = net_profit_element.replace(",", "")
#                     net_profit = float(net_profit)
#                 else:
#                     net_profit = float(net_profit_element)
#
#                 net_profit_list.append(net_profit)
#         except:
#             net_profit_list.append("end")
#
#     if net_profit_list[-1]=="end":
#         net_profit_list.remove("end")
#
#     # print("net_profit_list:"+" "+str(net_profit_list))
#
#
#     # year list
#     try:
#         for h in range(2,14):
#             year=int(str(driver.find_element(By.XPATH,f"/html/body/main/section[5]/div[3]/table/thead/tr/th[{h}]").text)[-4:])
#             year_list.append(year)
#     except:
#         try:
#             for p in range(2, 14):
#                 year = int(str(driver.find_element(By.XPATH,
#                                                    f"/html/body/main/section[5]/div[2]/table/thead/tr/th[{p}]").text)[
#                            -4:])
#                 year_list.append(year)
#         except:
#             year_list.append("end")
#
#     if year_list[-1]=="end":
#         year_list.remove("end")
#
#     # print("year list:"+" "+str(year_list))
#     print(year_list)
#     print(net_profit_list)
#     print(i)
#     # dict of year and net profit
#     for length in range(0,len(year_list)):
#         year_net_profit_dict[year_list[length]]=net_profit_list[length]
#
#     # print("year_profit_dict"+str(year_net_profit_dict))
#
#
#     # buy or not
#
#     if net_profit_list[-1] >= max(net_profit_list) and highest_price > current_price:
#         buy_or_not="buy"
#
#     else:
#         buy_or_not="sell"
#
#     # check growth time
#     array_of_profit=return_arrays(year_net_profit_dict,4)
#
#
#     # print("array_of_profit"+" "+str(array_of_profit))
#     if len(array_of_profit)==0:
#         growth_amount=0.0
#         year_profit_list["startyear"] = 0
#         year_profit_list["endyear"] = 0
#         year_profit_list["growth"] = growth_amount
#         # print("yeaar_profit_list:" + " " + str(year_profit_list))
#
#
#
#
#     else:
#         growth_amount = growth(float(array_of_profit[-1][-1][list(array_of_profit[-1][-1].keys())[0]]),
#                                float(array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]]))
#         print(growth_amount)
#         # growth_amount=  ((float(array_of_profit[-1][-1][list(array_of_profit[-1][-1].keys())[0]])-float(array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]]))/abs(float(array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]])))*100
#         year_profit_list["startyear"] = [list(array_of_profit[-1][0].keys())[0]]
#         year_profit_list["endyear"] = [list(array_of_profit[-1][-1].keys())[0]]
#         year_profit_list["growth"] = growth_amount
#         # print("yeaar_profit_list:" + " " + str(year_profit_list))
#
#     # diff from highest price
#     highest_diff_percentage=((highest_price-current_price)/current_price)*100
#
#     # diff from lowest price
#     lowest_diff_percentage=((current_price-lowest_price)/lowest_price)*100
#
#     jsonObject = {
#         "name":i,
#         "index":index+1,
#         "currentPrice":current_price,
#         "highestPrice":highest_price,
#         "lowestPrice":lowest_price,
#         "pe":pe,
#         "roce":roce,
#         "roe":roe,
#         "buyOrNot":buy_or_not,
#         "growthPeriod":year_profit_list,
#         "csg10":csg10,
#         "csg5":csg5,
#         "csg3":csg3,
#         "cp10":cp10,
#         "cp5":cp5,
#         "cp3":cp3,
#         "netProfitList":net_profit_list,
#         "highestDiffPercentage":highest_diff_percentage,
#         "lowestDiffPercentage":lowest_diff_percentage,
#         "pttm":p_ttm,
#         "sttm":s_ttm,
#         "growthrate":year_profit_list["growth"],
#     }
#
#     doc_ref = db.collection('stocksSmallCAP').document(f'stock{index + 1}')
#     doc = doc_ref.get()
#     if doc.exists:
#         db.collection("stocksSmallCAP").document(f"stock{index + 1}").set(jsonObject, merge=True)
#     else:
#         db.collection("stocksSmallCAP").document(f"stock{index + 1}").set(jsonObject)
#
#
#     jsonObject={}
#     newlist = []
#     net_profit_list = []
#     year_list = []
#     year_profit_list = {}
#     buy_or_not = ""
#     growth_time = ""
#     count=1
#     year_net_profit_dict = {}
#     growth_amount = 0.0
#
#     driver.get("https://www.screener.in/")
#     time.sleep(3)


