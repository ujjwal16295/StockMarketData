
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

# add firebase config here
firebase_config={
  "type": os.getenv("TYPE"),
  "project_id": os.getenv("PROJECT_ID"),
  "private_key_id": os.getenv("PRIVATE_KEY_ID"),
  "private_key": os.getenv("PRIVATE_KEY"),
  "client_email": os.getenv("CLIENT_EMAIL"),
  "client_id": os.getenv("CLIENT_ID"),
  "auth_uri":  os.getenv("AUTH_URI"),
  "token_uri": os.getenv("TOKEN_URI"),
  "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
  "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
  "universe_domain": os.getenv("UNIVERSE_DOMAIN")
}



cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred)
db=firestore.client()



chrome_driver_path='./chromedriver'





chr_options = Options()
chr_options.add_argument('--headless=new')
chr_options.add_argument('--no-sandbox')
chr_options.add_argument('--disable-dev-shm-usage')
chr_options.add_argument('--window-size=1920,1080') 



chr_options.add_experimental_option("detach", True)


service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service,options=chr_options)





password=os.getenv("PASSWORD")
email =os.getenv("EMAIL")
share_list= []
newlist=[]
net_profit_list=[]
year_list=[]
year_profit_list ={}
buy_or_not=""
growth_time=""
count = 1
year_fcf_list = []
capex_list = []
cash_from_operating_activity_list = []
free_cash_flow_list = {
    "year": [],
    "list": []
}

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
    time.sleep(2)



  # midcap


for k in range(1,5):
    driver.get(f"https://www.screener.in/company/CNXMIDCAP/?page={k}")
    stock_list = driver.find_elements(By.CSS_SELECTOR, "div table tbody tr td a")
    for item in stock_list:
        # print(item.text)
        newlist.append(str(item.text))
    time.sleep(2)

# smallcap
for k in range(1,5):
    driver.get(f"https://www.screener.in/company/CNXSMALLCA/?page={k}")
    stock_list = driver.find_elements(By.CSS_SELECTOR, "div table tbody tr td a")
    for item in stock_list:
        # print(item.text)
        newlist.append(str(item.text))
    time.sleep(2)







