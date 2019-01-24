import pandas as pd
import numpy as np
"""纽约的那个数据集合，16年7,8月的竟然也没有具体位置，所以只能够找16年4,5月份的"""
import datetime
def analysis_New_York_station_number():
    bike_df=pd.read_csv(r"H:\ExperimentData\NewYork\BSS\bike_station_data_797.csv",encoding="utf-8")
    """路径中不能出现中文"""
    print(bike_df[np.logical_and(np.logical_and(40.702<=bike_df["lat"],bike_df["lat"]<=40.800),
                                 np.logical_and(-74.017<=bike_df["lon"],bike_df["lon"]<=-73.928))])
    """纽约单车站点，得到487个单车站点"""
def analysis_Chicago_station_number():
    bike_df=pd.read_csv(r"H:\ExperimentData\Chicago\BSS\Divvy_Stations_2017_Q3Q4.csv",encoding="utf-8")
    """路径中不能出现中文"""
    print(bike_df[np.logical_and(np.logical_and(41.783<=bike_df["latitude"],bike_df["latitude"]<=41.968),
                                 np.logical_and(-87.721<=bike_df["longitude"],bike_df["longitude"]<=-87.603))])
"""纽约单车站点，得到487个单车站点"""

def analysis_Chicago_bike_trip_number():
    bike_df_4=pd.read_csv(r"H:\ExperimentData\Chicago\BSS\Divvy_Trips_2016_04.csv")
    bike_df_5 = pd.read_csv(r"H:\ExperimentData\Chicago\BSS\Divvy_Trips_2016_05.csv")
    station_df=pd.read_csv(r"H:\ExperimentData\Chicago\BSS\Divvy_Stations_2016_Q1Q2_in_downtown.csv")
    #bike_df['starttime']=pd.to_datetime(bike_df["starttime"])
    #bike_df["month"]=bike_df['starttime'].dt.month
    #bike_df=bike_df[np.logical_and(7<=bike_df["month"],bike_df["month"]<=8)]
    count=0
    for x in bike_df_4['from_station_id']:
        if x in list(station_df['id']):
           count+=1
    for x in bike_df_5['from_station_id']:
        if x in list(station_df['id']):
           count+=1
    print(count)
    """结果是937638"""
    return

def obtain_stations_in_downtown_in_Chicago():
    station_df=pd.read_csv(r"H:\ExperimentData\Chicago\BSS\Divvy_Stations_2016_Q1Q2.csv")
    station_df=station_df[np.logical_and(np.logical_and(41.783 <= station_df["latitude"], station_df["latitude"] <= 41.968),
                           np.logical_and(-87.721 <= station_df["longitude"], station_df["longitude"] <= -87.603))]
    station_df.to_csv(r"H:\ExperimentData\Chicago\BSS\Divvy_Stations_2016_Q1Q2_in_downtown.csv",index=False)
    """得到在downtown中的单车站点，Chicago"""

def analysis_New_York_bike_trip_number():
    bike_df_4=pd.read_csv(r"H:\ExperimentData\NewYork\BSS\201604-citibike-tripdata.csv")
    bike_df_5 = pd.read_csv(r"H:\ExperimentData\NewYork\BSS\201605-citibike-tripdata.csv")

    bike_df_4=bike_df_4[np.logical_and(np.logical_and(40.702 <= bike_df_4["start station latitude"], bike_df_4["start station latitude"] <= 40.800),
                           np.logical_and(-74.017 <= bike_df_4["start station longitude"], bike_df_4["start station longitude"] <= -73.928))]

    bike_df_5=bike_df_5[np.logical_and(np.logical_and(40.702 <= bike_df_5["start station latitude"], bike_df_5["start station latitude"] <= 40.800),
                           np.logical_and(-74.017 <= bike_df_5["start station longitude"], bike_df_5["start station longitude"] <= -73.928))]
    print(bike_df_4)
    print(bike_df_5)
    print(bike_df_5.shape[0]+bike_df_4.shape[0])
    """2081277"""

def analysis_New_York_taxi_trip_number():
    taxi_df=pd.read_csv(r"H:\ExperimentData\NewYork\Taxi\2016_Yellow_Taxi_Trip_Data.csv",usecols=['tpep_pickup_datetime','pickup_latitude','pickup_longitude'
                                                                                  ,'dropoff_latitude','dropoff_longitude'])
    taxi_df['datetime']=pd.to_datetime(taxi_df['tpep_pickup_datetime'])
    taxi_df['month']=taxi_df['datetime'].dt.month
    print(taxi_df.shape[0])
    taxi_df=taxi_df[np.logical_or(taxi_df['month']==4,taxi_df['month']==5)]
    print(taxi_df.shape[0])
    taxi_df=taxi_df[np.logical_and(np.logical_and(40.702<=taxi_df["pickup_latitude"],taxi_df["pickup_latitude"]<=40.800),
                                 np.logical_and(-74.017<=taxi_df["pickup_longitude"],taxi_df["pickup_longitude"]<=-73.928))]
    taxi_df=taxi_df[np.logical_and(np.logical_and(40.702<=taxi_df["dropoff_latitude"],taxi_df["dropoff_latitude"]<=40.800),
                                 np.logical_and(-74.017<=taxi_df["dropoff_longitude"],taxi_df["dropoff_longitude"]<=-73.928))]

    print(taxi_df.shape[0])
    #print(taxi_df)
    
def analysis_Chicago_taxi_trip_number():
    taxi_df=pd.read_csv(r"H:\ExperimentData\Chicago\Taxi\Taxi_Trips.csv",usecols=['Pickup Centroid Latitude','Pickup Centroid Longitude'
                                                                                  ,'Dropoff Centroid Latitude','Dropoff Centroid Longitude'])
    taxi_df=taxi_df[np.logical_and(np.logical_and(41.783<=taxi_df["Pickup Centroid Latitude"],taxi_df["Pickup Centroid Latitude"]<=41.968),
                                 np.logical_and(-87.721<=taxi_df["Pickup Centroid Longitude"],taxi_df["Pickup Centroid Longitude"]<=-87.603))]
    taxi_df=taxi_df[np.logical_and(np.logical_and(41.783<=taxi_df["Dropoff Centroid Latitude"],taxi_df["Dropoff Centroid Latitude"]<=41.968),
                                 np.logical_and(-87.721<=taxi_df["Dropoff Centroid Longitude"],taxi_df["Dropoff Centroid Longitude"]<=-87.603))]
    print(taxi_df.shape[0])
    """2548089"""
analysis_New_York_taxi_trip_number()