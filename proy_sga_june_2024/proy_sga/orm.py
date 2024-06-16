import os
import django
from django.db.models import F,Q,Sum,Max,Min,Count,Avg
from django.utils import timezone
from datetime import datetime
from django.db.models.functions import Length
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proy_sga.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Periodo, Asignatura, Profesor, Estudiante, Nota, DetalleNota

def probar_orm():
    def create_user(create=False):
        if create:
            User.objects.create_user(
                username='mpenafiel',
                password='123',
                email='mpc@example.com'
            )
        users = User.objects.all()
        print("Listado de Usuarios")
        print(users)

    create_user(True)

    def script_periodos(create=False):
        if create:
            user = User.objects.get(pk=1)
            Periodo.objects.bulk_create([
                Periodo(periodo="2014-2015", user=user),
                Periodo(periodo="2015-2016", user=user),
                Periodo(periodo="2016-2017", user=user, state=False),
                Periodo(periodo="2017-2018", user=user),
                Periodo(periodo="2018-2019", user=user),
                Periodo(periodo="2019-2020", user=user),
                Periodo(periodo="2020-2021", user=user),
                Periodo(periodo="2021-2022", user=user),
                Periodo(periodo="2022-2023", user=user),
                Periodo(periodo="2023-2024", user=user)
            ])
        print("Listado de Periodos")
        periodos = Periodo.objects.all()
        for periodo in periodos:
            print(periodo, periodo.state)

    script_periodos(True)

    def script_asignaturas(create=False):
        if create:
            user = User.objects.get(pk=1)
            Asignatura.objects.bulk_create([
                Asignatura(descripcion="Matematica", user=user),
                Asignatura(descripcion="Ingeniería Biológica 10", user=user),
                Asignatura(descripcion="Lengua y Literatura", user=user),
                Asignatura(descripcion="Ciencias Naturales", user=user),
                Asignatura(descripcion="Educacion para la Ciudadania", user=user),
                Asignatura(descripcion="Astrofisica Avanzada 10", user=user),
                Asignatura(descripcion="Ingles 5", user=user),
                Asignatura(descripcion="Quimica 3", user=user),
                Asignatura(descripcion="Informatica 5", user=user),
                Asignatura(descripcion="Estudios Sociales 2", user=user)
            ])
        print("Listado de Asignaturas")
        asignaturas = Asignatura.objects.all()
        for asignatura in asignaturas:
            print(asignatura, asignatura.state)

    script_asignaturas(True)

    def script_profesores(create=False):
        if create:
            user = User.objects.get(pk=1)
            Profesor.objects.bulk_create([
                Profesor(cedula="0940127097", nombre="Orlando", user=user),
                Profesor(cedula="0302273974", nombre="Daniel", user=user),
                Profesor(cedula="0912799350", nombre="Jackson", user=user),
                Profesor(cedula="0940127091", nombre="Vladimir", user=user),
                Profesor(cedula="0940127092", nombre="Victoria", user=user),
                Profesor(cedula="0940127093", nombre="Javier", user=user),
                Profesor(cedula="0940127094", nombre="Jorge", user=user),
                Profesor(cedula="0940127095", nombre="Miguel", user=user),
                Profesor(cedula="0940127096", nombre="Kevin", user=user),
                Profesor(cedula="0940127090", nombre="William", user=user)
            ])
        print("Listado de Profesores")
        profesores = Profesor.objects.all()
        for profesor in profesores:
            print(profesor, profesor.state)

    script_profesores(True)

    def script_estudiantes(create=False):
        if create:
            user = User.objects.get(pk=1)
            Estudiante.objects.bulk_create([
                Estudiante(cedula="0302273975", nombre="Cristopher", user=user),
                Estudiante(cedula="0302273976", nombre="Monica", user=user),
                Estudiante(cedula="0302273977", nombre="Anderson", user=user),
                Estudiante(cedula="0302273978", nombre="Evelyn", user=user),
                Estudiante(cedula="0302273979", nombre="Taylor", user=user),
                Estudiante(cedula="0402273975", nombre="Esteven", user=user),
                Estudiante(cedula="0502273975", nombre="Nathaly", user=user),
                Estudiante(cedula="0988588141", nombre="Estefania", user=user),
                Estudiante(cedula="0702273975", nombre="Esther", user=user),
                Estudiante(cedula="0990514031", nombre="Esteban", user=user)
            ])
        print("Listado de Estudiantes")
        estudiantes = Estudiante.objects.all()
        for estudiante in estudiantes:
            print(estudiante, estudiante.state)

    script_estudiantes(True)

    def create_nota(create=False):
        user = User.objects.get(pk=1)
        if create:
            for i in range(1, 11):
                periodo = Periodo.objects.get(id=i)
                profesor = Profesor.objects.get(id=i)
                asignatura = Asignatura.objects.get(id=i)
                nota = Nota(periodo=periodo, profesor=profesor, asignatura=asignatura, user=user)
                nota.save()

    create_nota(True)

    def create_detallenota(create=False):
        user = User.objects.get(pk=1)
        if create:
            for i in range(1, 11):
                estudiante = Estudiante.objects.get(id=i)
                nota = Nota.objects.get(id=i)
                detalle_nota = DetalleNota(
                    estudiante=estudiante, nota=nota, nota1=random.uniform(4, 10),
                    nota2=random.uniform(4, 10),
                    recuperacion=random.uniform(4, 10) if random.choice([True, False]) else None,
                    observacion='Sin Observacion', user=user
                )
                detalle_nota.save()

    create_detallenota(True)

