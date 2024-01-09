
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db=firestore.client()



# chrome_driver_path="/Users/ujjwalpatel/Desktop/chromedriver/chromedriver"
#
#
#
#
#
# chr_options = Options()
# chr_options.add_argument('--headless=new')
#
#
#
# chr_options.add_experimental_option("detach", True)
#
#
# service = Service(chrome_driver_path)
#
# driver = webdriver.Chrome(service=service,options=chr_options)
#
#
#
# newlist=[]
# net_profit_list=[]
# year_list=[]
# year_profit_list ={}
# buy_or_not=""
# growth_time=""
# count = 1
#
# year_net_profit_dict={}
# growth_amount=0.0
#
#
# def return_arrays(arr,n):
#     increasing = []
#     decreasing = []
#     new_arr = []
#     for i,elem in enumerate(arr):
#         # print("i:"+str(i))
#         # print("elem:"+str(elem))
#         if len(new_arr)>1:
#             # print("new_Arr"+str(new_arr))
#             # print(list(new_arr[0].keys())[0])
#             if new_arr[0][list(new_arr[0].keys())[0]]-new_arr[-1][list(new_arr[-1].keys())[0]]>=0:
#                 # Decreasing
#                 if new_arr[-1][list(new_arr[-1].keys())[0]]>=year_net_profit_dict[elem]:
#                     new_arr.append({elem:year_net_profit_dict[elem]})
#                 else:
#                     if len(new_arr)>=n:
#                         decreasing.append(new_arr)
#                     new_arr = [new_arr[-1],{elem:year_net_profit_dict[elem]}]

#             else:
#                 # Increasing
#                 if new_arr[-1][list(new_arr[-1].keys())[0]] <= year_net_profit_dict[elem]:
#                     new_arr.append({elem:year_net_profit_dict[elem]})
#                 else:
#                     if len(new_arr)>=n:
#                         increasing.append(new_arr)
#                     new_arr = [new_arr[-1],{elem:year_net_profit_dict[elem]}]
#         else:
#             new_arr.append({elem:year_net_profit_dict[elem]})
#             # print("n"+str(new_arr))
#         if i==len(arr)-1:
#             if len(new_arr)>=n:
#                 if new_arr[0][list(new_arr[0].keys())[0]]-new_arr[-1][list(new_arr[-1].keys())[0]]>=0:
#                     decreasing.append(new_arr)
#                 else:
#                     increasing.append(new_arr)
#     return increasing
#
#
# for k in range(1,5):
#     driver.get(f"https://www.screener.in/company/CNX100/?page={k}")
#     stock_list = driver.find_elements(By.CSS_SELECTOR, "div table tbody tr td a")
#     for item in stock_list:
#         # print(item.text)
#         newlist.append(str(item.text))
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
#         for j in range(2,15):
#             net_profit_element=driver.find_element(By.XPATH,f"/html/body/main/section[5]/div[3]/table/tbody/tr[10]/td[{j}]").text
#             if "," in net_profit_element:
#                 net_profit=net_profit_element.replace(",","")
#                 net_profit=int(net_profit)
#             else:
#                 net_profit=int(net_profit_element)
#
#             net_profit_list.append(net_profit)
#
#     except:
#         try:
#             for r in range(2, 15):
#                 net_profit_element = driver.find_element(By.XPATH,
#                                                          f"/html/body/main/section[5]/div[2]/table/tbody/tr[10]/td[{r}]").text
#                 if "," in net_profit_element:
#                     net_profit = net_profit_element.replace(",", "")
#                     net_profit = int(net_profit)
#                 else:
#                     net_profit = int(net_profit_element)
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
#         for h in range(2,15):
#             year=int(str(driver.find_element(By.XPATH,f"/html/body/main/section[5]/div[3]/table/thead/tr/th[{h}]").text)[-4:])
#             year_list.append(year)
#     except:
#         try:
#             for p in range(2, 15):
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
#         growth_amount=  ((float(array_of_profit[-1][-1][list(array_of_profit[-1][-1].keys())[0]])-float(array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]]))/abs(float(array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]])))*100
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
#     doc_ref = db.collection('stocks').document(f'stock{index + 1}')
#     doc = doc_ref.get()
#     if doc.exists:
#         db.collection("stocks").document(f"stock{index + 1}").set(jsonObject, merge=True)
#     else:
#         db.collection("stocks").document(f"stock{index + 1}").set(jsonObject)
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
# driver.close()







