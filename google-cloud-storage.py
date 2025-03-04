#!/usr/bin/env python3
import click
from google.cloud import storage

line = "__"

@click.group()
def cli():
    """Herramienta para realizar operaciones con objetos en Google Cloud Storage."""
    pass

@cli.command(name="last-modified")
@click.option('--bucket_name', '-b', required=True, help='Nombre del bucket de GCS')
@click.option('--folder_prefix', '-f', required=True, help='Ruta de la carpeta en GCS')
def get_folder_last_modified(bucket_name, folder_prefix):
    """
    Obtiene la fecha de modificación más reciente de objetos en un prefijo de GCS
    
    Args:
        bucket_name: Nombre del bucket de GCS
        folder_prefix: Prefijo de la "carpeta" (debe terminar con /)
        
    Returns:
        La fecha de modificación más reciente (datetime) y el nombre del blob
    """
    if not folder_prefix.endswith('/'):
        folder_prefix += '/'
    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=folder_prefix)
    
    latest_modified = None
    latest_blob_name = None
    
    for blob in blobs:
        if blob.name == folder_prefix:
            continue
        
        if latest_modified is None or blob.updated > latest_modified:
            latest_modified = blob.updated
            latest_blob_name = blob.name
    
    click.echo(line*20)
    click.echo('Resumen:')
    click.echo(f"Latest Modified '{latest_modified}' ")
    click.echo(f"Blob name '{latest_blob_name}' ")


@cli.command(name="size")
@click.option('--bucket', '-b', required=True, help='Nombre del bucket de GCS')
@click.option('--folder', '-f', required=True, help='Ruta de la carpeta en GCS')
def size(bucket, folder):
    """
    Calcula el tamaño total de todos los objetos en un prefijo (carpeta) de Google Cloud Storage.
    """
    def format_size(size_in_bytes):
        """Formatea un tamaño en bytes a una unidad legible (KB, MB, GB, TB)."""
        units = ['bytes', 'KB', 'MB', 'GB', 'TB']
        unit_index = 0
        size = float(size_in_bytes)
        while size >= 1024 and unit_index < len(units) - 1:
            size /= 1024
            unit_index += 1
        if unit_index == 0:
            return f"{size:.0f} {units[unit_index]}"
        else:
            return f"{size:.2f} {units[unit_index]}"
    
    if not folder.endswith('/'):
        folder += '/'

    storage_client = storage.Client()
    bucket_obj = storage_client.bucket(bucket)
    blobs = bucket_obj.list_blobs(prefix=folder)
    total_size = 0

    for blob in blobs:
        if blob.name == folder:
            continue
        total_size += blob.size
    

    formatted_size = format_size(total_size)
    click.echo(line*20)
    click.echo('Resumen:')
    
    click.echo(f"Bucket '{bucket}' ")
    click.echo(f"Folder Size '{folder}': {formatted_size} ({total_size} bytes) ")

if __name__ == '__main__':
    cli()