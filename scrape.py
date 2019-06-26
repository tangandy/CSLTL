
from bs4 import BeautifulSoup
import requests
import json

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

teams_dict = {}

def printPlayerInfo(players, team_data):
  players_array = []
  for player in players:
    player_data = {}
    link = player.find('a')
    player_name = link.text
    print(player_name) 

    title = player.get('title')
    index = title.find("STEAM")
    steam_id = title[index:]
    print(steam_id)

    player_data["player_name"] = player_name
    player_data["steam_id"] = steam_id
    players_array.append(player_data)
  team_data["players"] = players_array
  return

def getPlayers(team_num, team_data):
  url = "https://cstarleague.com/dota2/teams/" + str(team_num)
  r = requests.get(url)
  data = r.text
  soup = BeautifulSoup(data, features="html.parser")
  players = soup.findAll("span", {"class": "tool-tip"})
  printPlayerInfo(players, team_data)
  print("")
  return

def fix_name(team_name):
  fixed_string = team_name.replace(".", ",")
  last_index = len(team_name) - 1
  check_last = fixed_string[last_index]
  if(check_last == " "):
    fixed_string = fixed_string[:last_index]
  return fixed_string

def printTeamInfo(teams):
  for team in teams:
    team_data = {}
    team_uni = team.find("p", {"class": "truncate-text small"})
    team_uni = team_uni.text
    print("TEAM UNIVERSITY: " + team_uni)
    h3_container = team.find("h3")
    team_name = h3_container.text
    print("TEAM NAME: " + team_name)
    link = h3_container.find("a")
    team_num = link.get('href')
    team_num = team_num[13:]
    print("TEAM NUMBER: " + team_num)
    team_data["team_uni"] = team_uni
    team_data["team_num"] = team_num
    getPlayers(team_num, team_data)
    team_name_fixed = fix_name(team_name)
    teams_dict[team_name_fixed] = team_data
  return

print('-' * 12)
print("DIVISION ONE")
print('-' * 12)
print("")
printTeamInfo(teamsD1)
teams_json = json.dumps(teams_dict)
print(teams_json)

# print('-' * 12)
# print("DIVISION TWO")
# print('-' * 12)
# print("")
# printTeamInfo(teamsD2)
