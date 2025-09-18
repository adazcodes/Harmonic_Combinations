# Harmonic_Combinations
Technically permutations and combinations but who's counting :)


# Examples
## Example 1:

input
```
array = [1,3,5,8]
# downbeats must be 1, 5, or 8
constraints = {
    0: [1, 5, 8],
    2: [1, 5, 8]
}
```


output
```
1: (1, 3, 5, 8)
2: (1, 3, 8, 5)
3: (1, 5, 8, 3)
4: (1, 8, 5, 3)
5: (5, 1, 8, 3)
6: (5, 3, 1, 8)
7: (5, 3, 8, 1)
8: (5, 8, 1, 3)
9: (8, 1, 5, 3)
10: (8, 3, 1, 5)
11: (8, 3, 5, 1)
12: (8, 5, 1, 3)
```

## Example 2:

input
```
array = [1,2,3,5]
# downbeats must be 1 or 5
constraints = {
    0: [1, 5],
    2: [1, 5]
}
```


output
```
1: (1, 2, 5, 3)
2: (1, 3, 5, 2)
3: (5, 2, 1, 3)
4: (5, 3, 1, 2)
```


## Example 3:

input
```
array = [3,2,1,7]
# downbeats must be 1 or 3
constraints = {
    0: [1, 3],
    2: [1, 3]
}
```


output
```
1: (3, 2, 1, 7)
2: (3, 7, 1, 2)
3: (1, 2, 3, 7)
4: (1, 7, 3, 2)
```


## Example 4:

input
```
array = [1,3,5,7]
# downbeats must be 1 or 5
constraints = {
    0: [1, 5],
    2: [1, 5]
}
```


output
```
1: (1, 3, 5, 7)
2: (1, 7, 5, 3)
3: (5, 3, 1, 7)
4: (5, 7, 1, 3)
```

## Example 5:

input
```
array = [3,5,7,9]
# downbeats must be 3 or 5
constraints = {
    0: [3, 5],
    2: [3, 5]
}
```

I needed to manually include the original at the start here.

output
```
1: (3, 5, 7, 9)
2: (3, 7, 5, 9)
3: (3, 9, 5, 7)
4: (5, 7, 3, 9)
5: (5, 9, 3, 7)
```

## Example 6:

input
```
array = [5,7,9,'#11']
# the first downbeat must be 5 
constraints = {
    0: [5]
}
```

output
```
1: (5, 7, 9, #11)
2: (5, 7, #11, 9)
3: (5, 9, 7, #11)
4: (5, 9, #11, 7)
5: (5, #11, 7, 9)
6: (5, #11, 9, 7)
```
