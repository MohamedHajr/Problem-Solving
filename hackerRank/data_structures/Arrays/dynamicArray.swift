//
//  main.swift
//  HackerRank Playground project
//
//  Created by Mohamed on 2/27/18.
//  Copyright © 2018 MohamedHajr. All rights reserved.
//

import Foundation

var arr = readLine()!.components(separatedBy: " ").map{ Int($0)! }


var sequneces = [[Int]](repeating: [], count: arr[0])
var lastAnswer = 0

func findIndex (x: Int, lastAnswer: Int = 0, N: Int) -> Int {
    return (x ^ lastAnswer) % N
}

func appendToSeq(index: Int, value: Int) {
    sequneces[index].append(value)
}


for _ in 0...(arr[1] - 1) {
    let subArray = readLine()!.components(separatedBy: " ").map{ Int($0)! }
    if subArray[0] == 1 {
        appendToSeq(index: findIndex(x: subArray[1], lastAnswer: lastAnswer, N: arr[0]), value: subArray[2])
    } else {
        let index = findIndex(x: subArray[1], lastAnswer: lastAnswer, N: arr[0])
        lastAnswer = sequneces[index][subArray[2] % sequneces[index].count]
        print(lastAnswer)
    }
}