driver.get("https://www.screener.in/")
login_button = driver.find_element(By.XPATH,"/html/body/nav/div[2]/div/div/div/div[2]/div[2]/a[1]")
login_button.click()
email_input= driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/form/div[1]/input")
email_input.send_keys(email)
time.sleep(2)
password_input =driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/form/div[2]/input")
password_input.send_keys(password)
time.sleep(2)
submit_button = driver.find_element(By.XPATH,"/html/body/main/div[2]/div[2]/form/button")
submit_button.click()
time.sleep(2)
# search=driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/input")
for index,i in enumerate(newlist[157:len(newlist)]):  
    print(i)
    search = driver.find_element(By.XPATH, "/html/body/nav/div[2]/div/div/div/div[2]/div[1]/div/input")
    search.send_keys(i)
    time.sleep(3)
    search.send_keys(Keys.ENTER)
    extra_search = driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/div/div/div/input")
    extra_search.send_keys("Debt to equity")
    extra_search.send_keys(Keys.ENTER)
    time.sleep(2)
    extra_search = driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/div/div/div/input")
    extra_search.send_keys("Debt")
    extra_search.send_keys(Keys.ENTER)
    time.sleep(2)
    extra_search = driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/div/div/div/input")
    extra_search.send_keys("industry pe")
    extra_search.send_keys(Keys.ENTER)
    time.sleep(2)
    extra_search = driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/div/div/div/input")
    extra_search.send_keys("peg ratio")
    extra_search.send_keys(Keys.ENTER)
    time.sleep(2)

    
    #div yield
    div_yield_span = driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[6]/span[2]/span")
    if div_yield_span.text == "":
        div_yield = float(0)
    else:
        div_yield=float(div_yield_span.text)

    # current pe
    current_pe = driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[4]/span[2]/span").text
    if current_pe == "":
        new_current_pe = float(0)
    elif "," in current_pe:
        new_current_pe = float(current_pe.replace(",",""))  
    else:
        new_current_pe = float(current_pe)
        

    #industry pe
    industry_pe  = float(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[12]/span[2]/span").text)

    # peg ratio
    peg_ratio = driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[13]/span[2]/span").text
    if peg_ratio == "":
        new_peg_ratio = float(0)
    else:
        new_peg_ratio = float(peg_ratio)



        
    # mcap
    mcap = driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[1]/span[2]/span").text
    if "," in mcap:
        newmcap = float(mcap.replace(",",""))
    else:
        newmcap = float(mcap)
    
# debt
    time.sleep(1)
    debt=driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[11]/span[2]/span").text
    if "," in debt:
        new_debt = float(debt.replace(",",""))
    else:
        new_debt = float(debt)
    if driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[10]/span[2]/span").text =="":
        debt_equity_ratio=None
    else:
        debt_equity_ratio  = float(driver.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul/li[10]/span[2]/span").text)


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
    time.sleep(3)
    pe_ratio_button=driver.find_element(By.XPATH,"/html/body/main/section[1]/div[1]/div[2]/div/button[2]")
    pe_ratio_button.click()
    time.sleep(3)
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
    
   
    # sharholder
    shares = driver.find_element(By.XPATH, "/html/body/main/section[9]/div[2]/div/table/tbody").find_elements(By.TAG_NAME, "tr")[-1].find_elements(By.TAG_NAME,"td")


    for share in shares[1:]:
        if "," in share.text:
            new_share = float(share.text.replace(",",""))
        else:
            new_share = float(share.text)
            
        share_list.append(new_share)

    # sector and industry

    sector= driver.find_element(By.XPATH,"/html/body/main/section[3]/div[1]/div[1]/p[1]/a[1]").text
    industry = driver.find_element(By.XPATH,"/html/body/main/section[3]/div[1]/div[1]/p[1]/a[2]").text
  
    # free cash flow
    cash_from_operating_activity_button = driver.find_element(By.XPATH,"/html/body/main/section[7]/div[2]/table/tbody/tr[1]/td[1]/button")
    cash_from_investing_activity_button=driver.find_element(By.XPATH,"/html/body/main/section[7]/div[2]/table/tbody/tr[2]/td[1]/button")
    time.sleep(2)
    cash_from_investing_activity_button.click()
    time.sleep(2)
    year_fcf = driver.find_element(By.XPATH,"/html/body/main/section[7]/div[2]/table/thead/tr").find_elements(By.TAG_NAME,"th")
    for fcf in year_fcf[1:]:
        year_fcf_list.append(fcf.text)
   
    cash_from_operating_activity = driver.find_element(By.XPATH,"/html/body/main/section[7]/div[2]/table/tbody/tr[1]").find_elements(By.TAG_NAME,"td")
    for op  in cash_from_operating_activity[1:]:
        if op.text=="":
            cash_from_operating_activity_list.append('0')
        else:
            cash_from_operating_activity_list.append(op.text)
    print("cash_from_operating_list")
    print(cash_from_operating_activity_list)

    capexs = driver.find_element(By.XPATH,"/html/body/main/section[7]/div[2]/table/tbody/tr[3]").find_elements(By.TAG_NAME,"td")
    for capex in capexs[1:]:
        if capex.text=="":
            capex_list.append('0')
        else:
            capex_list.append(capex.text)
    print("capex_list")
    print(capex_list)


   
    for capex_index,item_of_list in enumerate(capex_list):
        if "," in cash_from_operating_activity_list[capex_index]:
            new_cash_op = float(cash_from_operating_activity_list[capex_index].replace(",", ""))
        else:
            new_cash_op = float(cash_from_operating_activity_list[capex_index])
        if "," in capex_list[capex_index]:
            new_capex = float(capex_list[capex_index].replace(",",""))
        else:
            new_capex = float(capex_list[capex_index])

                    
        free_cash_flow_list["year"].append(year_fcf_list[capex_index])
        free_cash_flow_list["list"].append(new_cash_op-new_capex)



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
        "sector":sector,
        "industry":industry,
        "free_cash_flow":free_cash_flow_list,
        "shares":share_list[-1],
        "debt":debt,
        "debt_equity_ratio":debt_equity_ratio,
        "mcap":newmcap,
        "industry_pe":industry_pe,
        "peg_ratio":new_peg_ratio,
        "current_pe":new_current_pe,
        "div_yield":div_yield,



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
    year_fcf_list = []
    capex_list = []
    cash_from_operating_activity_list = []
    free_cash_flow_list = {
        "year":[],
        "list":[]
    }
    share_list=[]



    # driver.get("https://www.screener.in/")
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


