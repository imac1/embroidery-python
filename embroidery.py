def draw_rectangle(width, height, border_color, fill_color):
    matrix = []
    border_width = 1
    for i in range(height):
        row = []
        if i < border_width or i >= height - border_width:
            for j in range(width):
                row.append(border_color)
            matrix.append(row)
        else:
            for j in range(width):
                if j < border_width or j >= width - border_width:
                    row.append(border_color)
                else:
                    row.append(fill_color)
            matrix.append(row)
    return matrix


def draw_triangle(height):
    matrix = []
    return matrix


def draw_christmas_tree(blocks):
    matrix = []
    return matrix


def draw_circle(radius):
    matrix = []
    return matrix


def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end="")
        print()
    print()


if __name__ == "__main__":
    color_scheme = {0: " ", 1: "*", 2: "."}
    color_scheme2 = {0: "", 1: "*", 2: "-"}
    color_scheme3 = {0: '0', 1: '1', 2: '2'}
    # embroider(
    #     [
    #         [0, 0, 0, 1, 0, 0, 0],
    #         [0, 0, 1, 2, 1, 0, 0],
    #         [0, 1, 2, 2, 2, 1, 0],
    #         [1, 1, 1, 1, 1, 1, 1],
    #     ],
    #     color_scheme,
    # )
    # draw_rectangle(7, 7, color_scheme_3)

    # This should have the same output:
    embroider(draw_rectangle(7, 7, border_color=1, fill_color=2), color_scheme3)
