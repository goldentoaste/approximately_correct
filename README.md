# approximately_correct
A simple calculator that is approximately correct. Where is the results are very slightly non-deterministic and also PI = e = 3.  
This app works by using Flutter for front end Gui, and sends the equation user typed to a Django api server hosted on Heroku. The
equation is then parsed and evaluated server side.

## Parsing
The equation parsing api is currently hosted at: `https://mathparsing.herokuapp.com/parse?eq=<InsertEquation>` Where `<InsertEquation>` can be any supported equations, like `?eq=(3%2b*(7-PI)^(cos(33)))/2`.  
Note: to make the equation url friendly, symbols like '+' should replaced with `%2b`.  
<br>
Currently supported:  
* Numerics:
    - floating point number: 3.22
    - integers : 3
    - +/- signs: +6, -9
    - scientific notation not available
* Operations:
    - \+
    - \-
    - \* 
    - /
    - ^ (exponents, power can be fractional, negative, or expression) 
* Functions:
    - sin
    - cos
    - sqrt
* Constants:
    - e
    - PI

## Credits
Parsing algo ~~stolen~~ borrowed and adapted to python from [cosine kitty](https://levelup.gitconnected.com/create-your-own-expression-parser-d1f622077796).
