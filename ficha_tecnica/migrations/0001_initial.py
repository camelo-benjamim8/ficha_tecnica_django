# Generated by Django 3.2.13 on 2022-06-10 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_prato', models.CharField(max_length=120)),
                ('tamanho_receita', models.DecimalField(decimal_places=1, max_digits=5)),
                ('classificacao_tamanho', models.CharField(choices=[('G', 'GRAMAS'), ('L', 'LITROS')], max_length=1)),
                ('preco_de_venda', models.DecimalField(decimal_places=2, max_digits=5)),
                ('usuario', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_ingrediente', models.CharField(max_length=125)),
                ('classificar_tamanho', models.CharField(choices=[('G', 'GRAMAS'), ('L', 'LITROS')], max_length=1)),
                ('quantidade_bruta', models.DecimalField(decimal_places=1, max_digits=5)),
                ('quantidade_liquida', models.DecimalField(decimal_places=1, max_digits=5)),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('prato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha_tecnica.prato')),
            ],
        ),
    ]
