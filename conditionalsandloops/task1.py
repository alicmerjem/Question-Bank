"""
Write a program using a loop to get 
the following output. The output should
be formatted the same way as below
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
"""

rows = 6

for i in range(rows):
    # printing spaces first
    print(" " * i, end="")

    # printing stars
    print("* " * (rows-i))
