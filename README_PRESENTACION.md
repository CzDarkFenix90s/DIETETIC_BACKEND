# 🥗 Dietética API - Proyecto Final

## 📋 Información del Proyecto
- **Nombre del Proyecto**: Dietética API
- **Integrantes del Grupo**: [Agregar nombres aquí]
- **Tecnologías Utilizadas**: Django, Django REST Framework, PostgreSQL, JWT

---

## 🚀 PASO 1: Configurar y Ejecutar el Proyecto (LOCAL)

### 1.1 Requisitos Previos
- Python 3.12+
- PostgreSQL (o usa la configuración local)
- `uv` (gestor de dependencias)

### 1.2 Instalación
1. **Clonar el repositorio**:
   ```bash
   cd "c:\Users\alexi\OneDrive\Desktop\Proyecto Final\DIETETIC_BACKEND"
   ```

2. **Instalar dependencias**:
   ```bash
   uv sync
   ```

3. **Configurar variables de entorno**:
   El archivo `.env` ya está configurado. Verifica que tenga:
   ```env
   # Django
   SECRET_KEY=12345
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1,10.0.2.2,68.211.112.75
   
   # PostgreSQL
   DB_NAME=dietetic
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=localhost
   DB_PORT=5432
   
   # CORS
   CORS_ALLOW_ALL_ORIGINS=True
   
   # Emails (Desarrollo - Console Backend)
   EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
   ```

4. **Aplicar migraciones**:
   ```bash
   uv run python manage.py makemigrations
   uv run python manage.py migrate
   ```

5. **Crear superusuario (opcional pero recomendado)**:
   ```bash
   uv run python manage.py createsuperuser
   ```

6. **Ejecutar el servidor**:
   ```bash
   uv run python manage.py runserver
   ```

✅ **El servidor estará corriendo en**: `http://localhost:8000`

---

## 📖 PASO 2: Verificar la Documentación de la API

### 2.1 Swagger UI (Más fácil de usar)
- Abre en tu navegador: `http://localhost:8000/api/docs/swagger/`
- Aquí puedes probar **todos los endpoints** directamente desde el navegador

### 2.2 Redoc (Documentación más bonita)
- Abre en tu navegador: `http://localhost:8000/api/docs/redoc/`

---

## 📮 PASO 3: Probar el Sistema de Correos

### 3.1 Modo Desarrollo (Sin Gmail)
El sistema ya está configurado para usar el **Console Backend**, lo que significa que los correos se imprimen en la terminal. ¡No necesitas una cuenta de Gmail para probarlo!

1. Asegúrate de que el servidor esté corriendo.
2. Usa Postman para registrar un nuevo usuario (endpoint `/api/auth/register/`).
3. Ve a la terminal donde está corriendo el servidor: ¡verás el correo de bienvenida impreso ahí!

### 3.2 Modo Producción (Con Gmail)
Si quieres probar con Gmail real:
1. Habilita la **Verificación en 2 pasos** en tu cuenta de Google.
2. Crea una **Contraseña de Aplicación**: https://myaccount.google.com/apppasswords
3. Edita tu `.env`:
   ```env
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=tu-correo@gmail.com
   EMAIL_HOST_PASSWORD=tu-contraseña-de-aplicacion
   DEFAULT_FROM_EMAIL=tu-correo@gmail.com
   ```
4. Reinicia el servidor y prueba registrandote: ¡recibirás el correo en tu bandeja de entrada!

---

## 📬 PASO 4: Probar con Postman

### 4.1 Importar la Colección
1. Abre Postman.
2. Haz clic en **Importar**.
3. Selecciona el archivo: `Postman_Completa_2026.json`.

### 4.2 Variables de la Colección
- `base_url`: `http://localhost:8000/api`
- `token`: Se guarda automáticamente después del login
- `paciente_id`, `nutricionista_id`, `plan_id`: Se guardan al crear los elementos

### 4.3 Flujo de Prueba (Sigue este orden)
1. **Health Check**: Verifica que el servidor funcione
2. **Autenticación**:
   - Registrar Usuario → Login (se guarda el token)
   - Ver Mi Perfil
