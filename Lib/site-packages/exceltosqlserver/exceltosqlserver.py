# -*- coding:utf-8 -*-
##############################################################
# Created Date: Monday, December 28th 2020
# Contact Info: luoxiangyong01@gmail.com
# Author/Copyright: Mr. Xiangyong Luo
##############################################################


import pandas as pd
import pyodbc
from sqlalchemy import create_engine
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Pandas to sql need to use sqlalcemy to create engine

class exceltoDBtable:
    #  Available for sql server and mysql now
    def __init__(self,filePath,hostORip=False,usrID =False,pwd=False,database=False,save2tableName=False):
        if not any([hostORip,database,usrID,pwd]):
            raise Exception("Partially inputs, please check your inputs...")
        else:
            self.filePath = filePath
            self.hostORip = hostORip
            self.database=database
            self.usrID = usrID
            self.pwd = pwd
            self.save2tableName = save2tableName
            
        self.dbType = ["sqlserver"]
        self.readData()
        self.connect2DB()
        
    def connect2DB(self) -> "Connect to Database Server":
        # This will test whether a sql server database or a mysql database
        sqlserverDriver=["{SQL Server}",
                         "{SQL Native Client}",
                         "{SQL Server Native Client 10.0}",
                         "{SQL Server Native Client 11.0}",
                         "{ODBC Driver 11 for SQL Server}",
                         "{ODBC Driver 13 for SQL Server}",
                         "{ODBC Driver 13.1 for SQL Server}",
                         "{ODBC Driver 17 for SQL Server}"]
        for i in sqlserverDriver:
            driveString = i.replace(" ","+").replace("{","").replace("}","")
            # print(driveString)
            
            
            try:
                self.engine = create_engine("mssql+pyodbc://%s:%s@%s/%s?driver=%s?"%(self.usrID,self.pwd,self.hostORip,self.database,driveString))
                print("Seccessfully connected to SQL Server...")
                
                if self.save2tableName:
                    tableName = self.save2tableName
                else:
                    if "/" in self.filePath:
                        tableName = self.filePath.split("/")[-1].split(".")[0]
                    else:
                        tableName = self.filePath.split(".")[0]
                
                self.file_data.to_sql(tableName,con=self.engine)
                print("Successfully saved %s into SQL Server..."%tableName)
                return None 
            except:
                self.engine = False
                continue
            
        raise Exception("Can not save table to sql server, please check your inputs.")
        
    def readData(self) -> "DataFrame":
        if self.filePath.split(".")[-1] in ["xlsx","xls"]:
            self.file_data = pd.read_excel(self.filePath)
            print("Successfully load excel data...")
        elif self.filePath.split(".")[-1] in ["csv"]:
            self.file_data = pd.read_csv(self.filePath)
            print("Successfully load csv data...")
        else:
            raise Exception("Unable to load input file...")


