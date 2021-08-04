Spain = {'wins':0 , 'loses':0 , 'draws':0 , 'goal difference':0 , 'points':0}
Iran = {'wins':0 , 'loses':0 , 'draws':0 , 'goal difference':0 , 'points':0}
Portugal = {'wins':0 , 'loses':0 , 'draws':0 , 'goal difference':0 , 'points':0}
Morocco = {'wins':0 , 'loses':0 , 'draws':0 , 'goal difference':0 , 'points':0}
"""
Iran - Spain
Iran - Portugal
Iran - Morocco
Spain - Portugal
Spain - Morocco
Portugal - Morocco
"""
"""
Teams = ['Spain','Iran','Portugal','Morocco']
T_Data = [Spain , Iran , Portugal , Morocco ]
final_data_sheet = dict(zip(Teams,T_Data))

"""
#t1 , t2 = input().split("-")
#t1 , t2 = int(t1),int(t2)
#print(t1 , t2)
"""
out put print function but need touch
for q ,w in Spain.items():
    print(f"{q}:{w}" ,end=" , ") 


use all in dic 
"""
def g_d_input(n):
    T1 = []
    T2 = []
    for i in range(0,n):
        t1 , t2 = input(":").split("-")
        T1.append(int(t1))
        T2.append(int(t2))
    return tuple (zip(T1,T2) )
games_data =g_d_input(6)
# if dic won't work lets try tuple
#note : dictionaies can't have duplicated data

def team_results(team1,team2,game_number):
    Data = games_data[game_number]
    team1_r = Data[0]
    team2_r = Data[-1]
    Delta = team1_r - team2_r
    if team1_r > team2_r :
        team1['wins'] += 1
        team2['loses'] += 1
        team1['goal difference'] += Delta
        team2['goal difference'] -= Delta
        team1['points'] += 3
    elif team2_r > team1_r :
        team2['wins'] += 1
        team1['loses'] += 1
        team2['goal difference'] += Delta
        team1['goal difference'] -= Delta
        team2['points'] += 3
    elif team1_r == team1_r :
        team1['draws'] += 1
        team2['draws'] += 1
        team1['points'] += 1
        team2['points'] += 1
    return team1 , team2


