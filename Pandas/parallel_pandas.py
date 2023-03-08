import psutil
import pandas as pd
import numpy as np
import concurrent.futures

def remove_text(df):
    df['name'] = df['name'].str.replace('test', '')
    return df

data = [
    {
        'name': 'this is a test of new text'
    },
    {
        'name': 'this is another test of text'
    },
    {
        'name': 'this is a test of text'
    },
    {
        'name': 'this is a test of text'
    }
]

if __name__ == '__main__':
    num_process = psutil.cpu_count()

    dataset = pd.DataFrame(data)

    splitted = np.array_split(dataset, 2)

    df_results = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_process) as executor:
        results = [ executor.submit(remove_text,df=df) for df in splitted ]
        for result in concurrent.futures.as_completed(results):
            df_results.append(result.result())

    df_results = pd.concat(df_results)
    print(df_results)
