# price list and item codes
+--------------|--------------|---------+
| Product Code |     Name     |  Price  |
+--------------|--------------|---------+
|     CH1      |   Chai       |  $3.11  |
|     AP1      |   Apples     |  $6.00  |
|     CF1      |   Coffee     | $11.23  |
|     MK1      |   Milk       |  $4.75  |
|     OM1      |   Oatmeal    |  $3.69  |
+--------------|--------------|---------+


# RUNNING
Pass cart items as command line inputs. final price of cart value after discounts is printed on screen
`./run.sh MK1`
like this 
`./run.sh CH1 AP1 CF1 MK1 AP1 AP1 AP1`

# RUN TESTS
`docker run --rm -it -v $(pwd)/challange:/challange -v $(pwd)/tests.py:/tests.py python:3 python -m unittest tests`

