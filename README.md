These are my submissions to the Tuenti Challenge 2 (2012).
I know some of them are not optimal at all, but I focused in development speed instead (to have enough time to solve the dificult ones).
There are almost all written in Python, except for the ones I thought they could be vastly improved by porting them to C.

Almost all my scripts share a common pattern, wich can be easily identified and read.
They are made to run in paralell (one subprocess for each test case), except when there's no significant advantage in doing so (very small test cases, one single test case, shared data...).

For example, this code execute each test in a different core (subproccess). To run each test case sequentially instead:
```python
if __name__ == '__main__':  
        data = parse_input()  
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count()) # comment this  
        for n, result in enumerate(pool.map(main, data)): # comment this  
        #for n, d in enumerate(data): # uncomment this  
        #    result = main(d) # uncomment this  
                print(str(result))
```