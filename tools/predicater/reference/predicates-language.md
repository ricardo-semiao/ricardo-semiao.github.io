# Type checks - Language objects

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

In R, there are three building blocks that compose the language itself:

- Syntactic literals: numbers, strings, and other literal values, e.g.
  `1.0`, `NULL`, etc. They can have many types
  ([`typeof()`](https://rdrr.io/r/base/typeof.html)).

- Symbols: variable names, e.g. `x`, `sum`, etc. They are of type
  `"symbol"` (SYMSXP).

- Function calls: `sum(1, 2)`, `1 + 2`, `if (TRUE) 1 else 2`, etc. They
  are of type `"language"` (LANGSXP).

For testing these building blocks, there are the following predicates:

- Syntactic literals:
  [`rlang::is_syntactic_literal()`](https://rlang.r-lib.org/reference/is_expression.html).

- Symbols: `is_symbol2` (based on
  [`rlang::is_symbol()`](https://rlang.r-lib.org/reference/is_symbol.html)).

- Function calls: `is_language()`. Also consider
  [`rlang::is_call()`](https://rlang.r-lib.org/reference/is_call.html)
  for testing the name, namespace, and number of arguments of a call.

- Expressions vector: R has an additional type, `"expression"`, which is
  a list of elements from any of the three building blocks above. It can
  be tested with `is_expression2()`.

- Any of the above: `is_code()`.

## Usage

``` r
is_syntactic_literal(x)

is_symbol2(x, name = NULL, valid = FALSE, empty = TRUE)

is_language(x, valid = FALSE)

is_call(x, name = NULL, n = NULL, ns = NULL)

is_expression2(x, n = NULL, valid = FALSE)

is_code(
  x,
  sym = TRUE,
  lang = TRUE,
  literal = TRUE,
  valid = FALSE,
  empty = TRUE
)
```

## Arguments

- x:

  \[`any`\] An object to test.

- name:

  \[`character(1)` \| `NULL`\] An optional name or vector of names that
  the symbol or call should match. Set to `NULL` to not test.

- valid:

  \[`TRUE` \| `FALSE`\] Whether to test if the code is 'valid', i.e. can
  be [`parse()`](https://rdrr.io/r/base/parse.html)'d, or is a syntactic
  symbol.

- empty:

  \[`TRUE` \| `FALSE`\] Whether to allow the empty symbol.

- n:

  \[`integer(1)` \| `NULL`\] Number of elements in the expression vector
  or arguments in the call, set to `NULL` to not test.

- ns:

  \[`character(1)` \| `NULL`\] Namespace of the call, set to `NULL` to
  not test.

- sym, lang, literal:

  \[`TRUE` \| `FALSE`\] Whether to allow symbols, language objects, or
  syntactic literals.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Examples

``` r
is_syntactic_literal(1) #> TRUE
#> [1] TRUE
is_syntactic_literal("a") #> TRUE
#> [1] TRUE
is_syntactic_literal(NULL) #> TRUE
#> [1] TRUE

is_symbol2(quote(x)) #> TRUE
#> [1] TRUE
is_symbol2(quote(x), name = "y") #> FALSE
#> [1] FALSE
is_symbol2(rlang::expr(), empty = FALSE) #> FALSE
#> [1] FALSE

is_language(quote(x + 1)) #> TRUE
#> [1] TRUE
is_language(quote(f(x))) #> TRUE
#> [1] TRUE
is_language(quote(if (TRUE) 1 else 2)) #> TRUE
#> [1] TRUE
# See ?rlang::is_call() for is_call() examples

is_expression2(expression(1, x, x + 1)) #> TRUE
#> [1] TRUE
is_expression2(rlang::exprs(1, x, x + 1)) #> FALSE (exprs generates a list)
#> [1] FALSE

x <- 1
is_code(x) #> TRUE
#> [1] TRUE
# Identical to is_syntactic_literal(x) || is_symbol2(x) || is_language(x)

is_code(x, literal = FALSE) #> FALSE
#> [1] FALSE
# Identical to is_symbol2(x) || is_language(x)
```

## On this page

In R, there are three building blocks that compose the language itself:

- Syntactic literals: numbers, strings, and other literal values, e.g.
  `1.0`, `NULL`, etc. They can have many types
  ([`typeof()`](https://rdrr.io/r/base/typeof.html)).

- Symbols: variable names, e.g. `x`, `sum`, etc. They are of type
  `"symbol"` (SYMSXP).

- Function calls: `sum(1, 2)`, `1 + 2`, `if (TRUE) 1 else 2`, etc. They
  are of type `"language"` (LANGSXP).

For testing these building blocks, there are the following predicates:

- Syntactic literals:
  [`rlang::is_syntactic_literal()`](https://rlang.r-lib.org/reference/is_expression.html).

- Symbols: `is_symbol2` (based on
  [`rlang::is_symbol()`](https://rlang.r-lib.org/reference/is_symbol.html)).

- Function calls: `is_language()`. Also consider
  [`rlang::is_call()`](https://rlang.r-lib.org/reference/is_call.html)
  for testing the name, namespace, and number of arguments of a call.

- Expressions vector: R has an additional type, `"expression"`, which is
  a list of elements from any of the three building blocks above. It can
  be tested with `is_expression2()`.

- Any of the above: `is_code()`.

## Usage

``` r
is_syntactic_literal(x)

is_symbol2(x, name = NULL, valid = FALSE, empty = TRUE)

is_language(x, valid = FALSE)

is_call(x, name = NULL, n = NULL, ns = NULL)

is_expression2(x, n = NULL, valid = FALSE)

is_code(
  x,
  sym = TRUE,
  lang = TRUE,
  literal = TRUE,
  valid = FALSE,
  empty = TRUE
)
```

## Arguments

- x:

  \[`any`\] An object to test.

- name:

  \[`character(1)` \| `NULL`\] An optional name or vector of names that
  the symbol or call should match. Set to `NULL` to not test.

- valid:

  \[`TRUE` \| `FALSE`\] Whether to test if the code is 'valid', i.e. can
  be [`parse()`](https://rdrr.io/r/base/parse.html)'d, or is a syntactic
  symbol.

- empty:

  \[`TRUE` \| `FALSE`\] Whether to allow the empty symbol.

- n:

  \[`integer(1)` \| `NULL`\] Number of elements in the expression vector
  or arguments in the call, set to `NULL` to not test.

- ns:

  \[`character(1)` \| `NULL`\] Namespace of the call, set to `NULL` to
  not test.

- sym, lang, literal:

  \[`TRUE` \| `FALSE`\] Whether to allow symbols, language objects, or
  syntactic literals.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Examples

``` r
is_syntactic_literal(1) #> TRUE
#> [1] TRUE
is_syntactic_literal("a") #> TRUE
#> [1] TRUE
is_syntactic_literal(NULL) #> TRUE
#> [1] TRUE

is_symbol2(quote(x)) #> TRUE
#> [1] TRUE
is_symbol2(quote(x), name = "y") #> FALSE
#> [1] FALSE
is_symbol2(rlang::expr(), empty = FALSE) #> FALSE
#> [1] FALSE

is_language(quote(x + 1)) #> TRUE
#> [1] TRUE
is_language(quote(f(x))) #> TRUE
#> [1] TRUE
is_language(quote(if (TRUE) 1 else 2)) #> TRUE
#> [1] TRUE
# See ?rlang::is_call() for is_call() examples

is_expression2(expression(1, x, x + 1)) #> TRUE
#> [1] TRUE
is_expression2(rlang::exprs(1, x, x + 1)) #> FALSE (exprs generates a list)
#> [1] FALSE

x <- 1
is_code(x) #> TRUE
#> [1] TRUE
# Identical to is_syntactic_literal(x) || is_symbol2(x) || is_language(x)

is_code(x, literal = FALSE) #> FALSE
#> [1] FALSE
# Identical to is_symbol2(x) || is_language(x)
```
