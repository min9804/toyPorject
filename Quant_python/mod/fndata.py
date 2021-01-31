import pandas as pd
import requests
import time
import numpy as np
import bs4


def make_fs_dataframe(firm_code): #재무데이터 만드는 함수
    fs_url = 'https://comp.fnguide.com/SVO2/asp/SVD_Finance.asp?pGB=1&cID=&MenuYn=Y&ReportGB=D&NewMenuID=103&stkGb=701&gicode=' + firm_code 
    fs_page = requests.get(fs_url) 
    fs_tables = pd.read_html(fs_page.text) 
 
    temp_df = fs_tables[0] 
    temp_df = temp_df.set_index(temp_df.columns[0]) 
    temp_df = temp_df[temp_df.columns[:4]] 
    temp_df = temp_df.loc[['매출액', '영업이익', '당기순이익']] 

    temp_df2 = fs_tables[2] 
    temp_df2 = temp_df2.set_index(temp_df2.columns[0]) 
    temp_df2 = temp_df2.loc[['자산', '자본', '부채']] 

    temp_df3 = fs_tables[4]
    temp_df3 = temp_df3.set_index(temp_df3.columns[0])
    temp_df3 = temp_df3.loc[['영업활동으로인한현금흐름']]

    fs_df = pd.concat([temp_df, temp_df2, temp_df3])
 
    return fs_df 


def make_fr_dataframe(firm_code): #재무비율 데이터 만들기함수
    fr_url = 'https://comp.fnguide.com/SVO2/asp/SVD_FinanceRatio.asp?pGB=1&cID=&MenuYn=Y&ReportGB=D&NewMenuID=104&stkGb=701&gicode=' + firm_code #fn가이드 재무비율 주소 fr_url로 지정
    fr_page = requests.get(fr_url) 
    fr_tables = pd.read_html(fr_page.text) 
    
    temp_df = fr_tables[0] 
    temp_df = temp_df.set_index(temp_df.columns[0]) 
    temp_df = temp_df.loc[['유동비율계산에 참여한 계정 펼치기',
                           '부채비율계산에 참여한 계정 펼치기',
                           '영업이익률계산에 참여한 계정 펼치기',
                           'ROA계산에 참여한 계정 펼치기',
                           'ROIC계산에 참여한 계정 펼치기']] 
    temp_df.index = ['유동비율', '부채비율', '영업이익률', 'ROA', 'ROIC']  
    return temp_df


def make_invest_dataframe(firm_code): #투자지표 만드는 함수
    invest_url = 'https://comp.fnguide.com/SVO2/asp/SVD_Invest.asp?pGB=1&cID=&MenuYn=Y&ReportGB=D&NewMenuID=105&stkGb=701&gicode=' + firm_code #주소 지정
    invest_page = requests.get(invest_url) 
    invest_tables = pd.read_html(invest_page.text) 
    temp_df = invest_tables[1] 
    
    temp_df = temp_df.set_index(temp_df.columns[0]) 
    temp_df = temp_df.loc[['PER계산에 참여한 계정 펼치기',
                           'PCR계산에 참여한 계정 펼치기',
                           'PSR계산에 참여한 계정 펼치기',
                           'PBR계산에 참여한 계정 펼치기',
                          '총현금흐름']]  
    temp_df.index = ['PER', 'PCR', 'PSR', 'PBR', '총현금흐름'] 
    return temp_df


def change_df(firm_code, dataframe): #데이터프레임의 행과열을 바꾸는 함수 만듬 
    for num, col in enumerate(dataframe.columns):
        temp_df = pd.DataFrame({firm_code : dataframe[col]})
        temp_df = temp_df.T
        temp_df.columns = [[col]*len(dataframe), temp_df.columns]
        if num == 0:
            total_df = temp_df
        else:
            total_df = pd.merge(total_df, temp_df, how='outer', left_index=True, right_index=True)
    
    return total_df


def come_code(): #종목코드 불러오기함수
    path = r'C:\Users\gjals\Desktop\코딩\data.xls'
    code_data = pd.read_excel(path)  
    code_data = code_data[['종목코드', '기업명']] 

    def make_code(x): #종목코드 정리함수 
        x = str(x)  
        return 'A' + '0' * (6-len(x)) + x 
    
    code_data['종목코드'] = code_data['종목코드'].apply(make_code)




