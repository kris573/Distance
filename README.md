# Distance
求导航距离和直线距离
在实际的项目中经常遇到求两点之间距离的情况，主要包括求直线距离和导航距离两类，有时候也要求球面距离，直线距离和球面距离比较接近，python也有现成的包，先给出一种求导航距离的方法。

1，将待求距离的两点放在同一个Excel的两个不同Sheet里 
2，每一个sheet主要包括'地址','经度','纬度'三列，且每个sheet行数一样
3，结果保存在excel里
