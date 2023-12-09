import pandas as pd
import numpy as np
#--------------------------------------Q1--------------------------------------------

def calculate_distance_matrix(dataset):
    df = pd.read_csv(dataset)
    #print(df)
    unique_ids = np.unique(df[['id_start', 'id_end']].values)

    num_ids = len(unique_ids)
    distance_matrix = np.zeros((num_ids, num_ids))

    for index, row in df.iterrows():
        start_index = np.where(unique_ids == row['id_start'])[0][0]
        end_index = np.where(unique_ids == row['id_end'])[0][0]

      
        distance_matrix[start_index, end_index] += row['distance']
        distance_matrix[end_index, start_index] += row['distance']

    np.fill_diagonal(distance_matrix, 0)

    result_df = pd.DataFrame(distance_matrix, index=unique_ids, columns=unique_ids)

    return result_df

# Example usage
dataset_path = r'C:\Users\Asus\Desktop\MapUp-Data-Assessment-F-main\datasets\dataset-3.csv'
result_distance_matrix = calculate_distance_matrix(dataset_path)
#print(result_distance_matrix)
#--------------------------------------Q2--------------------------------------------
 

def unroll_distance_matrix(distance_matrix_df):
    unique_combinations = pd.melt(distance_matrix_df.reset_index(), id_vars='index').dropna()

    unique_combinations.columns = ['id_start', 'id_end', 'distance']

    unique_combinations = unique_combinations[unique_combinations['id_start'] != unique_combinations['id_end']]

    unique_combinations.reset_index(drop=True, inplace=True)

    return unique_combinations

result_unrolled = unroll_distance_matrix(result_distance_matrix)
#print(result_unrolled)
#--------------------------------------Q3--------------------------------------------

def find_ids_within_ten_percentage_threshold(distance_df, reference_value):

    reference_rows = distance_df[distance_df['id_start'] == reference_value]

    avg_distance = reference_rows['distance'].mean()

    threshold_min = 0.9 * avg_distance
    threshold_max = 1.1 * avg_distance

    result_ids = sorted(distance_df[(distance_df['distance'] >= threshold_min) & (distance_df['distance'] <= threshold_max)]['id_start'].unique())

    return result_ids

reference_value = 1001402
result_within_threshold = find_ids_within_ten_percentage_threshold(result_unrolled, reference_value)
print(result_within_threshold)

#--------------------------------------Q4--------------------------------------------

def calculate_toll_rate(distance_df):
    result_df = distance_df.copy()

    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}


    for vehicle_type, coefficient in rate_coefficients.items():
        result_df[vehicle_type] = result_df['distance'] * coefficient

    return result_df

result_with_toll_rate = calculate_toll_rate(result_unrolled)
print(result_with_toll_rate)