//
//  TwoSum.swift
//  
//
//  Created by Mohamed on 4/8/18.
//

import Foundation

func twoSum (nums: [Int], target: Int) -> [Int] {
    var dic = [Int: Int]()
    
    for i in 0...(nums.count - 1) {
        let complement = target - nums[i]
        if let hasIt = dic[complement] {
            return [hasIt, i]
        }
        dic[nums[i]] = i
    }
    return []
}

var arr = [5,7,6,3]
let target = 9
twoSum(nums: arr, target: target)
