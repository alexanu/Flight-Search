import json
import requests
import method_temp


class Method():
    def getDict(__name__):
        headers = {
            'Accept':
            '*/*',
            'Accept-encoding':
            'gzip, deflate, br',
            'Accept-language':
            'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection':
            'keep-alive',
            'Content-length':
            '290',
            'Content-type':
            'application/json',
            'Cookie':
            r'_abtest_userid=aa51aa25-2900-4b5f-b8b0-e8ab6de1d4fc; _bfa=1.1575209493112.1801er.1.1575621253145.1575648985735.10.33; _RF1=113.4.53.44; _RSG=mu40V0ntd83qTvwvYxJZq9; _RDG=285d676ac5ebc524150d5faf0fa00c5953; _RGUID=3227df10-1f00-4e30-9d23-4fb8b9eb9774; Union=AllianceID=1095794&SID=2280904&OUID=; Session=SmartLinkCode=U2280904&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _jzqco=%7C%7C%7C%7C1575650181832%7C1.532513354.1575209496384.1575648989004.1575650179591.1575648989004.1575650179591.undefined.0.0.29.29; __zpspc=9.11.1575648989.1575650179.2%231%7Cbaiduppc%7Cbaidu%7Cty%7C%25E6%259C%25BA%25E7%25A5%25A8api%7C%23; MKT_Pagesource=PC; DomesticUserHostCity=HRB|%b9%fe%b6%fb%b1%f5; appFloatCnt=6; FD_SearchHistorty={"type":"S","data":"S%24%u54C8%u5C14%u6EE8%28%u592A%u5E73%u56FD%u9645%u673A%u573A%29%28HRB%29%24HRB%242020-01-11%24%u53A6%u95E8%28XMN%29%24XMN"}; StartCity_Pkg=PkgStartCity=5; _bfi=p1%3D600001375%26p2%3D10320673302%26v1%3D32%26v2%3D31; MKT_CKID=1575622305172.62cqm.mf3u; _bfs=1.4',
            'DNT':
            '1',
            'Host':
            'flights.ctrip.com',
            'Origin':
            'https://flights.ctrip.com',
            'Referer':
            'https://flights.ctrip.com/itinerary/oneway/hrb-xmn?date=2020-01-12',
            'TE':
            'Trailers',
            'User-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
        }

        data = {
            "airportParams": [{
                "acity": "XMN",
                "acityid": 25,
                "acityname": "厦门",
                "date": "2020-01-12",
                "dcity": "HRB",
                "dcityid": 5,
                "dcityname": "哈尔滨"
            }],
            "classType":
            "ALL",
            "date":
            "2020-01-12",
            "flightWay":
            "Oneway",
            "hasBaby":
            'false',
            "hasChild":
            'false',
            "searchIndex":
            1,
            "token":
            "e048188e0dc27a8c2dfc1b0c25536782"
        }

        url = 'https://flights.ctrip.com/itinerary/api/12808/products'

        response = requests.post(url=url, headers=headers, json=data)
        # print(response.text)

        dict_str = json.loads(response.text)
        return dict_str

    # 得到列表
    def get_routeList(__name__, dict_str):
        data = dict_str.setdefault("data")
        routeList = data.setdefault("routeList")  # Flight list
        return routeList

    def get_legs_dict(__name__, routeList_dict):
        legs = routeList_dict.setdefault("legs")  # 本航班总信息
        leg_dict = legs[0]  # 只有一个字典元素
        return leg_dict

    def Flight(__name__):
        pass

    def FlightTrain(__name__):
        pass

    def main(__name__):
        Method = method_temp.Method()
        dict_str = Method.getDict()
        routeList = Method.get_routeList(dict_str)
        for routeList_dict in routeList[:1]:
            leg_dict = Method.get_legs_dict(routeList_dict)
            if routeList_dict.setdefault("routeType") == "Flight":
                
            elif routeList_dict.setdefault("routeType") == "FlightTrain":
                pass
