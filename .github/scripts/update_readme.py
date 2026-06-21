import os, re

def problem_num(f):
    m = re.search(r'(\d+)', f)
    return int(m.group(1)) if m else 0

def build_table(folder):
    if not os.path.isdir(folder):
        return "| File | Problem |\n|------|---------|"
    files = sorted([f for f in os.listdir(folder) if f.endswith('.md')], key=problem_num)
    if not files:
        return "| File | Problem |\n|------|---------|"
    rows = ["| File | Problem |", "|------|---------|"]
    for f in files:
        m = re.search(r'(\d+)', f)
        label = f"Problem {m.group(1)}" if m else f
        rows.append(f"| [{f}](./{folder}/{f}) | {label} |")
    return "\n".join(rows)

with open("README.md", "r") as fh:
    content = fh.read()

content = re.sub(
    r'<!-- CPP-TABLE-START -->.*?<!-- CPP-TABLE-END -->',
    f'<!-- CPP-TABLE-START -->\n{build_table("C++")}\n<!-- CPP-TABLE-END -->',
    content, flags=re.DOTALL
)
content = re.sub(
    r'<!-- JAVA-TABLE-START -->.*?<!-- JAVA-TABLE-END -->',
    f'<!-- JAVA-TABLE-START -->\n{build_table("Java")}\n<!-- JAVA-TABLE-END -->',
    content, flags=re.DOTALL
)

with open("README.md", "w") as fh:
    fh.write(content)

print("Done!")