probar_orm()

def ej1():
        #1. Filtrar los estudiantes cuyos nombres comienzan con 'Est'
        estudiantes_con_est = Estudiante.objects.filter(nombre__startswith='Est')
        print("1. Filtrar los estudiantes cuyos nombres comienzan con 'Est'")
        print('-------------------------')
        for estudiante in estudiantes_con_est:
            print(estudiante.nombre)
def ej2():
        #2. Filtrar los profesores cuyos nombres contienen 'or'
        print("2. Filtrar los profesores cuyos nombres contienen 'or'")
        print('-------------------------')
        profesores_con_or = Profesor.objects.filter(nombre__contains='or')
        for profesor in profesores_con_or:
            print(profesor.nombre)
    
def ej3():
        #3. Seleccionar todas las asignaturas cuya descripción termina en '10':
        print("3. Seleccionar todas las asignaturas cuya descripción termina en '10'")
        asignaturas_terminan_10 = Asignatura.objects.filter(descripcion__endswith='10')
        for asignatura in asignaturas_terminan_10:
            print(asignatura.descripcion)

def ej4():
        #4. Seleccionar todas las notas con nota1 mayor que 8.0:
        detalles_nota1_mayor_8 = DetalleNota.objects.filter(nota1__gt=8.0)

        # Mostrar los resultados
        print("Detalle de Notas con nota1 mayor que 8.0:")
        for detalle in detalles_nota1_mayor_8:
            print(f'Detalle Nota ID: {detalle.id}, Nota1: {detalle.nota1}')

def ej5():
        #5. Seleccionar todas las notas con nota2 menor que 9.0:
        detalles_nota2_menor_9 = DetalleNota.objects.filter(nota2__lt=9.0)

        # Mostrar los resultados
        print("Detalle de Notas con nota2 menor que 9.0:")
        for detalle in detalles_nota2_menor_9:
            print(f'Detalle Nota ID: {detalle.id}, Nota2: {detalle.nota2}')

def ej6():
        #6. Seleccionar todas las notas con recuperacion igual a 9.5:
        detalles_recuperacion_9_5 = DetalleNota.objects.filter(recuperacion=9.5)

        # Mostrar los resultados
        print("Detalle de Notas con recuperación igual a 9.5:")
        for detalle in detalles_recuperacion_9_5:
            print(f'Detalle Nota ID: {detalle.id}, Recuperación: {detalle.recuperacion}')

        #Consultas usando condiciones lógicas (AND, OR, NOT)
def ej7():
        #7. Seleccionar todos los estudiantes cuyo nombre comienza con 'Est' y su y su cédula termina en '1':
        print("Detalle de todo los estudiantes cuyo nombre comienza con 'Est' y su y su cédula termina en '1':")
        estudiantes = Estudiante.objects.filter(nombre__startswith='Est', cedula__endswith='1')
        for estudiante in estudiantes:
            print(estudiante)

