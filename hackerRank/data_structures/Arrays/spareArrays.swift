//
//  main.swift
//  HackerRank Playground project
//
//  Created by Mohamed on 2/27/18.
//  Copyright © 2018 MohamedHajr. All rights reserved.
//


import Foundation

guard let N = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
    else { fatalError("Bad input") }

var strings: [String] =  []

for _ in 0..<N {
    guard let stringTemp = readLine() else { fatalError("Bad input") }
    strings.append(stringTemp)
}

guard strings.count == N else { fatalError("Bad input") }

guard let Q = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
    else { fatalError("Bad input") }

var queries: [String] = []

for _ in 0..<Q{
    guard let queriyTemp = readLine() else { fatalError("Bad input") }
    queries.append(queriyTemp)
}

guard queries.count == Q else { fatalError("Bad input") }

func findMultipleOccurences(strings : [String], quires: [String]) {
    for query in quires {
        print(strings.reduce(0, { (result: Int, string: String) in  string == query ? result + 1 : result} ))
    }
}

findMultipleOccurences(strings: strings, quires: queries)


