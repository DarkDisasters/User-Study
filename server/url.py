#!/usr/bin/env python
#coding:utf-8

import sys
# from imp import reload
# reload(sys)
# sys.setdefaultencoding('utf-8')

from handler.pointhandler import IndexHandler
from handler.pointhandler import LoadQuestionHandler
from handler.pointhandler import ImgStudyPageHandler
from handler.dbHandler import SaveUserInfoHandler
from handler.dbHandler import SaveAnswerInfoHandler



url=[
	(r'/', IndexHandler),
    (r'/saveUserInfo', SaveUserInfoHandler),
    (r'/loadQuestion', LoadQuestionHandler),
    (r'/imgstudypage', ImgStudyPageHandler),
    (r'/saveanswerinfo', SaveAnswerInfoHandler),
]