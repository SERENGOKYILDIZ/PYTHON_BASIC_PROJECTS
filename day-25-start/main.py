days = []
temperatures = []
condition = []

#ELLE YAPMA
# with open("./weather_data.csv", mode="r") as file:
#     line = file.readlines()
#     for i in range(1, len(line)):
#         line[i] = line[i].replace("\n", "")
#         line[i] = line[i].replace(" ", "")
#         new_list = line[i].split(",")
#         days.append(new_list[0])
#         temps.append(new_list[1])
#         condition.append(new_list[2])
#
# print(days)
# print(temps)
# print(condition)


#CSV İLE YAPMA
# import csv
#
# with open("./weather_data.csv", mode="r") as file:
#     data = csv.reader(file)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#
# print(temperatures)


#PANDAS İLE YAPMA
# import pandas
#
# data = pandas.read_csv("./weather_data.csv")
# # print(data)
# print(data["day"])
# # print(data["temp"])

#ÇEVİRME
# import pandas
#
# data = pandas.read_csv("./weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

#FARKLI KULLANIMLAR
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
#
# print(data["temp"].max())
#
# #DATA SÜTÜN
# print(data.condition)

#DATA SATIR
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()]) #Sıcaklığı max olan satırı aldık

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#Data Çerçevesi ile CSV oluşturma
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict) #dict'i csv formatına dönüştürüp dataya attı
# data.to_csv("new_data.csv") #datayı yeni bir cvs dosyasına çevirdi
# print(data)




#SİNCAP VERİLERİ
import pandas

file = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#Uzun yol
# Furs = {
#     "Fur Color": [],
#     "Count": []
# }
#
# for fur in file["Primary Fur Color"]:
#     var_mi = False
#     if type(fur) is float:
#         continue
#     for i in range(len(Furs["Fur Color"])):
#         if fur == Furs["Fur Color"][i]:
#             var_mi = True
#             Furs["Count"][i] += 1
#             break
#     if not var_mi:
#         Furs["Fur Color"].append(fur)
#         Furs["Count"].append(1)

#Kısa yol
grey_count = len(file[file["Primary Fur Color"] == "Gray"])
red_count = len(file[file["Primary Fur Color"] == "Cinnamon"])
black_count = len(file[file["Primary Fur Color"] == "Black"])

Furs = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count]
}

data = pandas.DataFrame(Furs)
data.to_csv("furs.csv")

