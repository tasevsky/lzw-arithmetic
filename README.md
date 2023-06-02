# Usage:

# LZW 

## LZW Encoder:
  
  ```lzw.py [-h] encode --mapping <mapping-dict> --word <word>```
  
  ### Example:

```python lzw.py encode --mapping "{\"/\": 1, \"H\": 2, \"I\": 3, \"S\": 4, \"T\": 5}" --word /THIS/IS/HIS/IS/```
  
  ### Output:

```[1, 5, 2, 3, 4, 1, 9, 1, 8, 10, 12]```

## LZW Decoder
  
  ```lzw.py [-h] decode --mapping <mapping-dict> --code <code>```
  
  ### Example:

```python lzw.py decode --mapping "{\"A\": 1, \"B\": 2, \"C\": 3, \"AB\": 4, \"BA\": 5, \"AC\": 6, \"CA\": 7, \"BC\": 8}" --code 1 2 3 4 5 6 7 8```
  
  ### Output:
  
  ```ABCABBAACCABC```

# Arithmetic coding

## Arithmetic encoder:

  ```arithmetic.py [-h] encode --mapping <mapping-dict> --word <word>```

  ### Example:

```python arithmetic.py encode --mapping "{\"u\": [0.0, 0.3],\"l\": [0.3, 0.6],\"t\": [0.6,0.8],\"m\": [0.8,0.9],\"i\": [0.9,1]}" --word multi```

 ### Output:

``` [0.81602, 0.8161999999999999]```


## Arithmetic decoder
  
  ```lzw.py [-h] decode --mapping <mapping-dict> --value <value> --input_length <word_length>```

   ### Example:

```python arithmetic.py decode --mapping "{\"u\": [0.0, 0.3],\"l\": [0.3, 0.6],\"t\": [0.6,0.8],\"m\": [0.8,0.9],\"i\": [0.9,1]}" --value 0.816028 --input-length 5```

  ### Output:

```multi```