def ej8():
    print("Detalle de todas las asignaturas cuya descripción contiene 'Asig' o termina en '5'")
    
    # Filtrar las asignaturas según los criterios requeridos
    asignaturas = Asignatura.objects.filter(Q(descripcion__icontains='Asig') | Q(descripcion__endswith='5'))
    
    # Iterar sobre las asignaturas filtradas y mostrar su descripción
    for asignatura in asignaturas:
        print(asignatura.descripcion)

def ej9():         
        #9. Seleccionar todos los profesores cuyo nombre no contiene 'or':
        print("Detalle de todos los profesores cuyo nombre no contiene 'or'")
        profesores = Profesor.objects.exclude(nombre__icontains='or')
        for profesor in profesores:
            print(profesor)

def ej10():
        #10. Seleccionar todas las notas con nota1 mayor que 7.0 y nota2 menor que 8.0:
        print("Detalle de las notas con nota1 mayor que 7.0 y nota2 menor que 8.0 ")
        notas = DetalleNota.objects.filter(nota1__gt=7.0, nota2__lt=8.0)
        for nota in notas:
            print(nota)

def ej11():
        #11. Seleccionar todas las notas con recuperacion igual a None o nota2 mayor que 9.0:
        print ("Detalle de las notas con recuperacion igual a None o nota2 mayor que 9.0:")
        notas = DetalleNota.objects.filter(recuperacion__isnull=True) | DetalleNota.objects.filter(nota2__gt=9.0)
        for nota in notas:
            print(nota)
    
def ej12():
        #12. Seleccionar todas las notas con nota1 entre 7.0 y 9.0:
        notas_filtradas = DetalleNota.objects.filter(nota1__gte=7.0, nota1__lte=9.0)

        print("Notas con nota1 entre 7.0 y 9.0:")
        for nota in notas_filtradas:
            print(f"{nota.estudiante.nombre}: {nota.nota1}")

def ej13():
        #13. Seleccionar todas las notas con nota2 fuera del rango 6.0 a 8.0:
        notas_filtradas = DetalleNota.objects.exclude(nota2__range=(6.0, 8.0))

        print("Notas con nota2 fuera del rango 6.0 a 8.0:")
        for nota in notas_filtradas:
            print(f"{nota.estudiante.nombre}: {nota.nota2}")

def ej14():
        #14. todas las notas cuya recuperacion no sea None:
        notas_filtradas = DetalleNota.objects.exclude(recuperacion=None)

        print("Notas con recuperación distinta de None:")
        for nota in notas_filtradas:
            print(f"{nota.estudiante.nombre}: Recuperación: {nota.recuperacion}")
        
        #Consultas usando funciones de fecha (asumiendo que los modelos incluyen campos de fecha)

def ej15():
        #15. Seleccionar todas las notas creadas en el último año:
        fecha_hace_un_año = timezone.now() - timezone.timedelta(days=365)
        notas_ultimo_año = DetalleNota.objects.filter(created__gte=fecha_hace_un_año)

        print("Notas creadas en el último año:")
        for nota in notas_ultimo_año:
            print(f"{nota}: {nota.created}")
def ej16():
        #16. Seleccionar todas las notas creadas en el último mes:
        fecha_hace_un_mes = timezone.now() - timezone.timedelta(days=30)
        notas_ultimo_mes = DetalleNota.objects.filter(created__gte=fecha_hace_un_mes)

        print("Notas creadas en el último mes:")
        for nota in notas_ultimo_mes:
            print(f"{nota}: {nota.created}")
def ej17():
        #17. Seleccionar todas las notas creadas en el último día:
        fecha_hoy = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        notas_ultimo_dia = DetalleNota.objects.filter(created__gte=fecha_hoy)

        print("Notas creadas en el último día:")
        for nota in notas_ultimo_dia:
            print(f"{nota}: {nota.created}")
def ej18():
        #18. Seleccionar todas las notas creadas antes del año 2023:
        fecha_limite = datetime(year=2023, month=1, day=1)
        notas_antes_2023 = DetalleNota.objects.filter(created__lt=fecha_limite)

        print("Notas creadas antes del año 2023:")
        for nota in notas_antes_2023:
            print(f"{nota}: {nota.created}")
def ej19():
        #19. Seleccionar todas las notas creadas en marzo de cualquier año:
        notas_marzo = DetalleNota.objects.filter(created__month=3)

        print("Notas creadas en marzo de cualquier año:")
        for nota in notas_marzo:
            print(f"{nota}: {nota.created}")    

        #Consultas combinadas con funciones avanzadas
