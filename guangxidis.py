#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: gaolei82@jd.com
"""
import pandas as pd
import json
from urllib.request import urlopen,quote


def navi_dis(inputpath,ori,des):
    '''
    求导航距离的函数
    :param inputpath: 待输入的excel的地址
    :param ori:
    :param des:
    :return:
    '''
    oridf = pd.read_excel(inputpath,sheet_name=ori)
    desdf = pd.read_excel(inputpath,sheet_name=des)
    distance_pd = pd.DataFrame(columns=['上级节点', '下级节点', '距离'])
    for index in oridf.index:
        origins = str(oridf.loc[index, '纬度']) + ',' + str(oridf.loc[index, '经度'])
        destinations = str(desdf.loc[index, '纬度']) + ',' + str(desdf.loc[index, '经度'])
        uri = url + '&origins=' + origins + '&destinations=' + destinations + '&ak=' + ak
        req = urlopen(uri)
        res = req.read().decode()
        temp = json.loads(res)
        distance = temp['result'][0]['distance']['text']
        distance_newrow = pd.Series({'上级节点': str(oridf.loc[index, '地址']), '下级节点': str(desdf.loc[index, '地址']), '距离': distance})
        distance_pd = distance_pd.append(distance_newrow, ignore_index=True)

    for index in distance_pd.index:
        distance_pd.loc[index,'修正后的距离'] = float(distance_pd.loc[index,'距离'][:-2])
    distance_pd.to_excel(r'县中心到收费站导航距离.xlsx')
    return distance_pd

if __name__ == '__main__':
    url = 'http://api.map.baidu.com/routematrix/v2/driving?output=json'
    ak = 'rUtS4uA8MDUK9B8dQSKczqSGRGRiBLCi'
    inputpath = r'服务区收费站列表.xlsx'
    ori = '县中心'
    des = '服务区'
    print(navi_dis(inputpath,ori,des))


