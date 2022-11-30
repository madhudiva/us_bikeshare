#!/usr/bin/env python
# coding: utf-8

# # Bike Share Project Data

# ## The main stats needed to be calculated are as follows:
# 
# #1 Popular times of travel (i.e., occurs most often in the start time)
# most common month 
# most common day of week
# most common hour of day
# 
# #2 Popular stations and trip
# most common start station
# most common end station
# most common trip from start to end (i.e., most frequent combination of start station and end station)
# 
# #3 Trip duration
# total travel time
# average travel time
# 
# #4 User info
# counts of each user type
# counts of each gender (only available for NYC and Chicago)
# earliest, most recent, most common year of birth (only available for NYC and Chicago)


# # Examining each of the data sets for chicago, new york and washington

# Basically visualising the data and using functions like .head(), .describe(), .isnull() 

# In[32]:


import numpy as np
import pandas as pd
import time 


# In[33]:


# df_chicago = pd.read_csv('chicago.csv')
# df_new_york_city = pd.read_csv('new_york_city.csv')
# df_washington = pd.read_csv('washington.csv')


# In[34]:


# df_chicago.head()


# In[35]:


# df_new_york_city.head()


# In[36]:


# df_washington.head()


# In[37]:


# # column information for the datasets
# df_chicago.info()


# In[38]:


# df_new_york_city.info()


# In[39]:


# # doesn't have gender and birth year - washington dataset
# df_washington.info()


# In[40]:


# Quick stats for the data
#df_chicago.describe()


# In[41]:


#df_new_york_city.describe()


# In[42]:


# df_washington.describe()


# In[43]:


# # check for null values - gender and birth year have a couple of missing values in the chicago dataset 
# df_chicago.isnull().sum().sort_values(ascending=False)


# In[44]:


# #  gender, birth year and user_type have nulls in the new york city dataset
# df_new_york_city.isnull().sum().sort_values(ascending=False)


# In[45]:


# #  no nulls in the washington dataset
# df_washington.isnull().sum().sort_values(ascending=False)


# In[46]:


# # Initilaise dictionaries for cities data and lists for the month and days data
# CITIES= { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv' }

# MONTHS  = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

# DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']


# In[47]:


# # checking for user input to match from the above dict
# city_names = ''
# while city_names.lower() not in CITIES:
#     city_names = input("\nPlease enter the what name of the city that would you like to see - chicago, new york, washington?\n")
#     if city_names.lower() in CITIES:
#         city = CITIES[city_names.lower()]
#     else:
#         print("Oops you've entered the wrong city name! Please try again!!!\n")
# city = CITIES[city_names.lower()]


# In[48]:


# # reading the df 
# df = pd.read_csv(city)


# In[49]:


#df.head()


# In[50]:


# df['Start Time'] = pd.to_datetime(df['Start Time'])

# # extract month and day of week from Start Time to create new columns
# df['month'] = df['Start Time'].dt.month
# df['week_day'] = df['Start Time'].dt.day_name()
# df['hour'] = df['Start Time'].dt.hour


# In[51]:


# # we can see that the month, weekday and time are extracted seperately. This is done for checking an example for the chicago dataset
# df.head()


# In[52]:


# # getting the most frequent occuring months, week days and hours from the above df
# freq_month = df['month'].mode()[0]
# print(freq_month)
# freq_week_day = df['week_day'].mode()[0]
# print(freq_week_day)
# freq_start_hour = df['hour'].mode()[0]
# print(freq_start_hour)


# In[53]:


# # getting the information regarding the most commonly occuring start station, end station and combo of the same
# freq_start_station = df['Start Station'].mode()[0]
# print(freq_start_station)
# freq_end_station = df['End Station'].mode()[0]
# print(freq_end_station)
# freq_combo_start_stop = df['Start Station'] + ' to ' + df['End Station']
# print(freq_combo_start_stop)


# In[54]:


# gettign the information for the total travel time and the trip duration in seconds and hours
# start_time = time.time()

# total_travel_time = df['Trip Duration'].sum()
# print(total_travel_time)
# #print(total_travel_time/3600)

# mean_travel_time = df['Trip Duration'].mean()
# print(mean_travel_time)
# #print(mean_travel_time/3600)


# In[55]:


# Splitting up the functions and executing them seperately 


# In[56]:


# def get_filters():
#     """
#     Asks user to specify a city, month, and day to analyze.
#     Returns:
#         (str) city - name of the city to analyze
#         (str) month - name of the month to filter by, or "all" to apply no month filter
#         (str) day - name of the day of week to filter by, or "all" to apply no day filter
#     """
#     print('Hello! Let\'s explore some US bikeshare data!')
    
#     # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#     # get the user input for the cities data and also check for invalid inputs and reponse using loops.
#     city_names = ''
#     while city_names.lower() not in CITIES:
#         city_names = input("\nPlease enter the what name of the city that would you like to see - chicago, new york, washington?\n")
#         if city_names.lower() in CITIES:
#             city = CITIES[city_names.lower()]
#         else:
#             print("Oops you've entered the wrong city name! Please try again!!!\n")

