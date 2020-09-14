import bs4
import requests
import pandas as pd
import datetime


class StatusOfOverseasOccurrenceModel:
    def api(self):
        now = datetime.datetime.now().strftime('%Y%m%d')
        response = requests.get('http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson?'
                                'serviceKey=H9LZk1JqZW5HU96FRw6WtzmxGOwUTa%2Fxn7NXmRLVUbAKwWLtQj18UKtYY'
                                '%2BHBtu2sT2qGkAXr8l%2Ff1IQbb%2BbQXQ%3D%3D& '
                                'pageNo=1&'
                                'numOfRows=10&'
                                'startCreateDt='+now+'&'
                                'endCreateDt='+now).text.encode('utf-8')
        xmlObj = bs4.BeautifulSoup(response, 'lxml-xml')

        return xmlObj

    def data_parsing(self, xmlObj):
        rows = xmlObj.findAll('item')
        rowList = []
        nameList = []
        columnList = []
        for i in range(len(rows)):
            columns = rows[i].find_all()
            for column in columns:
                if i == 0:
                    nameList.append(column.name)
                columnList.append(column.text)
            rowList.append(columnList)
            columnList = []
        result = []
        for item in pd.DataFrame(rowList, columns=nameList).to_dict('index').values():
            result.append(item)
        return result
