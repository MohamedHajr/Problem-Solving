//
//  InsertionSort.swift
//  
//
//  Created by Mohamed on 1/31/18.
//


func doInsertionSortOnArrayOfInts (array: [Int]) -> [Int]  {
    return array.reduce(array, {  insert(keyValue: $1, keyIndex: array.index(of: $1)!, array: $0) })
}


func insert(keyValue: Int, keyIndex: Int, array: [Int]) -> [Int]{
    
    var newArray = array
    
    if(keyIndex == 0) {
        newArray[keyIndex] = keyValue
        return newArray
    }
    
    let previousValue = array[keyIndex - 1]
    
    if(keyValue <  previousValue) {
        newArray[keyIndex] = previousValue
        return insert(keyValue: keyValue, keyIndex: keyIndex - 1, array: newArray)
    } else {
        newArray[keyIndex] = keyValue
        return newArray
    }
}


doInsertionSortOnArrayOfInts(array: [8,7,6,5,3,2,1])

