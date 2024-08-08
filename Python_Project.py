#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Main Menu
while (True):
    print("Type the corresponding numbers to view details")
    print("1. Fetch Data")
    print("2. Dataframe Statistics")
    print("3. Data Analytics")
    print("4. Working on Records")
    print("5. Working on Columns")
    print("6. Data Visualization")  
    print("7. Exit")
    print("-----------------------")
    print()
    result=pd.read_csv("D:\\12_result_management.csv",index_col=0)
    ch=int(input("Enter your choice: "))
    if ch==1:
        result=pd.read_csv("D:\\12_result_management.csv",index_col=0)
        print(result)
        print()
    elif ch==2:
        while (True):
            print("Dataframe Statistics Menu")
            print("1. Display the Transpose")
            print("2. Display all column names")
            print("3. Display the indexes")
            print("4. Display the shape")
            print("5. Display the dimension")
            print("6. Display the data types of all columns")
            print("7. Display the size")
            print("8. Exit")
            print("-----------------------")
            print()
            ch2=int(input("Enter your choice: "))
            if ch2==1:
                print(result.T)
                print()
            elif ch2==2:
                print(result.columns)
                print()
            elif ch2==3:
                print(result.index)
                print()
            elif ch2==4:
                print(result.shape)
                print()
            elif ch2==5:
                print(result.ndim)
                print()
            elif ch2==6:
                print(result.dtypes)
                print()
            elif ch2==7:
                print(result.size)
                print()
            else:
                print("EXIT")
                break
    elif ch==3:
        while (True):
            print("Data Analytics Menu")
            print("1. Specific number of records from the top")
            print("2. Specific number of records from the bottom")
            print("3. Details of a specific Subject")
            print("4. Search details of a specific as per a specific column heading")
            print("5. Subject with maximum highest marks") 
            print("6. Subject with minimum highest marks")
            print("7. Subject with maximum percentage of A1 and A2") 
            print("8. Subject with minimum percentage of A1 and A2") 
            print("9. Exit")
            print("-----------------------")
            ch3=int(input("Enter your choice: "))
            if ch3==1:
                n=int(input("Enter how many records you want to display from the top: "))
                print(result.head(n))
                print()
            elif ch3==2:
                n=int(input("Enter how many records you want to display from the bottom: "))
                print(result.tail(n))
                print()
            elif ch3==3:
                st=input("Enter the subject name for which you want to see the details: ")
                print(result.loc[st])
                print()
            elif ch3==4:
                col=input("Enter column/heading name whose details you want to see: ")
                print(result[col])
                print()
            elif ch3==5:
                m=result['Highest'].max()
                s=result.loc[result.Highest==m]
                print("Subject with maximum highest marks of ",m," is\n",s.index)
                print()
            elif ch3==6:
                m=result['Highest'].min()
                s=result.loc[result.Highest==m]
                print("Subject with minimum highest marks of ",m," is\n",s.index)
                print()
            elif ch3==7:
                m=result['percentage'].max()
                s=result.loc[result.percentage==m]
                print("Subject with maximum percentage of A1 and A2 ",s.index,"\n Percentage being",m)
                print()
            elif ch3==8:
                m=result['percentage'].min()
                s=result.loc[result.percentage==m]
                print("Subject with minimum percentage of A1 and A2 ",s.index,"\n Percentage being",m)
                print()
            else:
                print("EXIT")
                break
    elif ch==4:
        while (True):
            print('Working on records menu')
            print('1.Insert a specific subject detail')
            print('2.Delete a specific subject detail')
            print('3.Update a specific subject detail')
            print("4.Exit")
            print("-----------------------")
            print()
            ch4=int(input('Enter your choice: '))
            if ch4==1:
                a=input('Enter subject name: ')
                b=int(input("Enter number of students appeared: "))
                c=int(input("Enter highest marks obtained: "))
                d=int(input("Enter number of students getting A1's: "))
                e=int(input("Enter number of students getting A2's: "))
                f=((d+e)/b)*100
                g=int(input("Enter number of students getting B's: "))
                h=int(input("Enter number of students getting students getting C's: "))
                i=int(input("Enter number of students getting D's: "))
                total=d+e+g+h+i
                if (b==total):
                    result.loc[a]=[b,c,d,e,f,g,h,i]
                    print('Data successfully Inserted.')
                    print(result)
                    print()
                else:
                    print("Number of students appeared do not match the rest of the information provided.")
                    print("Try again.")
            elif ch4==2:
                a=input('Enter subject name whose data needs to be deleted: ')
                result.drop([a], inplace=True)
                print('Data successfully Deleted.')
                print(result)
                print()
            elif ch4==3:
                a=input('Enter subject name whose data needs to be updated: ')
                b=int(input("Enter number of students appeared: "))
                c=int(input("Enter highest marks obtained: "))
                d=int(input("Enter number of students getting A1's: "))
                e=int(input("Enter number of students getting A2's: "))
                f=((d+e)/b)*100
                g=int(input("Enter number of students getting B's: "))
                h=int(input("Enter number of students getting C's: "))
                i=int(input("Enter number of students getting D's: "))
                total=d+e+g+h+i
                if(b==total):
                    result.loc[a]=[b,c,d,e,f,g,h,i]
                    print('Data successfully Updated.')
                    print(result)
                    print()
                else:
                    print("Number of students appeared do not match with the rest of the information provided.")
                    print("Try again.")
            else:
                print("EXIT")
                break
    elif ch==5:
        while (True):
            print("Working on Columns Menu")
            print("1. Insert a new column data")
            print("2. Delete a specific column")
            print("3. Exit")
            print("-----------------------")
            print()
            ch5=int(input('Enter your choice: '))
            if ch5==1:
                print('Enter details: ')
                h=input('Enter column/heading name: ')
                det=eval(input("Enter details corresponding to all subject (enclosed in [ ]): "))
                result[h]=pd.Series(data=det,index=result.index)
                print("Column inserted.")
                print(result)
                print()
            elif ch5==2:
                a=input("Enter column name which needs to be deleted: ")
                result.drop([a],axis=1,inplace=True)
                print("Column Temporary deleted.")
                print("The new dataframe:")
                print(result)
                print()
            else:
                print("EXIT")
                break
    elif ch==6:
        while (True):
            print("Data Visualization Menu")
            print("1. Line Plot")
            print("2. Bar Plot")
            print("3. Histogram")
            print("4. Exit")
            print("-----------------------")
            ch6=int(input("Enter choice: ")) 
            if ch6==1:
                while (True):
                    print("Line Plot Subject Menu")
                    print("1. Subject wise Highest marks")
                    print("2. Subject wise number of students appeared") 
                    print("3. Subject wise comparison of percentage of A1 & A2") 
                    print("4. Exit")
                    print()
                    chline=int(input("Enter choice: "))
                    if chline==1:
                        plt.plot(result.index,result['Highest'],label="Highest Marks",color="orange",marker="D",markeredgecolor="blue")
                        plt.title("SUBJECTWISE HIGHEST MARKS")
                        plt.xlabel("SUBJECT")
                        plt.ylabel("HIGHEST MARKS")
                        plt.xticks(rotation=40)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chline==2:
                        plt.plot(result.index,result['Appeared'],label="Number of students appeared",color='yellow',marker="D",markeredgecolor="blue")
                        plt.title("SUBJECTWISE NUMBER OF STUDENTS APPEARED")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("NUMBER OF STUDENTS")
                        plt.xticks(rotation=40)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chline==3:
                        plt.plot(result.index,result['percentage'],label="Percentage of A1 and A2",color='orange',marker="D",markeredgecolor="blue")
                        plt.title("SUBJECTWISE PERCENTAGE OF A1 AND A2")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("PERCENTAGE OF A1 AND A2")
                        plt.xticks(rotation=40)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    else:
                        print("EXIT")
                        break
            elif ch6==2:
                while (True):
                    print("Bar Plot Subject Menu")
                    print("1. Subject wise Highest marks") 
                    print("2. Subject wise number of students appeared")
                    print("3. Subject wise comparison of percentage of A1 & A2")
                    print("4. Subject wise number of students who got grade D")
                    print("5. Exit")
                    print()
                    chbar=int(input("Enter choice: "))
                    if chbar==1:
                        plt.bar(result.index,result['Highest'],label="Highest Marks",color="orange")
                        plt.title("SUBJECTWISE HIGHEST MARKS")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("HIGHEST MARKS")
                        plt.xticks(rotation=40)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chbar==2:
                        plt.bar(result.index,result['Appeared'],label="Number of students appeared in each subject",color="yellow")
                        plt.title("SUBJECTWISE NUMBER OF STUDENTS APPEARED")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("NUMBER OF STUDENTS")
                        plt.xticks(rotation=40)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chbar==3:
                        plt.bar(result.index,result['percentage'],label="Percantage of A1 and A2",color="orange")
                        plt.title("SUBJECTWISE PERCENTAGE OF A1 AND A2")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("PERCENTAGE OF A1 AND A2")
                        plt.xticks(rotation=40)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    elif chbar==4:
                        plt.bar(result.index,result['D'],label="Number of Students who got D",color="red")
                        plt.title("NUMBER OF STUDENTS WHO GOT GRADE D IN EACH SUBJECT")
                        plt.xlabel("SUBJECTS")
                        plt.ylabel("NUMBER OF STUDENTS WHO GOT GRADE D")
                        plt.xticks(rotation=40)
                        plt.legend()
                        plt.grid(True)
                        plt.show()
                    else:
                        print("EXIT")
                        break
            elif ch6==3:
                while (True):
                    print("Histogram Subject Menu [Showing 5 bins]")
                    print("1. Highest marks")
                    print("2. Percentage of A1 & A2") 
                    print("3. Grade D")
                    print("4. Exit")
                    print()
                    chbar=int(input("Enter your choice: "))
                    if chbar==1:
                        plt.hist(result['Highest'],bins=5,label="Highest Marks", color='orange',edgecolor="black")
                        plt.title("COUNT OF SUBJECTS FOR DIFFERENT RANGE OF HIGHEST MARKS")
                        plt.xlabel("HIGHEST MARKS")
                        plt.ylabel("FREQUENCY")
                        plt.legend()
                        plt.show()
                    elif chbar==2:
                        plt.hist(result["percentage"],bins=5,label="Percentage of A1 and A2",color="green",edgecolor="black")
                        plt.title("COUNT OF SUBJECTS FOR DIFFERENT RANGE OF PERCENTAGE OF A1 AND A2")
                        plt.xlabel("PERCENTAGE OF A1 AND A2")
                        plt.ylabel("FREQUENCY")
                        plt.legend()
                        plt.show()
                    elif chbar==3:
                        plt.hist(result["D"],bins=5,label="Grade D",color="red",edgecolor="black")
                        plt.title("COUNT OF SUBJECTS FOR DIFFERENT RANGE OF PERCENTAGE OF A1 AND A2")
                        plt.xlabel("GRADE D")
                        plt.ylabel("FREQUENCY")
                        plt.legend()
                        plt.show()
                    else:
                        print("EXIT")
                        break
            else:
                print("EXIT")
                break
    else:
        print("EXIT")
        break


# In[ ]:





# In[ ]:




