# Generated by Django 2.2.9 on 2020-01-02 09:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='会社名')),
                ('name_kana', models.CharField(blank=True, default='', max_length=255, unique=True, verbose_name='会社名(カナ)')),
                ('description', models.TextField(blank=True, max_length=2500, null=True, verbose_name='会社説明')),
                ('corporate_name', models.BigIntegerField(blank=True, default=0, null=True, unique=True, verbose_name='法人番号')),
                ('foundation_date', models.DateField(blank=True, null=True, verbose_name='設立年月日')),
                ('postal_code', models.CharField(blank=True, default='', max_length=7, validators=[django.core.validators.RegexValidator(message='数字のみで入力してください', regex='^[0-9]+$'), django.core.validators.MinLengthValidator(7)], verbose_name='郵便番号')),
                ('prefecture_id', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Hokkaido'), (2, 'Aomori'), (3, 'Iwate'), (4, 'Miyagi'), (5, 'Akita'), (6, 'Yamagata'), (7, 'Fukushima'), (8, 'Ibaraki'), (9, 'Tochigi'), (10, 'Gunma'), (11, 'Saitama'), (12, 'Chiba'), (13, 'Tokyo'), (14, 'Kanagawa'), (15, 'Niigata'), (16, 'Toyama'), (17, 'Ishikawa'), (18, 'Fukui'), (19, 'Yamanashi'), (20, 'Nagano'), (21, 'Gifu'), (22, 'Shizuoka'), (23, 'Aichi'), (24, 'Mie'), (25, 'Shiga'), (26, 'Kyoto'), (27, 'Osaka'), (28, 'Hyogo'), (29, 'Nara'), (30, 'Wakayama'), (31, 'Tottori'), (32, 'Shimane'), (33, 'Okayama'), (34, 'Hiroshima'), (35, 'Yamaguchi'), (36, 'Tokushima'), (37, 'Kagawa'), (38, 'Ehime'), (39, 'Kochi'), (40, 'Fukuoka'), (41, 'Saga'), (42, 'Nagasaki'), (43, 'Kumamoto'), (44, 'Oita'), (45, 'Miyazaki'), (46, 'Kagoshima'), (47, 'Okinawa')], null=True, verbose_name='都道府県ID')),
                ('address', models.CharField(blank=True, default='', max_length=255, verbose_name='住所')),
                ('phone', models.CharField(blank=True, default='', max_length=12, validators=[django.core.validators.RegexValidator(message='数字のみで入力してください', regex='^[0-9]+$'), django.core.validators.MinLengthValidator(10)], verbose_name='電話番号')),
                ('url', models.URLField(unique=True, verbose_name='HP URL')),
                ('is_removed', models.BooleanField(default=False, verbose_name='削除フラグ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
    ]
