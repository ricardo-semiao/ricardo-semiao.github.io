# Compare - Pattern matching

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Pattern matching functions to return a value based on a case of `x`.
Similar to [`switch()`](https://rdrr.io/r/base/switch.html) but allows
for any type for object as the case. Cases are two sided formulas with
the LHS being the case and the RHS being the return value.

- For `match_hash` and `match_id`, cases are any R object to directly
  compare with `x`.

- For `match_ptype`, cases are prototypes to check if `x`
  [`is_ptype()`](is_ptype.md).

- For `match_when`, cases are any predicate expression, that matches
  when it evaluates to `TRUE`.

## Usage

``` r
match_hash(x, ..., nomatch = NULL, htab = NULL, type = NULL, size = NULL)

match_id(x, ..., nomatch = NULL, fun = "identical", args_id = list())

match_ptype(x, ..., nomatch = NULL, args_ptype = list())

match_when(x, ..., nomatch = NULL)
```

## Arguments

- x:

  \[`any`\] Object to match.

- ...:

  \[`<formula>` each\] Cases to match. Each case is a formula with the
  left-hand side being the value to match against and the right-hand
  side being the value to return if the case matches. Cases are
  evaluated in order, and in the caller environment.

- nomatch:

  \[`any`\] Value to return if no cases match. Use
  [`stop()`](https://rdrr.io/r/base/stop.html) or similar to err.

- htab, type, size:

  \[[`hashtab()`](https://rdrr.io/r/utils/hashtab.html) \| NULL,
  `character(1)` \| `NULL`, `integer(1)` \| `NULL`\] For `match_hash`:
  an existing hash table, or the arguments passed to
  [`utils::hashtab()`](https://rdrr.io/r/utils/hashtab.html) to create a
  new one.

- fun, args_id:

  \[`character(1)`, [`list()`](https://rdrr.io/r/base/list.html)\] For
  `match_id`: which 'identical' function to use, `"identical"` for
  [`identical()`](https://rdrr.io/r/base/identical.html) or
  `"identical2"` for [`identical2()`](identical2.md); and a list of
  arguments to pass to it.

- args_ptype:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] For `match_ptype`. A
  list of arguments to pass to [`is_ptype()`](is_ptype.md).

## Value

\[`any`\] The value of the first matching case, or `nomatch` if no cases
match.

## Details

The return value is evaluated dynamically and can refer to `x`, except
for `match_hash`, which in turn is faster and can be supplied a
pre-built hash table.

## Examples

``` r
match_hash(1.42, 1.42 ~ base::sum, "oi" ~ -Inf) #> base::sum
#> function (..., na.rm = FALSE)  .Primitive("sum")

# The htab can be reused to speed up repeated calls to match_hash():
htab <- utils::hashtab(size = 2)
utils::sethash(htab, 1.42, base::sum)
utils::sethash(htab, "oi", -Inf)
match_hash(1.42, htab = htab) #> base::sum
#> function (..., na.rm = FALSE)  .Primitive("sum")

match_id(1.42, "oi" ~ -Inf, 1.42 ~ .x * 2) #> 2.84
#> [1] 2.84

match_ptype(1.42, character() ~ "chr", double() ~ "dbl") #> "dbl"
#> [1] "dbl"

match_when("oi", grepl("1", .x) ~ "1", grepl("o", .x) ~ "o") #> "o"
#> [1] "o"
```

## On this page

Pattern matching functions to return a value based on a case of `x`.
Similar to [`switch()`](https://rdrr.io/r/base/switch.html) but allows
for any type for object as the case. Cases are two sided formulas with
the LHS being the case and the RHS being the return value.

- For `match_hash` and `match_id`, cases are any R object to directly
  compare with `x`.

- For `match_ptype`, cases are prototypes to check if `x`
  [`is_ptype()`](is_ptype.md).

- For `match_when`, cases are any predicate expression, that matches
  when it evaluates to `TRUE`.

## Usage

``` r
match_hash(x, ..., nomatch = NULL, htab = NULL, type = NULL, size = NULL)

match_id(x, ..., nomatch = NULL, fun = "identical", args_id = list())

match_ptype(x, ..., nomatch = NULL, args_ptype = list())

match_when(x, ..., nomatch = NULL)
```

## Arguments

- x:

  \[`any`\] Object to match.

- ...:

  \[`<formula>` each\] Cases to match. Each case is a formula with the
  left-hand side being the value to match against and the right-hand
  side being the value to return if the case matches. Cases are
  evaluated in order, and in the caller environment.

- nomatch:

  \[`any`\] Value to return if no cases match. Use
  [`stop()`](https://rdrr.io/r/base/stop.html) or similar to err.

- htab, type, size:

  \[[`hashtab()`](https://rdrr.io/r/utils/hashtab.html) \| NULL,
  `character(1)` \| `NULL`, `integer(1)` \| `NULL`\] For `match_hash`:
  an existing hash table, or the arguments passed to
  [`utils::hashtab()`](https://rdrr.io/r/utils/hashtab.html) to create a
  new one.

- fun, args_id:

  \[`character(1)`, [`list()`](https://rdrr.io/r/base/list.html)\] For
  `match_id`: which 'identical' function to use, `"identical"` for
  [`identical()`](https://rdrr.io/r/base/identical.html) or
  `"identical2"` for [`identical2()`](identical2.md); and a list of
  arguments to pass to it.

- args_ptype:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] For `match_ptype`. A
  list of arguments to pass to [`is_ptype()`](is_ptype.md).

## Value

\[`any`\] The value of the first matching case, or `nomatch` if no cases
match.

## Details

The return value is evaluated dynamically and can refer to `x`, except
for `match_hash`, which in turn is faster and can be supplied a
pre-built hash table.

## Examples

``` r
match_hash(1.42, 1.42 ~ base::sum, "oi" ~ -Inf) #> base::sum
#> function (..., na.rm = FALSE)  .Primitive("sum")

# The htab can be reused to speed up repeated calls to match_hash():
htab <- utils::hashtab(size = 2)
utils::sethash(htab, 1.42, base::sum)
utils::sethash(htab, "oi", -Inf)
match_hash(1.42, htab = htab) #> base::sum
#> function (..., na.rm = FALSE)  .Primitive("sum")

match_id(1.42, "oi" ~ -Inf, 1.42 ~ .x * 2) #> 2.84
#> [1] 2.84

match_ptype(1.42, character() ~ "chr", double() ~ "dbl") #> "dbl"
#> [1] "dbl"

match_when("oi", grepl("1", .x) ~ "1", grepl("o", .x) ~ "o") #> "o"
#> [1] "o"
```