#     # get user input for month (all, january, february, ... , june) and check for invalid inputs the same case as above
#     month_names = ''
#     while month_names.lower() not in MONTHS :
#         month_names = input("\nWhat name of the month do you wish to see the data for (january, february, march, april, may, june or all)? \n")
#         if month_names.lower() in MONTHS :
#             #We were able to get the name of the month to analyze data.
#             month = month_names.lower()
#         else:
#             #We were not able to get the name of the month to analyze data so we continue the loop.
#             print("Oops you have an invalid month entry! Please try again!! \n")

#     # get user input for day of week (all, monday, tuesday, ... sunday) ) and check for invalid inputs the same case as done for both
#     day_names = ''
#     while day_names.lower() not in DAYS:
#         day_names = input("\nWhat name of the day do you want to see the data for(sunday, monday, tuesday, wednesday, thursday, friday, saturday or all?\n")
#         if day_names.lower() in DAYS:
#             #We were able to get the name of the month to analyze data.
#             day = day_names.lower()
#         else:
#             #We were not able to get the name of the month to analyze data so we continue the loop.
#             print("Oops you have entered a wrong name for the day! Please try again!! \n")

#     print('-'*40)
#     return city, month, day


# In[57]:


# def load_data(city, month, day):
#     """
#     Loads data for the specified city and filters by month and day if applicable.
#     Args:
#         (str) city - name of the city to analyze
#         (str) month - name of the month to filter by, or "all" to apply no month filter
#         (str) day - name of the day of week to filter by, or "all" to apply no day filter
#     Returns:
#         df - Pandas DataFrame containing city data filtered by month and day
#     """
#     # load data into a df dataframe 
#     df = pd.read_csv(city)

#     # get the start time column from the dataset and convert it to a date timestamp for extracting the day and the month for new columns
#     df['Start Time'] = pd.to_datetime(df['Start Time'])

#     # extract month and days of the week from Start Time columns and store them as new columns in the dataframe
#     df['month'] = df['Start Time'].dt.month
#     df['week_day'] = df['Start Time'].dt.day_name()
#     df['hour'] = df['Start Time'].dt.hour


#     # Apply the month filter; use the index values to derive integers values
#     if month != 'all':
#         month = MONTHS.index(month)

#         # create new df and filter using month
#         df = df.loc[df['month'] == month]

#   # Apply the day filter;
#     if day != 'all':
#                 # create new df and filter using day of the week same way as done above for the month
#         df = df.loc[df['week_day'] == day.title()]

#     return df


# In[58]:


# def time_stats(df):
#     """Displays statistics on the most frequent times of travel.
#     Args:
#         (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
#     """

#     print('\nCalculating The Most Frequent Times of Travel...\n')
#     start_time = time.time()

#     # TO DO: display the most common month
#     freq_month = df['month'].mode()[0]
#     print("The most frequently occuring month is: " + MONTHS [freq_month].title())

#     # TO DO: display the most common day of week
#     freq_week_day = df['week_day'].mode()[0]
#     print("The most frequenlty occuring day is: " + freq_week_day)

#     # TO DO: display the most common start hour
#     freq_start_hour = df['hour'].mode()[0]
#     print("The most frequently occuring hour is : " + str(freq_start_hour))

#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


# In[59]:


# def station_stats(df):
#     """Displays statistics on the most popular stations and trip.
#     Args:
#         (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
#     """

#     print('\nCalculating The Most Popular Stations and Trip...\n')
#     start_time = time.time()

#      # TO DO: display most commonly used start station
#     freq_start_station = df['Start Station'].mode()[0]
#     print('The most frequently occuring start station is: ' + freq_start_station)

#     # TO DO: display most commonly used end station
#     freq_end_station = df['End Station'].mode()[0]
#     print('The most frequently occuring end station is: ' + freq_end_station)
    
#     # TO DO: display most frequent combination of start station and end station trip
#     freq_combo_start_stop = df['Start Station'] + ' to ' + df['End Station']
#     print('The most frequently start and end station trips are : ' +  freq_combo_start_stop.mode()[0])
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


# In[60]:


# def trip_duration_stats(df):
#     """Displays statistics on the total and average trip duration.
#     Args:
#         (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
#     """

#     print('\nCalculating Trip Duration...\n')
#     start_time = time.time()

#    # display the total travel time in seconds and hours 
#     total_travel_time = df['Trip Duration'].sum()
#     print('Total Travel Time : ', total_travel_time, 'seconds, or' , total_travel_time/3600, ' hours')
    
#     # display mean travel time in seconds and hours
#     mean_travel_time = df['Trip Duration'].mean()
#     print('Mean Travel time:' , mean_travel_time, 'seconds, or' , mean_travel_time/3600, ' hours' )


#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


# In[61]:


# def user_stats(df, city):
#     """Displays statistics on bikeshare users.
#     Args:
#         (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
#     """

#     print('\nCalculating User Stats...\n')
#     start_time = time.time()

