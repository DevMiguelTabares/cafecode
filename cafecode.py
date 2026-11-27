"""
Programa: cafecode.py
Proyecto: CaféCode · sistema de la tostadora de café
Autor: MIGUEL ANGEL TABARES RENDON · Ficha 3601599
Fecha: 2026-11-26
Versión: 1.0
Descripción: Sistema de consola para gestionar ventas, registro, consulta,
retiro y resumen diario de lotes de café en la tostadora CaféCode.
"""

# =====================================================================
# HITO 1 · CaféCode v1.0 · Menú + inventario
# =====================================================================

# ---------------------------------------------------------------------
# 1. CONSTANTES
# ---------------------------------------------------------------------
NOMBRE_TOSTADORA = "CaféCode · Tostadora de Café"
ANCHO = 40
ANCHO_TABLA = 60

# Ventas (semana 2)
PRECIO_LIBRA_ESPECIAL = 38000     # pesos por libra
PRECIO_LIBRA_TRADICIONAL = 26000
PORCENTAJE_DESCUENTO = 0.05       # descuento de temporada: 5 %
LIBRAS_TABLA = 5                  # filas de la tabla de precios

# Clasificación (semana 3)
PUNTAJE_MINIMO = 0
PUNTAJE_MAXIMO = 100
PUNTAJE_EXCEPCIONAL = 90
PUNTAJE_EXCELENTE = 85
PUNTAJE_ESPECIAL = 80
HUMEDAD_MINIMA = 10.0
HUMEDAD_MAXIMA = 12.0
HUMEDAD_POSIBLE = 100.0
PRECIO_EXCEPCIONAL = 52000
PRECIO_EXCELENTE = 45000
PRECIO_ESPECIAL = 38000
PRECIO_COMERCIAL = 26000

# PARTE B.1 · Tupla inmutable de orígenes
ORIGENES = ("Chinchiná", "Neira", "Villamaría", "Palestina", "Aguadas")

# ---------------------------------------------------------------------
# 2. DATOS DEL DÍA · PARTE B.2
# ---------------------------------------------------------------------
inventario = [
    {"codigo": "L-01", "origen": "Chinchiná", "kilos": 120.0,
     "puntaje": 86.5, "humedad": 11.2, "categoria": "Excelente",
     "precio_libra": 45000, "estado": "Apto para tostión"},
    {"codigo": "L-02", "origen": "Neira", "kilos": 85.0,
     "puntaje": 82.0, "humedad": 10.8, "categoria": "Muy bueno (especial)",
     "precio_libra": 38000, "estado": "Apto para tostión"},
    {"codigo": "L-03", "origen": "Villamaría", "kilos": 60.0,
     "puntaje": 78.5, "humedad": 12.4, "categoria": "Comercial",
     "precio_libra": 26000, "estado": "Muy húmedo: más secado"},
]
ventas = []      # cada venta será un diccionario: cliente, libras, total

