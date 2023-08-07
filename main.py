from utils import (
    read_resume_data,
    generate_latex_resume_escaped,
    write_to_tex_file,
    OUTPUT_FILENAME,
)


def main():
    """Main function to generate the LaTeX resume."""
    resume_data = read_resume_data()
    latex_output = generate_latex_resume_escaped(resume_data)
    write_to_tex_file(latex_output)
    print(f"LaTeX document written to {OUTPUT_FILENAME}! 🎉")


if __name__ == "__main__":
    main()
