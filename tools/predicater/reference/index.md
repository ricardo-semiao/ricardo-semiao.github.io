# Package index

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

## Simple predicates

### Atomic vectors

- [`is_logical()`](predicates-atomic.md)
  [`is_integer()`](predicates-atomic.md)
  [`is_double()`](predicates-atomic.md)
  [`is_complex()`](predicates-atomic.md)
  [`is_character()`](predicates-atomic.md)
  [`is_raw()`](predicates-atomic.md)
  [`is_atomic()`](predicates-atomic.md)
  [`is_numeric()`](predicates-atomic.md) : Type checks - Atomic vectors
- [`are_integer_like()`](is_integer_like.md)
  [`is_integer_like()`](is_integer_like.md) : Type checks - Integer-like
  values
- [`are_true()`](predicates-true-false.md)
  [`is_true2()`](predicates-true-false.md)
  [`are_false()`](predicates-true-false.md)
  [`is_false2()`](predicates-true-false.md)
  [`is_bool2()`](predicates-true-false.md) : Type checks - TRUE and
  FALSE values
- [`are_na2()`](is_na2.md) [`is_na2()`](is_na2.md) : Type checks - NA
  values
- [`are_finite()`](predicates-infinite.md)
  [`is_finite()`](predicates-infinite.md)
  [`are_nan()`](predicates-infinite.md)
  [`is_nan()`](predicates-infinite.md)
  [`are_inf()`](predicates-infinite.md)
  [`is_inf()`](predicates-infinite.md) : Type checks - Inf and NaN

### Other types

- [`is_list()`](predicates-collections.md)
  [`is_pairlist2()`](predicates-collections.md)
  [`is_environment2()`](predicates-collections.md)
  [`is_vector()`](predicates-collections.md)
  [`is_collection()`](predicates-collections.md) : Type checks -
  Collection types
- [`is_syntactic_literal()`](predicates-language.md)
  [`is_symbol2()`](predicates-language.md)
  [`is_language()`](predicates-language.md)
  [`is_call()`](predicates-language.md)
  [`is_expression2()`](predicates-language.md)
  [`is_code()`](predicates-language.md) : Type checks - Language objects
- [`is_function()`](is_function.md) [`is_closure()`](is_function.md)
  [`is_primitive()`](is_function.md)
  [`is_primitive_eager()`](is_function.md)
  [`is_primitive_lazy()`](is_function.md) : Type checks - Functions
- [`is_type()`](predicates-other-types.md)
  [`is_null()`](predicates-other-types.md)
  [`is_promise()`](predicates-other-types.md)
  [`is_dots()`](predicates-other-types.md)
  [`is_weakref()`](predicates-other-types.md)
  [`is_bytecode()`](predicates-other-types.md)
  [`is_externalptr()`](predicates-other-types.md)
  [`is_char()`](predicates-other-types.md)
  [`is_any()`](predicates-other-types.md) : Type checks - Other types

### attributes

- [`is_attrs_allowed()`](is_attrs_allowed.md) : Attribute checks - Check
  if object allows attributes
- [`has_names_valid()`](has_names_valid.md)
  [`are_names_valid()`](has_names_valid.md) : Attribute checks - Names
- [`n_dims()`](attributes-dimensions.md)
  [`n_dimnames()`](attributes-dimensions.md)
  [`has_dimnames()`](attributes-dimensions.md)
  [`has_rownames()`](attributes-dimensions.md)
  [`has_dim()`](attributes-dimensions.md) : Attribute checks -
  Dimensions existence and sizes
- [`attrs_rmv()`](attributes-filter.md)
  [`attrs_keep()`](attributes-filter.md)
  [`has_attrs_any()`](attributes-filter.md)
  [`has_attrs_all()`](attributes-filter.md)
  [`has_attrs_only()`](attributes-filter.md) : Attribute checks - Check
  for and filter attributes from object

### Object systems

- [`has_object_bit()`](predicates-objects.md)
  [`has_s4_bit()`](predicates-objects.md)
  [`has_class()`](predicates-objects.md)
  [`is_object_like()`](predicates-objects.md)
  [`is_s4()`](predicates-objects.md)
  [`is_object()`](predicates-objects.md) : Type checks - Objects
