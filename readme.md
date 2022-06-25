# Embroidery

## Story

Winter is coming, and so is Christmas. You have a small enterprise
that produces Christmas tree decorations. This year, you bought
a machine that is able to produce [embroidery](https://www.embroiderypanda.com/image/cache/data/A-A9933/Ornate-Christmas-Tree-Filled-Machine-Embroidery-Design-Digitized-Pattern-700x700.jpg)
and is controllable through a programmable interface.

The machine requests a matrix as an input where `0`
means an empty pixel, and positive integers mean different
colors.

Your job is to design simple ornament matrices for this year's Christmas fair.

## What are you going to learn?

- Think in algorithms.
- Handle edge cases.
- Use parameters and default arguments.
- Use nested lists and advanced list manipulation.


## Tasks

1. Implement the `draw_rectangle(width, height)` function to return matrices
similar to the following examples.
```
1 1 1 1 1 1 1          1 1 1 1 1 1 1          1 1 1 1 1 1 1
1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 1 1 1 1 1
1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 2 2 2 1 1
1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 2 2 2 1 1
1 1 1 1 1 1 1          1 2 2 2 2 2 1          1 1 1 1 1 1 1
1 1 1 1 1 1 1          1 1 1 1 1 1 1          1 1 1 1 1 1 1
```
    - There are optional parameters, such as `border_color`, `fill_color`, and `border_width`. The default value is `1` for all of these.
    - Called with default arguments, the returned matrix is a `width`-by-`height` rectangle shape marked by `1`s.
    - The border of the rectangle has `border_color`, and it is filled with `fill_color`.
    - The third optional parameter, `border_width`, specifies the width of the border.
    - There are no completely empty rows or columns in the returned matrix.
    - The function provides reasonable answers to edge cases (all combinations of integers as parameters).

2. Implement the `draw_triangle(height)` function to return arrays similar to
the following examples.
```
0 0 0 1 0 0 0          0 0 0 1 0 0 0
0 0 1 1 1 0 0          0 0 1 2 1 0 0
0 1 1 1 1 1 0          0 1 2 2 2 1 0
1 1 1 1 1 1 1          1 1 1 1 1 1 1
```
    - There are optional parameters, such as `border_color` and `fill_color`. The default value is `1` for all of these.
    - Called with default arguments, the returned matrix consists of `height` rows and shows a tringle filled with `1`s.
    - The border of the triangle has `border_color`, and it is filled with `fill_color`.
    - There are no completely empty rows or columns in the returned matrix.
    - The function provides reasonable answers to edge cases (all combinations of integers as parameters).

3. Implement the `draw_christmas_tree(blocks)` function to return arrays
similar to the following example (when `blocks == 4`).
```
0 0 0 0 0 1 0 0 0 0 0
0 0 0 0 1 2 1 0 0 0 0
0 0 0 1 2 2 2 1 0 0 0

0 0 0 0 1 2 1 0 0 0 0
0 0 0 1 2 2 2 1 0 0 0
0 0 1 2 2 2 2 2 1 0 0

0 0 0 1 2 2 2 1 0 0 0
0 0 1 2 2 2 2 2 1 0 0
0 1 2 2 2 2 2 2 2 1 0

0 0 1 2 2 2 2 2 1 0 0
0 1 2 2 2 2 2 2 2 1 0
1 1 1 1 1 1 1 1 1 1 1
```
    - There are optional parameters, such as `border_color` and `fill_color`. The default value is `1` for all of these.
    - Called with default arguments, the returned matrix shows a Christmas tree made of `blocks` pieces of trapezoid blocks and filled with `1`s. Each block has 3 rows, and each first row is one step shorter than the last row of the block above.
    - The border of the triangle has `border_color`, and it is filled with `fill_color`.
    - There are no completely empty rows or columns in the returned matrix.
    - The function provides reasonable answers to edge cases (all combinations of integers as parameters).

4. [OPTIONAL] Implement the `draw_circle(radius)` function to return similar to
the following example (truncated).
```
0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 1 2 2 2 2 2 2 2 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 1 1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0 0 0 0 0 0
0 0 0 0 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0 0 0 0 0
0 0 0 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0 0 0 0
0 0 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0 0 0
0 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0 0
0 0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0 0
0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0
0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0
0 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 0
1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1
1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1
1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1
```
    - There are optional parameters, such as `border_color` and `fill_color`. The default value is `1` for all of these.
    - Called with default arguments, the returned matrix shows a circle of radius `r` filled with `1`s.
    - The returned matrix shows a continuous circle outline of `border_color`, and filled with `fill_color`.
    - There are no completely empty rows or columns in the returned matrix.
    - The function provides reasonable answers to edge cases (all combinations of integers as parameters).

## General requirements

None

## Hints

- Try to solve the problems without distinguishing the border and the inside first
  (that is, `border_color == fill_color`), you may find them much easier this way.
- This is especially true for the `draw_circle` function. Drawing a nice border
  for a circle is a rather advanced exercise, even though the only extra math
  needed for the solution is the Pythagorean theorem to calculate distance.


## Background materials

- <i class="far fa-exclamation"></i> [Nested lists]
- <i class="far fa-exclamation"></i> [On default arguments](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions) in the documentation

