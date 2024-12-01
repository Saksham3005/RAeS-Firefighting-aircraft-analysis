import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def clean_and_load_csv(file_path, delimiter=",", max_columns=None):
    cleaned_rows = []

    with open(file_path, 'r') as file:
        for line in file:
            split_line = line.strip().split(delimiter)

            if max_columns:
                split_line += [""] * (max_columns - len(split_line))

            cleaned_rows.append(split_line)

    if not max_columns:
        max_columns = max(len(row) for row in cleaned_rows)

    cleaned_rows = [row[:max_columns] for row in cleaned_rows]
    df = pd.DataFrame(cleaned_rows)

    return df

def plot_labels_from_csv(file_path, label1, label1_index, label2, label2_index, t):
    df = clean_and_load_csv(file_path)
    # print("Cleaned DataFrame head:\n", df.head())

    df.set_index(0, inplace=True)

    unique_labels = df.index.unique()
    # print("Unique labels found:", unique_labels)

    if label1 not in unique_labels or label2 not in unique_labels:
        raise ValueError(f"Labels '{label1}' and/or '{label2}' not found in CSV file.")

    label1_rows = df.loc[label1]
    label2_rows = df.loc[label2]
    # print("Label 1 Rows:\n", label1_rows)
    # print("Label 2 Rows:\n", label2_rows)

    if label1_index >= len(label1_rows) or label2_index >= len(label2_rows):
        raise IndexError("Index out of range for the specified label.")

    data_label1 = label1_rows.iloc[label1_index].values
    data_label2 = label2_rows.iloc[label2_index].values

    data_label1= data_label1[:8].astype(np.float32)
    data_label2= data_label2[:8].astype(np.float32)

    if t == 0:
        return np.mean(data_label1),(np.mean(data_label2))
    else:
        return np.mean(data_label1),(np.mean(data_label2)*0.5*1.12*83*83*40)
    


times = 42

# Example usage
file_path = 'TSA_1_25_results.csv'  
label1 = 'Alpha'  
label1_index = 0   
label2 = 'CL' 
label2_index = 0

alpha=[]
cl=[]

for i in tqdm(range(0,times)):
  
    a,b=plot_labels_from_csv(file_path, label1,i, label2, i, 0)
    alpha.append(a)
    cl.append(b)


label1 = 'Alpha'  
label1_index = 0   
label2 = 'CMy' 
label2_index = 0

alpha=[]
CMy=[]


for i in tqdm(range(0,times)):
  
    a,b=plot_labels_from_csv(file_path, label1,i, label2, i, 0)
    alpha.append(a)
    CMy.append(b)
    

label1 = 'Alpha'  
label1_index = 0   
label2 = 'L/D' 
label2_index = 0

alpha=[]
Eff = []


for i in tqdm(range(0,times)):
  
    a,b=plot_labels_from_csv(file_path, label1,i, label2, i, 0)
    alpha.append(a)
    Eff.append(b)
    
 
label1 = 'Alpha'  
label1_index = 0   
label2 = 'CFz' 
label2_index = 0

alpha=[]
Fz=[]


for i in tqdm(range(0,times)):
  
    a,b=plot_labels_from_csv(file_path, label1,i, label2, i, 1)
    alpha.append(a)
    Fz.append(b)
    


# CL vs Alpha
plt.figure(figsize=(8, 6))
plt.plot(alpha, cl, marker='o', linestyle='-', color='b')
plt.xlabel('alpha')
plt.ylabel('CL')
plt.title('CL vs alpha')

# Show the plot
plt.grid(True)
plt.show()


#Cm vs Alpha
plt.figure(figsize=(8, 6))
plt.plot(alpha, CMy, marker='o', linestyle='-', color='b')
plt.xlabel('alpha')
plt.ylabel('Cm')
plt.title('Cm vs alpha')

# Show the plot
plt.grid(True)
plt.show()
 
 
#Efficiency vs Alpha
plt.figure(figsize=(8, 6))
plt.plot(alpha, Eff, marker='o', linestyle='-', color='b')
plt.xlabel('alpha')
plt.ylabel('L/D')
plt.title('L/D vs alpha')

# Show the plot
plt.grid(True)
plt.show()


#Lift vs Alpha
plt.figure(figsize=(8, 6))
plt.plot(alpha, Fz, marker='o', linestyle='-', color='b')
plt.xlabel('alpha')
plt.ylabel('Fz')
plt.title('Fz vs alpha')

# Show the plot
plt.grid(True)
plt.show()

 