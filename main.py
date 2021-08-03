for team in ['Spain' , 'Iran' ,'Portugal' , 'Morocco']:
    team = {"wins":0 , "loses":0 , "draws":0 , "goal difference":0 , "points":0 }
print(Morocco , Portugal,Iran,Spain) 

def dic_creation(team):
    team = {"wins":0 , "loses":0 , "draws":0 , "goal difference":0 , "points":0 }
    return team


class Group_B:
    def f_status(self):
        self = {"wins": 0, "loses": 0, "draws": 0, "goal difference": 0, "points": 0}
        return self
group_b = Group_B
Spain = group_b.f_status
print(Spain.items)