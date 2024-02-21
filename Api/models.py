from django.db import models

class TypeChoicesSpecialist(models.TextChoices):
    AKUSHER = 'Акушер'
    ALLERGOLOG = 'Аллерголог'
    ANDROLOG = "Андролог"
    ANESTEZIOLOG = "Анестезиолог"
    ARITMOLOG = "Аритмолог"
    AUDIOLOG = "Аудиолог"
    VENEROLOG = "Венеролог"
    VERTEBROLOG = "Вертебролог"
    VRACHLFK = "Врач ЛФК"
    VRACHSMP = "Врач СМП"
    GASTROENTEROLOG = "Гастроэнтеролог"
    GEMATOLOG = "Гематолог"
    GENETIK = "Генетик"
    GEPATOLOG = "Гепатолог"
    GINEKOLOGENDOKRINOLOG = "Гинеколог-эндокринолог"
    GINEKOLOG = "Гинеколог"
    GNOYNIYXIRURG = "Гнойный хирург"
    DERMATOVENEROLOG = "Дерматовенеролог"
    DERMATOLOG = "Дерматолог"
    DEFEKTOLOG = "Дефектолог"
    DIAGNOST = "Диагност"
    DIETOLOG = "Диетолог"
    IMMUNOLOG = "Иммунолог"
    INFEKTSIONIST = "Инфекционист"
    KARDIOLOG = "Кардиолог"
    KARDIOREVMATOLOG = "Кардиоревматолог"
    KARDIOXIRURG = "Кардиохирург"
    KINEZITERAPEVT = "Кинезитерапевт"
    KOSMETOLOG = "Косметолог"
    LABORANT = "Лаборант"
    LOGOPED = "Логопед"
    LOR = "ЛОР (Отоларинголог)"
    MAMMOLOG = "Маммолог"
    MANUALNIYTERAPEVT = "Мануальный терапевт"
    MASSAJIST = "Массажист"
    MIKOLOG = "Миколог"
    NARKOLOG = "Нарколог"
    NEVROLOG = "Невролог"
    NEVROPATOLOG = "Невропатолог"
    NEYROPSIXOLOG = "Нейропсихолог"
    NEYROFIZIOLOG = "Нейрофизиолог"
    NEYROXIRURG = "Нейрохирург"
    NEONATOLOG = "Неонатолог"
    NEFROLOG = "Нефролог"
    ONKOLOG = "Онколог"
    ONKOPROKTOLOG = "Онкопроктолог"
    ORTOPED = "Ортопед"
    OSTEOPAT = "Остеопат"
    OTOLARINGOLOGXIRURG = "Отоларинголог-хирург"
    OFTALMOLOG = "Офтальмолог"
    OFTALMOXIRURG = "Офтальмохирург"
    PARAZITOLOG = "Паразитолог"
    PEDIATR = "Педиатр"
    PLASTICHESKIYXIRURG = "Пластический хирург"
    PODOLOG = "Подолог"
    PROKTOLOG = "Проктолог"
    PSIXIATR = "Психиатр"
    PSIXOLOG = "Психолог"
    PSIXONEVROLOG = "Психоневролог"
    PSIXOTERAPEVT = "Психотерапевт"
    PULMONOLOG = "Пульмонолог"
    RADIOLOG = "Радиолог"
    REABILITOLOG = "Реабилитолог"
    REANIMATOLOG = "Реаниматолог"
    REVMATOLOG = "Ревматолог"
    RENTGENOLOG = "Рентгенолог"
    REPRODUKTOLOG = "Репродуктолог"
    REFLEKSOTERAPEVT = "Рефлексотерапевт"
    SEKSOLOG = "Сексолог"
    SOMNOLOG = "Сомнолог"
    SOSUDISTIYXIRURG = "Сосудистый хирург"
    STOMATOLOGGIGIENIST = "Стоматолог-гигиенист"
    STOMATOLOGIMPLANTOLOG = "Стоматолог-имплантолог"
    STOMATOLOGORTODONT = "Стоматолог-ортодонт"
    STOMATOLOGORTOPED = "Стоматолог-ортопед"
    STOMATOLOGPARODONTOLOG = "Стоматолог-пародонтолог"
    STOMATOLOGTERAPEVT = "Стоматолог-терапевт"
    STOMATOLOGXIRURG = "Стоматолог-хирург"
    STOMATOLOG = "Стоматолог"
    SURDOLOG = "Сурдолог"
    TERAPEVT = "Терапевт"
    TRAVMATOLOG = "Травматолог"
    TRANSFUZIOLOG = "Трансфузиолог"
    TRIXOLOG = "Трихолог"
    UZISPETSIALIST = "УЗИ-специалист"
    UROLOG = "Уролог"
    FIZIOTERAPEVT = "Физиотерапевт"
    FLEBOLOG = "Флеболог"
    XIMIOTERAPEVT = "Химиотерапевт"
    XIRURG = "Хирург"
    TSITOGENETIK = "Цитогенетик"
    TSITOLOG = "Цитолог"
    СHELYUSTNOLITSEVOYXIRURG = "Челюстно-лицевой хирург"
    EMBRIOLOG = "Эмбриолог"
    ENDOKRINOLOG = "Эндокринолог"
    ENDOSKOPIST = "Эндоскопист"
    EPIDEMIOLOG = "Эпидемиолог"
    EPILEPTOLOG = "Эпилептолог"
        

