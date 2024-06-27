import argparse
import os

def main(args):
  print(args)

def parse_args():
  argparse.ArgumentParser(
	  prog="MyProg",
	  description="Some description"
  )
  parser.add_argument('filename')
  parser.add_argument('--count')
  parser.add_argument('--enable', action='store_true')
  return parser.parse_args()

if __name__ == "__main__":
  args = parse_args()
  main(args)
