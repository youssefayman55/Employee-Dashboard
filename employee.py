# importing libraries
import streamlit as st 
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title = "Employee Dashboard",
    page_icon =  ":bar_chart:" ,
    layout = "wide",
    initial_sidebar_state = "expanded"
)

# Main Page 
st.title(":bar_chart: Empolyee Dashboard")
st.markdown("---")


# Read Data set To Build The Dashboard
st.subheader(":anger: Info about dataset :question:")
st.info(":star: this is our dataset which we will use in this data analysis project , this dataset on kaggle website.")
data = pd.read_excel("Employees.xlsx")
st.dataframe(data)
st.markdown("---")

# Sidebar 
st.sidebar.header(":bar_chart: Employee Dashboard")
st.sidebar.image("employee.jpeg")
st.sidebar.write(":star: This dashboard is using employee data from kaggle website for educational purposes.")
st.sidebar.markdown("---")

st.sidebar.header(":anger: Filter Your Data Hear :")

filter_one = st.sidebar.selectbox(":star: Filter One :" , [None ,"Gender" ,"Department","Country","Center"])
filter_two = st.sidebar.selectbox(":star: Filter Two :" , [None  ,"Overtime Hours","Sick Leaves","Unpaid Leaves"])
st.sidebar.markdown("---")

st.sidebar.markdown(":exclamation: Linkenin Account :heart_eyes:  Eng.[Youssef Ayman](https://www.linkedin.com/in/youssef-ayman-4440342a4/)")
st.sidebar.markdown(":exclamation: GitHub Account :heart_eyes: Eng.[Youssef Ayman](https://www.linkedin.com/in/youssef-ayman-4440342a4/)")

# important numbers from dataset
a1 , a2 , a3 , a4 = st.columns(4)

a1.metric(":maple_leaf: max years experience :" , data["Years"].max())
a1.metric(":maple_leaf: min years experience :" , data["Years"].min())

a2.metric(":maple_leaf: max monthly salary :" , data["Monthly Salary"].max())
a2.metric(":maple_leaf: min monthly salary :" , data["Monthly Salary"].min())

a3.metric(":maple_leaf: max annual salary :" , data["Annual Salary"].max())
a3.metric(":maple_leaf: min annual salary :" , data["Annual Salary"].min())

a4.metric(":maple_leaf: max overtime hours :" , data["Overtime Hours"].max())
a4.metric(":maple_leaf: min overtime hours :" , round(data["Overtime Hours"].mean(),4))

# Top KPI;s
number_of_employees = data["No"].sum()
total_Month_salary = data["Monthly Salary"].sum()
total_annumal_salary = data["Annual Salary"].sum()

c1 , c2 ,c3  = st.columns(3)

with c1:
    st.subheader("No_of_employees:")
    st.subheader(f"{number_of_employees} EMP")

with c2:
    st.subheader("total_Month_salary :")
    st.subheader(f"US $ : {total_Month_salary} ")

with c3:
    st.subheader("total_annumal_salary:")
    st.subheader(f"US $ : {total_annumal_salary}")
st.markdown("---")

# fig1 monthly salary by the department  (Bar Chart)
monthly_salary_by_years = (
    data.groupby(by=["Department"]).sum(numeric_only=True)
)
st.subheader(":bar_chart: Monthly Salary by The Department")
fig1 = px.bar(
    monthly_salary_by_years,
    x = data["Department"],
    y = data["Monthly Salary"],
    color_discrete_sequence=["#0083B8"] * len( monthly_salary_by_years),
    orientation ="v",
    template="plotly_white"
)

fig1.update_layout(
    xaxis = (dict(tickmode = "linear")),
    plot_bgcolor = "rgba(0,0,0,0)",
    yaxis = (dict(showgrid = False))
)

st.plotly_chart(fig1,use_container_width=True)
st.markdown("---")

# fig2 annual salary by the department  (Bar Chart)
annual_salary_by_years = (
    data.groupby(by=["Department"]).sum(numeric_only=True)
)
st.subheader(":bar_chart: Annual Aalary by The Department")
fig2 = px.bar(
    monthly_salary_by_years,
    x = data["Department"],
    y = data["Annual Salary"],
    color_discrete_sequence=["#0083B8"] * len( annual_salary_by_years),
    orientation ="v",
    template="plotly_white"
)
st.plotly_chart(fig2,use_container_width=True)
st.markdown("---")

# scatter plot one
st.subheader(":star: scatter plot one : Monthly Salary vs. Years")
figure1 = px.scatter(data_frame= data ,
                    x = "Department" ,
                    y= "Monthly Salary",
                    orientation= "h",
                    color= filter_one,
                    size= filter_two
                   )
# scatter plot two
st.subheader(":star: Gender vs. Years")
figure2 = px.scatter(data_frame= data ,
                    x = "Years" ,
                    y= "Monthly Salary",
                    orientation= "h",
                    color= filter_one,
                    size= filter_two
)

b1 , b2 = st.columns(2)
b1.plotly_chart(figure1 , use_container_width= True)
b2.plotly_chart(figure2 , use_container_width= True)
st.markdown("---")

# pie chart 1
st.subheader(":star: pie chart 1 : Gender vs. Years of experience")
fig3 = px.pie(data_frame=data , names= "Gender" , values= "Years" ,color= filter_one , hole= 0.3 )

# pie chart 2
st.subheader(":star: pie chart 2 : Country vs. No of Employee in each country")
fig4 = px.pie(data_frame= data , names= "Country" , values="No" ,color= filter_one , hole= 0.4 )

#pie chart 3
st.subheader(":star: pie chart 3 : Center vs. No of Employee in each center")
fig5 = px.pie(data_frame= data , names= "Center" , values="No" ,color= filter_one , hole= 0.3 )

d1 , d2 , d3 = st.columns(3)
d1.plotly_chart(fig3 , use_container_width= True)
d2.plotly_chart(fig4 , use_container_width= True)
d3.plotly_chart(fig5 , use_container_width= True)
