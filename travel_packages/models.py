from django.db import models


class TravelPackages(models.Model):
    image = models.ImageField(upload_to="travel_packages/", verbose_name="Imagem")
    name = models.CharField(max_length=255, verbose_name="Nome")
    original_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Preço Original"
    )
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Desconto"
    )
    final_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Preço Final", editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Edição")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "travel_packages"
        verbose_name = "Pacote de Viagem"
        verbose_name_plural = "Pacotes de Viagem"

    def save(self, *args, **kwargs):
        # Calcular o preço final antes de salvar
        self.final_price = self.original_price - self.discount
        super().save(*args, **kwargs)

    def get_discount(self):
        return "%.2f" % self.discount

    def get_final_price(self):
        return "%.2f" % self.final_price

    def get_original_price(self):
        return "%.2f" % self.original_price

    get_discount.short_description = "Desconto"
    get_final_price.short_description = "Preço Final"
    get_original_price.short_description = "Preço Original"
