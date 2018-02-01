//
//  RecursiveFactorial.swift
//  
//
//  Created by Mohamed on 2/1/18.
//


//Factorial for non negative numbers and 0

func factorial (accumlator: Int, number: Int) -> Int {
    return number == 1 ?  accumlator :  factorial(accumlator: accumlator * number ,number: number - 1)
}

factorial(accumlator: 1, number: 5)

