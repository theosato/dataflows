import sys 
sys.path.append('/opt/airflow/')

import pandas as pd

def script2_function():
    df = pd.read_csv('/opt/airflow/output/script1_output.csv')
    # Process the data...
    output_path = '/opt/airflow/output/script2_output.csv'
    df.to_csv(output_path, index=False)
    print(f"Output saved to {output_path}")
