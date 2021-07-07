
# 31/3/21-25

isldata=[
    {"team":"mumbai","mp":20,"won":12,"drawn":4,"los":4,"pts":40},
    {"team":"atk","mp":20,"won":12,"drawn":4,"los":4, "pts": 40},
    {"team":"ne","mp":20,"won":8,"drawn":9,"los":3, "pts": 33},
    {"team":"fcg","mp":20,"won":7,"drawn":10,"los":3, "pts":31},
    {"team":"hybd","mp":20,"won":6,"drawn":11,"los":3, "pts":29}
]


#highest drwn


#(1) # no of teams


teamno=len(isldata)
#print(teamno)
                                                     ## o/p
                                                      # 5
# (2) # map
team_name=list(map(lambda data:data["team"],isldata))
#print(team_name)

                                                    ## o/p
                                  # ['mumbai', 'atk', 'ne', 'fcg', 'hybd']

##(3) # highest point

points=max(list(map(lambda data:data["pts"],isldata)))
hpt=list(filter(lambda team:team["pts"]==points,isldata))
#print(hpt)
                                           ## o/p
#[{'team': 'mumbai', 'mp': 20, 'won': 12, 'drawn': 4, 'los': 4, 'pts': 40}, {'team': 'atk', 'mp': 20, 'won': 12, 'drawn': 4, 'los': 4, 'pts': 40}]


##(4) # highest point team

hptname=list(map(lambda team:team["team"],hpt))
#print(hptname)
                                                       ## o/p
                                                 # ['mumbai', 'atk']

## (5) #range b/w 30-40

#rageteam=list(filter(lambda data: (data["pts"]<=40) & (data["pts"]>30),isldata))
#print(rageteam)

                                            # o/p
 #   [{'team': 'mumbai', 'mp': 20, 'won': 12, 'drawn': 4, 'los': 4, 'pts': 40}, {'team': 'atk', 'mp': 20, 'won': 12, 'drawn': 4, 'los': 4, 'pts': 40}, {'team': 'ne', 'mp': 20, 'won': 8, 'drawn': 9, 'los': 3, 'pts': 33}, {'team': 'fcg', 'mp': 20, 'won': 7, 'drawn': 10, 'los': 3, 'pts': 31}]


## (6) #range b/w 30-40--- length

#rageteam=list(filter(lambda data: (data["pts"]<=40) & (data["pts"]>30),isldata))
#print(len(rageteam))

                                            #o/p
                                               #4

### (7)  or (5)

#rangeteam=list(filter(lambda data:30<data["pts"]<=40,isldata))
#print(rangeteam)

## (8) or (6)

rangeteam=list(filter(lambda data:30<data["pts"]<=40,isldata))
print(len(rangeteam))


