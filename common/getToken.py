"""
用来获取token,并将token返回
"""

from urllib3 import PoolManager
import json
def getToken():
    """
    获取token并返回
    :return: token
    """
    interface = 'https://lianjieit.net/his_dvp/api/api_operator/login_set_data'
    base_data = {
        'username': 'sxmming',
        'password': '123456'
    }
    req = PoolManager(num_pools=5, headers=None)
    response = req.request('POST', url=interface, fields=base_data,)
    #将返回的json转换成字典
    dic_token = json.loads(response.data)
    token = dic_token['data']['token']
    return token


data = {
    'tenant_id': '0000',
    'check_in_id': '31446'
        }
token = getToken()
headers = {
    'token': token,
}
url = 'https://lianjieit.net/his_dvp/api/api_settle/consignees_init'
http = PoolManager(num_pools=5, headers=headers)
date = http.request('POST', url=url, fields=data)

print(date.data.decode('utf-8'))
