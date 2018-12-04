# Generated by Django 2.1.3 on 2018-12-02 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181126_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='IP地址')),
                ('visit_count', models.IntegerField(default=0, verbose_name='访问次数')),
            ],
            options={
                'verbose_name': '访问用户信息',
                'verbose_name_plural': '访问用户信息',
            },
        ),
        migrations.CreateModel(
            name='VisitNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_count', models.IntegerField(default=0, verbose_name='网站访问总次数')),
            ],
            options={
                'verbose_name': '网站访问总次数',
                'verbose_name_plural': '网站访问总次数',
            },
        ),
    ]