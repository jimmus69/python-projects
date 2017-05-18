#!/usr/bin/python

import subprocess
import slackweb

wiki = "<insert_site_to_test>"
slack = slackweb.Slack(url="https://<insert_slack_webhook_url>")

bash_com = '/usr/bin/curl -s --head --request GET wiki | grep "200 OK" '

try:
        output = subprocess.getstatusoutput(bash_com)
        if output[0] == 0:
                print("Wiki is up", output)
        else :
                print("Wiki is down", output)
                attachments = []
                attachment = {"Link": wiki}
                attachments.append(attachment)
                slack.notify(text="This is a test message, please ignore: ", attachments=attachments)
except subprocess.CalledProcessError as err:
        print("Non-zero return code")
