# timetable_lab

## First part - genetic algorithm

Use genetic algorithm and python to effectively assign teachers to groups.

To run the genetic_alg.py:
1) set the groups of students at the top of main file (or leave unchanged)
2) set the teachers (or leave unchanged)
3) set the population size and number of iterations (or leave unchanged
4) run genetic_alg.py
5) inspect the outputs: first line is max possible score, then you can see progress of local maximum though the iterations. Then you see the best found schedule. At the bottom of the output you can compare metrics of a random population and the population after a genetic algorithm.

Example of the last output part:

```
-----genetic algorithm-----
@@@@ average score: 46.03125
@@@@ best score: 49
-----simple population-----
@@@@ average score: 38.4296875
@@@@ best score: 47
```

As we see, the average score among the population rises significantly.

## Second part - CSP algorithm

Then we solve a Constraint satisfaction problem to assign teachers and groups to correct hours and days.

The code for CSP algorithm is stored in CSP.py file.

To get the final schedule - run the main.py file.

Example output:

```
Monday
1: 1A english (john) 1B history (alice) 1C english (bob) 1D math (mike) 
2: 1A english (john) 1B history (alice) 1C english (bob) 1D math (mike) 
3: 1A history (bob) 1B english (john) 1C math (sarah) 1D science (victor) 
4: 1A history (bob) 1B english (john) 1C math (sarah) 1D science (victor) 

Tuesday
1: 1A history (bob) 1B english (john) 1C science (sam) 1D science (victor) 
2: 1A history (bob) 1B english (john) 1C science (sam) 1D science (victor) 
3: 1A history (bob) 1B literature (james) 1C science (sam) 1D science (victor) 
4: 1A math (mike) 1B literature (james) 1C history, arts (alice) 1D literature, arts (jane) 

Wednesday
1: 1A math (mike) 1B literature (james) 1C history, arts (alice) 
2: 1A literature (jane) 1C literature (james) 
3: 1A literature (jane) 1C literature (james) 
4: 1A literature (jane) 

Thursday
1: 1A literature (jane) 
2: 1A literature (jane) 
3: 1A literature (jane) 
4: 1A arts (alice) 1B arts (jane) 

Friday
1: 1A arts (alice) 1B arts (jane) 
2: 1A arts (alice) 1B arts (jane) 
```
