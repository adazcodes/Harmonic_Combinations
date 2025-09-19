# Harmonic_Combinations
### Technically permutations and combinations but who's counting :)
This is a small program or script which takes in an input of a 4-note jazz pattern and outputs every combination including harmonic constraints for necessary downbeat resonance. 
This is typically on beats 1 and 2 if played as eighth notes in 2 beats per chord or 1 and 3 if played as quarter notes in a whole measure.


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


