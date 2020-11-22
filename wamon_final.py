#!/usr/bin/python3


# import sys, traceback
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import os
import json
from pywebpush import webpush

from time import strftime, sleep
from notify_run import Notify

# import time
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

# from selenium.webdriver.support.ui import WebDriverWait  # this & next two both needed for waiting
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

from pyfcm import FCMNotification

push_service = FCMNotification(
    api_key="AAAAK38byIs:APA91bE38_IOtCtCaB7RBykOwQfg8OJ5Thu2NpSjT7oYsINGc6c96o5OILv11BQnEH1KCWbQq1CBD4vgsrPx7J25hKWFF9287Ef5iaveACcRpi7_P_tcfS98GgHH5I5L10ZiRoQe1aNv")

registration_id = "cH3pt0ZYRxKE7KBw0VTS4j:APA91bFaoW4oYlNzWw0NdW4z0Q59EDdh2dfhjhPaFu-D4z_0D3i9ueVydTw8NSH3qS_9z_hSWHweWukNliIH2Iws1wg_TN0cRWf39R7SV0dCBzlXMJNWSsbMnfz_TwudIH-KcvjzINGU"

VAPID_CLAIMS = {
    "sub": "mailto:supriyabaidya63@gmail.com"
}


def send_web_push_v2(subscription_information, message_body):
    return webpush(
        subscription_info=subscription_information,
        data=message_body,
        vapid_private_key='cLfnivpT-GEqRPEVgTimVEl66wQFOhZyk_WmbKMxKEI',
        vapid_claims=VAPID_CLAIMS
    )


def push_notify(message):
    # PASTE YOUR ENDPOINT HERE
    # endpoint = '{"endpoint":"https://fcm.googleapis.com/fcm/send/ci3W-wAR-lM:APA91bFnxlVnTytgIdSi0-YNbG41uaRQeRJrdOwGabGE0Jouxa7uiR2AU7_lTMsMKf4uovYCDer846E5phpgIJtt7WenLyTpTVBhW_oRw_wjc78Ev2PxZy77bdq2h5D5ooVheX_x2dcD","expirationTime":null,"keys":{"p256dh":"BKGtitE69MOjmxNyY6E9cOsIvCXX4G44vgk7xcuZYKgWt2FvXofYVnNboBSqWAQ8NxBqgut-yfLXVXUxBk-cZFc","auth":"McAAFncq8ZA_KcXqXsOl9w"}}'
    # endpoint = '{"endpoint":"https://fcm.googleapis.com/fcm/send/dOV0Rye1Vvw:APA91bGExTVRS_RPsskGR-dz6mxZRKFkcLUgXfplWhrDtI2H1OkiGOSrsg3oEpNPYaBMPCXdIXA3BVofftapZl9fE_jzP29lo-YeFFdiU17AhWPC9EktZocY8tQFguCVe1NLbconHMqO","expirationTime":null,"keys":{"p256dh":"BJ2OG1mskNMcZK6i4y_BCP8k5v7x84ytK_S2KKb-JRsT0kHTVuwg7wuqgthjRNeUmOjIS7JRxW6wc-YI5TcxcPw","auth":"aYLQdEnNM_louEQYcF_vuA"}}'
    endpoint = '{"endpoint":"https://fcm.googleapis.com/fcm/send/cVnq5iYieus:APA91bEIxi8mWS2FyhSQc6v-Z79rgvgTXHD3zu8fvh-3WD3Sq4v1Mn9q55f3pfVH1m2mBQqcl31oeiD-JOumkEfgp_b6G3sg7VWly_mzqmFiV9_Mw4IhgnTHbxQpfAR-7eMI90GzTxtO","expirationTime":null,"keys":{"p256dh":"BGbpUZNHV6E_5THJiPCiOq_P9TCNKXvJ5K6BBQX1elVvU1N2hEtlZLt0LthFCi4fuaOEAgqpQiMF-3UsY1s2sv4","auth":"RinU8xaKoQQUdoOcRuY1Cg"}}'

    try:
        token = json.loads(endpoint)
        response = send_web_push_v2(token, message)
        print('response')
        print(response)
        print('success')
    except Exception as e:
        print("error: ", e)
        print('failed: ', str(e))


print("PLEASE WAIT STARTING wa_monitor")
cwd = os.getcwd()

notify = Notify()

options = FirefoxOptions()
fp = webdriver.FirefoxProfile(cwd + "/profile")

