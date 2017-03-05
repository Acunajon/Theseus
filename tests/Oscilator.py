"""
JONATHAN ACUNA
OSCILATOR
"""

UP = 1.1
DOWN = .9
a = UP

T = 10
T_GOAL = 50
T_List = []
count = 0
"""APPROACHES A KNOWN TARGET VALUE"""
while count < 500:
    count += 1
    T *= a
    T_List.append(T)
    if T < T_GOAL:
        a = UP
    elif T > T_GOAL:
        a = DOWN
"""APPROACHES A KNOWN TARGET VALUE"""

        
        
        
T_OFF = 5
Chi_1 = (((T - T_GOAL)**2)/(T_OFF**2))
Chi_List = []
count = 0
T_Nu = []
"""APPROACHES A KNOWN TARGET VALUE BASED ON A CHI VALUE"""
while count < 500:
    count += 1
    print count
    T *= a
    T_Nu.append(T)
    
    
    Chi = (((T - T_GOAL)**2)/(T_OFF**2))
    Chi_List.append(Chi)
    
    
    if a == UP and Chi < Chi_1:
        a = UP
    elif a == UP and Chi > Chi_1:
        a = DOWN
        
    elif a == DOWN and Chi < Chi_1:
        a = DOWN
    elif a == DOWN and Chi > Chi_1:
        a = UP
        
        
    T_List.append(T)
    Chi_1 = Chi
"""APPROACHES A KNOWN TARGET VALUE BASED ON A CHI VALUE"""