#     # Display counts of user types
#     user_type_count = df['User Type'].value_counts()
#     print('The counts for the number of users are: \n', user_type_count)

#     # Display counts of gender
#     if 'Gender' in df:
#         gender_count = df['Gender'].value_counts()
#         print('The counts for the number of genders are: \n', gender_count)

#     # Display earliest, most recent, and most common year of birth
#     if 'Birth Year' in df:
#         earliest_birth_year = df['Birth Year'].min()
#         print('The earliest birth year is: \n', earliest_birth_year)
        
#         recent_birth_year = df['Birth Year'].max()
#         print('The most recent birth year is: \n', recent_birth_year)
        
#         freq_birth_year = df['Birth Year'].mode()[0]
#         print('The most frequently occuring birth year is: \n', freq_birth_year)

#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


# In[62]:


# def main():
#     while True:
#         city, month, day = get_filters()
#         df = load_data(city, month, day)

#         time_stats(df)
#         station_stats(df)
#         trip_duration_stats(df)
#         user_stats(df, city)
#         restart = input('\nWould you like to restart? Enter yes or no.\n')
#         if restart.lower() != 'yes':
#             break


# if __name__ == "__main__":
#     main()


# In[26]:


# Running the whole code and combinbing them as one code block and also it includes if the user needs to display the next 5 rows of the data simultaneously or not


# In[27]:


CITIES= { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv' }

MONTHS  = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # get the user input for the cities data and also check for invalid inputs and reponse using loops.
    city_names = ''
    while city_names.lower() not in CITIES:
        city_names = input("\nPlease enter the what name of the city that would you like to see - chicago, new york city, washington?\n")
        if city_names.lower() in CITIES:
            city = CITIES[city_names.lower()]
        else:
            print("Oops you've entered the wrong city name! Please try again!!!\n")

    # get user input for month (all, january, february, ... , june) and check for invalid inputs the same case as above
    month_names = ''
    while month_names.lower() not in MONTHS :
        month_names = input("\nWhat name of the month do you wish to see the data for (january, february, march, april, may, june or all)? \n")
        if month_names.lower() in MONTHS :
            #We were able to get the name of the month to analyze data.
            month = month_names.lower()
        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Oops you have an invalid month entry! Please try again!! \n")

    # get user input for day of week (all, monday, tuesday, ... sunday) ) and check for invalid inputs the same case as done for both
    day_names = ''
    while day_names.lower() not in DAYS:
        day_names = input("\nWhat name of the day do you want to see the data for(sunday, monday, tuesday, wednesday, thursday, friday, saturday or all?\n")
        if day_names.lower() in DAYS:
            #We were able to get the name of the month to analyze data.
            day = day_names.lower()
        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Oops you have entered a wrong name for the day! Please try again!! \n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data into a df dataframe 
    df = pd.read_csv(city)

    # get the start time column from the dataset and convert it to a date timestamp for extracting the day and the month for new columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and days of the week from Start Time columns and store them as new columns in the dataframe
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour


    # Apply the month filter; use the index values to derive integers values
    if month != 'all':
        month = MONTHS .index(month)

        # create new df and filter using month
        df = df.loc[df['month'] == month]

  # Apply the day filter;
    if day != 'all':
                # create new df and filter using day of the week same way as done above for the month
        df = df.loc[df['week_day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    freq_month = df['month'].mode()[0]
    print("The most frequently occuring month is: " + MONTHS [freq_month].title())

    # TO DO: display the most common day of week
    freq_week_day = df['week_day'].mode()[0]
    print("The most frequenlty occuring day is: " + freq_week_day)

    # TO DO: display the most common start hour
    freq_start_hour = df['hour'].mode()[0]
    print("The most frequently occuring hour is : " + str(freq_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

     # TO DO: display most commonly used start station
    freq_start_station = df['Start Station'].mode()[0]
    print('The most frequently occuring start station is: ' + freq_start_station)

    # TO DO: display most commonly used end station
    freq_end_station = df['End Station'].mode()[0]
    print('The most frequently occuring end station is: ' + freq_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    freq_combo_start_stop = df['Start Station'] + ' to ' + df['End Station']
    print('The most frequently start and end station trips are : ' +  freq_combo_start_stop.mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   # display the total travel time in seconds and hours 
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time : ', total_travel_time, 'seconds, or' , total_travel_time/3600, ' hours')
    
    # display mean travel time in seconds and hours
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel time:' , mean_travel_time, 'seconds, or' , mean_travel_time/3600, ' hours' )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('The counts for the number of users are: \n', user_type_count)

    # Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('The counts for the number of genders are: \n', gender_count)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest birth year is: \n', earliest_birth_year)
        
        recent_birth_year = df['Birth Year'].max()
        print('The most recent birth year is: \n', recent_birth_year)
        
        freq_birth_year = df['Birth Year'].mode()[0]
        print('The most frequently occuring birth year is: \n', freq_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # displays the raw data upon user request (5 rows)
def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nDo you want to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nDo you want to view the first five rows of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


# In[4]:





# In[ ]:




