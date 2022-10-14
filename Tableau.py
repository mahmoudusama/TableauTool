import pandas as pd
import tkinter
from tkinter import Tk, StringVar
import customtkinter
from tkinter.ttk import Label, Combobox, Button
from pathlib import Path
import os


customtkinter.set_appearance_mode("dark")      # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x300")
app.title("TableauCSV.py")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1,justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)

# To get the directory Name
#dirname = os.path.dirname(__file__)

def ExecutableCSV():
    # Browse the file path
     filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select " + optionmenu_1.get() + " " + Graphsshown.get() + " Figure File",
                                          filetypes = (("all files",
                                                        "*.*"),("Text files",
                                                        "*.txt*")
                                                       ))
    SheetName = Graphsshown.get()
    #filename = os.path.join(dirname)
    #print(filename)
    if optionmenu_1.get() == "Overview":
        if Graphsshown.get() == "Total SIMs":
            try:
                df = pd.read_csv(filename)
                executable_df = df.groupby(['Customer Name','Aggregation Date'])["D_Num Devices"].sum()
                print(executable_df.to_string())
                executable_df.to_csv(SheetName+'.csv')
            except:
                print("CSV Name Changed or CSV is not in the right location for "+SheetName)
        elif Graphsshown.get() == "Active Live SIMs":
            try:
                df = pd.read_csv(filename)
                executable_df = df.groupby(['Customer Name','Aggregation Date','Other Sim State'])["D_Num Devices"].sum()
                print(executable_df.to_string())
                executable_df.to_csv(SheetName + '.csv')
            except:
                print("CSV Name Changed or CSV is not in the right location for "+SheetName)
        elif Graphsshown.get() == "Data":
            try:
                df = pd.read_csv(filename)
                executable_df = df.groupby(['Customer Name','Aggregation Date'])["SUM_Bytes"].sum()
                print(executable_df.to_string())
                executable_df.to_csv(SheetName + '.csv')
            except:
                print("CSV Name Changed or CSV is not in the right location for "+SheetName)
        elif Graphsshown.get() == "SMS":
            try:
                df = pd.read_csv(filename)
                executable_df = df.groupby(['Customer Name','Aggregation Date'])["Num Sms"].sum()
                print(executable_df.to_string())
                #executable_df.to_csv(filename + '/' + SheetName + '.csv')
                executable_df.to_csv(SheetName + '.csv')
            except:
                print("CSV Name Changed or CSV is not in the right location for "+SheetName)
        elif Graphsshown.get() == "Voice":
            try:
                df = pd.read_csv(filename)
                executable_df = df.groupby(['Customer Name','Aggregation Date'])["SUM([Duration])/60","Duration"].sum()
                print(executable_df.to_string())
                executable_df.to_csv(SheetName + '.csv')
            except:
                print("CSV Name Changed or CSV is not in the right location for "+SheetName)
        elif Graphsshown.get() == "Data Per Day":
            try:
                df = pd.read_csv(filename)
                executable_df = df.groupby(['Customer Name','Aggregation Date'])["Bytes"].sum()/1024/1000
                executable_df = executable_df.astype({'Bytes': 'int'})
                #print(executable_df.dtypes)
                print(executable_df.to_string())
                executable_df.to_csv(SheetName + '.csv')
            except:
                print("CSV Name Changed or CSV is not in the right location for "+SheetName)
        elif Graphsshown.get() == "Global Data":
            try:
                df = pd.read_csv(filename)
                executable_df = df.groupby(['Customer Name','serving_country_desc','Aggregation Date'])["Bytes"].sum()/1024/1000
                executable_df = executable_df.astype({'Bytes': 'int'})
                #print(executable_df.dtypes)
                print(executable_df.to_string())
                executable_df.to_csv(SheetName + '.csv')
            except:
                print("CSV Name Changed or CSV is not in the right location for "+SheetName)
        elif Graphsshown.get() == "Weekly SIM Count":
            try:
                df = pd.read_csv(filename)
                executable_df = df.groupby(['Customer Name','Aggregation Date','Other Sim State'])["Num Devices"].sum()
                print(executable_df.to_string())
                executable_df.to_csv(SheetName + '.csv')
            except:
                print("CSV Name Changed or CSV is not in the right location for "+SheetName)


# For checking the value of ComboBox
def check(e):
    if optionmenu_1.get() == "Overview":
        Graphsshown.config(value=OverviewGraphs)
        Graphsshown.current(0)
    elif optionmenu_1.get() == "SIM History":
        Graphsshown.config(value=SimHistoryGraphs)
        Graphsshown.current(0)
    elif optionmenu_1.get() == "Data":
        Graphsshown.config(value=DataGraphs)
        Graphsshown.current(0)
    elif optionmenu_1.get() == "SMS":
        Graphsshown.config(value=SmsGraphs)
        Graphsshown.current(0)
    elif optionmenu_1.get() == "Voice":
        Graphsshown.config(value=VoiceGraphs)
        Graphsshown.current(0)
    else:
        Graphsshown.config(value=AnomaliesGraphs)
        Graphsshown.current(0)




# List for all Tableau pages
PagesofTableau = ["Overview", "SIM History", "Data", "SMS", "Voice", "Anomalies"]

# List of Graphs for each page
OverviewGraphs = ["Total SIMs", "Active Live SIMs", "Data", "SMS", "Voice", "Data Per Day",
                  "Global Data", "Weekly SIM Count"]
SimHistoryGraphs = ["SIMs per Home Country", "Communicating SIMs","SIMs per Device Type",
                    "SIM State History"]
DataGraphs = ["Usage History Per Country", "Monthly Global Data Usage for the Last 31 Days",
              "Unusual Data Usage", "Unusual Sessions", "Unusual Zero Byte Sessions"]
SmsGraphs = ["SMS MO Per Country", "All SMS by Event Type", "Unusual Recent SMS MO Activity Per Country",
             "All SMS Delivery Status"]
VoiceGraphs = ["Voice Usage History Per Country", "Daily Voice Minutes by Call Senario", "Unusal Voice Minutes",
               "Monthly Global Voice Usage for the Last 31 Days"]
AnomaliesGraphs = ["Anomalous IMSIs per Customer Service Profile", "Anomalous IMSIs",
                   "Anomalies for the Last 7 days", "Tree of Anomalies", "Map of Anomalous IMSIs per Country",
                   "Number of Anomalous IMSIs per Serving Network"]


optionmenu_1 = Combobox(frame_1,values=PagesofTableau)
optionmenu_1.pack(pady=12, padx=10)
optionmenu_1.set("Workbook")

optionmenu_1.bind("<<ComboboxSelected>>", check)

Graphsshown = Combobox(frame_1,values=[" "])
Graphsshown.pack(pady=12, padx=10)
Graphsshown.set("Graphs")

btn = Button(frame_1, text="Execute", command=ExecutableCSV)
btn.pack(pady=20, padx=10)


app.mainloop()
