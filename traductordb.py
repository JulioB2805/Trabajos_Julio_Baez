
import sqlite3

# Conectar y crear tabla si no existe
conexion = sqlite3.connect("bdTraductor.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS traductor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        espanol TEXT UNIQUE,
        ingles TEXT
    )
""")

# Insertar datos solo si no existen
datos = [
    ("casa", "house"),
    ("lapiz", "pen"),
    ("oro", "gold")
]

for esp, ing in datos:
    try:
        cursor.execute(
            "INSERT INTO traductor (espanol, ingles) VALUES (?, ?)",
            (esp, ing)
        )
    except sqlite3.IntegrityError:
        pass  # Ya existe, no lloramos

conexion.commit()
conexion.close()


# Traductor interactivo
while True:
    print("\nTraductor ESPAÑOL → INGLÉS")
    palabra = input("Ingresa una palabra (o 'salir'): ").lower()

    if palabra == "salir":
        print("Bye.")
        break

    conexion = sqlite3.connect("bdTraductor.db")
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT ingles FROM traductor WHERE espanol = ?",
        (palabra,)
    )

    resultado = cursor.fetchone()

    if resultado:
        print(f"{palabra} → {resultado[0]}")
    else:
        print("Palabra no encontrada.")

    conexion.close()