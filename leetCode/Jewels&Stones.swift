//
//  Jewels&Stones.swift
//  
//
//  Created by Mohamed on 4/8/18.
//

import Foundation

let J = "aA"
let S: String = "aAAbbbb"

var sum :Int = J.reduce(0) { result, char in
    let filtered = (S.filter{ $0 == char })
    return result + filtered.count
}