- [`object_system()`](object_system.md)
  [`is_system()`](object_system.md) : Type checks - Determine
  object-oriented system of object

### Data

- [`is_sorted()`](is_sorted.md) : Data checks - Check if object is
  ordered
- [`is_matching_set()`](is_matching_set.md) : Data checks - Check if
  object is in (and/or not in) a set
- [`any_duplicated()`](any_duplicated.md)
  [`are_duplicated()`](any_duplicated.md) : Data checks - Check for
  duplicate values
- [`is_empty2()`](is_empty2.md) : Metadata checks - Check if a
  collection is empty

## Object comparison

### Comparison and prototypes

- [`identical2()`](identical2.md) [`identical_flag()`](identical2.md) :
  Compare - Exact equality with more flexibility
- [`is_ptype()`](is_ptype.md) [`is_ptype_list()`](is_ptype.md) :
  Compare - Check if object is of prototype

### If-else and pattern matching

- [`match_hash()`](match_hash.md) [`match_id()`](match_hash.md)
  [`match_ptype()`](match_hash.md) [`match_when()`](match_hash.md) :
  Compare - Pattern matching
- [`if_else2()`](if_else2.md) : Compare - Vectorized if-else
- [`case_when2()`](case_when2.md) : Compare - Vectorized nested if-else

## Complex predicates and validation

### Atomic vectors

- [`test_integer()`](tests-numeric.md)
  [`test_double()`](tests-numeric.md)
  [`test_complex()`](tests-numeric.md)
  [`assert_integer()`](tests-numeric.md)
  [`assert_double()`](tests-numeric.md)
  [`assert_complex()`](tests-numeric.md) : Validation - Numeric vectors
- [`test_logical()`](test-logical_raw.md)
  [`test_raw()`](test-logical_raw.md)
  [`assert_logical()`](test-logical_raw.md)
  [`assert_raw()`](test-logical_raw.md) : Validation - Logical and Raw
  vectors
- [`test_character()`](test_character.md)
  [`assert_character()`](test_character.md) : Validation - Character
  vectors

### Language objects

- [`test_expression()`](test_expression.md)
  [`assert_expression()`](test_expression.md) : Validation - Expression
  vectors
- [`test_symbol()`](test_symbol.md) [`assert_symbol()`](test_symbol.md)
  : Validation - Symbol
- [`test_language()`](test_language.md)
  [`assert_language()`](test_language.md) : Validation - Language
- [`test_code()`](test_code.md) [`assert_code()`](test_code.md) :
  Validation - Code Objects

### Other types

- [`test_list()`](test_list.md) [`assert_list()`](test_list.md) :
  Validation - List
- [`test_vector()`](test_vector.md) [`assert_vector()`](test_vector.md)
  : Validation - General vectors
- [`test_environment()`](test_environment.md)
  [`assert_environment()`](test_environment.md) : Validation -
  Environment
- [`test_function()`](test_function.md)
  [`assert_function()`](test_function.md) : Validation - Function
- [`test_promise()`](tests-other_types.md)
  [`test_dots()`](tests-other_types.md)
  [`test_weakref()`](tests-other_types.md)
  [`test_bytecode()`](tests-other_types.md)
  [`test_externalptr()`](tests-other_types.md)
  [`assert_null()`](tests-other_types.md)
  [`assert_promise()`](tests-other_types.md)
  [`assert_dots()`](tests-other_types.md)
  [`assert_weakref()`](tests-other_types.md)
  [`assert_bytecode()`](tests-other_types.md)
  [`assert_externalptr()`](tests-other_types.md) : Validation - Other
  types

### Attributes

- [`test_names()`](test_names.md) [`assert_names()`](test_names.md) :
  Validation - Names attribute
- [`test_matrix()`](test_matrix.md) [`assert_matrix()`](test_matrix.md)
  : Validation - Matrix and array attributes
- [`test_class()`](test_class.md) [`assert_class()`](test_class.md) :
  Validation - Class attribute