def make_total_fs_df(code_data):
    for num, code in enumerate(code_data['종목코드']): #num, code 가 code_data['종목코드'] 안에 있을때
        try: #시도(1)
            print(num,code) #num, code 출력
            time.sleep(1) #1초 쉬고
            try: #시도(2)
                fs_df = make_fs_dataframe(code)  #make_fs_dataframe 함수 실행 데이터 프레임 만듬
            except requests.exceptions.Timeout: #시도(2)했다가 Timeout에러가 발행하면
                time.sleep(60) #60초간 쉬었다
                fs_df = make_fs_dataframe(code) #make_fs_dataframe 함수 실행 데이터 프레임 만듬
            fs_df_changed = change_df(code, fs_df) #행열 바꿈
            if num == 0: 
                total_fs =fs_df_changed #첫번째 행 만듬
            else:
                total_fs = pd.concat([total_fs, fs_df_changed]) #첫행부터 마지막 행까지 병합
        except ValueError: #시도(1)했다가 ValueError가 발생하면 
            continue #계속해라
        except KeyError: #시도(1)했다가 Keyerror가 발생하면 
            continue #계속해라

    total_fs.to_excel(r'C:\Users\gjals\Desktop\코딩\재무데이터test.xlsx') #엑셀로 저장   


def make_total_fr_df(code_data): #전 종목 재무비율데이터 만드는함수
    for num, code in enumerate(code_data['종목코드']): 
        try:
            print(num, code)
            time.sleep(1)
            try:
                fr_df = make_fr_dataframe(code)
            except requests.exceptions.Timeout:
                time.sleep(60)
                fr_df = make_fr_dataframe(code)
            fr_df_changed = change_df(code, fr_df)
            if num == 0:
                total_fr = fr_df_changed
            else:
                total_fr = pd.concat([total_fr, fr_df_changed])
        except ValueError:
            continue
        except KeyError:
            continue
        
    total_fr.to_excel(r'C:\Users\gjals\Desktop\코딩\재무비율데이터test.xlsx')


def make_total_invest_df(code_data): #전 종목 투자지표데이터 만드는함수
    for num,code in enumerate(code_data['종목코드']):
        try:
            print(num, code)
            time.sleep(1)
            try:
                invest_df = make_invest_dataframe(code)
            except requests.exceptions.Timeout:
                time.sleep(60)
                invest_df = make_invest_dataframe(code)
            invest_df_changed = change_df(code, invest_df)
            if num == 0:
                total_invest = invest_df_changed
            else:
                total_invest = pd.concat([total_invest, invest_df_changed])
        except ValueError:
            continue
        except KeyError:
            continue

    total_invest.to_excel(r'C:\Users\gjals\Desktop\코딩\투자지표데이터test.xlsx')


def make_price_dataframe(code, timeframe, count): #가격데이터 함수지정 종목코드, 시간, 갯수
    url = 'https://fchart.stock.naver.com/sise.nhn?requestType=0'
    price_url = url + '&symbol=' + code + '&timeframe=' + timeframe + '&count=' + count 

    price_data = requests.get(price_url) 
    price_data_bs = bs4.BeautifulSoup(price_data.text, 'lxml') 
    item_list = price_data_bs.find_all('item') 
    date_list =[] 
    price_list = [] 
    for item in item_list: 
        temp_data = item['data']
        datas = temp_data.split('|') 
        date_list.append(datas[0]) 
        price_list.append(datas[4]) 
      
    price_df = pd.DataFrame({code : price_list}, index=date_list) 

    return price_df


def make_total_price_df(): #전종목 가격데이터 함수
    for num, code in enumerate(code_data['종목코드']): 
        try: 
            print(num, code) 
            time.sleep(1) 
            try: 
                price_df = make_price_dataframe(code, 'day', '1500') 
            except requests.exception.Timeout: 
                time.sleep(60) 
                price_df = make_price_dataframe(code, 'day', '1500') 
            if num == 0: 
                total_price = price_df 
            else:
                total_price = pd.merge(total_price, price_df, how='outer', right_index=True, left_index=True) 
        except ValueError: 
            continue 
        except KeyError: 
            continue 
    
    total_price.index = pd.to_datetime(total_price.index) 
    total_price.to_excel(r'C:\Users\gjals\Desktop\코딩\가격데이터test.xlsx') 