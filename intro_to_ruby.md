# Introduction to Ruby
This document provides a brief introduction to the Ruby programming language. Whether you are new to programming or experienced in other languages, this guide will help you understand the basic concepts of Ruby. Ruby is a high-level, interpreted programming language. It was designed and developed in the mid-1990s by Yukihiro "Matz" Matsumoto in Japan.

## Table of Contents
- [Variables](#variables)
- [Numbers](#numbers)
- [Strings](#strings)
- [Arrays](#arrays)
- [Hashes](#hashes)
- [Control Flow](#control-flow)
- [Methods](#methods)
- [Classes](#classes)

## Getting Started

To get started with Ruby, you'll need to install it on your computer. You can find instructions for installing Ruby on various operating systems [here](https://www.ruby-lang.org/en/documentation/installation/)

Once you have Ruby installed, you can run Ruby code by typing `ruby` followed by the name of the file containing your code. For example, if your code is in a file named `hello.rb`, you would type `ruby hello.rb` to run it.

## Basic Syntax

Here's an example of some basic Ruby code:

```ruby
puts "Hello, world!"
```

This code uses the `puts` method to print the string `"Hello, world!"` to the screen.

## Variables
In Ruby, variables are used to store and manipulate data. They are dynamically typed, meaning you don't need to explicitly declare their type. To assign a value to a variable, use the assignment operator `=`.

In Ruby, you can store values in variables. Here's an example:

```ruby
name = "Alice"
age = 30
```

In this example, we're storing the string `"Alice"` in a variable named `name`, and the integer `30` in a variable named `age`.

Ruby has several built-in data types, including:

- Strings (e.g. `"Hello"`)
- Integers (e.g. `42`)
- Floats (e.g. `3.14`)
- Booleans (e.g. `true` and `false`)
- Arrays (e.g. `[1, 2, 3]`)
- Hashes (e.g. `{ "key" => "value" }`)

## Numbers
Ruby supports various numeric data types, including integers and floating-point numbers. You can perform arithmetic operations on numbers using operators like +, -, *, and /.

```ruby
count = 10
price = 3.99
total = count * price
```

## Strings

In Ruby, strings are objects that represent sequences of characters. You can create a string by enclosing characters in single or double quotes:

```ruby
my_string = "Hello, world!"
```

Ruby provides many methods for working with strings. Here are some common ones:

- length: returns the length of a string
- upcase: returns a new string with all the characters in uppercase
- downcase: returns a new string with all the characters in lowercase
- capitalize: returns a new string with the first character capitalized and the rest in lowercase
- reverse: returns a new string with the characters in reverse order
- strip - Removes leading and trailing whitespace from the string.

Here’s an example that uses some of these methods:

```ruby
my_string = "Hello, world!"

puts my_string.length      # 13
puts my_string.upcase      # HELLO, WORLD!
puts my_string.downcase    # hello, world!
puts my_string.capitalize  # Hello, world!
puts my_string.reverse     # !dlrow ,olleH
```

You can find more information about Ruby’s string methods in the [Ruby Documentation](https://ruby-doc.org/core-2.7.0/String.html).

## Arrays
Arrays are ordered collections of objects in Ruby. They can contain elements of any type, and you can access elements using their index.

```ruby
numbers = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Charlie']
mixed = [1, 'two', :three]
```

Here are some common array operations and methods in Ruby:
- Creating an Array:
    ```ruby
    my_array = []                 # Empty array
    my_array = [1, 2, 3]          # Array with initial values
    ```
- Accessing Elements:
    ```ruby
    my_array[0]                   # Access element at index 0
    my_array.first                # Get the first element
    my_array.last                 # Get the last element
    ```

- Modifying Elements:
    ```ruby
    my_array[1] = 10              # Modify element at index 1
    my_array.push(4)              # Add element at the end
    my_array << 5                 # Shorthand for adding an element at the end
    ```
- Array Size & Manipulation:
    ```ruby
    my_array.length               # Get the length of the array
    my_array.size                 # Alternative method to get the size
    my_array.empty?               # Check if the array is empty
    my_array.pop                  # Remove and return the last element
    my_array.shift                # Remove and return the first element
    my_array.concat([6, 7])       # Concatenate arrays
    my_array.reverse!             # Reverse the order of elements in place
    ```

- Iterating over an Array:
    ```ruby
    my_array.each do |element|
    # Do something with each element
    end
    ```

For more information and a comprehensive list of array methods in Ruby, you can refer to the official [Ruby Array Doc](https://ruby-doc.org/core-3.0.3/Array.html)
## Hashes
Hashes in Ruby are key-value pairs, similar to dictionaries in other languages. Each key in a hash is associated with a value. To create a hash, use curly braces {} and separate the key-value pairs with colons :.

```ruby
person = {
  name: "John",
  age: 25,
  city: "New York"
}
```

## Control Flow

Ruby has several control structures that allow you to control the flow of your program. These include:

- `if` statements
- `while` loops
- `for` loops
- `each` loops

Here's an example that uses an `if` statement:

```ruby
x = 5

if x > 0
  puts "x is positive"
else
  puts "x is not positive"
end
```
In this example, we're using an `if` statement to check if the value of `x` is greater than 0. If it is, we print `"x is positive"` to the screen. Otherwise, we print `"x is not positive"`.

