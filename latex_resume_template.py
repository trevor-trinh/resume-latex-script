# Preamble variable with LaTeX functions and setup
preamble = r"""%-------------------------
% Resume in Latex
% Author : Trevor Trinh
% Edited : 2023-08-06
%------------------------

% Document setup
\documentclass[letterpaper,11pt]{article}
\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}

% Hyperlink setup
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=blue,
    citecolor=blue
}

% Page style setup
\pagestyle{fancy}
\fancyhf{}
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\renewcommand{\arraystretch}{0.9}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-0.5in}
\addtolength{\textheight}{1.0in}

% URL style
\urlstyle{same}

% Layout adjustments
\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% PDF settings for machine readability
\pdfgentounicode=1


%-------------------------
% Custom commands

% Bullet point styles
\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

% Start and end commands for lists
\newcommand{\subHeadingListStart}{\begin{itemize}[leftmargin=0pt, label={}]}
\newcommand{\subHeadingListEnd}{\end{itemize}}
\newcommand{\itemListStart}{\begin{itemize}}
\newcommand{\itemListEnd}{\end{itemize}\vspace{-5pt}}

%----------
% Section heading
\newcommand{\sectionHeading}[2]{
  \vspace{-2pt}\item
    \begin{tabular*}{1\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & \textbf{#2} \\
    \end{tabular*}\vspace{-7pt}
}

% Job subheading
\newcommand{\jobSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{1\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{\small#1} & \textbf{\small#2} \\
      {\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

% Header for each experience: \experienceHeader{Name}{Date}{Role}{Location}
\newcommand{\experienceHeader}[4]{
  \jobSubheading{#1}{#2}{#3}{#4}
  \itemListStart
}

%----------
% Description bullet for each experience: \experienceItem{Description}
\newcommand{\experienceItem}[1]{
  \descriptionItem{#1}
}

% Individual description item
\newcommand{\descriptionItem}[1]{
  \item\footnotesize{
    {#1 \vspace{-2pt}}
  }
}

%----------
% Education entry: \education{Institution}{Grad Date}{Degree}{GPA or Details}{Certifications}
\newcommand{\education}[5]{
  \sectionHeading{#1}{#2}
    \item\footnotesize{
      \begin{tabular*}{1\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#3} & #4 \\
        #5 & \\
      \end{tabular*}\vspace{-5pt}
    }
}

% Coursework entry: \coursework{Courses}
\newcommand{\coursework}[1]{
  \sectionHeading{Relevant Coursework}{}
  \descriptionItem{#1}
}

% Skills entry: \skills{Technical Skills}{Software and Paradigms}
\newcommand{\skills}[2]{
  \sectionHeading{Skills}{}
  \descriptionItem{\textit{Technical Skills} - #1}
  \vspace{-7pt}
  \descriptionItem{\textit{Software \& Paradigms} - #2}
}
"""


def generate_latex_resume(data):
    """
    Generate a LaTeX resume based on structured data.
    """
    latex_output = preamble

    # Contact information
    latex_output += (
        r"""
% Main document content begins here
\begin{document}

\begin{center}
    \textbf{\huge \scshape """
        + data["name"]
        + r"""} \\
    \vspace{1pt}
    \small """
        + data["phone"]
        + r""" {\tiny{$\bullet$}} \href{mailto:"""
        + data["email"]
        + r"""}{"""
        + data["email"]
        + r"""} \\
    \href{https://"""
        + data["linkedin"]
        + r"""}{"""
        + data["linkedin"]
        + r"""} {\tiny{$\bullet$}} \href{https://"""
        + data["github"]
        + r"""}{"""
        + data["github"]
        + r"""} {\tiny{$\bullet$}} \href{https://"""
        + data["website"]
        + r"""}{"""
        + data["website"]
        + r"""}

\end{center}

\vspace{-15pt}

\section{\textbf{EDUCATION AND SKILLS}}
  \subHeadingListStart
    \education{"""
        + data["education"]["institution"]
        + r"""}{"""
        + data["education"]["grad_date"]
        + r"""}{"""
        + data["education"]["degree"]
        + r"""}{GPA: """
        + data["education"]["gpa"]
        + r"""}{"""
        + data["education"]["certifications"]
        + r"""}
    \coursework{"""
        + data["coursework"]
        + r"""}
    \skills{"""
        + data["skills"]["technical"]
        + r"""}{"""
        + data["skills"]["software"]
        + r"""}
"""
    )
    latex_output += r"""
  \subHeadingListEnd
    """

    # EXPERIENCES SECTION
    latex_output += r"""
\section{\textbf{PROFESSIONAL EXPERIENCE}}
  \subHeadingListStart"""

    for exp in data["experiences"]:
        latex_output += (
            r"""
    \experienceHeader{"""
            + exp["name"]
            + r"""}{"""
            + exp["date"]
            + r"""}{"""
            + exp["role"]
            + r"""}{"""
            + exp["location"]
            + r"""}
    """
        )
        for desc in exp["descriptions"]:
            latex_output += (
                r"""  \experienceItem{"""
                + desc
                + r"""}
    """
            )
        latex_output += r"""\itemListEnd
    """

    latex_output += r"""
  \subHeadingListEnd
    """

    # PROJECT SECTIONS
    latex_output += r"""
\section{\textbf{PROJECTS AND LEADERSHIP}}
  \subHeadingListStart"""

    for proj in data["projectsAndLeadership"]:
        latex_output += (
            r"""
    \experienceHeader{"""
            + proj["name"]
            + r"""}{"""
            + proj["date"]
            + r"""}{"""
            + proj["role"]
            + r"""}{"""
            + proj["location"]
            + r"""}
    """
        )
        for desc in proj["descriptions"]:
            latex_output += (
                r"""  \experienceItem{"""
                + desc
                + r"""}
    """
            )
        latex_output += r"""\itemListEnd
    """

    latex_output += r"""
  \subHeadingListEnd
    """

    # Close the LaTeX document
    latex_output += r"""
\end{document}
    """

    return latex_output
