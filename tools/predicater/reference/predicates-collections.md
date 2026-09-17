# Type checks - Collection types

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

In R, there are several types
([`typeof()`](https://rdrr.io/r/base/typeof.html)) that can "store
elements":

- The atomic vector types (see
  [predicates-atomic](predicates-atomic.md)).

- `"list"`: the generic vector type (can store elements of any type).
  Tested by
  [`rlang::is_list()`](https://rlang.r-lib.org/reference/type-predicates.html).

- `"pairlist"`: a linked list, used in R's internals. Tested by
  `is_pairlist2()`.

- `"environment"`: a hash table, used to store variables and their
  values. Tested by `is_environment2()`.

- `"expression"`: a vector of unevaluated R code objects. Tested by
  [`is_expression2()`](predicates-language.md).

See the 'Details' section for what behavior you can expect from these
types.

Additionally:

- [`rlang::is_atomic()`](https://rlang.r-lib.org/reference/type-predicates.html)
  tests for any atomic vector type.

- [`rlang::is_vector()`](https://rlang.r-lib.org/reference/type-predicates.html)
  tests for atomic or generic (list) vectors.

- `is_collection()` tests for any of the above collection types, with
  options to exclude any of them.

## Usage

``` r
is_list(x, n = NULL)

is_pairlist2(x, n = NULL)

is_environment2(x, n = NULL)

is_vector(x, n = NULL)

is_collection(
  x,
  n = NULL,
  expr = TRUE,
  pairlist = TRUE,
  env = TRUE,
  null = FALSE,
  dots = FALSE
)
```

## Arguments

- x:

  \[`any`\] An object to test.

- n:

  \[`integer(1)` \| `NULL`\] Length of `x`, set to `NULL` to not test.

- expr, pairlist, env, null, dots:

  \[`TRUE` \| `FALSE`\] Whether to include expression, pairlist,
  environment, `NILL`, or the `...` objects as collections.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Details

All collection types:

- Have varying [`length()`](https://rdrr.io/r/base/length.html).

- Can have [`names()`](https://rdrr.io/r/base/names.html).

- Can have their elements accessed by names (if present) via `[`, `[[`,
  and `$`.

- All but environment can have their elements accessed by integer
  indexes too, and their names set via `names(x) <- value`.

Note that the result of accessing out-of-bounds indexes depends on the
type and operator, and is very quirky and inconsistent across R. See
[Advanced R, 2nd edition, chapter
4](https://adv-r.hadley.nz/subsetting.html) for more details.

Objects that are not considered collections:

- Objects of type `"s4"` or `"object"` are a 'collection of slots', but
  their data is stored in their attributes, which any R object can do,
  and their length is always 1.

- The `"dots"` object is a collection of promises, have varying length,
  names, etc. But it is low-level, and removed from this definition for
  simplicity.

- 'NULL' (and 'any') have length 0, and are often thought as empty
  collections, but in face of `integer(0)` and
  [`list()`](https://rdrr.io/r/base/list.html), such thought is not the
  best.

- 'language' and 'promise' can have names, but don't have varying
  length.

- All the other types have length 1, and cannot have names.

See
[`rlang::is_namespace()`](https://rlang.r-lib.org/reference/is_namespace.html)
for another environment-related test.

## Examples

``` r
is_collection(list(1, 2, 3)) #> TRUE
#> [1] TRUE
is_collection(rlang::env(a = 1, b = 2), n = 2) #> TRUE
#> [1] TRUE

# NULL is not considered a collection:
is_collection(NULL) #> FALSE
#> [1] FALSE
is_collection(NULL, null = TRUE) #> TRUE
#> [1] TRUE

# This is the difference between rlang::is_empty() and predicater::is_empty2():
rlang::is_empty(NULL) #> TRUE
#> [1] TRUE
try(is_empty2(NULL)) #> Error
#> Error in is_empty2(NULL) : `x` is not a collection.
```

## On this page

In R, there are several types
([`typeof()`](https://rdrr.io/r/base/typeof.html)) that can "store
elements":

- The atomic vector types (see
  [predicates-atomic](predicates-atomic.md)).

- `"list"`: the generic vector type (can store elements of any type).
  Tested by
  [`rlang::is_list()`](https://rlang.r-lib.org/reference/type-predicates.html).

- `"pairlist"`: a linked list, used in R's internals. Tested by
  `is_pairlist2()`.

- `"environment"`: a hash table, used to store variables and their
  values. Tested by `is_environment2()`.

- `"expression"`: a vector of unevaluated R code objects. Tested by
  [`is_expression2()`](predicates-language.md).

See the 'Details' section for what behavior you can expect from these
types.

Additionally:

- [`rlang::is_atomic()`](https://rlang.r-lib.org/reference/type-predicates.html)
  tests for any atomic vector type.

- [`rlang::is_vector()`](https://rlang.r-lib.org/reference/type-predicates.html)
  tests for atomic or generic (list) vectors.

- `is_collection()` tests for any of the above collection types, with
  options to exclude any of them.

## Usage

``` r
is_list(x, n = NULL)

is_pairlist2(x, n = NULL)

is_environment2(x, n = NULL)

is_vector(x, n = NULL)

is_collection(
  x,
  n = NULL,
  expr = TRUE,
  pairlist = TRUE,
  env = TRUE,
  null = FALSE,
  dots = FALSE
)
```

## Arguments

- x:

  \[`any`\] An object to test.

- n:

  \[`integer(1)` \| `NULL`\] Length of `x`, set to `NULL` to not test.

- expr, pairlist, env, null, dots:

  \[`TRUE` \| `FALSE`\] Whether to include expression, pairlist,
  environment, `NILL`, or the `...` objects as collections.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Details

All collection types:

- Have varying [`length()`](https://rdrr.io/r/base/length.html).

- Can have [`names()`](https://rdrr.io/r/base/names.html).

- Can have their elements accessed by names (if present) via `[`, `[[`,
  and `$`.

- All but environment can have their elements accessed by integer
  indexes too, and their names set via `names(x) <- value`.

Note that the result of accessing out-of-bounds indexes depends on the
type and operator, and is very quirky and inconsistent across R. See
[Advanced R, 2nd edition, chapter
4](https://adv-r.hadley.nz/subsetting.html) for more details.

Objects that are not considered collections:

- Objects of type `"s4"` or `"object"` are a 'collection of slots', but
  their data is stored in their attributes, which any R object can do,
  and their length is always 1.

- The `"dots"` object is a collection of promises, have varying length,
  names, etc. But it is low-level, and removed from this definition for
  simplicity.

- 'NULL' (and 'any') have length 0, and are often thought as empty
  collections, but in face of `integer(0)` and
  [`list()`](https://rdrr.io/r/base/list.html), such thought is not the
  best.

- 'language' and 'promise' can have names, but don't have varying
  length.

- All the other types have length 1, and cannot have names.

See
[`rlang::is_namespace()`](https://rlang.r-lib.org/reference/is_namespace.html)
for another environment-related test.

## Examples

``` r
is_collection(list(1, 2, 3)) #> TRUE
#> [1] TRUE
is_collection(rlang::env(a = 1, b = 2), n = 2) #> TRUE
#> [1] TRUE

# NULL is not considered a collection:
is_collection(NULL) #> FALSE
#> [1] FALSE
is_collection(NULL, null = TRUE) #> TRUE
#> [1] TRUE

# This is the difference between rlang::is_empty() and predicater::is_empty2():
rlang::is_empty(NULL) #> TRUE
#> [1] TRUE
try(is_empty2(NULL)) #> Error
#> Error in is_empty2(NULL) : `x` is not a collection.
```
