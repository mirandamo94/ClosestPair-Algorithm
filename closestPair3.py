# coding: utf-8

#CSC 421
#Miranda Mo
#replace text file names in main() to test different results
#Results are printed in float as I wanted to test decimal points

import math

"""Pseudo Code Logic-
 * 
 * Given a set S = {P1, P2, P3....Pn} of points in the plane
 * where Pi = (Xi,Yi) for i = 1,2,...n Computer a pair of distinct points
 * in S of minimum distance delta
 * 
 * 1). X: S sorted by x-coordinate O(nlgn)
 * 
 * 2). Y: S sorted by y-coordinate O(nlgn)
 * 
 * 3). If |S|<=3 then return a closest pair (Pmin, Qmin) in S by brute force
 * 
 * 4). Using X, find a vertical line D of equation x=l that partitions S 
 * into 2 sets of SLeft, SRight of roughly equal size such that SLeft are on D
 * or to its left, and SRight are on D or to its right
 * 
 * 5). Using X and Y compute the arrays XLeft, YLeft, XRight, YRight
 * 
 * 6). Recurse on SLeft to compute a closest pair (Pleft,Qleft) of SLeft, 
 * and on Sright to compute a closest pair (Pright,Qright) of Sright
 * 
 * 7). Let DeltaL = |Pleft Qleft|; DeltaR = |Pright Qright|; and Delta = min{DeltaL, DeltaR}
 * 
 * 8). Using Y, compute the set of points Ymid whose X-coordinate satifies 
 * l-delta <= x <= l+delta, sorted with the request to their Y-coordinate
 * 
 * 9). Traverse Ymid, in the sorted order, and for each point, 
 * compute its distance to the next 7 points in Ymid, and
 * keep track of the pair (Pmid, Qmid) of minimum distance overall
 * 
 * 10). Return the pair in (Pleft, Qleft), (Pright, Qright), (Pmid, Qmid) of minimum distance"""

def distance(a, b):
    
    x = pow((a[0] - b[0]), 2)
    y = pow((a[1] - b[1]), 2)
    dis = math.sqrt(x + y)
    
    return dis

def brute(P):
    
    minimum = distance(P[0], P[1])
    p1 = P[0]
    p2 = P[1]
    length = len(P)
    
    for i in range(length - 1):       
        for j in range(i + 1, length):                         
            d = distance(P[i], P[j])                
            if d < minimum:      
                minimum = d                    
                p1, p2 = P[i], P[j]
                
    print("Used Brute Force")
    return minimum
# 3). If |S|<=3 then return a closest pair (Pmin, Qmin) in S by brute force


def closest_pair(list,length):
    
    by_x = sorted(list,key = lambda x: x[0])
    # 1). X: S sorted by x-coordinate O(nlgn)
    by_y = sorted(list,key = lambda y: y[1])
    # 2). Y: S sorted by y-coordinate O(nlgn)
    
    if length == 0: 
        print("not eought points in list:")
        return list
    
    elif length == 1:
        return float('Inf'), None
    
    elif length == 2:
        return distance(by_x[0],by_x[1]), (by_x[0],by_x[1])
    # 3). If |S|<=3 then return a closest pair (Pmin, Qmin) in S by brute force

    else:       
        mid = length // 2
        left = by_x[ :mid]
        right = by_x[mid: ]
        mid_p = by_x[mid][0]          
        Sub_y = []
        sub_len = 0
    # 4). Using X, find a vertical line D(named mid in this case) 
    #of equation x=l that partitions S into 2 sets of SLeft, SRight 
    #of roughly equal size such that SLeft are on D or to its left, 
    #and SRight are on D or to its right
    
    # 5). Using X and Y compute the arrays XLeft, YLeft, XRight, YRight
    
        deltaL, point1 = closest_pair(left, len(left))
        deltaR, point2 = closest_pair(right, len(right))
    #6) Recurse on SLeft to compute a closest pair (Pleft,Qleft) of SLeft,
    #and on Sright to compute a closest pair (Pright,Qright) of Sright
        
        if deltaR < deltaL:
            delta = deltaR
            point = point2
            
        else:
            delta = deltaL
            point = point1
        #7). Let DeltaL = |Pleft Qleft|; DeltaR = |Pright Qright|;
        # and Delta = min{DeltaL, DeltaR}
        
        for i in range(length):
            if abs((by_x[mid - 1][0]) - (by_y[i][0])) <= delta:
                Sub_y.append(by_y[i])
                
        sub_len = len(Sub_y)
        # 8). Using Y, compute the set of points Ymid whose X-coordinate satifies 
        # l-delta <= x <= l+delta, sorted with the request to their Y-coordinate
        
        for i in range(sub_len - 1):
            for j in range(i + 1, min((sub_len - 1), i + 7)):
                mini = distance(Sub_y[i], Sub_y[j])
        #9). Traverse Ymid, in the sorted order, and for each point
        #compute its distance to the next 7 points in Ymid, and
        #keep track of the pair (Pmid, Qmid) of minimum distance overall
                if mini < delta:
                    point = (Sub_y[i], Sub_y[j])
                    delta = mini
        
        return delta, point
        #10). Return the pair in (Pleft, Qleft), (Pright, Qright), (Pmid, Qmid) of minimum distance

def main():
    with open('10points.txt') as file:
        x = []
        y = []
        
        for lines in file:
            row = lines.split()
            x.append(float(row[0]))
            y.append(float(row[1]))
            
        data = list(zip(x, y))
        length = len(data)
        #print(data)
        
        print("The minimum distance | between these two points:")
        print(closest_pair(data,length))
