def my_first_func():
    pass

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."


if __name__ == "__main__":
    dog = Dog("Buddy", 3)
    print(dog.speak())
    
    cat = Cat("Whiskers", 2)
    print(cat.speak())

import csv
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import glob
import os 
import subprocess



if __name__ == "__main__":
    holgers_files_dir = '/home/kgomesdo/Downloads/logs_for_test/'
    demo_csv = "demofile.csv"

    folder_path = "/home/kgomesdo/Downloads/logs_for_test/bunch_of_logs" 
    counter = 0
    xyts_list = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".xyt"):
                file_path =os. path.join(root,file)   
                df=pd.read_csv(file_path, sep =r"\s+" , names = ["x" , "y" , "time"])
                print("File :" , file_path)
                print(df)
                counter = counter+1

                xyts_list.append(file_path)
    print("list of founded files: ", xyts_list[:3])


    for csv_file in xyts_list:
        df = pd.read_csv(csv_file, delimiter=" ", names=['x', 'y', 't'], dtype=np.float64, decimal=",")
    
        df["distance"] = (
            df["x"].diff()**2 + df["y"].diff()**2)
    
        df["time_diffrence"] = df["t"].diff()
        df["speed"] = df["distance"] /  df["time_diffrence"] 
        total_distance = df["distance"].sum()
        max_val= df["t"].max()
        average = total_distance / max_val
    
        print("average speed:", average) 
        print("total_distance:" ,  total_distance)

        plt.plot(df["x"],df["y"])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("car trajectory")
        plt.show() 
