import bs4
import requests


class KoreanPatientModel:

    def api(self):
        response = requests.get('http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?'
                                'serviceKey=fzXpNfK7ET%2BeoMdDcL%2FpjXUdnRVz2opP7AVswDFG7w3n2FKDY8%2BjoBEhaCL3oYEsxhXqBU2bymNrha1xyQtFMw%3D%3D&'
                                'pageNo=1&'
                                'numOfRows=10&'
                                'startCreateDt=20200901&'
                                'endCreateDt=20200901').text.encode('utf-8')
        xmlObj = bs4.BeautifulSoup(response, 'lxml-xml')

        return xmlObj


if __name__ == "__main__":
    kp = KoreanPatientModel()
    result = kp.api()
    print(result)