def ej20():
        # Consulta 20: Seleccionar todos los estudiantes cuyo nombre tiene exactamente 10 caracteres
        estudiantes_nombre_10_caracteres = Estudiante.objects.annotate(nombre_length=Length('nombre')).filter(nombre_length=10)

        print("Estudiantes cuyo nombre tiene exactamente 10 caracteres:")
        for estudiante in estudiantes_nombre_10_caracteres:
            print(f"{estudiante.nombre}")

def ej21():
        # Consulta 21: Seleccionar todas las notas con nota1 y nota2 mayores a 7.5
        notas_mayores_7_5 = DetalleNota.objects.filter(nota1__gt=7.5, nota2__gt=7.5)

        print("Notas con nota1 y nota2 mayores a 7.5:")
        for nota in notas_mayores_7_5:
            print(f"{nota}: nota1={nota.nota1}, nota2={nota.nota2}")

def ej22():
        # Consulta 22: Seleccionar todas las notas con recuperacion no nula y nota1 mayor a nota2
        notas_recuperacion_y_nota1_mayor_nota2 = DetalleNota.objects.exclude(recuperacion=None).filter(nota1__gt=F('nota2'))

        print("Notas con recuperación no nula y nota1 mayor a nota2:")
        for nota in notas_recuperacion_y_nota1_mayor_nota2:
            print(f"{nota}: nota1={nota.nota1}, nota2={nota.nota2}, recuperación={nota.recuperacion}")

def ej23():
        # Consulta 23: Seleccionar todas las notas con nota1 mayor a 8.0 o nota2 igual a 7.5
        notas_nota1_mayor_8_o_nota2_igual_7_5 = DetalleNota.objects.filter(Q(nota1__gt=8.0) | Q(nota2=7.5))

        print("Notas con nota1 mayor a 8.0 o nota2 igual a 7.5:")
        for nota in notas_nota1_mayor_8_o_nota2_igual_7_5:
            print(f"{nota}: nota1={nota.nota1}, nota2={nota.nota2}")

def ej24():
        # Consulta 24: Seleccionar todas las notas con recuperación mayor a nota1 y nota2
        notas_recuperacion_mayor_nota1_y_nota2 = DetalleNota.objects.filter(Q(recuperacion__gt=F('nota1')) & Q(recuperacion__gt=F('nota2')))

        print("Notas con recuperación mayor a nota1 y nota2:")
        for nota in notas_recuperacion_mayor_nota1_y_nota2:
            print(f"{nota}: nota1={nota.nota1}, nota2={nota.nota2}, recuperación={nota.recuperacion}")

        #Consultas con subconsultas y anotaciones

def ej25():
        #25. Seleccionar todos los estudiantes con al menos una nota de recuperación:
        print("Detalle de los estudiantes con al menos una nota de recuperación")
        estudiantes = Estudiante.objects.filter(detallenota__recuperacion__isnull=False).distinct()
        for estudiante in estudiantes:
            print(estudiante)

def ej26():
        #26. Seleccionar todos los profesores que han dado una asignatura específica:
        print("Detalle de los profesores que han dado una asignatura específica:")
        asignatura_especifica = Asignatura.objects.get(id=1)  # Cambiar el ID por el de la asignatura específica
        profesores = Profesor.objects.filter(nota__asignatura=asignatura_especifica).distinct()
        for profesor in profesores:
            print(profesor)

def ej27():
        #27. Seleccionar todas las asignaturas que tienen al menos una nota registrada:
        print("Detalle de las asignaturas que tienen al menos una nota registrad")
        asignaturas = Asignatura.objects.filter(nota__isnull=False).distinct()
        for asignatura in asignaturas:
            print(asignatura)

def ej28():
        #28. Seleccionar todas las asignaturas que no tienen notas registradas:
        print("Detalle de las asignaturas que no tienen notas registradas")
        asignaturas = Asignatura.objects.filter(nota__isnull=True)
        for asignatura in asignaturas:
            print(asignatura)

def ej29():
        #29. Seleccionar todos los estudiantes que no tienen notas de recuperación:
        print("Detalle de los estudiantes que no tienen notas de recuperación: ")
        estudiantes = Estudiante.objects.filter(detallenota__recuperacion__isnull=True).distinct()
        for estudiante in estudiantes:
            print(estudiante)