# ---------------------------------------------------------------------
# 3. MENÚ PRINCIPAL
# ---------------------------------------------------------------------
opcion = ""
while opcion != "0":
    print()
    print("=" * ANCHO)
    print(f"{NOMBRE_TOSTADORA:^{ANCHO}}")
    print("=" * ANCHO)
    print("1. Registrar venta")
    print("2. Registrar lote")
    print("3. Ver inventario")
    print("4. Buscar lote")
    print("5. Retirar lote")
    print("6. Tabla de precios")
    print("7. Resumen del día")
    print("0. Salir")
    opcion = input("Elige una opción: ").strip()

    match opcion:
        case "1":
            # ---------- REGISTRAR VENTA (base v0.4) ----------
            nombre_cliente = input("Nombre del cliente: ").strip()
            while nombre_cliente == "":
                print("  Error: el nombre no puede estar vacío.")
                nombre_cliente = input("Nombre del cliente: ").strip()

            texto = input("Libras de café especial: ").strip()
            texto = texto.replace(",", ".")
            while not texto.replace(".", "", 1).isdigit():
                print("  Error: escribe un número positivo, ej. 2,5.")
                texto = input("Libras de café especial: ").strip()
                texto = texto.replace(",", ".")
            libras_especial = float(texto)

            texto = input("Libras de café tradicional: ").strip()
            texto = texto.replace(",", ".")
            while not texto.replace(".", "", 1).isdigit():
                print("  Error: escribe un número positivo, ej. 2,5.")
                texto = input("Libras de café tradicional: ").strip()
                texto = texto.replace(",", ".")
            libras_tradicional = float(texto)

            libras_venta = libras_especial + libras_tradicional
            if libras_venta == 0:
                print("La venta no tiene café. No se registró.")
                continue

            valor_especial = libras_especial * PRECIO_LIBRA_ESPECIAL
            valor_tradicional = libras_tradicional * PRECIO_LIBRA_TRADICIONAL
            subtotal = valor_especial + valor_tradicional
            descuento = subtotal * PORCENTAJE_DESCUENTO
            total = subtotal - descuento

            # PARTE C · Guardar la venta en la lista
            venta = {
                "cliente": nombre_cliente,
                "libras": libras_venta,
                "total": total,
            }
            ventas.append(venta)

            total_txt = f"${total:,.0f}".replace(",", ".")
            print("-" * ANCHO)
            print(f"{'Cliente:':<16}{nombre_cliente}")
            print(f"{'Libras:':<16}" + f"{libras_venta:.1f}".replace(".", ","))
            print(f"{'Total a pagar:':<16}{total_txt}")
            print(f"Venta n.° {len(ventas)} registrada.")

        case "2":
            # ---------- PARTE D · REGISTRAR LOTE ----------
            while True:
                codigo_lote = input("Código del lote: ").strip().upper()
                codigos = [lote["codigo"] for lote in inventario]
                if codigo_lote == "":
                    print("  Error: el código no puede estar vacío.")
                    continue
                if codigo_lote in codigos:
                    print("  Error: ya existe un lote con ese código.")
                    continue
                break

            print("Orígenes disponibles:")
            for i in range(len(ORIGENES)):
                print(f"  {i + 1}. {ORIGENES[i]}")

            while True:
                opcion_origen = input("Elige el número de origen: ").strip()
                if not opcion_origen.isdigit():
                    print(f"  Error: el número debe estar entre 1 "
                          f"y {len(ORIGENES)}.")
                    continue
                num_origen = int(opcion_origen)
                if 1 <= num_origen <= len(ORIGENES):
                    origen = ORIGENES[num_origen - 1]
                    break
                print(f"  Error: el número debe estar entre 1 "
                      f"y {len(ORIGENES)}.")

            while True:
                texto = input("Kilos del lote: ").strip()
                texto = texto.replace(",", ".")
                if not texto.replace(".", "", 1).isdigit():
                    print("  Error: los kilos son un número, ej. 85,0.")
                    continue
                kilos = float(texto)
                if kilos > 0:
                    break
                print("  Error: los kilos deben ser mayores que 0.")

            while True:
                texto = input("Puntaje de catación (0 a 100): ").strip()
                texto = texto.replace(",", ".")
                if not texto.replace(".", "", 1).isdigit():
                    print("  Error: el puntaje es un número, ej. 86,5.")
                    continue
                puntaje = float(texto)
                if PUNTAJE_MINIMO <= puntaje <= PUNTAJE_MAXIMO:
                    break
                print("  Error: el puntaje debe estar entre 0 y 100.")

            while True:
                texto = input("Humedad del grano (%): ").strip()
                texto = texto.replace(",", ".")
                if not texto.replace(".", "", 1).isdigit():
                    print("  Error: la humedad es un número, ej. 11,2.")
                    continue
                humedad = float(texto)
                if humedad <= HUMEDAD_POSIBLE:
                    break
                print("  Error: la humedad no puede pasar de 100 %.")

            if puntaje >= PUNTAJE_EXCEPCIONAL:
                categoria = "Excepcional"
                precio_libra = PRECIO_EXCEPCIONAL
            elif puntaje >= PUNTAJE_EXCELENTE:
                categoria = "Excelente"
                precio_libra = PRECIO_EXCELENTE
            elif puntaje >= PUNTAJE_ESPECIAL:
                categoria = "Muy bueno (especial)"
                precio_libra = PRECIO_ESPECIAL
            else:
                categoria = "Comercial"
                precio_libra = PRECIO_COMERCIAL

            if HUMEDAD_MINIMA <= humedad <= HUMEDAD_MAXIMA:
                estado_humedad = "Apto para tostión"
            elif humedad < HUMEDAD_MINIMA:
                estado_humedad = "Muy seco: revisar bodega"
            else:
                estado_humedad = "Muy húmedo: más secado"

            lote = {
                "codigo": codigo_lote,
                "origen": origen,
                "kilos": kilos,
                "puntaje": puntaje,
                "humedad": humedad,
                "categoria": categoria,
                "precio_libra": precio_libra,
                "estado": estado_humedad,
            }
            inventario.append(lote)

            precio_txt = f"${precio_libra:,.0f}".replace(",", ".")
            kilos_txt = f"{kilos:.1f}".replace(".", ",")
            print("-" * ANCHO)
            print(f"{'Lote:':<16}{codigo_lote} ({origen}, {kilos_txt} kg)")
            print(f"{'Categoría:':<16}{categoria}")
            print(f"{'Precio por lb:':<16}{precio_txt}")
            print(f"{'Estado:':<16}{estado_humedad}")
            print(f"Lote agregado. Lotes en inventario: {len(inventario)}")

        case "3":
            # ---------- PARTE E · VER INVENTARIO ----------
            if len(inventario) == 0:
                print("El inventario está vacío.")
            else:
                print("-" * ANCHO_TABLA)
                print(f"{'Código':<8}{'Origen':<12}{'Kilos':>8}"
                      f"{'Puntaje':>9}  {'Categoría'}")
                print("-" * ANCHO_TABLA)
                for lote in inventario:
                    kilos_txt = f"{lote['kilos']:.1f}".replace(".", ",")
                    puntaje_txt = f"{lote['puntaje']:.1f}".replace(".", ",")
                    print(f"{lote['codigo']:<8}{lote['origen']:<12}"
                          f"{kilos_txt:>8}{puntaje_txt:>9}"
                          f"{lote['categoria']}")
                print("-" * ANCHO_TABLA)
                total_kilos = sum([lote["kilos"] for lote in inventario])
                total_kilos_txt = f"{total_kilos:.1f}".replace(".", ",")
                print(f"{len(inventario)} lotes · {total_kilos_txt} kg")

        case "4":
            # ---------- PARTE F · BUSCAR LOTE ----------
            codigo_buscado = input(
              "Código del lote a buscar: ").strip().upper()
            encontrado = None
            for lote in inventario:
                if lote["codigo"] == codigo_buscado:
                    encontrado = lote
                    break

            if encontrado is None:
                print(f"No existe un lote con el código {codigo_buscado}.")
            else:
                precio_txt = (
                  f"${encontrado['precio_libra']:,.0f}".replace(",", ".")
                )
                kilos_txt = f"{encontrado['kilos']:.1f}".replace(".", ",")
                puntaje_txt = f"{encontrado['puntaje']:.1f}".replace(".", ",")
                humedad_txt = f"{encontrado['humedad']:.1f}".replace(".", ",")
                print("-" * ANCHO)
                print(f"{'Código:':<16}{encontrado['codigo']}")
                print(f"{'Origen:':<16}{encontrado['origen']}")
                print(f"{'Kilos:':<16}{kilos_txt} kg")
                print(f"{'Puntaje:':<16}{puntaje_txt}")
                print(f"{'Humedad:':<16}{humedad_txt} %")
                print(f"{'Categoría:':<16}{encontrado['categoria']}")
                print(f"{'Precio por lb:':<16}{precio_txt}")
                print(f"{'Estado:':<16}{encontrado['estado']}")

        case "5":
            # ---------- PARTE G · RETIRAR LOTE ----------
            codigo_retirar = input(
              "Código del lote a retirar: ").strip().upper()
            encontrado = None
            for lote in inventario:
                if lote["codigo"] == codigo_retirar:
                    encontrado = lote
                    break

            if encontrado is None:
                print(f"No existe un lote con el código {codigo_retirar}.")
            else:
                inventario.remove(encontrado)
                print(f"Lote {codigo_retirar} retirado. "
                      f"Lotes en inventario: {len(inventario)}")

        case "6":
            # ---------- TABLA DE PRECIOS (base v0.4) ----------
            print("-" * ANCHO)
            print(f"{'Libras':<8}{'Especial':>16}{'Tradicional':>16}")
            for libras in range(1, LIBRAS_TABLA + 1):
                especial = libras * PRECIO_LIBRA_ESPECIAL
                tradicional = libras * PRECIO_LIBRA_TRADICIONAL
                especial_txt = f"${especial:,.0f}".replace(",", ".")
                tradicional_txt = f"${tradicional:,.0f}".replace(",", ".")
                print(f"{libras:<8}{especial_txt:>16}{tradicional_txt:>16}")

        case "7":
            # ---------- PARTE H · RESUMEN DEL DÍA ----------
            print("-" * ANCHO)
            print("RESUMEN DE VENTAS")
            if len(ventas) == 0:
                print("Todavía no hay ventas hoy.")
            else:
                libras_vendidas = sum([v["libras"] for v in ventas])
                total_vendido = sum([v["total"] for v in ventas])
                venta_promedio = total_vendido / len(ventas)
                venta_mas_alta = max([v["total"] for v in ventas])

                libras_txt = f"{libras_vendidas:.1f}".replace(".", ",")
                total_txt = f"${total_vendido:,.0f}".replace(",", ".")
                promedio_txt = f"${venta_promedio:,.0f}".replace(",", ".")
                alta_txt = f"${venta_mas_alta:,.0f}".replace(",", ".")

                print(f"{'Ventas:':<20}{len(ventas)}")
                print(f"{'Libras vendidas:':<20}{libras_txt}")
                print(f"{'Total vendido:':<20}{total_txt}")
                print(f"{'Venta promedio:':<20}{promedio_txt}")
                print(f"{'Venta más alta:':<20}{alta_txt}")

            print("-" * ANCHO)
            print("RESUMEN DE INVENTARIO")
            if len(inventario) == 0:
                print("El inventario está vacío.")
            else:
                kilos_inv = sum([lote["kilos"] for lote in inventario])
                lotes_especiales = len([
                    lote for lote in inventario
                    if lote["categoria"] != "Comercial"
                ])
                origenes = set([lote["origen"] for lote in inventario])
                kilos_inv_txt = f"{kilos_inv:.1f}".replace(".", ",")

                print(f"{'Lotes:':<20}{len(inventario)}")
                print(f"{'Kilos:':<20}{kilos_inv_txt}")
                print(f"{'Lotes especiales:':<20}{lotes_especiales}")
                print(f"{'Orígenes:':<20}{', '.join(sorted(origenes))}")

        case "0":
            print("Cerrando CaféCode...")

        case _:
            print("Opción no válida. Elige un número del menú.")

# ---------------------------------------------------------------------
# 4. CIERRE · PARTE H
# ---------------------------------------------------------------------
total_dia = sum([venta["total"] for venta in ventas])
total_dia_txt = f"${total_dia:,.0f}".replace(",", ".")
print(f"Ventas del día: {len(ventas)} · Total: {total_dia_txt}")
print("¡Hasta pronto!")