- [`test_object()`](test_object.md) [`assert_object()`](test_object.md)
  : Validation - Object-related attributes

### Validation via external functions

- [`assert_from_msg()`](assert_from_msg.md)
  [`assert_from_error()`](assert_from_msg.md) : Validation - Rethrow
  errors with more information
- [`assert_ptype()`](assert_ptype.md) : Validation - If object is of
  prototype
- [`assert_predicate()`](assert_predicate.md) : Validation - Throw error
  from custom predicate
- [`test_multiple()`](test_multiple.md) : Validation - Test for one of
  multiple types

## Utilities

### Logical utilities

- [`pany()`](pany.md) [`pall()`](pany.md) [`pany_na()`](pany.md)
  [`pall_na()`](pany.md) : Parallel any and all
- [`reduce_predicate()`](reduce_predicate.md)
  [`accumulate_predicate()`](reduce_predicate.md) : Reduce binary
  predicate over a list

### Attributes utilities

- [`attrs_rmv()`](attributes-filter.md)
  [`attrs_keep()`](attributes-filter.md)
  [`has_attrs_any()`](attributes-filter.md)
  [`has_attrs_all()`](attributes-filter.md)
  [`has_attrs_only()`](attributes-filter.md) : Attribute checks - Check
  for and filter attributes from object
- [`names3()`](attributes-getters-setters.md)
  [`` `names3<-`() ``](attributes-getters-setters.md)
  [`dimnames2()`](attributes-getters-setters.md)
  [`` `dimnames2<-`() ``](attributes-getters-setters.md)
  [`rownames2()`](attributes-getters-setters.md)
  [`` `rownames2<-`() ``](attributes-getters-setters.md)
  [`class2()`](attributes-getters-setters.md)
  [`` `class2<-`() ``](attributes-getters-setters.md) : Attribute
  utilities - Getters and setters
- [`attr2()`](attr2.md) : Attribute utilities - Get attribute of object

### Others

- [`check_installed2()`](check_installed2.md) : Check if user accepted a
  package installation
- [`c2()`](c2.md) : Combine many vectors into one vector

## On this page

## Simple predicates

### Atomic vectors

- [`is_logical()`](predicates-atomic.md)
  [`is_integer()`](predicates-atomic.md)
  [`is_double()`](predicates-atomic.md)
  [`is_complex()`](predicates-atomic.md)
  [`is_character()`](predicates-atomic.md)
  [`is_raw()`](predicates-atomic.md)
  [`is_atomic()`](predicates-atomic.md)
  [`is_numeric()`](predicates-atomic.md) : Type checks - Atomic vectors
- [`are_integer_like()`](is_integer_like.md)
  [`is_integer_like()`](is_integer_like.md) : Type checks - Integer-like
  values
- [`are_true()`](predicates-true-false.md)
  [`is_true2()`](predicates-true-false.md)
  [`are_false()`](predicates-true-false.md)
  [`is_false2()`](predicates-true-false.md)
  [`is_bool2()`](predicates-true-false.md) : Type checks - TRUE and
  FALSE values
- [`are_na2()`](is_na2.md) [`is_na2()`](is_na2.md) : Type checks - NA
  values
- [`are_finite()`](predicates-infinite.md)
  [`is_finite()`](predicates-infinite.md)
  [`are_nan()`](predicates-infinite.md)
  [`is_nan()`](predicates-infinite.md)
  [`are_inf()`](predicates-infinite.md)
  [`is_inf()`](predicates-infinite.md) : Type checks - Inf and NaN

### Other types

- [`is_list()`](predicates-collections.md)
  [`is_pairlist2()`](predicates-collections.md)
  [`is_environment2()`](predicates-collections.md)
  [`is_vector()`](predicates-collections.md)
  [`is_collection()`](predicates-collections.md) : Type checks -
  Collection types
- [`is_syntactic_literal()`](predicates-language.md)
  [`is_symbol2()`](predicates-language.md)
  [`is_language()`](predicates-language.md)
  [`is_call()`](predicates-language.md)
  [`is_expression2()`](predicates-language.md)
  [`is_code()`](predicates-language.md) : Type checks - Language objects
