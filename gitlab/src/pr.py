import sys
import base64
import getpass
import requests
import bs4
import argparse

parser = argparse.ArgumentParser('Extract PR\'s from the Junos release')
parser.add_argument("-r", help = "Junos release", required = True)
parser.add_argument("-x", help = "Includes a Synopsis", action = "store_true")
args = parser.parse_args()

version = str(args.r)

base_url = 'https://punch.juniper.net/punch/detail.mhtml?component_name=monolithic.junos-2009&release_name='
url = base_url + version
passWord = ''
userName = getpass.getuser()
print userName
while passWord == '':
    passWord = getpass.getpass(prompt='Enter your JPR password:')
headers = {'Authorization': 'Basic %s' % base64.b64encode(str( userName + ':' + passWord ))}


builds = []
pr_set = []
punch_page = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(punch_page.content, 'html.parser')
tabledata = soup.find("table", class_="center-pane")
rows = tabledata.find_all("tr", align="left")
for row in rows:
    if 'Archived' in str(row) or 'Available' in str(row):
        tags = row.find_all("td")
        for tag in tags:
            version_str_len = len(version)
            if version in str(tag)[:version_str_len+4]:
                builds.append(tag.get_text())
            if '/volume/build' in str(tag)[:17]:
                build_path = tag.get_text()
                trim_point = build_path.find(version)
                build_path = build_path[:trim_point]
pr_dict = {}
for build in builds:
    detail_url = 'https://punch.juniper.net/mba_function/detail_bugfix_report.mhtml?component_name=monolithic.junos-2009&release_name='+version+'&build_name='+build+'&build_path='+build_path+build
    punch_detail = requests.get(detail_url, headers=headers)
    detail_soup = bs4.BeautifulSoup(punch_detail.content, 'html.parser')
    for pr in detail_soup.find_all('a'):
        pr_set.append(pr.get_text().replace(u'\xa0',u''))
        new_tag = pr.parent
        new_tag2 = new_tag.findNext('td').contents[0]
        pr_dict[pr.get_text().replace(u'\xa0',u'')] = new_tag2

if args.x is True:
    for item in pr_dict:
        print "{} - {}".format(item, pr_dict[item])
else:
    for item in pr_dict:
        print item