from selenium import  webdriver
from flask import  Flask,request
from  selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

app=Flask(__name__)

def download_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    newlist = []
    net_profit_list = []
    year_list = []
    year_profit_list = {}
    buy_or_not = ""
    growth_time = ""
    count = 1

    year_net_profit_dict = {}
    growth_amount = 0.0

    def return_arrays(arr, n):
        increasing = []
        decreasing = []
        new_arr = []
        for i, elem in enumerate(arr):
            # print("i:"+str(i))
            # print("elem:"+str(elem))
            if len(new_arr) > 1:
                # print("new_Arr"+str(new_arr))
                # print(list(new_arr[0].keys())[0])
                if new_arr[0][list(new_arr[0].keys())[0]] - new_arr[-1][list(new_arr[-1].keys())[0]] >= 0:
                    # Decreasing
                    if new_arr[-1][list(new_arr[-1].keys())[0]] >= year_net_profit_dict[elem]:
                        new_arr.append({elem: year_net_profit_dict[elem]})
                    else:
                        if len(new_arr) >= n:
                            decreasing.append(new_arr)
                        new_arr = [new_arr[-1], {elem: year_net_profit_dict[elem]}]
                else:
                    # Increasing
                    if new_arr[-1][list(new_arr[-1].keys())[0]] <= year_net_profit_dict[elem]:
                        new_arr.append({elem: year_net_profit_dict[elem]})
                    else:
                        if len(new_arr) >= n:
                            increasing.append(new_arr)
                        new_arr = [new_arr[-1], {elem: year_net_profit_dict[elem]}]
            else:
                new_arr.append({elem: year_net_profit_dict[elem]})
                # print("n"+str(new_arr))
            if i == len(arr) - 1:
                if len(new_arr) >= n:
                    if new_arr[0][list(new_arr[0].keys())[0]] - new_arr[-1][list(new_arr[-1].keys())[0]] >= 0:
                        decreasing.append(new_arr)
                    else:
                        increasing.append(new_arr)
        return increasing

    for k in range(1, 5):
        driver.get(f"https://www.screener.in/company/CNX100/?page={k}")
        stock_list = driver.find_elements(By.CSS_SELECTOR, "div table tbody tr td a")
        for item in stock_list:
            # print(item.text)
            newlist.append(str(item.text))

    driver.get("https://www.screener.in/")
    search = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/input")
    for index, i in enumerate(newlist):
        search = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/input")
        search.send_keys(i)
        time.sleep(3)
        search.send_keys(Keys.ENTER)

        # getting all csg and cp
        try:
            s_ttm = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[4]/table[1]/tbody/tr[5]/td[2]").text[
                    :1]))
        except:
            try:
                s_ttm = int(str(driver.find_element(By.XPATH,
                                                    "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[5]/td[2]").text[
                                :1]))
            except:
                s_ttm = 0
        try:
            p_ttm = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[4]/table[2]/tbody/tr[5]/td[2]").text[
                    :1]))
        except:
            try:
                p_ttm = int(str(driver.find_element(By.XPATH,
                                                    "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[5]/td[2]").text[
                                :1]))
            except:
                p_ttm = 0

        try:
            csg10 = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[4]/table[1]/tbody/tr[2]/td[2]").text)[
                :-1])
        except:
            try:
                csg10 = int(
                    str(driver.find_element(By.XPATH,
                                            "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[2]/td[2]").text)[
                    :-1])
            except:
                csg10 = 0

        try:
            csg5 = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[4]/table[1]/tbody/tr[3]/td[2]").text)[
                :-1])
        except:
            try:
                csg5 = int(
                    str(driver.find_element(By.XPATH,
                                            "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[3]/td[2]").text)[
                    :-1])
            except:
                csg5 = 0

        try:
            csg3 = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[4]/table[1]/tbody/tr[4]/td[2]").text)[
                :-1])
        except:
            try:
                csg3 = int(
                    str(driver.find_element(By.XPATH,
                                            "/html/body/main/section[5]/div[3]/table[1]/tbody/tr[4]/td[2]").text)[
                    :-1])
            except:
                csg3 = 0

        try:
            cp10 = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[4]/table[2]/tbody/tr[2]/td[2]").text)[
                :-1])
        except:
            try:
                cp10 = int(
                    str(driver.find_element(By.XPATH,
                                            "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[2]/td[2]").text)[
                    :-1])
            except:
                cp10 = 0

        try:
            cp5 = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[4]/table[2]/tbody/tr[3]/td[2]").text)[
                :-1])
        except:
            try:
                cp5 = int(
                    str(driver.find_element(By.XPATH,
                                            "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[3]/td[2]").text)[
                    :-1])
            except:
                cp5 = 0

        try:
            cp3 = int(
                str(driver.find_element(By.XPATH, "/html/body/main/section[5]/div[4]/table[2]/tbody/tr[4]/td[2]").text)[
                :-1])
        except:
            try:
                cp3 = int(
                    str(driver.find_element(By.XPATH,
                                            "/html/body/main/section[5]/div[3]/table[2]/tbody/tr[4]/td[2]").text)[
                    :-1])
            except:
                cp3 = 0

        # getting current price
        # print(i)
        current_price_element = str(
            driver.find_element(By.XPATH, "/html/body/main/div[3]/div[3]/div[2]/ul/li[2]/span[2]/span").text)
        if "," in current_price_element:
            current_price = current_price_element.replace(",", "")
            current_price = float(current_price)

        else:
            current_price = float(current_price_element)

        # getting highest
        highest_price_element = str(
            driver.find_element(By.XPATH, "/html/body/main/div[3]/div[3]/div[2]/ul/li[3]/span[2]/span[1]").text)
        if "," in highest_price_element:
            highest_price = highest_price_element.replace(",", "")
            highest_price = float(highest_price)

        else:
            highest_price = float(highest_price_element)

        # getting lowest price
        lowest_price_element = str(
            driver.find_element(By.XPATH, "/html/body/main/div[3]/div[3]/div[2]/ul/li[3]/span[2]/span[2]").text)
        if "," in lowest_price_element:
            lowest_price = lowest_price_element.replace(",", "")
            lowest_price = float(lowest_price)

        else:
            lowest_price = float(lowest_price_element)

        # get roe
        try:
            roe = float(
                driver.find_element(By.XPATH, "/html/body/main/div[3]/div[3]/div[2]/ul/li[8]/span[2]/span").text)
        except:
            roe = 0.0

        # get roce
        try:
            roce = float(
                driver.find_element(By.XPATH, "/html/body/main/div[3]/div[3]/div[2]/ul/li[7]/span[2]/span").text)
        except:
            roce = 0.0

        # get pe

        try:
            pe = float(driver.find_element(By.XPATH, "/html/body/main/div[3]/div[3]/div[2]/ul/li[4]/span[2]/span").text)
        except:
            pe = 0.0

        # net profit

        try:
            for j in range(2, 15):
                net_profit_element = driver.find_element(By.XPATH,
                                                         f"/html/body/main/section[5]/div[3]/table/tbody/tr[10]/td[{j}]").text
                if "," in net_profit_element:
                    net_profit = net_profit_element.replace(",", "")
                    net_profit = int(net_profit)
                else:
                    net_profit = int(net_profit_element)

                net_profit_list.append(net_profit)

        except:
            try:
                for r in range(2, 15):
                    net_profit_element = driver.find_element(By.XPATH,
                                                             f"/html/body/main/section[5]/div[2]/table/tbody/tr[10]/td[{r}]").text
                    if "," in net_profit_element:
                        net_profit = net_profit_element.replace(",", "")
                        net_profit = int(net_profit)
                    else:
                        net_profit = int(net_profit_element)

                    net_profit_list.append(net_profit)
            except:
                net_profit_list.append("end")

        if net_profit_list[-1] == "end":
            net_profit_list.remove("end")

        # print("net_profit_list:"+" "+str(net_profit_list))

        # year list
        try:
            for h in range(2, 15):
                year = int(str(driver.find_element(By.XPATH,
                                                   f"/html/body/main/section[5]/div[3]/table/thead/tr/th[{h}]").text)[
                           -4:])
                year_list.append(year)
        except:
            try:
                for p in range(2, 15):
                    year = int(str(driver.find_element(By.XPATH,
                                                       f"/html/body/main/section[5]/div[2]/table/thead/tr/th[{p}]").text)[
                               -4:])
                    year_list.append(year)
            except:
                year_list.append("end")

        if year_list[-1] == "end":
            year_list.remove("end")

        # print("year list:"+" "+str(year_list))

        # dict of year and net profit
        for length in range(0, len(year_list)):
            year_net_profit_dict[year_list[length]] = net_profit_list[length]

        # print("year_profit_dict"+str(year_net_profit_dict))

        # buy or not

        if net_profit_list[-1] >= max(net_profit_list) and highest_price > current_price:
            buy_or_not = "buy"

        else:
            buy_or_not = "sell"

        # check growth time
        array_of_profit = return_arrays(year_net_profit_dict, 4)

        # print("array_of_profit"+" "+str(array_of_profit))
        if len(array_of_profit) == 0:
            growth_amount = 0.0
            year_profit_list["startyear"] = 0
            year_profit_list["endyear"] = 0
            year_profit_list["growth"] = growth_amount
            # print("yeaar_profit_list:" + " " + str(year_profit_list))




        else:
            growth_amount = ((float(array_of_profit[-1][-1][list(array_of_profit[-1][-1].keys())[0]]) - float(
                array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]])) / abs(
                float(array_of_profit[-1][0][list(array_of_profit[-1][0].keys())[0]]))) * 100
            year_profit_list["startyear"] = [list(array_of_profit[-1][0].keys())[0]]
            year_profit_list["endyear"] = [list(array_of_profit[-1][-1].keys())[0]]
            year_profit_list["growth"] = growth_amount
            # print("yeaar_profit_list:" + " " + str(year_profit_list))

        # diff from highest price
        highest_diff_percentage = ((highest_price - current_price) / current_price) * 100

        # diff from lowest price
        lowest_diff_percentage = ((current_price - lowest_price) / lowest_price) * 100

        jsonObject = {
            "name": i,
            "index": index + 1,
            "currentPrice": current_price,
            "highestPrice": highest_price,
            "lowestPrice": lowest_price,
            "pe": pe,
            "roce": roce,
            "roe": roe,
            "buyOrNot": buy_or_not,
            "growthPeriod": year_profit_list,
            "csg10": csg10,
            "csg5": csg5,
            "csg3": csg3,
            "cp10": cp10,
            "cp5": cp5,
            "cp3": cp3,
            "netProfitList": net_profit_list,
            "highestDiffPercentage": highest_diff_percentage,
            "lowestDiffPercentage": lowest_diff_percentage,
            "pttm": p_ttm,
            "sttm": s_ttm,
            "growthrate": year_profit_list["growth"],
        }

        doc_ref = db.collection('stocks').document(f'stock{index + 1}')
        doc = doc_ref.get()
        if doc.exists:
            db.collection("stocks").document(f"stock{index + 1}").set(jsonObject, merge=True)
        else:
            db.collection("stocks").document(f"stock{index + 1}").set(jsonObject)

        jsonObject = {}
        newlist = []
        net_profit_list = []
        year_list = []
        year_profit_list = {}
        buy_or_not = ""
        growth_time = ""
        count = 1
        year_net_profit_dict = {}
        growth_amount = 0.0

        driver.get("https://www.screener.in/")
        time.sleep(3)

    driver.close()


@app.route("/",methods=["GET","POST"])
def home():
    if(request.method=="GET"):
        return download_selenium()


if __name__=="__main__":
    app.run(debug=True,port=3000)












