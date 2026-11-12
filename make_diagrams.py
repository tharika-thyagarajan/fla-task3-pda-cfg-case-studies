from pathlib import Path
from xml.sax.saxutils import escape

OUTPUT = Path(__file__).resolve().parent.parent / "diagrams"
OUTPUT.mkdir(exist_ok=True)


def create_svg(filename, title, subtitle, body):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
    width="1100" height="650" viewBox="0 0 1100 650">
    <rect width="1100" height="650" fill="white"/>
    <text x="550" y="55" text-anchor="middle"
          font-size="27" font-weight="bold"
          font-family="Arial">{escape(title)}</text>
    <text x="550" y="90" text-anchor="middle"
          font-size="17" font-family="Arial">{escape(subtitle)}</text>
    {body}
    </svg>"""

    path = OUTPUT / filename
    path.write_text(svg, encoding="utf-8")
    print("Created:", path.name)


def state(x, y, label, final=False):
    circle = f"""
    <circle cx="{x}" cy="{y}" r="48"
            fill="#EAF2FF" stroke="#174EA6" stroke-width="3"/>
    """
    if final:
        circle += f"""
        <circle cx="{x}" cy="{y}" r="40"
                fill="none" stroke="#174EA6" stroke-width="2"/>
        """
    return circle + f"""
    <text x="{x}" y="{y+7}" text-anchor="middle"
          font-size="22" font-family="Arial">{escape(label)}</text>
    """


def arrow(x1, y1, x2, y2, label, tx, ty):
    return f"""
    <defs>
      <marker id="arrow" markerWidth="10" markerHeight="10"
              refX="8" refY="3" orient="auto">
        <path d="M0,0 L0,6 L9,3 z" fill="#174EA6"/>
      </marker>
    </defs>
    <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"
          stroke="#174EA6" stroke-width="3"
          marker-end="url(#arrow)"/>
    <text x="{tx}" y="{ty}" text-anchor="middle"
          font-size="17" font-family="Arial"
          fill="#222">{escape(label)}</text>
    """


# DIAGRAM 1: BALANCED PARENTHESES PDA

body1 = state(300, 320, "q0") + state(800, 320, "qf", True)

body1 += arrow(100, 320, 245, 320, "Start", 170, 290)

body1 += """
<path d="M300 270 C210 100 390 100 300 270"
      fill="none" stroke="#174EA6" stroke-width="3"/>
<text x="300" y="125" text-anchor="middle"
      font-size="18" font-family="Arial">
Push (, [, { onto stack
</text>

<path d="M300 370 C210 540 390 540 300 370"
      fill="none" stroke="#174EA6" stroke-width="3"/>
<text x="300" y="535" text-anchor="middle"
      font-size="18" font-family="Arial">
Read matching closing bracket and pop
</text>
"""

body1 += arrow(350, 320, 750, 320,
               "Input consumed and stack empty", 550, 285)

create_svg(
    "01_balanced_parentheses_pda.svg",
    "BALANCED PARENTHESES - PDA",
    "Push opening brackets and pop matching closing brackets",
    body1
)


# DIAGRAM 2: ARITHMETIC EXPRESSION CFG

body2 = """
<rect x="100" y="140" width="900" height="420"
      rx="18" fill="#F3F7FF" stroke="#174EA6" stroke-width="3"/>

<text x="550" y="190" text-anchor="middle"
      font-size="25" font-weight="bold" font-family="Arial">
Context-Free Grammar Productions
</text>

<g font-family="Arial" font-size="22" fill="#222">
<text x="170" y="250">E  → T E'</text>
<text x="170" y="295">E' → + T E' | - T E' | ε</text>
<text x="170" y="340">T  → F T'</text>
<text x="170" y="385">T' → * F T' | / F T' | ε</text>
<text x="170" y="430">F  → (E) | id | number</text>
</g>

<rect x="170" y="465" width="760" height="65"
      rx="10" fill="#DCEBFF" stroke="#174EA6" stroke-width="2"/>

<text x="550" y="505" text-anchor="middle"
      font-size="19" font-family="Arial">
Example: (5 + 2) * 3
</text>
"""

create_svg(
    "02_arithmetic_expression_cfg.svg",
    "ARITHMETIC EXPRESSION VALIDATOR - CFG",
    "Grammar for arithmetic expressions with operator precedence",
    body2
)


# DIAGRAM 3: BINARY PALINDROME NPDA

body3 = state(170, 320, "q0")
body3 += state(460, 320, "q1")
body3 += state(780, 320, "q2")
body3 += state(1000, 320, "qf", True)

body3 += arrow(40, 320, 115, 320, "Start", 75, 285)

body3 += arrow(215, 320, 410, 320,
               "Read 0 / push 0", 310, 285)

body3 += arrow(460, 260, 460, 150,
               "Read 1 / push 1", 570, 190)

body3 += arrow(510, 320, 730, 320,
               "ε: Guess midpoint", 620, 285)

body3 += arrow(780, 265, 780, 150,
               "Read same symbol / pop", 900, 190)

body3 += arrow(830, 320, 950, 320,
               "Input consumed and stack empty", 890, 285)

body3 += """
<text x="460" y="440" text-anchor="middle"
      font-size="18" font-family="Arial">
Push first half
</text>
<text x="780" y="440" text-anchor="middle"
      font-size="18" font-family="Arial">
Match second half
</text>
"""

create_svg(
    "03_binary_palindrome_npda.svg",
    "BINARY PALINDROME - NPDA",
    "Nondeterministically guess the midpoint and compare symbols",
    body3
)

print("\nALL THREE DIAGRAMS CREATED SUCCESSFULLY!")