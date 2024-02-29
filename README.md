# wc_tool

This is my attempt to build my own unix command line wc

Here's the task:

https://codingchallenges.fyi/challenges/challenge-wc


## Description
wc tool runs different statistics on a file such as word count, byte count, char count and etc.


## Usage
if unsure on how to run the function
```commandline
usage: ccwc.py [-h] [-c] [-l] [-w] [-m] [file]

wc tool

positional arguments:
  file

optional arguments:
  -h, --help  show this help message and exit
  -c          gets the byte count
  -l          outputs number of lines in file
  -w          outputs number of words in files
  -m          outputs number of characters in files

```

## Examples

```commandline
python3 ccwc.py -l test.txt
```

```commandline
cat test.txt | ccwc.py -l
```

## unit testing

Unit testing were used to test the different functions to make sure each values return the correct values. These can be found in

***wc_tool.py***

To run the file, run this in the terminal:

```python -m unittest test_wc_tool.py```


Next steps:

add setup.py so that i wouldn't need to explicitly use python / python3 to receive the output.