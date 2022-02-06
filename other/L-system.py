import turtle

def draw_rule(axiom, length, angle):
    for move in axiom:
        if move == 'F':
            turtle.forward(length)
        elif move == '+':
            turtle.left(angle)
        elif move == '-':
            turtle.right(angle)


def make_rule(rule, n_iter):
    A = ''
    for i in range(n_iter):
        for sym in rule:
            if sym == 'F':
                A += rule
            if sym == '+':
                A += '+'
            if sym == '-':
                A += '-'
        rule = A
    return A

turtle.speed(100)
print(make_rule('F+F--F+F', 2))
# draw_rule(make_rule('F+F--F+F', 2), 10, 60)
turtle.exitonclick()