# useragent = "Mozilla/5.0 (X11; Linux i686; rv:77.0) Gecko/20100101 Firefox/77.0"
# #works perfectly fine without useragent modification in windows awa heroku
# fp.set_preference("general.useragent.override", useragent)

# switch headless option accordingly
# options.add_argument('--no-sandbox')
# options.add_argument("--headless")


# ///////////////// Init binary & driver
new_driver_path = cwd + '/geckodriver/geckodriver'
new_binary_path = '/usr/bin/firefox'
options.binary_location = new_binary_path
serv = Service(new_driver_path)
# driver = webdriver.Firefox(firefox_profile=fp, options=options, service=serv)
driver = webdriver.Firefox(firefox_profile=fp, options=options, executable_path=new_driver_path,
                           firefox_binary=new_binary_path)
# driver = webdriver.Firefox(firefox_profile=fp, options=options,
#                            executable_path='/home/kali/Documents/geckodriver/geckodriver',
#                            firefox_binary='/usr/bin/firefox')
driver.get('https://web.whatsapp.com')

sleep(15)

while True:

    try:
        chat = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div")
        chat.click()
        print("CONNECTED TO WA SERVER")
        sleep(5)
        save = True
        # search = driver.find_element_by_xpath(
        #    "/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/input")
        search = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]")
        search.click()
        sleep(5)
        name = "Sujoy Adhikari"
        search.send_keys(name)
        sleep(5)
        _open = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div")
        _open.click()
        sleep(5)
        print("NOW TRACKING IS LIVE")
        t = strftime("%d/%m/%Y %H:%M:%S")
        speako, speakf = True, True
        while True:
            try:
                status = driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]/span").text
                t = strftime("%Y-%m-%d %H:%M:%S")
                print("{1} :  {2} is {0}".format(status, t[11:], name))
                if speako and status == 'online':
                    notify.send('📱 ' + name + ' is online 📱 ')
                    print("{}  {} : online".format(t[11:], name) + '\n')
                    push_notify('{} is OnLinE'.format(name))

                    android_noti_result = push_service.notify_single_device(registration_id=registration_id,
                                                                            message_title='WaMon_Notification',
                                                                            message_body='{} is OnLinE'.format(name))
                    print('android_noti_result')
                    print(android_noti_result)

                    speako = False
                    speakf = True
                if status != 'online':
                    speako = True
                    notify.send('📴 {} is {} 📴 '.format(name, status))
                    print("{} {} : {}".format(t[11:], name, status) + '\n')
                    push_notify('{} is {}'.format(name, status))

                    android_noti_result = push_service.notify_single_device(registration_id=registration_id,
                                                                            message_title='WaMon_Notification',
                                                                            message_body='{} is {}'.format(name,
                                                                                                           status))
                    print('android_noti_result')
                    print(android_noti_result)

                    speakf = True
                sleep(60)
            except Exception as ex:
                print("Exception IN INNER LOOP OF STATUS CHECKING, str(ex.args): " + str(ex.args))
                status = "Offline"
                speako = True
                t = strftime("%Y-%m-%d %H:%M:%S")

                if speakf:
                    notify.send('📴 {} is {} 📴 '.format(name, status))
                    print("{} {} : offline".format(t[11:], name) + '\n')
                    push_notify('{} is oFfLinE'.format(name))

                    android_noti_result = push_service.notify_single_device(registration_id=registration_id,
                                                                            message_title='WaMon_Notification',
                                                                            message_body='{} is oFfLinE'.format(name))
                    print('android_noti_result')
                    print(android_noti_result)

                    speakf = False
                print("{1} :  {2} is  {0}".format(status, t[11:], name))
                sleep(60)
                pass
    # except Exception as err:
    # print("Exception, str(err.args): " + str(err.args))
    # traceback.print_exc(file=sys.stdout)
    # for i in range(30):
    # sleep(0.5)
    # print('.',end="")
    # print()
    # pass
    except Exception as ex:
        print("Exception IN OUTER LOOP OF CONNECTIVITY TO WA SERVER, str(ex.args): " + str(ex.args))
        # traceback.print_exc(file=sys.stdout)
        print("PLEASE OPEN WA IN YOUR PHONE")
        print("CONNECTING TO WA SERVER.", end="")
        for i in range(30):
            sleep(0.5)
            print('.', end="")
        print()
        pass
