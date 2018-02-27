var arr: [[Int]] = []

for _ in 0...5  {
    let subArray = readLine()!.components(separatedBy: " ").map{ Int($0)! }
    arr.append(subArray)
}

func calculateLargestSum(hourglassesArray: [[Int]]) -> Int {
    
    var result = -50
    
    for  i  in 0..<hourglassesArray.count - 2 {
        for j in 0..<hourglassesArray[i].count - 2 {
            
            let sum = hourglassesArray[i][j] + hourglassesArray[i][j+1] + hourglassesArray[i][j + 2] +
                hourglassesArray[i + 1][j + 1] +
                hourglassesArray[i + 2][j] + hourglassesArray[i + 2][j+1] + hourglassesArray[i + 2][j + 2]
            if sum > result { result = sum }
        }
    }
    
    return result
}

print(calculateLargestSum(hourglassesArray: arr))
