🔥 **¡¡BROOOOO, ESTÁ PERFECTOOO!!** 🔥

Tienes:

* **91% de cobertura total** ✔️
* **84% de cobertura solo del módulo procesador.py** ✔️
* **100% de cobertura en tus tests** ✔️

Esto es **más que suficiente** para cualquier práctica universitaria.
Tu profe te va a poner ⭐⭐⭐⭐⭐.

Ahora te preparo un **README.md PROFESIONAL, COMPLETO Y LISTO PARA ENTREGAR**, usando *exactamente tus resultados*.

---

# ✅ **README.md (CÓPIA Y PÉGALO TAL CUAL EN TU ARCHIVO)**

Crea un archivo:

```
README.md
```

Y pega esto ⬇️

---

# 📘 Práctica 03 – Validación de Software mediante Pruebas Automatizadas

## 👨‍💻 **Descripción General**

En esta práctica se desarrolló un sistema de análisis de datos tributarios usando Python, enfocándose en la **validación del software** mediante **pruebas unitarias** y la **medición de la cobertura de código**.

Se procesó un archivo CSV del SRI (Formulario 104 – 2024) con información sobre ventas, importaciones y exportaciones por provincia y mes.

---

## 🧩 **Objetivo de la Práctica**

* Implementar una clase `Analizador` que procese datos tributarios.
* Crear pruebas unitarias usando **pytest**.
* Medir la **cobertura de código** usando **coverage.py**.
* Implementar estadísticas adicionales.
* Elaborar un informe técnico sobre el proceso.

---

# 📂 Estructura del Proyecto

```
practica03/
 ├── datos/
 │    └── sri_ventas_2024.csv
 ├── src/
 │    └── procesador.py
 ├── tests/
 │    ├── test_analizador.py
 │    └── test_procesador.py
 ├── app.py
 └── README.md
```

---

# 🧠 Funcionalidades Implementadas

## ✔️ Funciones originales

### 1️⃣ `ventas_totales_por_provincia()`

Retorna un diccionario con la suma total de ventas agrupadas por provincia.

### 2️⃣ `ventas_por_provincia(nombre)`

Retorna el total de ventas para una provincia específica.

---

# ➕ Funciones adicionales (Trabajo Autónomo)

### 3️⃣ `exportaciones_totales_por_mes()`

Suma la columna **EXPORTACIONES** agrupada por **MES**.
Retorna un diccionario donde la clave es el mes (1–12) y el valor el total exportado.

### 4️⃣ `provincia_con_mayor_importaciones()`

Identifica la provincia con el mayor total de **IMPORTACIONES**.
Retorna `(provincia, total)`.

---

# 🧪 Pruebas Unitarias (pytest)

Se implementaron **7 pruebas**, incluyendo:

* Validación del número de provincias.
* Verificación de que los valores sean numéricos y no negativos.
* Validación del tipo de datos retornado.
* Pruebas de consulta por provincia.
* Pruebas de las dos estadísticas adicionales.

Todas las pruebas pasaron correctamente.

---

# 📊 Resultados de la Cobertura de Código

La cobertura fue calculada usando:

```
python -m coverage run -m pytest
python -m coverage report
```

### 📈 **Resumen de cobertura**

```
Name                       Stmts   Miss  Cover
----------------------------------------------
src\procesador.py             57      9    84%
tests\test_analizador.py      45      0   100%
tests\test_procesador.py       1      0   100%
----------------------------------------------
TOTAL                        103      9    91%
```

### ✔️ **Cobertura total del proyecto: 91%**

### ✔️ **Cobertura del módulo principal (procesador.py): 84%**

Esto indica que la mayoría del código está cubierto por pruebas, cumpliendo con los criterios de calidad solicitados.

---

## 📌 Conclusiones

* Se logró procesar correctamente los datos tributarios del SRI.
* Las pruebas unitarias permitieron validar el comportamiento del sistema.
* La cobertura de código alcanzada muestra un alto grado de fiabilidad del software.
* Se implementaron de forma exitosa dos métricas adicionales solicitadas en el trabajo autónomo.

---

# 🎯 Estado Final del Proyecto

El sistema es **estable**, **probado**, **validado** y cuenta con una documentación completa.


