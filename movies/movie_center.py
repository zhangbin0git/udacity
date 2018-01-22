#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2017/12/24 22:37 
# @Author : Mark 
# @Site :  home
# @File : movie_center.py 
# @Software: PyCharm Community Edition
import media
import fresh_tomatoes

toy_story = media.Movie('《爸爸去哪儿专题》天天森碟照片显夫妻相 网友：天森一对',
                        '《爸爸去哪儿专题》天天森碟照片显夫妻相 网友：天森一对',
                        'http://t3.baidu.com/it/u=3666720111,1287387588&fm=20',
                        'http://www.56.com/u20/v_MTAyMDE0ODAx.html')
toy = media.Movie('天天向上郎平女儿现身《天天》催泪团圆，相拥而泣回忆母女情',
                        '天天向上郎平女儿现身《天天》催泪团圆，相拥而泣回忆母女情',
                        'http://t3.baidu.com/it/u=3969342787,988033769&fm=20',
                        'https://v.qq.com/x/cover/6sef7vjgz5riy8t/'
                        'v0536fg5ska.html')
movies_z = [toy, toy_story]
fresh_tomatoes.open_movies_page(movies_z)