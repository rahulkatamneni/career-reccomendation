import scrapy
#import pypyodbc
import logging
from scrapy.selector import Selector
from pymongo import MongoClient


mongoClient = MongoClient('mongodb://127.0.0.1:27017/')
mongoDb = mongoClient.blsData
highestPayingURLs = mongoDb.highestPayingURLs
fastestGrowingJobURLs = mongoDb.fastestGrowingJobURLs
mostNewJobsURLs = mongoDb.mostNewJobsURLs

url = []
items = []

habitation_arr = []
noOfPensionReleased_arr = []
noOfPensionDisbursed_arr = []
perOfDisbursed_arr = []
amtReleased_arr = []
perOfDisbursement_arr = []

class BlogSpider(scrapy.Spider):

    # cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0}; "
    #                         "uid=sa; pwd=Info(runch; "
    #                         "Server=45.114.246.206; PORT=1433; "
    #                         "Database=chitrt; "
    #                         "Trusted_Connection=No;")
    # cursor = cnxn.cursor()
    #
    # cursor.execute("SELECT NEXT VALUE FOR Sequence_for_BatchId AS BatchId")
    # BatchId = cursor.fetchone()[0]
    #
    #
    # cursor.execute("select DISTINCT Habitation_Id, Panchayat_Id, Mandal_Id from [chitrt].[dbo].[RegionMaster] where Mandal_Id != 0")
    # data = cursor.fetchall()
    # #print(data)
    # #cursor.close()
    # for datas in data:
    #
    #     Habitation_Id = datas[0]
    #     Panchayat_Id = datas[1]
    #     Mandal_Id = datas[2]
    #
    #     firstUrl = "http://ntrbharosa.ap.gov.in/NBP/CoreHabitationDashBoardCM.do?mode=getAllDetails&distcode=10"
    #     midUrl = "&mndcode="+str(Mandal_Id)+"&pancode="+str(Panchayat_Id)
    #     lastUrl ="&fromday=null&today=null&montval="+disbursementMonth+"&yearval="+disbursementYear
    #
    #     mainUrl = firstUrl+midUrl+lastUrl
    #     url.append(mainUrl)
    #     #print(url)
    #     #print(len(url))


    name = 'stack'


    #urls =['https://www.bls.gov/ooh/highest-paying.htm']
    urls =['https://www.bls.gov/ooh/most-new-jobs.htm']
    start_urls = urls

    def parse(self, response):
        sel = Selector(response)
        tables = sel.xpath('//*[@id="landing-page-table"]/tbody/tr/td/h4/a')
        for data in tables:
            url = data.xpath('@href').extract()[0]
            profession = data.xpath('text()').extract()[0]
            mostNewJobsURLs.insert({'profession':profession, 'url' : url})

