from fpdf import FPDF
from math_generator import MathProblem, UnknownElement, MathProblemType


def createExercices(problems):
    exercises_per_column = 28
    columns = 5
    column_width = 50
    cell_height = 7
    number_width = 6
    spacer = 2

    pdf = FPDF(orientation="L")
    pdf.set_top_margin(5)
    pdf.set_auto_page_break(True, 1)
    pdf.add_page()
    pdf.set_font("Arial", size=12)


    start_x = pdf.get_x()
    start_y = pdf.get_y()

    for i in range(len(problems)):
        problem = problems[i]
        pdf.set_xy(start_x + int(i/exercises_per_column) * column_width, start_y + (i % exercises_per_column) * cell_height)

        border = "R"
        if (int(i / exercises_per_column) == columns - 1):
            border = 0

        if (problem.unknown == UnknownElement.Z):
            pdf.cell(spacer, cell_height)
            pdf.cell(number_width, cell_height, txt=str(problem.x), align="C")
            pdf.cell(number_width, cell_height, txt=str(problem.operator), align="C")
            pdf.cell(number_width, cell_height, txt=str(problem.y), align="C")
            pdf.cell(number_width, cell_height, "=", align="C")
            pdf.cell(column_width - 4 * number_width - spacer, cell_height, border=border)
        elif (problem.unknown == UnknownElement.X):
            pdf.cell(column_width - 4 * number_width - spacer, cell_height)
            pdf.cell(number_width, cell_height, txt=str(problem.operator), align="C")
            pdf.cell(number_width, cell_height, txt=str(problem.y), align="C")
            pdf.cell(number_width, cell_height, "=", align="C")
            pdf.cell(number_width, cell_height, str(problem.z), align="C")
            pdf.cell(spacer, cell_height, border=border)

    pdf.output("simple_demo.pdf")
