# Generated by Django 4.2.4 on 2023-08-23 10:27

from django.db import migrations, models
import django.db.models.deletion
import django_quanttide.models.fields
import django_quanttide_projects.models.fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="RATask",
            fields=[
                (
                    "id",
                    django_quanttide.models.fields.IDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    django_quanttide.models.fields.NumberField(
                        editable=False, unique=True, verbose_name="编号"
                    ),
                ),
                (
                    "title",
                    django_quanttide.models.fields.TitleField(
                        blank=True,
                        default=None,
                        max_length=255,
                        null=True,
                        verbose_name="标题",
                    ),
                ),
                (
                    "description",
                    django_quanttide.models.fields.DescriptionField(
                        blank=True, default=None, null=True, verbose_name="描述"
                    ),
                ),
                (
                    "status",
                    django_quanttide_projects.models.fields.StatusField(
                        choices=[
                            ("drafting", "起草中"),
                            ("evaluating", "评估中"),
                            ("awaiting", "等待开始"),
                            ("in_progress", "进行中"),
                            ("delayed", "已延迟"),
                            ("paused", "已暂停"),
                            ("reviewing", "评审中"),
                            ("delivering", "交付中"),
                            ("summarizing", "复盘中"),
                            ("completed", "已完成"),
                            ("cancelled", "已取消"),
                        ],
                        default="drafting",
                        max_length=50,
                        verbose_name="状态",
                    ),
                ),
                (
                    "priority",
                    django_quanttide_projects.models.fields.PriorityField(
                        choices=[(10, "低"), (20, "中"), (30, "高"), (40, "紧急")],
                        default=10,
                        verbose_name="优先级",
                    ),
                ),
                (
                    "created_at",
                    django_quanttide.models.fields.CreatedAtField(
                        auto_now_add=True, verbose_name="创建时间"
                    ),
                ),
                (
                    "updated_at",
                    django_quanttide.models.fields.UpdatedAtField(
                        auto_now=True, verbose_name="更新时间"
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_%(app_label)s.%(class)s_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "任务",
                "verbose_name_plural": "任务列表",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RAStory",
            fields=[
                (
                    "id",
                    django_quanttide.models.fields.IDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    django_quanttide.models.fields.NumberField(
                        editable=False, unique=True, verbose_name="编号"
                    ),
                ),
                (
                    "title",
                    django_quanttide.models.fields.TitleField(
                        blank=True,
                        default=None,
                        max_length=255,
                        null=True,
                        verbose_name="标题",
                    ),
                ),
                (
                    "description",
                    django_quanttide.models.fields.DescriptionField(
                        blank=True, default=None, null=True, verbose_name="描述"
                    ),
                ),
                (
                    "status",
                    django_quanttide_projects.models.fields.StatusField(
                        choices=[
                            ("drafting", "起草中"),
                            ("evaluating", "评估中"),
                            ("awaiting", "等待开始"),
                            ("in_progress", "进行中"),
                            ("delayed", "已延迟"),
                            ("paused", "已暂停"),
                            ("reviewing", "评审中"),
                            ("delivering", "交付中"),
                            ("summarizing", "复盘中"),
                            ("completed", "已完成"),
                            ("cancelled", "已取消"),
                        ],
                        default="drafting",
                        max_length=50,
                        verbose_name="状态",
                    ),
                ),
                (
                    "priority",
                    django_quanttide_projects.models.fields.PriorityField(
                        choices=[(10, "低"), (20, "中"), (30, "高"), (40, "紧急")],
                        default=10,
                        verbose_name="优先级",
                    ),
                ),
                (
                    "created_at",
                    django_quanttide.models.fields.CreatedAtField(
                        auto_now_add=True, verbose_name="创建时间"
                    ),
                ),
                (
                    "updated_at",
                    django_quanttide.models.fields.UpdatedAtField(
                        auto_now=True, verbose_name="更新时间"
                    ),
                ),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_%(app_label)s.%(class)s_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "用户故事",
                "verbose_name_plural": "用户故事列表",
                "abstract": False,
            },
        ),
    ]