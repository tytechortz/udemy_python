from bokeh.plotting import figure 
from bokeh.io import output_file, show 
import pandas as pd 

df=pd.read_csv("http://pythonhow.com/data/bachelors.csv")
x=df['Year']
y=df['Engineering']

output_file("bachelors_csv.html")

f=figure()

f.line(x,y)

show (f)