- [`is_function()`](is_function.md) [`is_closure()`](is_function.md)
  [`is_primitive()`](is_function.md)
  [`is_primitive_eager()`](is_function.md)
  [`is_primitive_lazy()`](is_function.md) : Type checks - Functions
- [`is_type()`](predicates-other-types.md)
  [`is_null()`](predicates-other-types.md)
  [`is_promise()`](predicates-other-types.md)
  [`is_dots()`](predicates-other-types.md)
  [`is_weakref()`](predicates-other-types.md)
  [`is_bytecode()`](predicates-other-types.md)
  [`is_externalptr()`](predicates-other-types.md)
  [`is_char()`](predicates-other-types.md)
  [`is_any()`](predicates-other-types.md) : Type checks - Other types

### attributes

- [`is_attrs_allowed()`](is_attrs_allowed.md) : Attribute checks - Check
  if object allows attributes
- [`has_names_valid()`](has_names_valid.md)
  [`are_names_valid()`](has_names_valid.md) : Attribute checks - Names
- [`n_dims()`](attributes-dimensions.md)
  [`n_dimnames()`](attributes-dimensions.md)
  [`has_dimnames()`](attributes-dimensions.md)
  [`has_rownames()`](attributes-dimensions.md)
  [`has_dim()`](attributes-dimensions.md) : Attribute checks -
  Dimensions existence and sizes
- [`attrs_rmv()`](attributes-filter.md)
  [`attrs_keep()`](attributes-filter.md)
  [`has_attrs_any()`](attributes-filter.md)
  [`has_attrs_all()`](attributes-filter.md)
  [`has_attrs_only()`](attributes-filter.md) : Attribute checks - Check
  for and filter attributes from object

### Object systems

- [`has_object_bit()`](predicates-objects.md)
  [`has_s4_bit()`](predicates-objects.md)
  [`has_class()`](predicates-objects.md)
  [`is_object_like()`](predicates-objects.md)
  [`is_s4()`](predicates-objects.md)
  [`is_object()`](predicates-objects.md) : Type checks - Objects
- [`object_system()`](object_system.md)
  [`is_system()`](object_system.md) : Type checks - Determine
  object-oriented system of object

### Data

- [`is_sorted()`](is_sorted.md) : Data checks - Check if object is
  ordered
- [`is_matching_set()`](is_matching_set.md) : Data checks - Check if
  object is in (and/or not in) a set
- [`any_duplicated()`](any_duplicated.md)
  [`are_duplicated()`](any_duplicated.md) : Data checks - Check for
  duplicate values
- [`is_empty2()`](is_empty2.md) : Metadata checks - Check if a
  collection is empty

## Object comparison

### Comparison and prototypes

- [`identical2()`](identical2.md) [`identical_flag()`](identical2.md) :
  Compare - Exact equality with more flexibility
- [`is_ptype()`](is_ptype.md) [`is_ptype_list()`](is_ptype.md) :
  Compare - Check if object is of prototype

### If-else and pattern matching

- [`match_hash()`](match_hash.md) [`match_id()`](match_hash.md)
  [`match_ptype()`](match_hash.md) [`match_when()`](match_hash.md) :
  Compare - Pattern matching
- [`if_else2()`](if_else2.md) : Compare - Vectorized if-else
- [`case_when2()`](case_when2.md) : Compare - Vectorized nested if-else

## Complex predicates and validation

### Atomic vectors

- [`test_integer()`](tests-numeric.md)
  [`test_double()`](tests-numeric.md)
  [`test_complex()`](tests-numeric.md)
  [`assert_integer()`](tests-numeric.md)
  [`assert_double()`](tests-numeric.md)
  [`assert_complex()`](tests-numeric.md) : Validation - Numeric vectors
- [`test_logical()`](test-logical_raw.md)
  [`test_raw()`](test-logical_raw.md)
  [`assert_logical()`](test-logical_raw.md)
  [`assert_raw()`](test-logical_raw.md) : Validation - Logical and Raw
  vectors
