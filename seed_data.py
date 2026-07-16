import os
import django
import random
from datetime import datetime, timedelta

# Configurar entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from dietetic.models import (
    CategoriaAlimento, AlimentoProgramado, PlanNutricional,
    DiaPlan, MomentoComida, Nutricionista, UserProfile, RutinaEjercicio
)

def seed():
    print("Iniciando carga de datos de prueba...")

    # 1. Asegurar Nutricionista
    user_nutri, _ = User.objects.get_or_create(
        username='nutri_pro',
        defaults={'email': 'nutri@test.com', 'is_staff': True}
    )
    user_nutri.set_password('Admin1234')
    user_nutri.save()

    UserProfile.objects.get_or_create(user=user_nutri, defaults={'role': 'NUTRICIONISTA', 'is_verified': True})

    Nutricionista.objects.get_or_create(
        user=user_nutri,
        defaults={
            'first_name': 'Carlos',
            'last_name': 'Mendoza',
            'professional_id': 'MED-9988',
            'specialty': 'Nutrición Deportiva',
            'consultation_fee': 60.0
        }
    )

    # 2. Categorías
    cats = ['Proteínas', 'Carbohidratos', 'Vegetales', 'Frutas', 'Grasas Saludables']
    cat_objs = []
    for c in cats:
        obj, _ = CategoriaAlimento.objects.get_or_create(
            name=c,
            defaults={'description': f'Categoría de {c}'}
        )
        cat_objs.append(obj)

    # 3. Alimentos
    alimentos = [
        ('Pollo a la plancha', cat_objs[0]),
        ('Arroz integral', cat_objs[1]),
        ('Ensalada verde', cat_objs[2]),
        ('Manzana roja', cat_objs[3]),
        ('Aguacate', cat_objs[4]),
    ]
    for nom, cat in alimentos:
        AlimentoProgramado.objects.get_or_create(
            name=nom,
            categoria_alimento=cat,
            defaults={
                'calories': random.randint(50, 300),
                'portion_grams': 100,
                'protein': 20.0,
                'carbs': 5.0,
                'fat': 2.0,
                'description': 'Alimento de prueba'
            }
        )

    # 4. Planes Nutricionales
    planes_data = [
        ('Plan Definición 2026', 'Enfocado en pérdida de grasa manteniendo músculo.', 25.50),
        ('Plan Volumen Limpio', 'Aumento de masa muscular controlado.', 30.00),
        ('Dieta Antiinflamatoria', 'Mejora la salud digestiva y reduce inflamación.', 20.00),
    ]

    for titulo, desc, precio in planes_data:
        plan, created = PlanNutricional.objects.get_or_create(
            name=titulo,
            defaults={
                'description': desc,
                'estimated_cost': precio,
                'duration_weeks': 4,
                'goal': 'PERDIDA_PESO',
                'is_active': True,
                'target_calories': 2000
            }
        )

        if created:
            # Crear Días y Momentos
            dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
            momentos = ['Desayuno', 'Almuerzo', 'Cena', 'Snack']

            for idx, d in enumerate(dias):
                dia_obj = DiaPlan.objects.create(
                    plan_nutricional=plan,
                    nombre_dia=d,
                    orden=idx + 1
                )
                for midx, m in enumerate(momentos):
                    MomentoComida.objects.create(
                        dia_plan=dia_obj,
                        nombre_momento=m,
                        orden=midx + 1
                    )

            # 5. Crear Rutinas para el plan
            RutinaEjercicio.objects.get_or_create(
                plan_nutricional=plan,
                descripcion_rutina=f"Rutina enfocada en {titulo}. Realizar ejercicios multiarticulares.",
                defaults={
                    'dias_semana': "Lunes, Miércoles, Viernes",
                    'duracion_minutos': 45
                }
            )

    print("¡Datos de prueba cargados exitosamente!")

if __name__ == '__main__':
    seed()
