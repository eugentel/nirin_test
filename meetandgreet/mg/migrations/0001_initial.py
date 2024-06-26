# Generated by Django 5.0.6 on 2024-06-21 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=14, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('result', models.TextField(blank=True, default=None, null=True, verbose_name='Результат')),
                ('time_add', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Услуга')),
                ('desc', models.CharField(max_length=500, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Стоимость')),
                ('time_add', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='SearchAirport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_name', models.CharField(max_length=200, verbose_name='Название аэропорта')),
                ('iata', models.CharField(max_length=3, verbose_name='Код аэропорта')),
                ('country', models.CharField(max_length=200, verbose_name='Страна')),
                ('city', models.CharField(max_length=200, verbose_name='Город')),
                ('time_add', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('service', models.ManyToManyField(related_name='services', to='mg.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Аэропорт',
                'verbose_name_plural': 'Аэропорты',
            },
        ),
        migrations.CreateModel(
            name='BookingNoAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200, verbose_name='Имя клиента')),
                ('phone_number', models.CharField(max_length=14, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('flight', models.CharField(max_length=200, verbose_name='Рейс')),
                ('booking_date', models.DateTimeField(verbose_name='Дата бронирования')),
                ('number_of_passengers', models.IntegerField(verbose_name='Количество пассажиров')),
                ('note', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Примечание')),
                ('time_add', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('airport', models.ManyToManyField(to='mg.searchairport', verbose_name='Аэропорт')),
                ('service', models.ManyToManyField(to='mg.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Бронирование без аккаунта',
                'verbose_name_plural': 'Бронирования без аккаунта',
            },
        ),
    ]