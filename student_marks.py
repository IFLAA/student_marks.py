# # import pandas as pd
# # data={
# #     "name":['aman','neha','ravi'],
# #     "department":['hr','it','sales'],
# #     "salary":[25000,40000,30000]
# # }
# # df=pd.DataFrame(data)
# # print(df)
# # avg_sal=df.groupby('department')['salary'].mean()
# # print(avg_sal)
# # sales = df[df['salary']>30000]
# # print(sales)

# # highest_paid=df.loc[df["salary"].idxmax()]
# # print("highest_paid")

# import pandas as pd
# wheather={
#     "date":['2025-09-01','2025-09-01','2025-09-01','2025-09-02','2025-09-02','2025-09-02','2025-09-03','2025-09-03','2025-09-03',
#             '2025-09-04','2025-09-04','2025-09-04','2025-09-05','2025-09-05','2025-09-05','2025-09-06','2025-09-06','2025-09-06'],
#     "city":['delhi','mumbai','chandigarh','delhi','mumbai','chandigarh','delhi','mumbai','chandigarh','delhi','mumbai','chandigarh','delhi','mumbai','chandigarh',
#             'delhi','mumbai','chandigarh'],
#     "temperature":[35, 30, 28, 36, 31, 27,34, 29, 26, 33, 30, 28, 32, 31,27,31,32,29]
# }
# df=pd.DataFrame(wheather)
# print(df)

# for key in wheather:
#     print(f"{key}:{len(wheather[key])}")

# # Convert Date column to datetime
# df['date']=pd.to_datetime(df["date"])
# df.columns=df.columns.str.strip()

# # # Step 2: City-wise average temperature
# avg_temp=df.groupby('city')['temperature'].mean()
# print(avg_temp)

# # # Step 3: Hottest city (maximum temperature)
# hottes_city=df.loc[df["temperature"].idxmax()]
# print(hottes_city)

# import matplotlib.pyplot as plt

# # # Step 4: Last 5 days Delhi temperature trend
# delhi_data = df[df['city'] == 'delhi'].sort_values('date').tail(5)
# plt.plot(delhi_data['date'], delhi_data['temperature'], marker="o", color="red")
# plt.title("Delhi Last 5 Days temperature Trend")
# plt.xlabel("date")
# plt.ylabel("temperature (°C)")
# plt.grid(True)
# plt.show()         

import numpy as np
import pandas as pd

array_marks=np.random.randint(40, 101, size=(10, 3))
print(array_marks)

# List of student names
students = [f"Student{i}" for i in range(1, 11)]
print(students)

# Create DataFrame
df = pd.DataFrame(array_marks, columns=["Math", "Science", "English"])
df["Student"] = students

# Reorder columns to put "Student" first
df = df[["Student", "Math", "Science", "English"]]
print(df)

avg_marks=df[['Math','Science','English']].mean()
print(avg_marks)

df['total_marks']=df[['Math','Science','English']].sum(axis=1)
top_student = df.loc[df['total_marks'].idxmax()]
print(top_student)

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.bar(df['Student'], df['total_marks'], color="skyblue")
plt.title("Total Marks per Student")
plt.xlabel("Student")
plt.ylabel("Total Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
