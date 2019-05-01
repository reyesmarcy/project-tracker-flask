"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""
    print(request.args, '======================')
    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    student_projects = hackbright.get_grades_by_github(github)

    # return "{} is the GitHub account for {} {}".format(github, first, last)
    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            student_projects=student_projects)

    return html 

@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html") 

@app.route("/project")
def get_project():

    title = request.args.get('title')
    project_info = hackbright.get_project_by_title(title)

    html = render_template("project_info.html",
                           project_info=project_info)

    return html

@app.route("/project_search")
def get_project_form():

    return render_template("project_search.html")

#renders to add new student form
@app.route("/new_student")
def new_student():

    return render_template("new_student.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    first = request.form.get("first_name")   
    last = request.form.get("last_name")
    github = request.form.get("github")
    print(request.form.get("name"))
    hackbright.make_new_student(first, last, github)

    html = render_template("student_added.html",
                           first=first,
                           last=last,
                           github=github)

    return html 


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
