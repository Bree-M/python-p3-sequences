#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []

    if length == 0:
      print(fib_sequence)
      return
   
    fib_sequence.append(0)

    if length > 1:
      fib_sequence.append(1)

    while len(fib_sequence) < length:
         next_number = fib_sequence[-1] + fib_sequence[-2]
         fib_sequence.append(next_number)


    print(fib_sequence)
      