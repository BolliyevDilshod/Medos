# Generated by Django 5.0.2 on 2024-02-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0010_alter_section_name_alter_specialist_specialty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospitals',
            old_name='hard',
            new_name='selected',
        ),
        migrations.RenameField(
            model_name='pharmacys',
            old_name='hard',
            new_name='selected',
        ),
        migrations.AddField(
            model_name='hospitals',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pharmacys',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(choices=[('Андрология', 'Andrologiya'), ('Анестезиология и реаниматология', 'Anesteziologiyaireanimatologiya'), ('Венерология', 'Venerologiya'), ('Гастроентерология', 'Gastroenterologiya'), ('Гинекология', 'Ginekologiya'), ('Дерматология', 'Dermatologiya'), ('Иммунология', 'Immunologiya'), ('Кардиология', 'Kardiologiya'), ('Маммология', 'Mammologiya'), ('Неврология', 'Nevrologiya'), ('Педиатрия', 'Pediatriya'), ('Пластическаяхирургия', 'Plasticheskayaxirurgiya'), ('Проктология', 'Proktologiya'), ('Стоматология', 'Stomatologiya'), ('Урология', 'Urologiya'), ('Хирургия', 'Xirurgiya'), ('Ендокринология', 'Endokrinologiya'), ('Терапия', 'Terapiya'), ('Невропатология', 'Nevropatologiya'), ('Отоларингология', 'Otolaringologiya'), ('Офталмология', 'Oftalmologiya'), ('Сомнология', 'Somnologiya'), ('Колопроктология', 'Koloproktologiya'), ('Акушерство', 'Akusherstvo'), ('Гематология', 'Gematologiya'), ('Ортопедия', 'Ortopediya'), ('Травматология', 'Travmatologiya'), ('Онкология', 'Onkologiya'), ('Епидемиология', 'Epidemiologiya'), ('Дерматовенерология', 'Dermatovenerologiya'), ('Нейрохирургия', 'Neyroxirurgiya'), ('Нефрология', 'Nefrologiya'), ('Диетология', 'Dietologiya'), ('Вертебрология', 'Vertebrologiya'), ('Дефектология', 'Defektologiya'), ('Гепатология', 'Gepatologiya'), ('Флебология', 'Flebologiya'), ('Ревматология', 'Revmatologiya'), ('Алтернативная медицина', 'Alternativnayamedicina'), ('Пулъмонология', 'Pulmonologiya'), ('Сурдология', 'Surdologiya'), ('Аритмология', 'Aritmologiya')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialty',
            field=models.CharField(blank=True, choices=[('Акушер', 'Akusher'), ('Аллерголог', 'Allergolog'), ('Андролог', 'Androlog'), ('Анестезиолог', 'Anesteziolog'), ('Аритмолог', 'Aritmolog'), ('Аудиолог', 'Audiolog'), ('Венеролог', 'Venerolog'), ('Вертебролог', 'Vertebrolog'), ('Врач ЛФК', 'Vrachlfk'), ('Врач СМП', 'Vrachsmp'), ('Гастроэнтеролог', 'Gastroenterolog'), ('Гематолог', 'Gematolog'), ('Генетик', 'Genetik'), ('Гепатолог', 'Gepatolog'), ('Гинеколог-эндокринолог', 'Ginekologendokrinolog'), ('Гинеколог', 'Ginekolog'), ('Гнойный хирург', 'Gnoyniyxirurg'), ('Дерматовенеролог', 'Dermatovenerolog'), ('Дерматолог', 'Dermatolog'), ('Дефектолог', 'Defektolog'), ('Диагност', 'Diagnost'), ('Диетолог', 'Dietolog'), ('Иммунолог', 'Immunolog'), ('Инфекционист', 'Infektsionist'), ('Кардиолог', 'Kardiolog'), ('Кардиоревматолог', 'Kardiorevmatolog'), ('Кардиохирург', 'Kardioxirurg'), ('Кинезитерапевт', 'Kineziterapevt'), ('Косметолог', 'Kosmetolog'), ('Лаборант', 'Laborant'), ('Логопед', 'Logoped'), ('ЛОР (Отоларинголог)', 'Lor'), ('Маммолог', 'Mammolog'), ('Мануальный терапевт', 'Manualniyterapevt'), ('Массажист', 'Massajist'), ('Миколог', 'Mikolog'), ('Нарколог', 'Narkolog'), ('Невролог', 'Nevrolog'), ('Невропатолог', 'Nevropatolog'), ('Нейропсихолог', 'Neyropsixolog'), ('Нейрофизиолог', 'Neyrofiziolog'), ('Нейрохирург', 'Neyroxirurg'), ('Неонатолог', 'Neonatolog'), ('Нефролог', 'Nefrolog'), ('Онколог', 'Onkolog'), ('Онкопроктолог', 'Onkoproktolog'), ('Ортопед', 'Ortoped'), ('Остеопат', 'Osteopat'), ('Отоларинголог-хирург', 'Otolaringologxirurg'), ('Офтальмолог', 'Oftalmolog'), ('Офтальмохирург', 'Oftalmoxirurg'), ('Паразитолог', 'Parazitolog'), ('Педиатр', 'Pediatr'), ('Пластический хирург', 'Plasticheskiyxirurg'), ('Подолог', 'Podolog'), ('Проктолог', 'Proktolog'), ('Психиатр', 'Psixiatr'), ('Психолог', 'Psixolog'), ('Психоневролог', 'Psixonevrolog'), ('Психотерапевт', 'Psixoterapevt'), ('Пульмонолог', 'Pulmonolog'), ('Радиолог', 'Radiolog'), ('Реабилитолог', 'Reabilitolog'), ('Реаниматолог', 'Reanimatolog'), ('Ревматолог', 'Revmatolog'), ('Рентгенолог', 'Rentgenolog'), ('Репродуктолог', 'Reproduktolog'), ('Рефлексотерапевт', 'Refleksoterapevt'), ('Сексолог', 'Seksolog'), ('Сомнолог', 'Somnolog'), ('Сосудистый хирург', 'Sosudistiyxirurg'), ('Стоматолог-гигиенист', 'Stomatologgigienist'), ('Стоматолог-имплантолог', 'Stomatologimplantolog'), ('Стоматолог-ортодонт', 'Stomatologortodont'), ('Стоматолог-ортопед', 'Stomatologortoped'), ('Стоматолог-пародонтолог', 'Stomatologparodontolog'), ('Стоматолог-терапевт', 'Stomatologterapevt'), ('Стоматолог-хирург', 'Stomatologxirurg'), ('Стоматолог', 'Stomatolog'), ('Сурдолог', 'Surdolog'), ('Терапевт', 'Terapevt'), ('Травматолог', 'Travmatolog'), ('Трансфузиолог', 'Transfuziolog'), ('Трихолог', 'Trixolog'), ('УЗИ-специалист', 'Uzispetsialist'), ('Уролог', 'Urolog'), ('Физиотерапевт', 'Fizioterapevt'), ('Флеболог', 'Flebolog'), ('Химиотерапевт', 'Ximioterapevt'), ('Хирург', 'Xirurg'), ('Цитогенетик', 'Tsitogenetik'), ('Цитолог', 'Tsitolog'), ('Челюстно-лицевой хирург', 'Сhelyustnolitsevoyxirurg'), ('Эмбриолог', 'Embriolog'), ('Эндокринолог', 'Endokrinolog'), ('Эндоскопист', 'Endoskopist'), ('Эпидемиолог', 'Epidemiolog'), ('Эпилептолог', 'Epileptolog')], max_length=100, null=True),
        ),
    ]