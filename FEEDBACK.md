
@import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} 

<!-- code_chunk_output -->

- [LAB-6 Feedback](#lab-6-feedback)
    - [Blind Test](#blind-test)
    - [Open Test](#open-test)
    - [Documents for Participation Grade](#documents-for-participation-grade)
    - [Comments on the grading](#comments-on-the-grading)
    - [Grade:](#grade)
    - [Participation Grade:](#participation-grade)

<!-- /code_chunk_output -->


# LAB-6 Feedback

| Test Case	| description	    | in: coice	|in: amount	|out: balance	|out: info	        |out: menu |
| ----------|-------------------|-----------|-----------|---------------|-------------------|----------|
| 1	        | normal deposit	| D	        |100	    |1,100	        |NA	                |do you want to use atm again|
| 2	        | normal withdrawal	| W	        |800	    |1,800	        |NA	                |do you want to use atm again|
| 3	        | view balance	    | V	        |NA	        |1,000	        |NA	                |do you want to use atm again|
| 4	        | higher withdrawl	| W	        |1,200	    |-200	        |negative balance	|do you want to use atm again|
| 5	        | proper exit	    | E	        |NA		    |NA	            |NA                 |Thank you|
| 6	        | deposit negative	| D	        |-100	    |NA	            |negative number	|do you want to use atm again|
| 7	        | withdraw negative	| W	        |-100	    |NA	            |negative number	|do you want to use atm again|


### Blind Test
|Result      |Description|
|------------|--------------------|
| **YES-** | Passes Test case 1 |  
| **YES-** | Passes Test case 2 |   
| **YES-** | Passes Test case 3 |   
| **-NO** | Passes Test case 4 |    
| **NO-** | Passes Test case 5 |   
| **YES-** | Passes Test case 6 |   
| **YES-** | Passes Test case 7 |   
| **YES-** | Program clearly states the purpose in the output |   
| **-NO** | Input prompts are clear |   
| **-NO** | ATM Menu is properly displayed and validates|  


### Open Test
|Result |Description|
|--------------|-----------------------------------------|
|**-NO**| The algorithm matches the code   |
|**-NO**| Refactoring is properly done   |
|**YES-**| There are at least three functions   |
|**YES-**| Purpose of the program is clearly stated |  
|**YES-**| There are comments in the code|
|**YES-**| There is a block of introductory comments at the top |

### Documents for Participation Grade

|Result         |Type            |
|---------------|----------------|
|**-NO** | Reflection 1   |
|**YES-** | Reflection 2   |
|**-NO** | Reflection 3   |
|**-NO** | Algorithm      |


### Comments on the grading
- Unnecessary use of global variables 
- The refactoring is not properly done. 
- There is no main function 
- There is no algorithm. 
- The program does not exist properly. 
### Grade: R

### Participation Grade: S
N for megan and Jhon
 - If participation grade is unsatisfactory check the `NO` in the documents sections
