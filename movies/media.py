#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2017/12/24 22:33 
# @Author : Mark 
# @Site : home
# @File : media.py 
# @Software: PyCharm Community Edition
import webbrowser
# 包含类，Movie
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open_new(self.trailer_youtube)




