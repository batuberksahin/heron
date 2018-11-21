from heron import *

while True:
    edges = input('Enter triangle edges length: ').split(',')

    print('Please input values correctly!' if edges.__len__()==2 else
          ('Please input values correctly!' if not all([i.isdigit() for i in edges]) else
           '- ' + str(round(heron(int(edges[0]),int(edges[1]),int(edges[2])),3))))
