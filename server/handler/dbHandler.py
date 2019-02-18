import tornado.web
from tornado.options import options

import pymongo

from handler.madb import MADB

ssDB = MADB();
ssDB.connectDB("userstudy","localhost",27017)

class SaveUserInfoHandler(tornado.web.RequestHandler):
    def post(self):
        print("save start")
        userInfo_age = self.get_argument("age")
        userInfo_gender = self.get_argument("gender")
        userInfo_studyinterest = self.get_argument("studyinterest")
        userInfo_academiclevel = self.get_argument("academiclevel")
        userInfo_experience = self.get_argument("experience")

        print("academiclevel", userInfo_academiclevel)
        ssDB.saveUserInfo({
            "userage": userInfo_age,
            "usergender": userInfo_gender,
            "userstudyinterest": userInfo_studyinterest,
            "useracademiclevel": userInfo_academiclevel,
            "userexperience": userInfo_experience,
        });

        self.set_header("Access-Control-Allow-Origin", "*")
        self.write({"save": "ok"})