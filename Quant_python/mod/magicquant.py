def magic_by_pd(path): 
    import pandas as pd 

    per_data = pd.read_excel(path, sheet_name='per', index_col=0)
    filtered_per = per_data[per_data['per'] > 0]
    sorted_per = filtered_per.sort_values(by='per')
    sorted_per['per랭킹'] = sorted_per['per'].rank()


    roa_data = pd.read_excel(path, sheet_name='roa', index_col=0)
    filtered_roa = roa_data.dropna()
    filtered_roa.columns = ['roa']
    sorted_roa = filtered_roa.sort_values(by='roa', ascending=False)
    sorted_roa['roa랭킹'] = sorted_roa.rank(ascending=False)

    total_df = pd.merge(sorted_per, sorted_roa, how='inner', left_index=True, right_index=True)

    total_df['종합랭크'] = (total_df['per랭킹'] + total_df['roa랭킹']).rank()
    return total_df.sort_values(by='종합랭크') 