def ej30():
        #30. Seleccionar todas las notas cuyo promedio de nota1 y nota2 es mayor a 8.0:
        print("Detalle de las notas cuyo promedio de nota1 y nota2 es mayor a 8.0:")
        notas = DetalleNota.objects.annotate(promedio=(F('nota1') + F('nota2')) / 2).filter(promedio__gt=8.0)
        for nota in notas:
            print(nota)

def ej31():
        #31. Seleccionar todas las notas con nota1 menor que 6.0 y nota2 mayor que 7.0:    
        print("Detalle de las notas con nota1 menor que 6.0 y nota2 mayor que 7.0: ")
        notas = DetalleNota.objects.filter(nota1__lt=6.0, nota2__gt=7.0)
        for nota in notas:
            print(nota)

def ej32():
        #32. Seleccionar todas las notas con nota1 en la lista [7.0, 8.0, 9.0]:
        print ("Detalle de las notas con nota1 en la lista [7.0, 8.0, 9.0]:")
        notas = DetalleNota.objects.filter(nota1__in=[7.0, 8.0, 9.0])
        for nota in notas:
            print(nota)

def ej33():
        #33. Seleccionar todas las notas cuyo id está en un rango del 1 al 5:
        print("Detalle de las notas cuyo id está en un rango del 1 al 5: ")
        notas = DetalleNota.objects.filter(id__range=(1, 5))
        for nota in notas:
            print(nota)

def ej34():
        #34. Seleccionar todas las notas cuyo recuperacion no está en la lista [8.0, 9.0, 10.0]:
        print("Detalle de las notas cuyo recuperacion no está en la lista [8.0, 9.0, 10.0]:")
        notas = DetalleNota.objects.exclude(recuperacion__in=[8.0, 9.0, 10.0])
        for nota in notas:
            print(nota)

def ej35():
        #35. Suma de todas las notas de un estudiante:
        print("Detalle de las notas de un estudiante:")
        estudiante = Estudiante.objects.get(id=1)  # Cambiar el ID por el del estudiante
        suma_notas = DetalleNota.objects.filter(estudiante=estudiante).aggregate(Sum('nota1'), Sum('nota2'))
        print(f"Suma de nota1: {suma_notas['nota1__sum']}, Suma de nota2: {suma_notas['nota2__sum']}")

def ej36():
        #36. Nota máxima obtenida por un estudiante:
        print ("Detalle de la nota máxima obtenida por un estudiante:")
        estudiante = Estudiante.objects.get(id=1)  # Cambiar el ID por el del estudiante
        nota_maxima = DetalleNota.objects.filter(estudiante=estudiante).aggregate(Max('nota1'), Max('nota2'))
        print(f"Nota1 máxima: {nota_maxima['nota1__max']}, Nota2 máxima: {nota_maxima['nota2__max']}")

def ej37():
        #37. Nota mínima obtenida por un estudiante:
        print("Detalle de la nota mínima obtenida por un estudiante:")
        estudiante = Estudiante.objects.get(id=1)  # Cambiar el ID por el del estudiante
        nota_minima = DetalleNota.objects.filter(estudiante=estudiante).aggregate(Min('nota1'), Min('nota2'))
        print(f"Nota1 mínima: {nota_minima['nota1__min']}, Nota2 mínima: {nota_minima['nota2__min']}")

def ej38():
        #38. Contar el número total de notas de un estudiante:
        print("Detalle de contar el número total de notas de un estudiante:")
        estudiante = Estudiante.objects.get(id=1)  # Cambiar el ID por el del estudiante
        total_notas = DetalleNota.objects.filter(estudiante=estudiante).aggregate(Count('id'))
        print(f"Número total de notas: {total_notas['id__count']}")

def ej39():
        #39. Promedio de todas las notas de un estudiante sin incluir recuperación
        print("Detalle del promedio de todas las notas de un estudiante sin incluir recuperación")
        estudiante = Estudiante.objects.get(id=1)  # Cambiar el ID por el del estudiante
        promedio_notas = DetalleNota.objects.filter(estudiante=estudiante).aggregate(
            avg_nota1=Avg('nota1'), avg_nota2=Avg('nota2')
        )
        print(f"Promedio de nota1: {promedio_notas['avg_nota1']}, Promedio de nota2: {promedio_notas['avg_nota2']}")

