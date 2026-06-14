# Gestión de Datos de Países en Python

**Trabajo Práctico Integrador — Programación 1 |**
Universidad Tecnológica Nacional — Tecnicatura Universitaria en Programación a Distancia (TUPaD)

---

## Descripción del proyecto

Sistema de gestión de información sobre países del mundo desarrollado en Python.
Permite cargar datos desde un archivo CSV y realizar búsquedas, filtros, ordenamientos
y estadísticas desde un menú interactivo en consola.

---

## Datos institucionales

| Campo | Detalle |
|---|---|
| Universidad | Universidad Tecnológica Nacional (UTN) |
| Carrera | Tecnicatura Universitaria en Programación a Distancia |
| Materia | Programación 1 |
| Docente | Alberto Cortez |

---

## 👤 Integrante

| Nombre |
|---|---|
| Jorge Puz Benítez | [@JorgePuz](https://github.com/JorgePuz) |

---

## 📁 Estructura del repositorio

```
TPI_Programacion_Jorge_Puz_Benitez/
│
├── TPI_Programacion_Jorge_Puz_Benitez.py   
├── paises.csv                              
├── README.md                                
└── Informe_TPI_Programacion1.pdf           
```

---

## Instrucciones de ejecución

### Requisitos
- Python 3. instalado
- No requiere librerías externas (solo el módulo `csv` de la biblioteca estándar)

### Pasos

**1.** Cloná el repositorio:
```bash
git clone https://github.com/JorgePuz/TPI_Programacion_Jorge_Puz_Benitez.git
cd TPI_Programacion_Jorge_Puz_Benitez
```

**2.** Verificá que el archivo `paises.csv` esté en la misma carpeta que el `.py`

**3.** Ejecutá el programa:

py TPI_Programacion_Jorge_Puz_Benitez.py

---

## Dataset — paises.csv

Cada país contiene los siguientes campos:

| Campo | Tipo | Descripción |
|---|---|---|
| nombre | string | Nombre del país |
| poblacion | int | Cantidad de habitantes |
| superficie | int | Superficie en km² |
| continente | string | Continente al que pertenece |

**Ejemplo:**
```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
```

---

## Funcionalidades

| Opción | Función |
|---|---|
| 1 | Agregar un país (valida campos vacíos y duplicados) |
| 2 | Actualizar población y superficie de un país existente |
| 3 | Buscar país por nombre (parcial o exacto) |
| 4 | Filtrar por continente, rango de población o superficie |
| 5 | Ordenar por nombre, población o superficie (asc/desc) |
| 6 | Ver estadísticas: máximos, mínimos, promedios y conteo por continente |
| 7 | Listar todos los países |
| 0 | Guardar cambios y salir |

---

## Ejemplos de entrada y salida

### Agregar un país
```
--- AGREGAR PAÍS ---
  Nombre del país: España
  Población: 47420000
  Superficie en km: 505990
  Continente: Europa
  'España' agregado correctamente.
```

### Buscar por nombre parcial
```
--- BUSCAR PAÍS ---
  Ingresá el nombre o parte del nombre: ar

  Se encontraron 1 resultado:

  NOMBRE                    POBLACIÓN      SUPERFICIE   CONTINENTE
  ──────────────────────────────────────────────────────────────────
  Argentina            45,376,763      2,780,400    América
  
```

### Estadísticas
```
--- ESTADÍSTICAS ---

  Población:
    Mayor:    China (1,411,778,724 hab.)
    Menor:    Australia (25,690,000 hab.)
    Promedio: 358,420,423 hab.

  Superficie:
    Mayor:    China (9,596,960 km²)
    Menor:    Japón (377,975 km²)
    Promedio: 2,566,553 km²

  Países por continente:
    América         3 país/es
    Asia            3 país/es
    Europa          2 país/es
    África          1 país/es
    Oceanía         1 país/es
```

### Ordenar por población descendente
```
--- ORDENAR PAÍSES ---
  1. Por nombre
  2. Por población
  3. Por superficie
  Elegí criterio: 2
  ¿Orden? (a=ascendente / d=descendente): d

  NOMBRE                    POBLACIÓN      SUPERFICIE   CONTINENTE
  ──────────────────────────────────────────────────────────────────
  China                1,411,778,724      9,596,960    Asia
  India                1,393,409,038      3,287,263    Asia
  Brasil                 213,993,437      8,515,767    América
  ...
```

---

## Documentación

El informe académico en PDF se encuentra en la raíz del repositorio:  
📎 [Informe_TPI_Programacion1.pdf](./Informe_TPI_Programacion1_Jorge_Puz_Benitez.pdf)

---

## Video explicativo

📹 [Ver video en YouTube](https://youtu.be/PTDYz29WqpM)

---

## Conceptos aplicados

- **Listas** — estructura principal para almacenar los países
- **Diccionarios** — cada país es un diccionario de clave/valor
- **Funciones** — modularización con responsabilidad única
- **Condicionales** — control de flujo y validaciones
- **Algoritmo de burbuja** — ordenamiento manual sin librerías externas
- **Estadísticas básicas** — máximo, mínimo, promedio y conteo
- **Archivos CSV** — lectura y escritura con el módulo `csv`
