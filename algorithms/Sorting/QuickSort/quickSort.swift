//
//  quickSort.swift
//  
//
//  Created by Mohamed on 2/23/18.
//
//  Implementing Quick Sort

//  Swap 2 elements in an array Function
func swap(array: [Int], firstIndex: Int, secondIndex: Int) -> [Int] {
    let firstValue = array[firstIndex]
    let secondValue = array[secondIndex]
    
    var newArray = array
    newArray[firstIndex] = secondValue
    newArray[secondIndex] = firstValue
    return newArray
}

//  Partitining a sub array and sorting it using a the right most element as a pivot
func partitioning(array: [Int], smallerGroupEndIndex: Int, iterator: Int) -> [Int] {
    let pivot = array.last!
    
    if iterator == (array.count - 1) {
        return swap(array: array, firstIndex: array.index(of: pivot)!, secondIndex: smallerGroupEndIndex)
    }
    if pivot < array[iterator] {
        return partitioning(array: array, smallerGroupEndIndex: smallerGroupEndIndex, iterator: (iterator + 1))
    } else {
        let newArray = swap(array: array, firstIndex: iterator, secondIndex: smallerGroupEndIndex)
        return partitioning(array: newArray, smallerGroupEndIndex: (smallerGroupEndIndex + 1), iterator: (iterator + 1))
    }
}

func quickSortDatArray(array : [Int]) -> [Int] {
    
    if array.count > 2 {
        
    }
    
    return array
}


var array = [4,3,11,15,12,5,9,1,7]

partitioning(array: array, smallerGroupEndIndex: 0, iterator: 0)
