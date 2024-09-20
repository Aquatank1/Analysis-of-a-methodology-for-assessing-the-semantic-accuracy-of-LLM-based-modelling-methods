import numpy as np
import pandas as pd
import os
def hilfsdinfs(a1,b1,c1,d1,e1,f2,g1,f1):
    a = np.array(a1).reshape(-1, 1)
    b = np.array(b1).reshape(-1, 1)
    c = np.array(c1).reshape(-1, 1)
    d = np.array(d1).reshape(-1, 1)
    e = np.array(e1).reshape(-1, 1)
    f3 = np.array(f2).reshape(-1, 1)
    g3 = np.array(g1).reshape(-1, 1)
    f = np.array(f1).reshape(-1, 1)
    #print(matrix)
    ap =  ['Names changed', 'other arrangements', '2 associations removed', 'all associations removed', 'other structure', 'small class removed', 'large class removed', 'classdiagram{}']
    asp =  np.array(ap).reshape(-1, 1)
    # Stack the vectors to form a matrix
    matrix = np.hstack([asp,f,a,b,c,d,e,f3,g3])
    # Convert the NumPy array to a pandas DataFrame
    df = pd.DataFrame(matrix, columns=['Change','Average', 'Universitybetter', 'Mycompanybetter', 'Pizzeriabetter', 'Elevatorbetter', 'BicycleIObetter',"Trainbetter" ,"BicycleSellerbetter" ])
    # Specify the location where you want to save the Excel file
    file_path = 'C:/Users/fredg/Documents/Semester 6/Bachelor/Code/matrix_output.xlsx'
    try:
        os.remove(file_path)
    except Exception as e:
        i = 0
    # Save the DataFrame to the specified location
    df.to_excel(file_path, index=False)
    print(df)

def hilfsding_testing(a1,b1,c1,e1,f1):
    a = np.array(a1).reshape(-1, 1)
    b = np.array(b1).reshape(-1, 1)
    c = np.array(c1).reshape(-1, 1)
    e = np.array(e1).reshape(-1, 1)
    f = np.array(f1).reshape(-1, 1)
    #print(matrix)
    ap =  [ 'Names changed', 'other arrangements', '2 associations removed', 'all associations removed', 'other structure', 'small class removed', 'large class removed', 'testing', 'classdiagram{}']
    asp =  np.array(ap).reshape(-1, 1)
    # Stack the vectors to form a matrix
    matrix = np.hstack([asp,f,a,b,c,e])
    # Convert the NumPy array to a pandas DataFrame
    df = pd.DataFrame(matrix, columns=['Change','Average', 'University', 'Mycompany', 'Pizzeria',  'BicycleIO' ])
    # Specify the location where you want to save the Excel file
    file_path = 'C:/Users/fredg/Documents/Semester 6/Bachelor/Code/matrix_output.xlsx'
    try:
        os.remove(file_path)
    except Exception as e:
        i = 0
    # Save the DataFrame to the specified location
    df.to_excel(file_path, index=False)
    print(df)

def hilfsding(a1,b1,c1,e1,f1):
    a = np.array(a1).reshape(-1, 1)
    b = np.array(b1).reshape(-1, 1)
    c = np.array(c1).reshape(-1, 1)
    e = np.array(e1).reshape(-1, 1)
    f = np.array(f1).reshape(-1, 1)
    #print(matrix)
    ap =  [ 'Names changed', 'other arrangements', '2 associations removed', 'all associations removed', 'other structure', 'small class removed', 'large class removed', 'classdiagram{}']
    asp =  np.array(ap).reshape(-1, 1)
    # Stack the vectors to form a matrix
    matrix = np.hstack([asp,f,a,b,c,e])
    # Convert the NumPy array to a pandas DataFrame
    df = pd.DataFrame(matrix, columns=['Change','Average', 'University', 'Mycompany', 'Pizzeria',  'BicycleIO', ])
    # Specify the location where you want to save the Excel file
    file_path = 'C:/Users/fredg/Documents/Semester 6/Bachelor/Code/matrix_output.xlsx'
    try:
        os.remove(file_path)
    except Exception as e:
        i = 0
    # Save the DataFrame to the specified location
    df.to_excel(file_path, index=False)
    print(df)

#hilfsding([0.9801, 0.9979, 0.9981, 0.9902, 0.9957, 0.9977, 0.9921, 0.8452] , [0.9839, 0.9966, 0.9974, 0.9938, 0.9908, 0.998, 0.9973, 0.8608] , [0.9766, 0.9984, 0.9996, 0.998, 0.9857, 0.9994, 0.9973, 0.8434] , [0.9797, 0.996, 0.9994, 0.9974, 0.9866, 0.9995, 0.9961, 0.8478] , [0.980075, 0.9972249999999999, 0.998625, 0.99485, 0.9897, 0.99865, 0.9957, 0.8492999999999999])

hilfsding([0.9535, 0.9904, 0.9938, 0.9689, 0.9838, 0.9943, 0.9791, 0.4016] , [0.944, 0.9856, 0.9942, 0.9856, 0.9827, 0.9945, 0.9944, 0.3119] , [0.9433, 0.9821, 0.9978, 0.995, 0.9661, 0.9959, 0.9924, 0.3495] , [0.9354, 0.9729, 0.9977, 0.9962, 0.9543, 0.9979, 0.9949, 0.3372] , [0.94405, 0.98275, 0.9958750000000001, 0.986425, 0.971725, 0.99565, 0.9902, 0.35005])