from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Route de base pour vérifier que l'application fonctionne
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI RPN Calculator API!"}

# Modèle pour les expressions
class Expression(BaseModel):
    expression: str

# Fonction pour évaluer une expression en notation polonaise inverse
def evaluate_rpn(expression):
    stack = []
    for token in expression.split():
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
        else:
            stack.append(float(token))
    return stack[0]

# Initialisation de la base de données
def init_db():
    conn = sqlite3.connect("operations.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS operations (
        id INTEGER PRIMARY KEY,
        expression TEXT,
        result REAL
    )
    """)
    conn.commit()
    conn.close()

# Endpoint pour évaluer une expression
@app.post("/evaluate/")
async def evaluate(expression: Expression):
    try:
        result = evaluate_rpn(expression.expression)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    conn = sqlite3.connect("operations.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO operations (expression, result) VALUES (?, ?)", (expression.expression, result))
    conn.commit()
    conn.close()

    return {"expression": expression.expression, "result": result}

# Endpoint pour exporter les données
@app.get("/export/")
async def export_data():
    import csv
    conn = sqlite3.connect("operations.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM operations")
    rows = cursor.fetchall()
    conn.close()

    output_dir = "data"  # Utiliser un répertoire relatif dans le répertoire courant
    os.makedirs(output_dir, exist_ok=True)  # Assure que le répertoire existe
    output_file = os.path.join(output_dir, "operations.csv")

    with open(output_file, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["id", "expression", "result"])
        csvwriter.writerows(rows)

    return {"message": f"Data exported to {output_file}"}

# Endpoint pour télécharger le fichier CSV
@app.get("/download/")
async def download_file():
    file_path = "data/operations.csv"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path=file_path, filename="operations.csv", media_type='text/csv')

init_db()
