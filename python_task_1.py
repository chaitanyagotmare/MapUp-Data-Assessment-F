#---------------------- Q1 -------------------------------------
import pandas as pd

def generate_car_matrix(dataset):
    df = pd.read_csv(dataset) #for reading csv and converting to dataframe
    result = df.pivot_table(values='car', index='id_1', columns='id_2', fill_value=0)
    
    return result

datasetPath = r'C:\Users\Asus\Desktop\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
new_df = generate_car_matrix(datasetPath)
print(new_df)

#---------------------- Q2 -------------------------------------
import pandas as pd
import numpy as np
def get_type_count(dataset):

    df = pd.read_csv(dataset)
    conditions = [
                (df['car'] <= 15),
                ((df['car'] > 15) & (df['car'] <= 25)),
                (df['car'] > 25)
                  ]
    choices = ['low', 'medium', 'high']
    for i,j in zip(conditions, choices):
        df.loc[i,"car_type"] = j
    typeCount = df['car_type'].value_counts().to_dict() #calc occurence
    typeCount = dict(sorted(type_count.items())) # sorting dict in alpha order

    return typeCount

datasetPath =r'C:\Users\Asus\Desktop\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
sorted_typeCount = get_type_count(datasetPath)
print("SORTED DICT--->", sorted_typeCount)

#-------------------------- Q3 --------------------------------------
import pandas as pd

def get_bus_indexes(dataset):
    df = pd.read_csv(dataset)
    
    bus_mean = df['bus'].mean() #mean value
    print("Mean value: ", bus_mean)

    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()  #bus' values are greater than twice the mean
    #print("Bus indexes list-->", bus_indexes)
    bus_indexes.sort() #asc sort
    #print("Sorted list---->", bus_indexes)
    return bus_indexes

# Example usage
datasetPath = r'C:\Users\Asus\Desktop\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
result_busIndexes = get_bus_indexes(datasetPath)
print("sorted list--->",result_busIndexes)

#----------------------Q4------------------------------------
import pandas as pd

def filter_routes(dataset):
    df = pd.read_csv(dataset)

   
    route_avg_truck = df.groupby('route')['truck'].mean() #calculating average by grouping

    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist() #filtering > 7

    filtered_routes.sort() #sorted list

    return filtered_routes

# Example usage
datasetPath = r'C:\Users\Asus\Desktop\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
result_filteredRoutes = filter_routes(datasetPath)
print(result_filteredRoutes)

#----------------------------- Q5 -------------------------
import pandas as pd
def generate_car_matrix(dataset):
    df = pd.read_csv(dataset) #for reading csv and converting to dataframe
    result = df.pivot_table(values='car', index='id_1', columns='id_2', fill_value=0)
    
    return result

datasetPath = r'C:\Users\Asus\Desktop\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
new_df = generate_car_matrix(datasetPath)
#print(new_df)

def multiply_matrix(input_matrix):
    
    modified_matrix = input_matrix.copy() #copy the df 

    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25

    modified_matrix = modified_matrix.round(1) # to decimal one

    return modified_matrix

modifiedResult = multiply_matrix(new_df) #using df of generate_car_matrix function
print(modifiedResult)