class Specialist(models.Model):
    times = [
        ("00:00","00:00"),
        ("01:00","01:00"),
        ("02:00","02:00"),
        ("03:00","03:00"),
        ("04:00","04:00"),
        ("05:00","05:00"),
        ("06:00","06:00"),
        ("07:00","07:00"),
        ("08:00","08:00"),
        ("09:00","09:00"),
        ("10:00","10:00"),
        ("11:00","11:00"),
        ("12:00","12:00"),
        ("13:00","13:00"),
        ("14:00","14:00"),
        ("15:00","15:00"),
        ("16:00","16:00"),
        ("17:00","17:00"),
        ("18:00","18:00"),
        ("19:00","19:00"),
        ("20:00","20:00"),
        ("21:00","21:00"),
        ("22:00","22:00"),
        ("23:00","23:00"),
    ]
    workday = [
        ("Dushanba-Juma","Dushanba-Juma"),
        ("Dushanba-Shanba","Dushanba-Shanba"),
        ("Dushanba-Chorshanba-Juma","Dushanba-Chorshanba-Juma"),
        ("Seshanba-Payshanba-Shanba","Seshanba-Payshanba-Shanba"),
        ("Xar kuni","Xar kuni"),
    ]
    image = models.ImageField(null=True)
    lastname = models.CharField(max_length=20,null=True)
    firstname = models.CharField(max_length=25,null=True)
    middlename = models.CharField(max_length=25,null=True)
    specialty = models.CharField(max_length=100, null=True, blank=True, choices = TypeChoicesSpecialist.choices)
    category = models.CharField(max_length=25,null=True)
    experience = models.IntegerField(null=True)
    consultation_price = models.IntegerField(null=True)
    office = models.CharField(max_length=100,null=True)
    working_days = models.CharField(max_length=25,null=True,blank=True,choices=workday)
    begin_time = models.CharField(choices=times,max_length=10,null=True)
    end_time = models.CharField(choices=times,max_length=10,null=True)
    phone = models.CharField(max_length = 20, null=True)
    bio = models.TextField()
    level = models.FloatField(max_length=15,null=True)
    view = models.IntegerField(null=True)
    hard = models.CharField(max_length=15, null=True)

    
    def __str__(self):
        return self.specialty

class TypeChoices(models.TextChoices):
        DAVLAT = 'davlat'
        HUSUSIY = 'hususiy'

class Hospitals(models.Model):
    times = [
        ("00:00","00:00"),
        ("01:00","01:00"),
        ("02:00","02:00"),
        ("03:00","03:00"),
        ("04:00","04:00"),
        ("05:00","05:00"),
        ("06:00","06:00"),
        ("07:00","07:00"),
        ("08:00","08:00"),
        ("09:00","09:00"),
        ("10:00","10:00"),
        ("11:00","11:00"),
        ("12:00","12:00"),
        ("13:00","13:00"),
        ("14:00","14:00"),
        ("15:00","15:00"),
        ("16:00","16:00"),
        ("17:00","17:00"),
        ("18:00","18:00"),
        ("19:00","19:00"),
        ("20:00","20:00"),
        ("21:00","21:00"),
        ("22:00","22:00"),
        ("23:00","23:00"),
    ]
    workday = [
        ("Dushanba-Juma","Dushanba-Juma"),
        ("Dushanba-Shanba","Dushanba-Shanba"),
        ("Dushanba-Chorshanba-Juma","Dushanba-Chorshanba-Juma"),
        ("Seshanba-Payshanba-Shanba","Seshanba-Payshanba-Shanba"),
        ("Xar kuni","Xar kuni"),
    ]
    type = models.CharField(max_length = 30, blank=True, null=True, choices = TypeChoices.choices)
    image = models.ImageField(null=True)
    name = models.CharField(max_length=100,null=True)
    region = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=50,null=True)
    adress = models.CharField(max_length=100,null=True)
    level = models.FloatField(max_length=15,null=True)
    view = models.IntegerField(null=True)
    phone = models.CharField(max_length = 20, null = True)
    selected = models.CharField(max_length=15, null=True)
    web_site = models.CharField(max_length=50,null=True)
    begin_time = models.CharField(choices=times,max_length=10,null=True)
    end_time = models.CharField(choices=times,max_length=10,null=True)
    working_days = models.CharField(max_length=25,null=True,blank=True,choices=workday)

    
    def __str__(self):
        return self.name



