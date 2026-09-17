# Type checks - Objects

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Functions to test for 'object'-related properties:

- `has_class()`: checks if `x` has a "class" attribute.

- `has_object_bit()`: checks if `x` has the "object" bit set, identical
  to [is.object](https://rdrr.io/r/base/is.object.html).

- `has_s4_bit()`: checks if `x` has the "S4" bit set, identical to
  [isS4](https://rdrr.io/r/base/isS4.html).

- `is_s4()`: checks if `x` is of type "S4".

- `is_object()`: checks if `x` is of type "object".

- `is_object_like()`: checks if object has the "object" bit, while
  testing for inconsistencies with the other properties above (see
  'Details' below).

## Usage

``` r
has_object_bit()

has_s4_bit()

has_class(x, invalid = "warn", bad = "warn")

is_object_like(x, bad = "warn")

is_s4(x)

is_object(x)
```

## Arguments

- x:

  \[`any`\] An object to test.

- invalid:

  \[`"warn"` \| `"false"`\] How to handle `NA` or `""` values in the
  class attribute: `"warn"` to issue a warning and return `TRUE`;
  `"false"` to return `FALSE`.

- bad:

  \[`"warn"` \| `"false"`\] How to handle inconsistencies in
  `is_object_like()`: `"warn"` to issue a warning and return if `x` has
  a class attribute; `"false"` to return `FALSE`.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Details

The relationship between the object-related properties is as follows:

- *class* \<-\> *object bit*

- *s4 bit* -\> *class*/*object bit* (ideally)

- *s4 typeof* -\> *s4 bit*, and -\> *class/object bit* (ideally)

- *object typeof* -\> *class*/*object bit* (ideally)

`is_object_like()` tests if any of the above are violated.

## Examples

``` r
xbase <- 1:10
xs3 <- structure(1:10, class = "my_s3")
xs4_int <- methods::setClass("my_s4_int", contains = "integer")(1:10)
xs4_s4 <- methods::setClass("my_s4_s4", slots = c(x = "integer"))(x = 1:10)

# If has class, should have the object bit set, and vice versa:
has_class(xbase) #> FALSE
#> [1] FALSE
has_class(xs3) #> TRUE
#> [1] TRUE
has_object_bit(xs3) #> TRUE
#> [1] TRUE
has_class(xs4_int) #> TRUE
#> [1] TRUE

# S4 objects have the S4 bit set:
has_s4_bit(xs3) #> FALSE
#> [1] FALSE
has_s4_bit(xs4_int) #> TRUE
#> [1] TRUE

# is_s4 test for the typeof() "S4":
typeof(xs4_int) #> "integer"
#> [1] "integer"
is_s4(xs4_int) #> FALSE
#> [1] FALSE
typeof(xs4_s4) #> "S4"
#> [1] "S4"
is_s4(xs4_s4) #> TRUE
#> [1] TRUE

# is_object() test for the typeof() "object", which some OOP systems use,
# and also when an S4 object has its class modified:
suppressWarnings(class(xs4_s4) <- c("new_class", class(xs4_s4)))
typeof(xs4_s4) #> "object"
#> [1] "object"
is_object(xs4_s4) #> TRUE
#> [1] TRUE

# is_object_like() is similar to checking the object bit/existence of a class
# attribute, while cheking for inconsistencies with the other properties:
is_object_like(xbase) #> FALSE
#> [1] FALSE
is_object_like(xs4_int) #> TRUE
#> [1] TRUE

attr(xs4_int, "class") <- NULL
has_s4_bit(xs4_int) #> TRUE (S4 bit is still set)
#> [1] TRUE
is_object_like(xs4_int, bad = FALSE) #> FALSE
#> [1] FALSE

# has_class() is similar, but also checks for NA, "", or duplicate values in
# the class attribute:
class(xs3) <- c("a", "b", "a")
has_class(xs3, invalid = "false") #> FALSE
#> [1] FALSE
```

## On this page

Functions to test for 'object'-related properties:

- `has_class()`: checks if `x` has a "class" attribute.

- `has_object_bit()`: checks if `x` has the "object" bit set, identical
  to [is.object](https://rdrr.io/r/base/is.object.html).

- `has_s4_bit()`: checks if `x` has the "S4" bit set, identical to
  [isS4](https://rdrr.io/r/base/isS4.html).

- `is_s4()`: checks if `x` is of type "S4".

- `is_object()`: checks if `x` is of type "object".

- `is_object_like()`: checks if object has the "object" bit, while
  testing for inconsistencies with the other properties above (see
  'Details' below).

## Usage

``` r
has_object_bit()

has_s4_bit()

has_class(x, invalid = "warn", bad = "warn")

is_object_like(x, bad = "warn")

is_s4(x)

is_object(x)
```

## Arguments

- x:

  \[`any`\] An object to test.

- invalid:

  \[`"warn"` \| `"false"`\] How to handle `NA` or `""` values in the
  class attribute: `"warn"` to issue a warning and return `TRUE`;
  `"false"` to return `FALSE`.

- bad:

  \[`"warn"` \| `"false"`\] How to handle inconsistencies in
  `is_object_like()`: `"warn"` to issue a warning and return if `x` has
  a class attribute; `"false"` to return `FALSE`.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Details

The relationship between the object-related properties is as follows:

- *class* \<-\> *object bit*

- *s4 bit* -\> *class*/*object bit* (ideally)

- *s4 typeof* -\> *s4 bit*, and -\> *class/object bit* (ideally)

- *object typeof* -\> *class*/*object bit* (ideally)

`is_object_like()` tests if any of the above are violated.

## Examples

``` r
xbase <- 1:10
xs3 <- structure(1:10, class = "my_s3")
xs4_int <- methods::setClass("my_s4_int", contains = "integer")(1:10)
xs4_s4 <- methods::setClass("my_s4_s4", slots = c(x = "integer"))(x = 1:10)

# If has class, should have the object bit set, and vice versa:
has_class(xbase) #> FALSE
#> [1] FALSE
has_class(xs3) #> TRUE
#> [1] TRUE
has_object_bit(xs3) #> TRUE
#> [1] TRUE
has_class(xs4_int) #> TRUE
#> [1] TRUE

# S4 objects have the S4 bit set:
has_s4_bit(xs3) #> FALSE
#> [1] FALSE
has_s4_bit(xs4_int) #> TRUE
#> [1] TRUE

# is_s4 test for the typeof() "S4":
typeof(xs4_int) #> "integer"
#> [1] "integer"
is_s4(xs4_int) #> FALSE
#> [1] FALSE
typeof(xs4_s4) #> "S4"
#> [1] "S4"
is_s4(xs4_s4) #> TRUE
#> [1] TRUE

# is_object() test for the typeof() "object", which some OOP systems use,
# and also when an S4 object has its class modified:
suppressWarnings(class(xs4_s4) <- c("new_class", class(xs4_s4)))
typeof(xs4_s4) #> "object"
#> [1] "object"
is_object(xs4_s4) #> TRUE
#> [1] TRUE

# is_object_like() is similar to checking the object bit/existence of a class
# attribute, while cheking for inconsistencies with the other properties:
is_object_like(xbase) #> FALSE
#> [1] FALSE
is_object_like(xs4_int) #> TRUE
#> [1] TRUE

attr(xs4_int, "class") <- NULL
has_s4_bit(xs4_int) #> TRUE (S4 bit is still set)
#> [1] TRUE
is_object_like(xs4_int, bad = FALSE) #> FALSE
#> [1] FALSE

# has_class() is similar, but also checks for NA, "", or duplicate values in
# the class attribute:
class(xs3) <- c("a", "b", "a")
has_class(xs3, invalid = "false") #> FALSE
#> [1] FALSE
```
