//
//  Palindrome.swift
//  
//
//  Created by Mohamed on 2/1/18.
//

//Checking if a given string is Palindrome or not

func isPalindrome(string: String) -> Bool {
    return string.count <= 1 ? true : string.first == string.last  ? isPalindrome(string: String(string.dropFirst().dropLast())) : false
}

isPalindrome(string: "madam")

