#Implement Union, Intersection, Complement and Difference operations on fuzzy sets. 
#Also create fuzzy relations by Cartesian product of any two fuzzy sets and perform max-min composition on any two fuzzy relations.

A = {'x1':0.2,'x2':0.5,'x3':0.8}
B = {'x1':0.6,'x2':0.3,'x3':0.4}
C = {'y1': 0.7, 'y2': 0.4, 'y3': 0.9}

def fuzzy_union(A,B):
    result={}
    for key in A :
        result[key]=max(A[key],B[key])
    return result

def fuzzy_intersection(A,B):
    result={}
    for key in A :
        result[key]=min(A[key],B[key])
    return result

def fuzzy_complement(A):
    result={}
    for key in A : 
        result[key] = 1 - A[key]
    return result

def fuzzy_difference(A,B):
    result={}
    for key in A : 
        result[key]= min(A[key],1-B[key])
    return result

def cartesian_product(A,B):
    relation={}
    for i in A :
        for j in B :
            relation[(i,j)]=min(A[i],B[j])
    return relation

def max_min_composition(R1,R2,X,Y,Z):
    result={}
    for x in X :
        for z in Z :
            max_val = 0 
            for y in Y :
                val = min(R1[(x,y)],R2[(y,z)])
                if val > max_val :
                    max_val = val
            result[(x,z)] = max_val
    return result 

print('Union :',fuzzy_union(A,B))
print('Intersection :',fuzzy_intersection(A,B))
print('Complement of A :',fuzzy_complement(A))
print('Difference : ',fuzzy_difference(A,B))

R1 = cartesian_product(A,B)
print('Fuzzy Relation (A x B ) :',R1)

R2 = cartesian_product(B,C)
print('Fuzzy Relation (B x C) :',R2)

X=A.keys()
Y=B.keys()
Z=C.keys()
composition = max_min_composition(R1,R2,X,Y,Z)

print('Max-Min Compostion :')
print(composition)
