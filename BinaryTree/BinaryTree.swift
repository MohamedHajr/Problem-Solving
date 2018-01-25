//
//  BinaryTree.swift
//  
//
//  Created by Mohamed on 1/25/18.
//

import Foundation

func guessNumberUsingBinaryTree(start : Int, limit: Int, pickedNumber: Int) -> Int {
    var min = start
    var max = limit
    let average : Int =  (min + max) / 2
    
    
    if average > pickedNumber  {
        max = average - 1
        
        return guessNumberUsingBinaryTree(start: min, limit: max, pickedNumber: pickedNumber)
    }
    else if average < pickedNumber {
        min = average + 1
        
        return guessNumberUsingBinaryTree(start: min, limit : max,  pickedNumber : pickedNumber)
    } else {
        return pickedNumber
    }
}


func searchArrayForDesiredNumber(start : Int, limit: Int, desiredNumber: Int, array: [Int]) -> Int {
    var min = start
    var max = limit
    let average : Int =  (min + max) / 2
    
    
    if array[average] > desiredNumber  {
        max = average - 1
        
        return searchArrayForDesiredNumber(start: min, limit: max, desiredNumber: desiredNumber, array:  array)
    }
    else if array[average] < desiredNumber {
        min = average + 1
        
        return searchArrayForDesiredNumber(start: min, limit : max,  desiredNumber : desiredNumber, array: array)
    } else {
        return average
    }
}

let primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

//test example
searchArrayForDesiredNumber(start: 0, limit: (primes.count - 1), desiredNumber: 67, array: primes)
