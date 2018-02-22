//
//  MergeSort.swift
//  
//
//  Created by Mohamed on 2/9/18.
//

//Implementing Merge Sort For Array of Integers

func mergeSortDatArray(array : [Int]) -> [Int] {
    if array.count < 2 {
        return array
    } else {
        let splitIndex = array.count / 2
        let firstArray = mergeSortDatArray(array: Array(array[..<splitIndex]))
        let secondArray = mergeSortDatArray(array: Array(array[splitIndex...]))
        return merge(firstArray: firstArray, secondArray: secondArray, finalArray: [])
    }
}

func merge(firstArray: [Int], secondArray: [Int], finalArray: [Int]) -> [Int] {
    
    if firstArray.count == 0  {
        return finalArray + secondArray
    }
    else if secondArray.count == 0 {
        return finalArray + firstArray
    }
    
    var newArray = finalArray
    if firstArray.first! > secondArray.first! {
        newArray.append(secondArray.first!)
        return merge(firstArray: firstArray, secondArray: Array(secondArray.dropFirst()), finalArray: newArray)
    } else {
        newArray.append(firstArray.first!)
        return merge(firstArray: Array(firstArray.dropFirst()), secondArray: secondArray, finalArray: newArray)
    }
}

//Tests
let testArray = [2,10,8,4,1,5,5,5,3,7]
mergeSortDatArray(array: testArray)

let firstArray = [7,8,9]
let secondArray = [3,5,8]
merge(firstArray: firstArray, secondArray: secondArray, finalArray: [])
