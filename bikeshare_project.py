#!/usr/bin/env python
# coding: utf-8

# In[6]:


import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        
        city = input('Which city do would you like to explore: chicago, new york city or washington?: ').lower()
        
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('You did select the wrong city! Please select chicago, new york city or washington')
            continue
    
    while True:
        month = input('Select the month from january to june: ').lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            
            break
        else:
            print('You did select the wrong month! Please write again')
            continue
    
    while True:
        day = input('Select the week day : ').lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else:
            print('You did select the wrong week day! Write again: ')
            continue


    print('-'*40)
    
    return city, month, day     

def load_data(city, month, day):
    
    df=pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
       
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
   
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print('The most common month is: {}'.format(months[month-1]))

   
    day = df['day_of_week'].mode()[0]
    print(f'The most common day of week is: {day}')


    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'The most common start hour is: {popular_hour}')

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    pop_start_station= df['Start Station'].mode()[0]
    print("The most commonly used Start Station is {}".format(pop_start_station))


    pop_end_station= df['End Station'].mode()[0]
    print("The most commonly used End Station is {}".format(pop_end_station))

    df['combination']=df['Start Station']+" "+"to"+" "+ df['End Station']
    pop_com= df['combination'].mode()[0]
    print("The most frequent combination of Start and End Station is {} ".format(pop_com))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()  
   
    total_duration=df['Trip Duration'].sum()
    minute,second=divmod(total_duration,60)
    hour,minute=divmod(minute,60)
    print("The total trip duration: {} hour(s) {} minute(s) {} second(s)".format(hour,minute,second))
    
    average_duration=round(df['Trip Duration'].mean())
    m,sec=divmod(average_duration,60)
    if m>60:
        h,m=divmod(m,60)
        print("The total trip duration: {} hour(s) {} minute(s) {} second(s)".format(h,m,sec))
    else:
        print("The total trip duration: {} minute(s) {} second(s)".format(m,sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_counts= df['User Type'].value_counts()
    print("The user types are:\n",user_counts)

    if city.title() == 'Chicago' or city.title() == 'New York City':
        gender_counts= df['Gender'].value_counts()
        print("\nThe counts of each gender are:\n",gender_counts)
    
        earliest= int(df['Birth Year'].min())
        print("\nThe oldest user is born of the year",earliest)
        most_recent= int(df['Birth Year'].max())
        print("The youngest user is born of the year",most_recent)
        common= int(df['Birth Year'].mode()[0])
        print("Most users are born of the year",common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
                
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
    



            
            


# In[ ]:




