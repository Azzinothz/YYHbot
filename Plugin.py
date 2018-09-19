# -*- coding: utf-8 -*-
from CourseStatus import CourseStatus


def onQQMessage(bot, contact, member, content):
    if contact.name == "文明寝室，文明你我他":
        if content == "yyh hello":
            bot.SendTo(contact, "YYHbot is ON")
        
        if content == "yyh run CourseStatus":
            CourseStatus().run()
