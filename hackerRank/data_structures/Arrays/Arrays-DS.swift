// number of elements
let n = Int(readLine()!)!

// read array
let arr = readLine()!.components(separatedBy: " ").map{ Int($0)! }

// iterate over the array in reverse order and print the elements separated by space

func printArrayReversed (array: [Int]) {
    if(array.count > 0) {
        print(array.last!, terminator:" ")
        printArrayReversed(array: Array(array.dropLast()))
    }
}

printArrayReversed(array: arr)
