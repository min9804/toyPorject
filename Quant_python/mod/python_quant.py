import pandas as pd
import requests
import time
import numpy as np
import bs4


# 데이터 전처리 개선
def get_finance_data(path):
    data_path = path
    raw_data = pd.read_excel(data_path)
    big_col = list(raw_data.columns)
    small_col = list(raw_data.iloc[0])

    big_col[0] = '종목'
    small_col[0] = ''
    new_big_col = []
    for num, col in enumerate(big_col):
        if 'Unnamed' in col:
            new_big_col.append(new_big_col[num-1])
        else:
            new_big_col.append(big_col[num])

    raw_data.columns = [new_big_col, small_col]
    raw_data = raw_data.drop(0)
    clean_df = raw_data.drop(1)

    if clean_df.index[0] == clean_df['종목'][2]:
        pass
    else:
        for i in clean_df.index:
            clean_df = clean_df.rename(index={i: clean_df['종목'][i]})

    clean_df = clean_df.drop(clean_df.columns[0:1], axis=1, inplace=False)

    return clean_df


def check_IFRS(x):  # N/A_IFRS(x)를 Nan으로 바꾸기
    if x == 'N/A(IFRS)':
        return np.NaN
    else:
        return x


def low_per(invest_df, index_date, num):  # per기준으로 오름차순 정렬
    invest_df[(index_date, 'PER')] = pd.to_numeric(
        invest_df[(index_date, 'PER')])
    per_sorted = invest_df.sort_values(by=(index_date, 'PER'))
    return per_sorted[index_date][:num]


def high_roa(fr_df, index_date, num):  # roa기준으로 내림차순 정렬
    fr_df[(index_date, 'ROA')] = fr_df[(index_date, 'ROA')].apply(check_IFRS)
    fr_df[(index_date, 'ROA')] = pd.to_numeric(fr_df[(index_date, 'ROA')])
    sorted_roa = fr_df.sort_values(by=(index_date, 'ROA'), ascending=False)
    return sorted_roa[index_date][:num]


def magic_formula(fr_df, invest_df, index_date, num):  # 마법공식 저per, 고roa 합성 함수
    per = low_per(invest_df, index_date, None)
    roa = high_roa(fr_df, index_date, None)
    per['per순위'] = per['PER'].rank()
    roa['roa순위'] = roa['ROA'].rank(ascending=False)
    magic = pd.merge(per, roa, how='outer', left_index=True, right_index=True)
    magic['마법공식 순위'] = (magic['per순위'] + magic['roa순위']).rank().sort_values()
    magic = magic.sort_values(by='마법공식 순위')
    return magic[:num]


def get_value_rank(invest_df, value_type, index_date, num):  # 저평가 지수 기준으로 정렬해 순위 만들어 주는 함수
    invest_df[(index_date, value_type)] = pd.to_numeric(
        invest_df[(index_date, value_type)])
    value_sorted = invest_df.sort_values(
        by=(index_date, value_type))[index_date]
    value_sorted[value_type + '순위'] = value_sorted[value_type].rank()
    return value_sorted[[value_type, value_type + '순위']][:num]


def make_value_combo(value_list, invest_df, index_date, num):  # 저평가 지표 조합 함수

    for i, value in enumerate(value_list):
        temp_df = get_value_rank(invest_df, value, index_date, None)
        if i == 0:
            value_combo_df = temp_df
            rank_combo = temp_df[value + '순위']
        else:
            value_combo_df = pd.merge(
                value_combo_df, temp_df, how='outer', right_index=True, left_index=True)
            rank_combo = rank_combo + temp_df[value + '순위']

    value_combo_df['종합순위'] = rank_combo.rank()
    value_combo_df = value_combo_df.sort_values(by='종합순위')

    return value_combo_df[:num]


