# Weather Simulator

Simulador de estaciones meteorológicas para análisis y visualización de temperaturas diarias de diferentes ciudades.

## Características

- Añade nuevas estaciones meteorológicas y genera datos aleatorios de temperatura simulados con numpy.
- Guarda los datos en formato JSON.
- Visualiza la evolución de temperaturas mínimas, medias y máximas de cada ciudad durante 30 días.
- Gráficas comparativas entre ciudades usando Matplotlib.
- Menús interactivos en terminal para gestionar estaciones y análisis.

## Estructura del Proyecto

```
weather_simulator/
│
├── menu.py
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── weather.py
│   ├── graph.py
│   └── utils/
│       ├── __init__.py
│       ├── utils.py
│       ├── validation.py
│       ├── dict_builder.py
│       └── json_builder.py
│
└── src/data/
    └── station_data.json
```

## Instalación

1. Clona el repositorio.
2. Instala las dependencias:

```sh
pip install -r requirements.txt
```

## Uso

Ejecuta el menú principal:

```sh
python menu.py
```

Desde el menú podrás:

- Añadir nuevas estaciones meteorológicas.
- Visualizar y analizar los datos de temperatura.
- Generar gráficas de comparación entre ciudades.

## Ejemplo de Uso

1. Añade una nueva estación introduciendo el nombre de la ciudad.
2. El sistema generará automáticamente 30 días de datos de temperatura (Min Temp., Med. Temp., Max. Temp.).
3. Selecciona el tipo de análisis o gráfica que deseas visualizar.

## Dependencias

- numpy
- matplotlib

Consulta [requirements.txt](requirements.txt) para la lista completa.

## Estructura de Datos

Los datos de cada ciudad se almacenan en `src/data/station_data.json` con la siguiente estructura:

```json
{
  "Madrid": {
    "Day-1": {"min_temp": 19, "med_temp": 25, "max_temp": 31},
    ...
    "Day-30": {"min_temp": 19, "med_temp": 24, "max_temp": 32}
  },
  ...
}
```