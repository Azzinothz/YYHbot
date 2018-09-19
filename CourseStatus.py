import requests
import json
import winsound
import time

from qqbot import QQBot
import qqbot

qq_url = "http://127.0.0.1:8188/send/group/%E6%96%87%E6%98%8E%E5%AF%9D%E5%AE%A4%EF%BC%8C%E6%96%87%E6%98%8E%E4%BD%A0%E6%88%91%E4%BB%96/"

url = "http://jwxt.shmtu.edu.cn/shmtu/stdElectCourse!queryStdCount.action?profileId=863"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Connection": "keep-alive",
    "Host": "jwxt.shmtu.edu.cn",
    "If-None-Match": "1537370306371",
    "Referer": "http://jwxt.shmtu.edu.cn/shmtu/stdElectCourse!defaultPage.action?electionProfile.id=863",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
cookies = {
    "JSESSIONID": "A7C46F250C3886F3BB1FF8941E3CD213",
    "SVRNAME": "xk63",
    "arp_scroll_position": "arp_scroll_position",
    "semester.id": "155"
}

course_ids = {
    "173891": "电子商务法律法规",
    "173587": "航运服务管理",
    "173606": "物流产业规划"
}

i = 0
while course_ids:
    resp = requests.request("get", url, headers=headers, cookies=cookies)
    if resp.status_code != 200:
        msg = "出问题了，返回" + str(resp.status_code)
        requests.get(qq_url + msg)
        break
    raw = resp.text[53:]

    for course_id in course_ids:
        c_index = raw.find(course_id)
        course = raw[c_index:]
        sc_index = course.find("sc:")
        lc_index = course.find("lc:")
        wc_index = course.find("wc:")

        sc = int(course[sc_index + 3: lc_index - 1])
        lc = int(course[lc_index + 3: wc_index - 1])
        wc = course[wc_index + 3: wc_index + 5]

        last_char = [str(c) for c in range(10)]
        if wc[-1] not in last_char:
            wc = int(wc[:len(wc) - 1])
        else:
            wc = int(wc)

        if (sc < lc) or (wc != 0):
            msg= course_ids[course_id] + " 可以选了"
            requests.get(qq_url + msg)
            del course_ids[course_id]

    i += 1
    print(i)
    time.sleep(10)