def ej40():
        # 40. Dado un estudiante obtener todas sus notas con el detalle de todos sus datos relacionados
        estudiante = Estudiante.objects.get(id=1)  # Suponiendo que tienes el ID del estudiante
        notas_estudiante = DetalleNota.objects.filter(estudiante=estudiante)

        print(f"Notas del estudiante {estudiante.nombre}:")
        for nota in notas_estudiante:
            print(f"Nota: {nota}")
            print(f"Período: {nota.nota.periodo}")
            print(f"Asignatura: {nota.nota.asignatura}")
            print(f"Profesor: {nota.nota.profesor}")
            print("")

def ej41():
        # 41. Obtener todas las notas de un período específico
        periodo = Periodo.objects.get(id=1)  # Suponiendo que tienes el ID del período
        notas_periodo = Nota.objects.filter(periodo=periodo)

        print(f"Notas del período {periodo.periodo}:")
        for nota in notas_periodo:
            print(f"Nota: {nota}")
            print(f"Asignatura: {nota.asignatura}")
            print(f"Profesor: {nota.profesor}")
            print("")

def ej42():
        # 42. Consultar todas las notas de una asignatura dada en un período
        periodo = Periodo.objects.get(id=1)
        asignatura = Asignatura.objects.get(id=1)  # Suponiendo que tienes el ID de la asignatura
        notas_asignatura_periodo = Nota.objects.filter(asignatura=asignatura, periodo=periodo)

        print(f"Notas de la asignatura {asignatura.descripcion} en el período {periodo.periodo}:")
        for nota in notas_asignatura_periodo:
            print(f"Nota: {nota}")
            print(f"Profesor: {nota.profesor}")
            print("")

def ej43():
        # 43. Obtener todas las notas de un profesor en particular
        profesor = Profesor.objects.get(id=1)  # Suponiendo que tienes el ID del profesor
        notas_profesor = Nota.objects.filter(profesor=profesor)

        print(f"Notas del profesor {profesor.nombre}:")
        for nota in notas_profesor:
            print(f"Nota: {nota}")
            print(f"Estudiantes:")
            for detalle in nota.detallenota_set.all():
                print(f"- {detalle.estudiante}")

def ej44():
        # 44. Consultar todas las notas de un estudiante con notas superiores a un valor dado
        estudiante = Estudiante.objects.get(id=1)  # Suponiendo que tienes el ID del estudiante
        valor_limite = 8.0
        notas_estudiante_superiores = DetalleNota.objects.filter(estudiante=estudiante, nota1__gt=valor_limite)

        print(f"Notas del estudiante {estudiante.nombre} con nota1 superior a {valor_limite}:")
        for nota in notas_estudiante_superiores:
            print(f"Nota: {nota}")

def ej45():
        # 45. Obtener todas las notas de un estudiante ordenadas por período
        estudiante = Estudiante.objects.get(id=2)
        notas_estudiante_ordenadas = DetalleNota.objects.filter(estudiante=estudiante).order_by('nota__periodo__created')

        print(f"Notas del estudiante {estudiante.nombre} ordenadas por período:")
        for nota in notas_estudiante_ordenadas:
            print(f"Nota: {nota} - Período: {nota.nota.periodo}")

def ej46():
        # 46. Consultar la cantidad total de notas para un estudiante
        estudiante = Estudiante.objects.get(id=3)
        cantidad_notas_estudiante = DetalleNota.objects.filter(estudiante=estudiante).count()
        print(f"Cantidad total de notas para el estudiante {estudiante.nombre}: {cantidad_notas_estudiante}")

def ej47():
        # 47. Calcular el promedio de las notas de un estudiante en un período dado
        periodo = Periodo.objects.get(id=4)
        estudiante = Estudiante.objects.get(id=4)
        notas_estudiante_promedio = DetalleNota.objects.filter(estudiante=estudiante, nota__periodo=periodo).aggregate(promedio=Avg('nota1'))
        promedio = notas_estudiante_promedio['promedio'] if notas_estudiante_promedio['promedio'] else 0.0
        print(f"Promedio de notas del estudiante {estudiante.nombre} en el período {periodo.periodo}: {promedio}")