def get_fscore(fs_df, index_date, num):  # f스코어
    fscore_df = fs_df[index_date]
    fscore_df['당기순이익점수'] = fscore_df['당기순이익'] > 0
    fscore_df['영업활동점수'] = fscore_df['영업활동으로인한현금흐름'] > 0
    fscore_df['더큰영업활동점수'] = fscore_df['영업활동으로인한현금흐름'] > fscore_df['당기순이익']
    fscore_df['종합점수'] = fscore_df[[
        '당기순이익점수', '영업활동점수', '더큰영업활동점수']].sum(axis=1)
    fscore_df = fscore_df[fscore_df['종합점수'] == 3]
    return fscore_df[:num]


price_path = r'C:\Users\gjals\Desktop\코딩\가격데이터.xlsx'


def new_price_data(path):  # 가격데이터 전처리함수
    price_df = pd.read_excel(path)

    for i in range(0, 1500):
        price_df = price_df.rename(index={i: price_df['Unnamed: 0'][i]})

    price_df = price_df.drop(price_df.columns[0:1], axis=1, inplace=False)

    return price_df


def get_momentum_rank(price_df, index_date, date_range, num):  # 모멘텀 함수
    momentum_df = pd.DataFrame(price_df.pct_change(date_range).loc[index_date])
    momentum_df.columns = ['모멘텀']
    momentum_df['모멘텀순위'] = momentum_df['모멘텀'].rank(ascending=False)
    momentum_df = momentum_df.sort_values(by='모멘텀순위')
    return momentum_df[:num]


def get_value_quality(invest_df, fs_df, index_date, num):  # 저평가 지수 + f스코어
    value = make_value_combo(
        ['PER', 'PBR', 'PSR', 'PCR'], invest_df, index_date, None)
    quality = get_fscore(fs_df, index_date, None)
    value_quality = pd.merge(value, quality, how='outer',
                             right_index=True, left_index=True)
    value_quality_filtered = value_quality[value_quality['종합점수'] == 3]
    vq_df = value_quality_filtered.sort_values(by='종합순위')
    return vq_df[:num]


# 기본세팅
# import pandas as pd
# import requests
# import time
# import numpy as np
# import bs4

# from mod.python_quant import get_finance_data #(fs,fr,invest_path)
# from mod.python_quant import check_IFRS #(x): #N/A_IFRS(x)를 Nan으로 바꾸기
# from mod.python_quant import low_per #(invest_df, index_date, num): #per기준으로 오름차순 정렬
# from mod.python_quant import high_roa #(fr_df, index_date, num): #roa기준으로 내림차순 정렬
# from mod.python_quant import magic_formula #(fr_df, invest_df, index_date, num): #마법공식 저per, 고roa 합성 함수
# from mod.python_quant import get_value_rank #(invest_df, value_type, index_date, num): #저평가 지수 기준으로 정렬해 순위 만들어 주는 함수
# from mod.python_quant import make_value_combo #(value_list, invest_df, index_date, num): #저평가 지표 조합 함수
# from mod.python_quant import get_fscore #(fs_df, index_date, num): #f스코어
# from mod.python_quant import new_price_data #(path): #가격데이터 전처리함수
# from mod.python_quant import get_momentum_rank #(price_df, index_date, date_range, num): #모멘텀 함수
# from mod.python_quant import get_value_quality #(invest_df, fs_df, index_date, num): #저평가 지수 + f스코어

# fs_path = r'C:\Users\gjals\Desktop\코딩\재무데이터.xlsx'
# fr_path = r'C:\Users\gjals\Desktop\코딩\재무비율데이터.xlsx'
# invest_path = r'C:\Users\gjals\Desktop\코딩\투자지표데이터.xlsx'
# price_path = r'C:\Users\gjals\Desktop\코딩\가격데이터.xlsx'

# fs_df = get_finance_data(fs_path)
# fr_df = get_finance_data(fr_path)
# invest_df = get_finance_data(invest_path)
# price_df = new_price_data(price_path)
# higit
