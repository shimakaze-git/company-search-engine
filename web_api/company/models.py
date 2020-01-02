"""companyモデル ."""
from django.db import models

from django.core.validators import MinLengthValidator, RegexValidator
from localflavor.jp.jp_prefectures import JP_PREFECTURE_CODES


class Company(models.Model):
    """Companyモデル."""

    """バリデーション."""
    numeric_regex = RegexValidator(
        regex=r"^[0-9]+$", message=("数字のみで入力してください")
    )

    """カラム(フィールド値)."""
    name = models.CharField(
        verbose_name="会社名",
        unique=True,
        blank=False,
        null=False,
        max_length=255
    )

    name_kana = models.CharField(
        verbose_name="会社名(カナ)",
        unique=True,
        blank=True,
        max_length=255,
        default=""
    )

    description = models.TextField(
        verbose_name="会社説明",
        blank=True,
        null=True,
        max_length=2500
    )

    corporate_name = models.BigIntegerField(
        verbose_name='法人番号',
        unique=True,
        blank=True,
        null=True,
        default=0
    )

    foundation_date = models.DateField(
        verbose_name="設立年月日",
        blank=True,
        null=True
    )

    postal_code = models.CharField(
        verbose_name="郵便番号",
        validators=[numeric_regex, MinLengthValidator(7)],
        max_length=7,
        blank=True,
        default="",
    )

    prefecture_id = models.PositiveSmallIntegerField(
        verbose_name="都道府県ID",
        blank=True,
        null=True,
        choices=[(int(value), name) for value, name in JP_PREFECTURE_CODES],
    )

    address = models.CharField(
        verbose_name="住所",
        blank=True,
        max_length=255,
        default=""
    )

    phone = models.CharField(
        validators=[numeric_regex, MinLengthValidator(10)],
        verbose_name="電話番号",
        blank=True,
        max_length=12,
        default="",
    )

    url = models.URLField(
        verbose_name="HP URL",
        unique=True,
        max_length=200,
        blank=False
    )

    is_removed = models.BooleanField(verbose_name="削除フラグ", default=False)
    created_at = models.DateTimeField(
        verbose_name="作成日", blank=False, null=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="更新日", blank=False, null=False, auto_now=True
    )
