## 0. 문제 목록
|문제 번호|문제|날짜|
|----|----|----|
|BOJ 10870|[피보나치 수5](https://www.acmicpc.net/problem/10870)|24.09.02|
|BOJ 4779|[칸토어 집합](https://www.acmicpc.net/problem/4779)|24.09.03|


## 1. 함수와 재귀함수

- **함수란?**
    
    : 일련의 작업을 수행하는 코드의 블록이며, 이 블록은 재사용이 가능하다는 장점이 있다.
    
    ```cpp
    function(..) {
    	...
    	// codes
    	...
    }
    ```
    
- **재귀함수란?**
    
    : 함수의 일종이며, 재귀함수는 함수 내에서 자기 자신을 호출하는 함수를 의미한다.
    
    ```cpp
    recursion_function(..) {
    	...
    	// codes
    	recursion_function(..);
    	...
    }
    ```
    

- ***“ 1부터 n까지 더하는 함수를 만들어보세요. “***
    - 함수를 이용하여 구현
        - `Python`
            
            ```python
            def sum_func(n):
            	ret = 0
            	for i in range(1, n + 1):
            		ret += i
            	return ret
            ```
            
    - 재귀함수를 이용하여 구현
        - `Python`
            
            ```python
            def sum_func(n):
            	if n == 1:
            		return 1
            	return sum_func(n - 1) + n
            ```
            

## 2. 재귀함수의 구조

- `sum_func1()`**과** `sum_func2()`**는 무슨 차이가 있을까요?**
    
    ```python
    def sum_func1(n):
    	if n == 1:
    		return 1
    	return sum_func1(n - 1) + n
    
    def sum_func2(n):
    	return sum_func2(n - 1) + n
    ```
    

- **Base Case(기본 케이스)와 Recursive Case(재귀 케이스)**
    - Base Case: 재귀 함수를 종료하는 부분
    - Recursive Case: 자기 자신을 호출 하는 부분

- **재귀함수의 구조를 이해하고 1부터 n까지의 합을 구하는 함수 만들기**
    - `Python`
        
        ```python
        def sum_func(n):
        	# Base Case
        	if n == 1:
        		return 1
        
        	# Recursive Case
        	return sum_func(n-1) + n
        ```