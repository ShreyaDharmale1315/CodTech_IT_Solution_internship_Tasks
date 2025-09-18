import pandas as pd
from fpdf import FPDF

# Create data
with open("data.csv", "w") as f:
    f.write("Name, Score, Subject\n")  # keep spaces if you want
    f.write("Priti,85,cloud computing\n")
    f.write("Shreya,90,DBMS\n")
    f.write("Mohit,78,English\n")
    f.write("Jayshri,95,physics\n")
    f.write("Rajesh,78,chemistry\n")

# Read CSV
df = pd.read_csv("data.csv")

# Strip any leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Optional: Strip spaces from string data in the DataFrame
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Analyze data (example)
summary = df.describe()

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="You are Welcome!", ln=True, align='C')

pdf.ln(10)  # Add space

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Top Records:", ln=True)

pdf.set_font("Courier", size=10)
for index, row in df.iterrows():
    line = f"{row['Name']} - {row['Score']} - {row['Subject']}"
    pdf.cell(200, 8, txt=line, ln=True)

# Save the PDF
pdf.output("Sample.pdf")
print("PDF generated successfully!")
