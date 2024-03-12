# Generated by Django 4.2.1 on 2024-03-12 14:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["created_on"]},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_on"]},
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="content",
            new_name="body",
        ),
    ]