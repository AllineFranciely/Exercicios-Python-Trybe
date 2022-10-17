#! /usr/bin/env python3

def media(numbers):
  total = 0
  for number in numbers:
    total += number
  return total / len(numbers)
