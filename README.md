# 🪣 Mini-S3 API

Implementación de una API RESTful que simula el funcionamiento de Amazon S3 (Simple Storage Service) para la gestión de buckets y objetos.

## 👥 Equipo de Desarrollo

- **Integrante 1**: [Tu Nombre]
- **Integrante 2**: [Nombre compañero]
- **Integrante 3**: [Nombre compañero]
- **Curso**: Desarrollo de Aplicaciones Web
- **Universidad**: [Tu Universidad]
- **Fecha**: Noviembre 2025

## 📋 Descripción del Proyecto

Mini-S3 es una API RESTful que replica la funcionalidad básica de Amazon S3, permitiendo:
- Crear y gestionar buckets (contenedores de almacenamiento)
- Subir, listar, actualizar y eliminar objetos (archivos)
- Gestionar metadata de los objetos
- Operaciones CRUD completas

## 🏗️ Arquitectura
```
Cliente (Postman/Browser) 
    ↓
API REST (Flask)
    ↓
Almacenamiento en Memoria (Dict Python)
    ↓
Respuestas JSON
```

## 🚀 Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje de programación
- **Flask 3.0**: Framework web para crear la API
- **JSON**: Formato de intercambio de datos

## 📦 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/mini-s3-api.git
cd mini-s3-api
```

### 2. Crear entorno virtual
```bash
python -m venv venv
```

### 3. Activar entorno virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Ejecutar la API
```bash
python app.py
```

La API estará disponible en: `http://localhost:5000`

## 🔌 Endpoints Disponibles

### Buckets

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/buckets` | Crear bucket |
| GET | `/api/buckets` | Listar todos los buckets |
| GET | `/api/buckets/<nombre>` | Obtener detalles de un bucket |
| DELETE | `/api/buckets/<nombre>` | Eliminar bucket |

### Objetos

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/buckets/<bucket>/objects` | Subir objeto |
| GET | `/api/buckets/<bucket>/objects` | Listar objetos |
| GET | `/api/buckets/<bucket>/objects/<key>` | Descargar objeto |
| PUT | `/api/buckets/<bucket>/objects/<key>` | Actualizar metadata |
| DELETE | `/api/buckets/<bucket>/objects/<key>` | Eliminar objeto |

## 📝 Ejemplos de Uso

### Crear un Bucket
```bash
POST http://localhost:5000/api/buckets
Content-Type: application/json

{
  "name": "mi-bucket"
}
```

### Subir un Objeto
```bash
POST http://localhost:5000/api/buckets/mi-bucket/objects
Content-Type: application/json

{
  "key": "documentos/archivo.txt",
  "content": "SGVsbG8gV29ybGQ=",
  "contentType": "text/plain",
  "metadata": {
    "author": "John Doe"
  }
}
```

## 🧪 Pruebas

### Verificar Estado de la API
```bash
GET http://localhost:5000/api/health
```

### Usar Postman
1. Importar la colección de pruebas (si existe)
2. Ejecutar las peticiones en orden
3. Verificar las respuestas JSON

## 📊 Estructura del Proyecto
```
mini-s3-api/
├── app.py              # Código principal de la API
├── requirements.txt    # Dependencias del proyecto
├── README.md          # Este archivo
├── .gitignore         # Archivos ignorados por Git
└── venv/              # Entorno virtual (no se sube a Git)
```

## 🔄 Comparación con Amazon S3 Real

| Característica | Mini-S3 | Amazon S3 Real |
|----------------|---------|----------------|
| Almacenamiento | Memoria RAM | Discos distribuidos |
| Persistencia | Temporal | Permanente |
| Autenticación | No | IAM, Access Keys |
| Escalabilidad | Limitada | Ilimitada |
| Costo | Gratis | Pago por uso |

## ⚠️ Limitaciones

- Los datos se almacenan en memoria (se pierden al reiniciar)
- No hay autenticación ni autorización
- No soporta archivos muy grandes
- Solo para propósitos educativos

## 🚀 Mejoras Futuras

- [ ] Integrar base de datos (MongoDB/PostgreSQL)
- [ ] Añadir autenticación JWT
- [ ] Implementar versionamiento de objetos
- [ ] Agregar límites de tamaño y rate limiting
- [ ] Crear interfaz web (frontend)
- [ ] Dockerizar la aplicación

## 📚 Referencias

- [Documentación de Flask](https://flask.palletsprojects.com/)
- [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/)
- [REST API Best Practices](https://restfulapi.net/)

## 📄 Licencia

Este proyecto es solo para fines educativos.

## 📧 Contacto

Para preguntas o sugerencias, contactar a: [tu-email@ejemplo.com]"# mini-s3-api" 
