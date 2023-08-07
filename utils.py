import json
from latex_resume_template import generate_latex_resume

# Configuration
DATA_FILENAME = "data.json"
OUTPUT_FILENAME = "Resume.tex"


def escape_latex_characters(s):
    """Escape special characters for LaTeX."""
    latex_special_chars = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\^{}",
        "\\": r"\textbackslash{}",
        "<": r"\textless{}",
        ">": r"\textgreater{}",
    }
    return "".join(latex_special_chars.get(c, c) for c in s)


def generate_latex_resume_escaped(data):
    """Generate LaTeX resume with escaped characters based on structured data."""
    # Escape the data for LaTeX
    escaped_data = {
        k: escape_latex_characters(v) if isinstance(v, str) else v
        for k, v in data.items()
    }
    escaped_data["education"] = {
        k: escape_latex_characters(v) if isinstance(v, str) else v
        for k, v in data["education"].items()
    }
    for exp in escaped_data["experiences"]:
        exp["name"] = escape_latex_characters(exp["name"])
        exp["date"] = escape_latex_characters(exp["date"])
        exp["role"] = escape_latex_characters(exp["role"])
        exp["location"] = escape_latex_characters(exp["location"])
        exp["descriptions"] = [
            escape_latex_characters(desc) for desc in exp["descriptions"]
        ]
    for proj in escaped_data["projectsAndLeadership"]:
        proj["name"] = escape_latex_characters(proj["name"])
        proj["date"] = escape_latex_characters(proj["date"])
        proj["role"] = escape_latex_characters(proj["role"])
        proj["location"] = escape_latex_characters(proj["location"])
        proj["descriptions"] = [
            escape_latex_characters(desc) for desc in proj["descriptions"]
        ]

    # Generate LaTeX using the escaped data
    return generate_latex_resume(escaped_data)


def write_to_tex_file(output, filename=OUTPUT_FILENAME):
    """Write the LaTeX output to a .tex file."""
    try:
        with open(filename, "w") as file:
            file.write(output)
    except Exception as e:
        print(f"Error writing to {filename}: {str(e)}")


def read_resume_data(filename=DATA_FILENAME):
    """Read resume data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: {filename} contains invalid JSON.")
        return None
