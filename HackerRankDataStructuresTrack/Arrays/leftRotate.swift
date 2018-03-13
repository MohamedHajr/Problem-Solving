//
//  main.swift
//  HackerRank Playground project
//
//  Created by Mohamed on 2/27/18.
//  Copyright © 2018 MohamedHajr. All rights reserved.
//

import Foundation

var instructions = readLine()!.components(separatedBy: " ").map{ Int($0)! }
var arr = readLine()!.components(separatedBy: " ").map{ Int($0)! }

func rotate(array: [Int], numberOfRotations: Int) -> [Int] {
    let length = array.count

    if numberOfRotations == 0 || length <= 1 {
        return array // The resulting array is similar to the input array
    }
    
    let rotations: Int = (length + numberOfRotations % length) % length
    let indicator = length - rotations
    
    let reversed: Array = array.reversed()
    let leftPart: Array = reversed[0..<indicator].reversed()
    let rightPart: Array = reversed[indicator..<length].reversed()
    
    return leftPart + rightPart
}


let arrayAfterRotation = rotate(array: arr, numberOfRotations: instructions[1])


for number in arrayAfterRotation {
    print(number, separator: " ", terminator: " ")
}