3. **Crear Paciente**: Usa el endpoint de Pacientes
4. **Crear Nutricionista**: Usa el endpoint de Nutricionistas
5. **Crear Plan Nutricional**: Crea un plan
6. **Crear Categoría y Alimentos**: Agrega alimentos al plan
7. **Estructurar el Plan**: Crea días, momentos y detalles
8. **Crear Consulta**: Programa una consulta
9. **Seguimiento**: Agrega registros de consumo, agua, ejercicio, etc.
10. **Fotos de Progreso**: Sube una foto (usa form-data en Postman)
11. **Notas y Evaluaciones**: Crea notas y evaluaciones para la consulta

---

## 🛡️ Endpoints Principales (Resumen)

| Módulo | Base URL | Métodos |
|--------|----------|---------|
| **Autenticación** | `/api/auth/` | `POST` (register, login, logout, reset) |
| **Pacientes** | `/api/pacientes/` | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` |
| **Nutricionistas** | `/api/nutricionistas/` | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` |
| **Planes Nutricionales** | `/api/planes/` | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` |
| **Alimentos** | `/api/alimentos/` | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` |
| **Consultas** | `/api/consultas/` | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` |
| **Fotos de Progreso** | `/api/progresos-fotos/` | `GET`, `POST` |

---

## 📊 Modelos (24 Tablas en Total)

1. `User` (Django Default)
2. `UserProfile` (role, avatar)
3. `Paciente`
4. `SeguimientoNutricional`
5. `Nutricionista`
6. `HorarioNutricionista`
7. `ConsultaDietetica`
8. `NotaConsulta`
9. `HistorialClinico`
10. `EvaluacionAntropometrica`
11. `PlanNutricional`
12. `DiaPlan`
13. `MomentoComida`
14. `CategoriaAlimento`
15. `AlimentoProgramado`
16. `DetallePlanAlimento`
17. `SeguimientoConsumo`
18. `RegistroAgua`
19. `ProgresoFoto`
20. `RutinaEjercicio`
21. `RegistroEjercicio`
22. `SintomaDiario`
23. `MensajeChat`
24. `NotificacionPush`
25. `FacturaPago`

---

## 🔑 Autenticación y Autorización

- **JWT**: Usa `djangorestframework-simplejwt`
- **Permisos**:
  - `AllowAny`: Para register, login
  - `IsAuthenticated`: Para endpoints protegidos
  - `IsStaffOrReadOnly`: Solo admin puede modificar, todos pueden leer

---

## 📱 Archivos Subidos (Media)

- **Media URL**: `/media/`
- **Media Root**: `media/` (carpeta en el proyecto)
- **Validaciones**: Máximo 2MB, formatos: JPG, PNG, WebP

---

## 🎫 Pasos para la Presentación

1. **Inicia el servidor**:
   ```bash
   uv run python manage.py runserver
   ```

2. **Muestra el Admin Django**:
   - Abre: `http://localhost:8000/admin/`
   - Inicia sesión con el superusuario que creaste
   - Muestra todas las tablas registradas

3. **Muestra la Documentación API**:
   - Abre: `http://localhost:8000/api/docs/swagger/`
   - Prueba algunos endpoints directamente desde Swagger

4. **Prueba con Postman**:
   - Importa la colección: `Postman_Completa_2026.json`
   - Sigue el flujo de prueba paso a paso
   - Muestra cómo se crea un usuario, paciente, plan, etc.

5. **Muestra el sistema de correos**:
   - Registra un nuevo usuario
   - Muestra el correo impreso en la terminal (o en tu bandeja de entrada si configuraste Gmail)

---

## 📚 Entregables

1. ✅ Código Fuente Completo
2. ✅ Colección de Postman
3. ✅ README detallado (este archivo)
4. ✅ 24 Modelos/Tablas en la Base de Datos
5. ✅ Documentación API (Swagger y Redoc)
6. ✅ Sistema de Autenticación JWT
7. ✅ Sistema de Recuperación de Contraseña
8. ✅ Subida de Archivos/Media
9. ✅ Permisos y Autorización

---

## 💡 Tips Útiles

- Si tienes problemas con las migraciones:
  ```bash
  uv run python manage.py makemigrations dietetic
  uv run python manage.py migrate
  ```

- Para crear un superusuario rápidamente:
  ```bash
  uv run python manage.py createsuperuser
  ```

- Para reiniciar la base de datos (si es necesario):
  ```bash
  # BORRA la base de datos PostgreSQL
  # Luego:
  uv run python manage.py makemigrations
  uv run python manage.py migrate
  ```

---

¡¡Proyecto Listo para la Presentación!! 🥳🎉