class Pharmacys(models.Model):
    times = [
        ("00:00","00:00"),
        ("01:00","01:00"),
        ("02:00","02:00"),
        ("03:00","03:00"),
        ("04:00","04:00"),
        ("05:00","05:00"),
        ("06:00","06:00"),
        ("07:00","07:00"),
        ("08:00","08:00"),
        ("09:00","09:00"),
        ("10:00","10:00"),
        ("11:00","11:00"),
        ("12:00","12:00"),
        ("13:00","13:00"),
        ("14:00","14:00"),
        ("15:00","15:00"),
        ("16:00","16:00"),
        ("17:00","17:00"),
        ("18:00","18:00"),
        ("19:00","19:00"),
        ("20:00","20:00"),
        ("21:00","21:00"),
        ("22:00","22:00"),
        ("23:00","23:00"),
    ]
    workday = [
        ("Dushanba-Juma","Dushanba-Juma"),
        ("Dushanba-Shanba","Dushanba-Shanba"),
        ("Dushanba-Chorshanba-Juma","Dushanba-Chorshanba-Juma"),
        ("Seshanba-Payshanba-Shanba","Seshanba-Payshanba-Shanba"),
        ("Xar kuni","Xar kuni"),
    ]
    type = models.CharField(max_length = 30, blank=True, null=True, choices = TypeChoices.choices)
    image = models.ImageField(null=True)
    name = models.CharField(max_length=100,null=True)
    region = models.CharField(max_length= 100,null=True)
    city = models.CharField(max_length=100,null=True)
    adress = models.CharField(max_length=100,null=True)
    level = models.FloatField(max_length=15,null=True)
    view = models.IntegerField(null=True)
    phone = models.CharField(max_length = 20, null = True)
    selected = models.CharField(max_length=15, null=True)
    web_site = models.CharField(max_length=50,null=True)
    begin_time = models.CharField(choices=times,max_length=10,null=True)
    end_time = models.CharField(choices=times,max_length=10,null=True)
    
    
    def __str__(self):
        return self.name
    


class SectionChoices(models.TextChoices):
    Andrologiya  = "Андрология"
    Anesteziologiyaireanimatologiya = "Анестезиология и реаниматология"
    Venerologiya = "Венерология"
    Gastroenterologiya = "Гастроентерология"
    Ginekologiya = "Гинекология"
    Dermatologiya = "Дерматология"
    Immunologiya = "Иммунология"
    Kardiologiya = "Кардиология"
    Mammologiya = "Маммология"
    Nevrologiya = "Неврология"
    Pediatriya = "Педиатрия"
    Plasticheskayaxirurgiya = "Пластическаяхирургия"
    Proktologiya = "Проктология"
    Stomatologiya = "Стоматология"
    Urologiya = "Урология"
    Xirurgiya = "Хирургия"
    Endokrinologiya = "Ендокринология"
    Terapiya = "Терапия"
    Nevropatologiya = "Невропатология"
    Otolaringologiya = "Отоларингология"
    Oftalmologiya = "Офталмология"
    Somnologiya = "Сомнология"
    Koloproktologiya = "Колопроктология"
    Akusherstvo = "Акушерство"
    Gematologiya = "Гематология"
    Ortopediya = "Ортопедия"
    Travmatologiya = "Травматология"
    Onkologiya = "Онкология"
    Epidemiologiya = "Епидемиология"
    Dermatovenerologiya = "Дерматовенерология"
    Neyroxirurgiya = "Нейрохирургия"
    Nefrologiya = "Нефрология"
    Dietologiya = "Диетология"
    Vertebrologiya = "Вертебрология"
    Defektologiya = "Дефектология"
    Gepatologiya = "Гепатология"
    Flebologiya = "Флебология"
    Revmatologiya = "Ревматология"
    Alternativnayamedicina = "Алтернативная медицина"
    Pulmonologiya = "Пулъмонология"
    Surdologiya = "Сурдология"
    Aritmologiya = "Аритмология"



class Section(models.Model):
    name = models.CharField(max_length=100,null=True,choices = SectionChoices.choices)
    icon = models.FileField(null=True)

    def __str__(self):
        return self.name