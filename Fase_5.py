# ============================================================
# Universidad Nacional Abierta y a Distancia — UNAD
# Fundamentos de Programación 
# Ingeniería de Sistemas
# Fase 5 - Evaluación Final POA
# Problema 2: Gestión de precios con promoción en menú
# Estudiante: Geraldine Muñoz Jaramillo
# Grupo: 213022_168
# ============================================================

# --- inicio - datos menu ---
# Matriz: [Nombre del Producto, Categoría, Precio Base]
menu = [
    ["Hamburguesa",   "Comida rápida", 18000],
    ["Pizza",         "Comida rápida", 28000],
    ["Jugo Natural",  "Bebidas",        9000],
    ["Cafe",          "Bebidas",        7000],
    ["Ensalada Cesar","Saludable",     22000],
    ["Pasta Alfredo", "Plato fuerte",  30000]
]

# --- Menu y precios ---
categoria_objetivo = "Comida rápida"
umbral_precio      = 20000   # Precio mínimo para que aplique el descuento


# --- menu / categoria y precio final ---
def calcular_precio_final(categoria, precio_base, categoria_objetivo, umbral):
    """
    Calcula el precio final de un producto aplicando
    el 15% de descuento si cumple ambas condiciones:
      - Su categoria coincide con la categoria objetivo
      - Su precio base es mayor al umbral definido

    Parametros:
        categoria          : str   - Categoria del producto
        precio_base        : float - Precio original del producto
        categoria_objetivo : str   - Categoria a la que aplica la promocion
        umbral             : float - Precio minimo para aplicar el descuento

    Retorna:
        precio_final : float - Precio con o sin descuento aplicado
    """
    if categoria == categoria_objetivo and precio_base > umbral:
        precio_final = precio_base * 0.85   # Aplica 15% de descuento
    else:
        precio_final = precio_base          # Mantiene el precio base

    return precio_final


# --- Salida / cuenta ---
print("=" * 45)
print("   MENU DEL RESTAURANTE CON PROMOCION")
print("=" * 45)
print("Categoria con descuento:", categoria_objetivo)
print("Descuento: 15% en productos con precio > $", umbral_precio)
print("=" * 45)

for producto in menu:
    nombre      = producto[0]
    categoria   = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(
        categoria,
        precio_base,
        categoria_objetivo,
        umbral_precio
    )

    print("Producto :", nombre)
    print("Categoria:", categoria)
    print("Precio base : $", precio_base)
    print("Precio final: $", round(precio_final))
    print("-" * 45)
