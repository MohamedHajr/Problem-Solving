//
//  File.swift
//  
//
//  Created by Mohamed on 1/30/18.
//

func swap(firstIndex: Int, secondIndex: Int, array: [Int]) -> [Int] {
    let firstValue = array[firstIndex]
    let secondValue = array[secondIndex]
    
    var newArray = array
    newArray[firstIndex] = secondValue
    newArray[secondIndex] = firstValue
    
    return newArray
}

func getMinValueIndex(startIndex: Int, array: [Int]) -> Int {
    let subArray = array[startIndex...]
    let minIndex = subArray.enumerated().reduce(startIndex, { subArray[$0] > $1.element ? subArray.index(of: $1.element)! : $0 })
    return minIndex
}



func doSelectionSort(startIndex: Int, array: [Int]) -> [Int] {
    if  startIndex == (array.count) {
        return array
    }
    let minIndex = getMinValueIndex(startIndex: startIndex, array: array)
    let arrayAfterSwap = swap(firstIndex: startIndex, secondIndex: minIndex, array: array)
    return doSelectionSort(startIndex: startIndex + 1, array: arrayAfterSwap)
}

doSelectionSort(startIndex: 0, array:  [2,3,10,3,7,5,6,1,0,0])