- [`test_character()`](test_character.md)
  [`assert_character()`](test_character.md) : Validation - Character
  vectors

### Language objects

- [`test_expression()`](test_expression.md)
  [`assert_expression()`](test_expression.md) : Validation - Expression
  vectors
- [`test_symbol()`](test_symbol.md) [`assert_symbol()`](test_symbol.md)
  : Validation - Symbol
- [`test_language()`](test_language.md)
  [`assert_language()`](test_language.md) : Validation - Language
- [`test_code()`](test_code.md) [`assert_code()`](test_code.md) :
  Validation - Code Objects

### Other types

- [`test_list()`](test_list.md) [`assert_list()`](test_list.md) :
  Validation - List
- [`test_vector()`](test_vector.md) [`assert_vector()`](test_vector.md)
  : Validation - General vectors
- [`test_environment()`](test_environment.md)
  [`assert_environment()`](test_environment.md) : Validation -
  Environment
- [`test_function()`](test_function.md)
  [`assert_function()`](test_function.md) : Validation - Function
- [`test_promise()`](tests-other_types.md)
  [`test_dots()`](tests-other_types.md)
  [`test_weakref()`](tests-other_types.md)
  [`test_bytecode()`](tests-other_types.md)
  [`test_externalptr()`](tests-other_types.md)
  [`assert_null()`](tests-other_types.md)
  [`assert_promise()`](tests-other_types.md)
  [`assert_dots()`](tests-other_types.md)
  [`assert_weakref()`](tests-other_types.md)
  [`assert_bytecode()`](tests-other_types.md)
  [`assert_externalptr()`](tests-other_types.md) : Validation - Other
  types

### Attributes

- [`test_names()`](test_names.md) [`assert_names()`](test_names.md) :
  Validation - Names attribute
- [`test_matrix()`](test_matrix.md) [`assert_matrix()`](test_matrix.md)
  : Validation - Matrix and array attributes
- [`test_class()`](test_class.md) [`assert_class()`](test_class.md) :
  Validation - Class attribute
- [`test_object()`](test_object.md) [`assert_object()`](test_object.md)
  : Validation - Object-related attributes

### Validation via external functions

- [`assert_from_msg()`](assert_from_msg.md)
  [`assert_from_error()`](assert_from_msg.md) : Validation - Rethrow
  errors with more information
- [`assert_ptype()`](assert_ptype.md) : Validation - If object is of
  prototype
- [`assert_predicate()`](assert_predicate.md) : Validation - Throw error
  from custom predicate
- [`test_multiple()`](test_multiple.md) : Validation - Test for one of
  multiple types

## Utilities

### Logical utilities

- [`pany()`](pany.md) [`pall()`](pany.md) [`pany_na()`](pany.md)
  [`pall_na()`](pany.md) : Parallel any and all
- [`reduce_predicate()`](reduce_predicate.md)
  [`accumulate_predicate()`](reduce_predicate.md) : Reduce binary
  predicate over a list

### Attributes utilities

- [`attrs_rmv()`](attributes-filter.md)
  [`attrs_keep()`](attributes-filter.md)
  [`has_attrs_any()`](attributes-filter.md)
  [`has_attrs_all()`](attributes-filter.md)
  [`has_attrs_only()`](attributes-filter.md) : Attribute checks - Check
  for and filter attributes from object
- [`names3()`](attributes-getters-setters.md)
  [`` `names3<-`() ``](attributes-getters-setters.md)
  [`dimnames2()`](attributes-getters-setters.md)
  [`` `dimnames2<-`() ``](attributes-getters-setters.md)
  [`rownames2()`](attributes-getters-setters.md)
  [`` `rownames2<-`() ``](attributes-getters-setters.md)
  [`class2()`](attributes-getters-setters.md)
  [`` `class2<-`() ``](attributes-getters-setters.md) : Attribute
  utilities - Getters and setters
- [`attr2()`](attr2.md) : Attribute utilities - Get attribute of object

### Others

- [`check_installed2()`](check_installed2.md) : Check if user accepted a
  package installation
- [`c2()`](c2.md) : Combine many vectors into one vector
