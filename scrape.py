from bs4 import BeautifulSoup
import requests

url = "https://cstarleague.com/dota2/standings?division=Varsity&year=2018-2019"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, features="html.parser")
teamsD1 = soup.findAll("div", {"class": "match-team"})

url2 = "https://cstarleague.com/dota2/standings?division=Junior+Varsity&year=2018-2019"
r2 = requests.get(url2)
data2 = r2.text
soup2 = BeautifulSoup(data2, features="html.parser")
teamsD2 = soup2.findAll("div", {"class": "match-team"})

def printPlayers(team_num):
  url = "https://cstarleague.com/dota2/teams/" + str(team_num)
  r = requests.get(url)
  data = r.text
  soup = BeautifulSoup(data, features="html.parser")
  players = soup.findAll("span", {"class": "tool-tip"})
  print(players)
  return

def printTeamInfo(teams):
  for team in teams:
    team_uni = team.find("p", {"class": "truncate-text small"})
    # print("TEAM UNIVERSITY: " + team_uni.text)
    h3_container = team.find("h3")
    team_name = h3_container.text
    print("TEAM NAME: " + team_name)
    link = h3_container.find("a")
    team_num = link.get('href')
    team_num = team_num[13:]
    # print("TEAM NUMBER: " + team_num)
    # print("")
    printPlayers(team_num)
  return

print('-' * 12)
print("DIVISION ONE")
print('-' * 12)
print("")
printTeamInfo(teamsD1)

print('-' * 12)
print("DIVISION TWO")
print('-' * 12)
print("")
printTeamInfo(teamsD2)

