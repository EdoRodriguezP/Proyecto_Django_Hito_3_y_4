from django.db import models
from django.core.exceptions import ValidationError
import uuid
from PIL import Image

# Create your models here.
from django.db import models

class Producto(models.Model):
    nombre = models.CharField("nombre", max_length=50)
    descripcion = models.TextField("descripcion")
    precio = models.DecimalField("precio", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("stock", default=0)
    creado = models.DateTimeField('creado', auto_now_add=True)
    actualizado = models.DateTimeField("actualizado", auto_now=True)
    imagen = models.ImageField("imagen principal", upload_to="productos/", blank=True, null=True)
    premium = models.BooleanField("premium", default=False)

    def __str__(self):
        return self.nombre


class Contactoform(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    customer_message = models.TextField()


class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/imagenes/')
    orden = models.PositiveIntegerField(default=0)  # Para ordenar imágenes

    def __str__(self):
        return f"Imagen de {self.producto.nombre} (Orden {self.orden})"

    def clean(self):
        # Validar máximo de 6 imágenes por producto
        if self.producto_id and not self.pk:
            if self.producto.imagenes.count() >= 6:
                raise ValidationError("No se pueden subir más de 6 imágenes por producto.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Validaciones
        super().save(*args, **kwargs)  # Guardar primero

        # --- Recorte automático ---
        if self.imagen:
            img_path = self.imagen.path
            img = Image.open(img_path)

            # Convertir a RGB si tiene transparencia
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Tamaño objetivo
            target_size = (1200, 1200)  # Cambia si quieres otro tamaño

            # Obtener proporción de la imagen
            width, height = img.size
            aspect_ratio = width / height
            target_ratio = target_size[0] / target_size[1]

            # Recorte al centro manteniendo proporción
            if aspect_ratio > target_ratio:
                # Imagen más ancha → recortar lados
                new_width = int(target_ratio * height)
                left = (width - new_width) // 2
                img = img.crop((left, 0, left + new_width, height))
            else:
                # Imagen más alta → recortar arriba y abajo
                new_height = int(width / target_ratio)
                top = (height - new_height) // 2
                img = img.crop((0, top, width, top + new_height))

            # Redimensionar al tamaño final
            img = img.resize(target_size, Image.LANCZOS)

            # Guardar sobre el mismo archivo
            img.save(img_path, format="JPEG", quality=90)
