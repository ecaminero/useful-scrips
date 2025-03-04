# CLI Tool

Herramienta que contiene comandos utiles para usar usados en google o cualquier otra cloud, no se limita en funcionalidades

## Descripción

CLI Tool es una utilidad de línea de comandos diseñada para simplificar operaciones frecuentes en diferentes entornos cloud como Google Cloud, AWS, Azure y otros. Esta herramienta ofrece comandos para verificar fechas de modificación, obtener tamaños de carpetas, monitorear recursos, y otras operaciones útiles para el trabajo diario en la nube. La herramienta no se limita en funcionalidades y puede expandirse según las necesidades del usuario.


## Requisitos

- Python 3.6 o superior
- Paquetes de Python:
  - `click`
  - `google-cloud-storage`

## Instalación

1. Clona este repositorio o descarga el script:
   ```bash
   git clone  git@github.com:ecaminero/useful-scrips.git
   cd useful-scrips
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Comando general

```bash
python [SCRIPT].py [OPCIONES] COMANDO [ARGUMENTOS]
```


## Ejemplos

### Obtener la última modificación de una carpeta

```bash
python google-cloud-storage.py last-modified --bucket NOMBRE_BUCKET --folder RUTA_CARPETA
```

## Personalización

Puedes extender esta herramienta fácilmente añadiendo nuevos comandos al grupo CLI de Click. Consulta la [documentación de Click](https://click.palletsprojects.com/) para más información.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, siente libre de enviar un Pull Request o abrir un Issue si encuentras algún problema o tienes sugerencias de mejora.

## Licencia

[MIT](LICENSE)