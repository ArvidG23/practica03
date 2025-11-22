import csv
from collections import defaultdict

class Analizador:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.datos = []
        self._leer_archivo()

    def _leer_archivo(self):
        """
        Lee el archivo CSV separado por '|' y guarda su contenido en una lista de diccionarios.
        Convierte automáticamente los campos numéricos y normaliza claves.
        """
        try:
            with open(self.archivo_csv, mode='r', encoding='latin1', newline='') as file:
                lector = csv.DictReader(file, delimiter='|')

                for fila in lector:
                    # Normalizamos claves y valores
                    fila = {k.strip().upper(): (v.strip() if v else "") for k, v in fila.items() if k}

                    if "PROVINCIA" not in fila or "TOTAL_VENTAS" not in fila:
                        continue

                    # Intentamos convertir números. Si algo falla, saltamos la fila.
                    try:
                        fila["TOTAL_VENTAS"] = float(fila.get("TOTAL_VENTAS", 0) or 0)
                        fila["EXPORTACIONES"] = float(fila.get("EXPORTACIONES", 0) or 0)
                        fila["IMPORTACIONES"] = float(fila.get("IMPORTACIONES", 0) or 0)
                        fila["VENTAS_NETAS_TARIFA_0"] = float(fila.get("VENTAS_NETAS_TARIFA_0", 0) or 0)

                        # MES puede ser vacío → lo convertimos solo si es válido
                        mes_raw = fila.get("MES", "")
                        fila["MES"] = int(mes_raw) if mes_raw.isdigit() else None

                        self.datos.append(fila)

                    except ValueError:
                        continue

            print(f"✅ Archivo cargado correctamente ({len(self.datos)} filas).")

        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo '{self.archivo_csv}'.")
        except Exception as e:
            print("❌ Error inesperado:", e)

    # ----------------------------------------------------------------------
    # MÉTODOS ORIGINALES
    # ----------------------------------------------------------------------

    def ventas_totales_por_provincia(self):
        ventas_por_prov = {}

        for fila in self.datos:
            provincia = fila["PROVINCIA"].strip().upper()
            total = fila["TOTAL_VENTAS"]
            ventas_por_prov[provincia] = ventas_por_prov.get(provincia, 0) + total

        return ventas_por_prov

    def ventas_por_provincia(self, nombre):
        nombre = nombre.strip().upper()
        total = sum(f["TOTAL_VENTAS"] for f in self.datos if f["PROVINCIA"].strip().upper() == nombre)
        return total

    # ----------------------------------------------------------------------
    # NUEVOS MÉTODOS PARA EL TRABAJO AUTÓNOMO
    # ----------------------------------------------------------------------

    def exportaciones_totales_por_mes(self):
        """
        Suma exportaciones agrupadas por MES.
        Retorna {mes: total_exportaciones}
        """
        export_por_mes = defaultdict(float)

        for fila in self.datos:
            mes = fila.get("MES")
            if mes is None:
                continue
            export_por_mes[mes] += fila.get("EXPORTACIONES", 0.0)

        return dict(export_por_mes)

    def provincia_con_mayor_importaciones(self):
        """
        Retorna la provincia que tiene mayor total de importaciones.
        Devuelve (provincia, total_importaciones)
        """
        import_por_prov = defaultdict(float)

        for fila in self.datos:
            provincia = fila["PROVINCIA"].strip().upper()
            import_por_prov[provincia] += fila.get("IMPORTACIONES", 0.0)

        if not import_por_prov:
            return (None, 0.0)

        # devuelve la provincia con mayor total de importaciones
        return max(import_por_prov.items(), key=lambda x: x[1])
