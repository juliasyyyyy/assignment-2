#!/usr/bin/env python
# coding: utf-8

# # 1. 

# def relationship_status(from_member, to_member, social_graph):
#     '''
#     Item 1.
#     Relationship Status. 10 points.
#     Let us pretend that you are building a new app.
#     Your app supports social media functionality, which means that users can have
#     relationships with other users.
#     There are two guidelines for describing relationships on this social media app:
#     1. Any user can follow any other user.
#     2. If two users follow each other, they are considered friends.
#     This function describes the relationship that two users have with each other.
#     Please see "assignment-2-sample-data.py" for sample data. The social graph
#     will adhere to the same pattern.
#     Parameters
#     ----------
#     from_member: str
#         the subject member
#     to_member: str
#         the object member
#     social_graph: dict
#         the relationship data    
#     Returns
#     -------
#     str
#         "follower" if fromMember follows toMember,
#         "followed by" if fromMember is followed by toMember,
#         "friends" if fromMember and toMember follow each other,
#         "no relationship" if neither fromMember nor toMember follow each other.
#     '''
#     # Write your code below this line

# In[12]:


social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}



    





# In[24]:





def relationship_status(from_member, to_member, social_graph):
    if to_member in (social_graph[from_member]["following"]) and from_member in (social_graph[to_member]["following"]):
        return "friends"

    if from_member in (social_graph[to_member]["following"]):
        return "followed by"

    if to_member in (social_graph[from_member]["following"]):
        return"follower"
    
    else:
        return "no relationship" 
    
from_member=str(input("enter the subject member: "))

to_member=str(input("enter the object member: "))

print(relationship_status(from_member, to_member, social_graph))

    


# # 2. 

# In[ ]:


def tic_tac_toe(board):
    '''
    Item 2.
    Tic Tac Toe. 10 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-2-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Write your code below this line


# In[30]:


Sample data for Tic Tac Toe below:
'''

 board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]


# In[ ]:



 


# In[95]:




board = [
['X','X','O','X'],
['O','X','O','X'],
['X','','O','X'],
['X','','X','O'],
]




def tic_tac_toe(board):
    if len(board[0]) == 6 and board[0][0] == board[1][1] == board [2][2]== board[3][3]==board[4][4]==board[5][5]: 
        return str(board[0][0])
    
    if len(board[0]) == 6 and board [0][5] == board[1][4]== board[2][3]==board[3][2]==board[4][1]==board[5][0]:
        return str(board[0][5])

    for r in range(6):
        if len(board[0]) == 6 and board [r][0] ==  board [r][1] == board [r][2] == board [r][3] == board [r][4] == board [r][5]:
            return str(board[r][0])
    
    for c in range(6):
        if len(board[0]) == 6 and board [0][c] ==  board [1][c] == board [2][c] == board [3][c] == board [4][c] == board [5][c]:
            return str(board[0][c])
    
    if len(board[0]) == 5 and board[0][0] == board[1][1] == board [2][2]== board[3][3]==board[4][4]:  
        return str(board[2][2])
    
    if len(board[0])== 5 and board [0][4]==board[1][3]==board[2][2]==board[3][1]==board[4][0]:
        return str(board[2][2])
    
    for r in range(5):
        if len(board[0]) == 5 and board [r][0] ==  board [r][1] == board [r][2] == board [r][3] == board [r][4]: 
            return str(board[r][0])
    
    for c in range(5):
        if len(board[0]) == 5 and board [0][c] ==  board [1][c] == board [2][c] == board [3][c] == board [4][c]:
            return str(board[0][c])

    if len(board[0]) == 4 and board[0][0] == board[1][1] == board [2][2]== board[3][3]: 
        return str(board[0][0])
    
    if len(board[0]) == 4 and board [0][3] == board[1][2]== board[2][1]==board[3][0]:
        return str(board[0][3])

    for r in range(4):
        if len(board[0]) == 4 and board [r][0] ==  board [r][1] == board [r][2] == board [r][3]: 
            return str(board[r][0])
    
    for c in range(4):
        if len(board[0]) == 4 and board [0][c] ==  board [1][c] == board [2][c] == board [3][c]: 
            return str(board[0][c])

    if len(board[0]) == 3 and board[0][0] == board[1][1] == board [2][2]: 
        return str(board[1][1])
                   
    if len(board[0]) == 3 and board [0][2] == board[1][1] == board[2][0]:
        return str(board[1][1])
    
    for r in range(3):
        if len(board[0]) == 3 and board [r][0] ==  board [r][1] == board[r][2]:
            return str(board[r][0])
    
    for c in range(3):
        if len(board[0]) == 3 and board [0][c] ==  board [1][c] == board [2][c]: 
            return str(board[0][c])
    
    else:
        return "NO WINNER"

    

print(tic_tac_toe(board))  
    
    





    


# In[ ]:





# # 3. 

# In[ ]:


def eta(first_stop, second_stop, route_map):
    '''
    Item 3.
    ETA. 10 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "assignment-2-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Write your code below this line


# In[ ]:


Sample data for ETA below:
(from_stop, to_stop)
'''

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}


# In[123]:


legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }, 
    
    
}

def eta(first_stop, second_stop):
    
    if (first_stop,second_stop)in legs: 
        return legs[first_stop,second_stop]["travel_time_mins"] 
    
    else: 
        a = [x for x in legs if x[0] == first_stop][0]
        b =  [x for x in legs if x[1] == second_stop][0]
        if a[1] == b[0]:
            return legs[a]["travel_time_mins"] + legs[b]["travel_time_mins"] 
        else:
            return legs[a]["travel_time_mins"] + legs[(a[1],b[0])]["travel_time_mins"] +legs[b]["travel_time_mins"] 
        
    
    
    

    
first_stop=str(input("First stop: "))
second_stop=str(input("Second stop: "))

print(eta(first_stop, second_stop))


# In[ ]:





# In[ ]:




