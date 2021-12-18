#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
# modules to import
#
import argparse

#
# user functions
#

def nb2fr(n):
  """Displays a number in French format.

  Keyword argument:
  n -- float: number to format
  """
  return str(n).replace('.', ',')

# main function
def main(price, discount):
  """Returns the discounted price of an item.

  Keywords arguments:
  price -- int: initial price of an item
  discount -- int: reduction rate
  """
  result = price - (price * (discount / 100))

  print(f"Le prix soldé est de { nb2fr(result) } €")

#
# main procedure
#
if __name__ == "__main__":

  # parse arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("-p", "--price", type=int,
    help="price of the item")
  parser.add_argument("-d", "--discount", type=int,
    help="discount to apply in percentage")
  args = parser.parse_args()

  #
  # program
  #
  main(args.price, args.discount)