def ej48():
        # 48. Consultar todas las notas con una observación específica
        observacion_especifica = "Falta de asistencia"
        notas_con_observacion = DetalleNota.objects.filter(observacion=observacion_especifica)

        print(f"Notas con la observación '{observacion_especifica}':")
        for nota in notas_con_observacion:
            print(f"Nota: {nota} - Observación: {nota.observacion}")

def ej49():
        # 49. Obtener todas las notas de un estudiante ordenadas por asignatura
        estudiante = Estudiante.objects.get(id=5)
        notas_estudiante_ordenadas_asignatura = DetalleNota.objects.filter(estudiante=estudiante).order_by('nota__asignatura__descripcion')

        print(f"Notas del estudiante {estudiante.nombre} ordenadas por asignatura:")
        for nota in notas_estudiante_ordenadas_asignatura:
            print(f"Nota: {nota} - Asignatura: {nota.nota.asignatura}")

def ej50():
        # 50. Actualizar nota1 para alumnos con nota1 < 20
        DetalleNota.objects.filter(nota1__lt=20).update(nota1=20)

def ej51():
        # 51. Actualizar nota2 para alumnos con nota2 < 15
        DetalleNota.objects.filter(nota2__lt=15).update(nota2=15)

def ej52():
        # 52. Actualizar recuperación para alumnos con recuperación < 10
        DetalleNota.objects.filter(recuperacion__lt=10).update(recuperacion=10)

def ej53():
        # 53. Actualizar observación para alumnos que hayan aprobado
        # Suponiendo que "aprobado" significa nota1 >= 5.0 y nota2 >= 5.0
        DetalleNota.objects.filter(nota1__gte=5.0, nota2__gte=5.0).update(observacion="Aprobado")


def ej54():
        # 54. Actualizar todas las notas en un período específico
        periodo_descripcion = "2014-2015"  # Descripción del período específico
        profesor_id = 10
        asignatura_id = 10

        periodo = Periodo.objects.get(periodo=periodo_descripcion)

        # No es necesario obtener instancias individuales de profesor y asignatura
        # para usar sus IDs directamente en la actualización
        Nota.objects.filter(periodo=periodo).update(profesor_id=profesor_id, asignatura_id=asignatura_id)

        #Sentencias delete
        #55. Eliminar físicamente todas las notas de un estudiante:

def ej55():        
        print("Detalle de como eliminar físicamente todas las notas de un estudiante:")
        estudiante = Estudiante.objects.get(id=10)  # Cambiar el ID por el del estudiante
        DetalleNota.objects.filter(estudiante=estudiante).delete()
        print(f"Todas las notas del estudiante {estudiante.nombre} han sido eliminadas físicamente.")

def ej56():
        #56. Eliminar lógicamente todas las notas de un estudiante (en el campo state que indica si el registro está activo o no):
        print("Detalle de 56. Eliminar lógicamente todas las notas de un estudiante (en el campo state que indica si el registro está activo o no):")
        estudiante = Estudiante.objects.get(id=9)  # Cambiar el ID por el del estudiante
        DetalleNota.objects.filter(estudiante=estudiante).update(state=False)
        print(f"Todas las notas del estudiante {estudiante.nombre} han sido eliminadas lógicamente.")

def ej57():
        #57. Eliminar físicamente todas las notas de un período específico:
        print("Detalle de Eliminar físicamente todas las notas de un período específico:")
        periodo = Periodo.objects.get(id=8)  # Cambiar el ID por el del período específico
        DetalleNota.objects.filter(nota__periodo=periodo).delete()
        print(f"Todas las notas del período {periodo.periodo} han sido eliminadas físicamente.")

def ej58():
        #58. Eliminar lógicamente todas las notas de un período específico:
        print("Detalle de Eliminar lógicamente todas las notas de un período específico:")
        periodo = Periodo.objects.get(id=7)  # Cambiar el ID por el del período específico
        DetalleNota.objects.filter(nota__periodo=periodo).update(state=False)
        print(f"Todas las notas del período {periodo.periodo} han sido eliminadas lógicamente.")

def ej59():
        #59. Eliminar físicamente todas las notas que tengan una nota1 menor a 10:
        print("Detalle de Eliminar físicamente todas las notas que tengan una nota1 menor a 10:")
        DetalleNota.objects.filter(nota1__lt=10).delete()
        print(f"Todas las notas con una nota1 menor a 10 han sido eliminadas físicamente.")




