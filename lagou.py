import requests
import json
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
mydb = client['mydb']
lagou = mydb['lagou']

headers = {'Cookie':'xxxxxxxxxxxxxxxxx','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36','Referer':'https://www.lagou.com/jobs/list_pyhton?labelWords=&fromSearch=true&suginput='}

def get_page(url,params):
    html = requests.post(url,data=params,headers=headers)
    json_data = json.loads(html.text)

    print(json_data)

    total_Count = int(json_data['content']['positionResult']['totalCount'])
    page_number = total_Count/15 if total_Count/15 < 30 else 30
    get_info(url,page_number)

def get_info(url,page):
    for pn in range(1,page+1):
        params = {'first':'true','pn':str(pn),'kd':'python'}
        try:
            html = requests.post(url,data=params,headers=headers)
            json_data = json.loads(html.text)
            results = json_data['content']['positionResult']['result']
            for result in results:
                infos = {'businessZones':result['businessZones'],'city':result['city'],'companyFullName':result['companyFullName'],'companyLabelList':result['companyLabelList'],'companySize':result['companySize'],'district':result['district'],'education':result['education'],'explain':result['explain'],'financeStage':result['financeStage'],'firstType':result['firstType'],'formatCreateTime':result['formatCreateTime'],'gradeDescription':result['gradeDescription'],'imState':result['imState'],'industryField':result['industryField'],'jobNature':result['jobNature'],'positionAdvantage':result['positionAdvantage'],'salary':result['salary'],'secondType':result['secondType'],'workYear':result['workYear']}
                lagou.insert_one(infos)
                time.sleep(5)
        except requests.exceptions.ConnectionError:
            pass

if __name__ == '__main__':
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    params = {'first':'true','pn':'1','kd':'python'}
    get_page(url,params)
