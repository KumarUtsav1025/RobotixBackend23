# Generated by Django 4.2 on 2023-05-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alumni",
            name="branch",
            field=models.CharField(default="na", max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="alumni",
            name="domain_assign",
            field=models.CharField(
                choices=[
                    ("WA", "WEB & APP"),
                    ("PM", "PR MARKETING"),
                    ("DO", "DOCUMENTATION"),
                    ("SS", "SPONSERSHIP"),
                    ("DV", "DESIGN"),
                    ("TT", "TECHNICAL"),
                ],
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="alumni",
            name="name",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="team",
            name="branch",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="team",
            name="domain_assign",
            field=models.CharField(
                choices=[
                    ("WA", "WEB & APP"),
                    ("PM", "PR MARKETING"),
                    ("DO", "DOCUMENTATION"),
                    ("SS", "SPONSERSHIP"),
                    ("DV", "DESIGN"),
                    ("TT", "TECHNICAL"),
                ],
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="team",
            name="post_assign",
            field=models.CharField(
                choices=[
                    ("AA", "Alumini"),
                    ("CC", "Convenor"),
                    ("MM", "Manager"),
                    ("EXC", "Executive"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="studying_year",
            field=models.CharField(max_length=250),
        ),
    ]