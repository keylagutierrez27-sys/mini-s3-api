# 🪣 Mini-S3 API - Simulación de Amazon S3

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-Educational-orange?style=for-the-badge)](LICENSE)

> **API RESTful que replica el comportamiento de Amazon S3 (Simple Storage Service) para la gestión de buckets y objetos de almacenamiento en la nube.**

---

## 👥 Información del Proyecto

### Equipo de Desarrollo

| Rol | Nombre | Responsabilidad |
|-----|--------|-----------------|
| **Desarrollador Backend** | Keyla | Implementación de endpoints, lógica de negocio |
| **Arquitecto de Datos** | | Diseño del modelo de datos, documentación |
| **QA & Testing** | | Pruebas con Postman, validación de funcionalidades |

---

## 📑 Índice

1. [Resumen Ejecutivo](#-resumen-ejecutivo)
2. [¿Qué es Amazon S3?](#-qué-es-amazon-s3)
3. [Por qué elegimos S3](#-por-qué-elegimos-amazon-s3)
4. [Objetivos del Proyecto](#-objetivos-del-proyecto)
5. [Arquitectura Completa](#-arquitectura-completa)
6. [Diseño de la API](#-diseño-de-la-api)
7. [Modelo de Datos](#-modelo-de-datos)
8. [Implementación Técnica](#-implementación-técnica)
9. [Instalación y Configuración](#-instalación-y-configuración)
10. [Guía de Uso](#-guía-de-uso-completa)
11. [Documentación de Endpoints](#-documentación-completa-de-endpoints)
12. [Ejemplos Prácticos](#-ejemplos-prácticos-de-uso)
13. [Pruebas Realizadas](#-pruebas-realizadas)
14. [Comparación con S3 Real](#-comparación-detallada-con-amazon-s3)
15. [Tecnologías y Herramientas](#-tecnologías-y-herramientas-utilizadas)
16. [Decisiones de Diseño](#-decisiones-de-diseño-y-justificación)
17. [Desafíos y Soluciones](#-desafíos-enfrentados-y-soluciones)
18. [Aprendizajes Obtenidos](#-aprendizajes-obtenidos)
19. [Limitaciones Actuales](#-limitaciones-actuales)
20. [Roadmap de Mejoras](#-roadmap-de-mejoras-futuras)
21. [Referencias y Fuentes](#-referencias-y-fuentes)
22. [FAQ](#-preguntas-frecuentes-faq)
23. [Contacto](#-contacto)

---

## 🎯 Resumen Ejecutivo

**Mini-S3** es una implementación educativa de una **API RESTful** que simula el funcionamiento del servicio de almacenamiento en la nube más popular del mundo: **Amazon Simple Storage Service (S3)**.

### Alcance del Proyecto

Este proyecto fue desarrollado como parte del curso de **Desarrollo de Aplicaciones Web**, con el objetivo de aplicar conocimientos sobre:

- ✅ Diseño y desarrollo de APIs RESTful
- ✅ Protocolo HTTP y métodos estándar (GET, POST, PUT, DELETE)
- ✅ Arquitectura Cliente-Servidor
- ✅ Manejo de datos en formato JSON
- ✅ Validaciones y manejo de errores
- ✅ Buenas prácticas de programación
- ✅ Documentación técnica
- ✅ Control de versiones con Git/GitHub

### ¿Qué hace Mini-S3?

Permite a los usuarios (a través de peticiones HTTP):

1. **Crear buckets** (contenedores de almacenamiento)
2. **Gestionar objetos** (subir, listar, descargar, eliminar archivos)
3. **Manejar metadata** (información adicional sobre los archivos)
4. **Realizar operaciones CRUD completas** sobre recursos

### Tecnología Principal

- **Backend:** Python 3.8+ con Flask 3.1.2
- **Almacenamiento:** Memoria RAM (diccionarios Python)
- **Formato:** JSON para intercambio de datos
- **Protocolo:** HTTP/1.1

---

## 🌐 ¿Qué es Amazon S3?

### Introducción a S3

**Amazon Simple Storage Service (S3)** es uno de los servicios fundamentales de **Amazon Web Services (AWS)**, lanzado en 2006. Es un servicio de almacenamiento de objetos diseñado para almacenar y recuperar cualquier cantidad de datos desde cualquier lugar de la web.

### Características de S3 Real

| Característica | Descripción |
|----------------|-------------|
| **Durabilidad** | 99.999999999% (11 nueves) de durabilidad |
| **Disponibilidad** | 99.99% de disponibilidad anual |
| **Escalabilidad** | Almacenamiento prácticamente ilimitado |
| **Velocidad** | Millones de peticiones por segundo |
| **Global** | Múltiples regiones geográficas |
| **Seguridad** | Cifrado, IAM, políticas de acceso |

### ¿Quién usa S3?

Empresas líderes mundiales utilizan S3:

- 🎬 **Netflix:** Almacena y distribuye contenido multimedia a millones de usuarios
- 🏠 **Airbnb:** Guarda fotos de propiedades y documentos de reservas
- 📁 **Dropbox:** Utiliza S3 como backend para su servicio de almacenamiento
- 📸 **Instagram:** Almacena miles de millones de fotos y videos
- 🛒 **Amazon.com:** Almacena catálogos de productos e imágenes

### Conceptos Clave de S3

#### 1. Buckets (Cubos)
- Contenedores principales de almacenamiento
- Nombres únicos globalmente
- Similar a carpetas raíz, pero con características especiales

#### 2. Objects (Objetos)
- Archivos individuales almacenados
- Identificados por una "key" (clave/ruta)
- Pueden tener metadata personalizada

#### 3. Keys (Claves)
- Identificador único del objeto dentro del bucket
- Puede incluir "/" para simular jerarquías (ej: `fotos/2025/enero/img1.jpg`)

#### 4. Metadata
- Información adicional sobre el objeto
- Pares clave-valor personalizables
- Ejemplos: autor, fecha, tipo de contenido, versión

### Modelo de S3 vs Sistema de Archivos Tradicional

**Sistema de Archivos (Windows/Linux):**
```
C:\
├── Usuarios\
│   ├── Documentos\
│   │   └── reporte.pdf
│   └── Fotos\
│       └── vacaciones\
│           └── playa.jpg
```

**Amazon S3:**
```
Bucket: mi-bucket
├── Object: "usuarios/documentos/reporte.pdf"
├── Object: "usuarios/fotos/vacaciones/playa.jpg"
└── Object: "backup/2025/datos.zip"
```

**Diferencias clave:**
- S3 usa un modelo **plano** (no hay carpetas reales)
- Las "carpetas" son solo parte del nombre del objeto (key)
- Permite búsquedas y accesos más rápidos
- Optimizado para acceso HTTP/HTTPS

---

## 💡 Por qué elegimos Amazon S3

### Justificación de la Elección

Elegimos Amazon S3 como caso de estudio por las siguientes razones:

#### 1. Relevancia en la Industria
- ✅ Servicio más utilizado de AWS
- ✅ Presente en el 90% de aplicaciones cloud modernas
- ✅ Conocimiento valioso para el mercado laboral

#### 2. Complejidad Apropiada
- ✅ Suficientemente complejo para ser desafiante
- ✅ Lo suficientemente acotado para un proyecto académico
- ✅ Permite aplicar múltiples conceptos de backend

#### 3. Aplicabilidad Práctica
- ✅ Caso de uso real y tangible
- ✅ Fácil de demostrar y entender
- ✅ Múltiples escenarios de prueba

#### 4. Valor Educativo
- ✅ Enseña diseño de APIs RESTful
- ✅ Introduce conceptos de cloud computing
- ✅ Practica manejo de archivos y metadata
- ✅ Desarrolla habilidades de arquitectura de software

### Casos de Uso que Inspiraron el Proyecto

1. **Sistema de Gestión Documental**
   - Empresas necesitan almacenar contratos, facturas, reportes
   - Mini-S3 simula cómo se gestionarían estos documentos

2. **Plataforma de Contenido Multimedia**
   - Aplicaciones como YouTube o Spotify necesitan almacenar media
   - Nuestro proyecto replica esta arquitectura

3. **Backup y Archivado**
   - Sistemas de respaldo automático de datos
   - Recuperación ante desastres

4. **CDN (Content Delivery Network)**
   - Servir archivos estáticos a aplicaciones web
   - Imágenes, CSS, JavaScript, etc.

---

## 🎯 Objetivos del Proyecto

### Objetivos Generales

1. **Comprender arquitectura de APIs RESTful**
   - Diseñar endpoints siguiendo convenciones REST
   - Implementar métodos HTTP correctamente
   - Manejar códigos de estado apropiados

2. **Aplicar principios CRUD**
   - Create (POST)
   - Read (GET)
   - Update (PUT)
   - Delete (DELETE)

3. **Simular servicio cloud real**
   - Replicar comportamiento de Amazon S3
   - Entender modelos de datos NoSQL
   - Gestión de recursos jerárquicos

### Objetivos Específicos

#### Técnicos
- ✅ Implementar 9 endpoints funcionales
- ✅ Validar entradas de usuario
- ✅ Manejar errores apropiadamente
- ✅ Responder en formato JSON estándar
- ✅ Gestionar estado en memoria

#### Funcionales
- ✅ Crear y eliminar buckets
- ✅ Subir y descargar objetos
- ✅ Listar recursos
- ✅ Actualizar metadata
- ✅ Validar nombres y restricciones

#### Documentación
- ✅ README completo
- ✅ Comentarios en código
- ✅ Ejemplos de uso
- ✅ Guía de instalación

#### Calidad
- ✅ Código limpio y organizado
- ✅ Manejo robusto de errores
- ✅ Pruebas exhaustivas
- ✅ Versionamiento con Git

---

## 🏗️ Arquitectura Completa

### Visión General del Sistema
```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENTE                              │
│  (Navegador Web, Postman, Aplicación, cURL, etc.)         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ Peticiones HTTP
                         │ (GET, POST, PUT, DELETE)
                         │ + JSON Payload
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                     API MINI-S3                             │
│                     (Flask App)                             │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  1. RECEPCIÓN                                        │  │
│  │     • Recibe petición HTTP                          │  │
│  │     • Parsea JSON del body                          │  │
│  │     • Extrae parámetros de ruta                     │  │
│  └─────────────────────────────────────────────────────┘  │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  2. VALIDACIÓN                                       │  │
│  │     • Valida formato de datos                       │  │
│  │     • Verifica existencia de recursos               │  │
│  │     • Aplica reglas de negocio                      │  │
│  │     • Valida nombres de buckets/objetos             │  │
│  └─────────────────────────────────────────────────────┘  │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  3. LÓGICA DE NEGOCIO                               │  │
│  │     • Ejecuta operación solicitada                  │  │
│  │     • Calcula estadísticas                          │  │
│  │     • Genera timestamps                             │  │
│  │     • Actualiza estructuras de datos                │  │
│  └─────────────────────────────────────────────────────┘  │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  4. GESTIÓN DE ALMACENAMIENTO                       │  │
│  │     • Interactúa con buckets_storage                │  │
│  │     • Crea/Lee/Actualiza/Elimina datos              │  │
│  │     • Mantiene integridad referencial               │  │
│  └─────────────────────────────────────────────────────┘  │
│                         │                                   │
│                         ▼                                   │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  5. CONSTRUCCIÓN DE RESPUESTA                       │  │
│  │     • Formatea datos como JSON                      │  │
│  │     • Asigna código HTTP (200, 201, 404, etc.)     │  │
│  │     • Agrega headers apropiados                     │  │
│  └─────────────────────────────────────────────────────┘  │
│                         │                                   │
└─────────────────────────┼───────────────────────────────────┘
                         │
                         │ Respuesta HTTP
                         │ + JSON Response
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   ALMACENAMIENTO                            │
│                    (Memoria RAM)                            │
│                                                              │
│  buckets_storage = {                                        │
│    "bucket1": {                                             │
│      "name": "bucket1",                                     │
│      "createdAt": "2025-11-26T10:00:00Z",                  │
│      "objects": {                                           │
│        "file1.txt": {                                       │
│          "key": "file1.txt",                                │
│          "size": 1024,                                      │
│          "content": "base64...",                            │
│          "metadata": {...}                                  │
│        }                                                     │
│      }                                                       │
│    }                                                         │
│  }                                                           │
└─────────────────────────────────────────────────────────────┘
```

### Componentes del Sistema

#### 1. Cliente (Frontend/Interfaz)
**Descripción:** Cualquier aplicación que realiza peticiones HTTP a la API.

**Ejemplos:**
- Navegador web (para GET /api/health)
- Postman (para pruebas)
- Aplicación web con JavaScript (fetch/axios)
- Script Python con requests
- Aplicación móvil
- Herramienta cURL desde terminal

**Responsabilidades:**
- Construir peticiones HTTP correctas
- Enviar datos en formato JSON
- Interpretar respuestas
- Manejar errores del lado del cliente

#### 2. API Flask (Backend)
**Descripción:** Servidor que procesa peticiones y gestiona recursos.

**Componentes internos:**

**a) Rutas (Routes):**
```python
@app.route('/api/buckets', methods=['POST'])
def create_bucket():
    # Lógica para crear bucket
```

**b) Validadores:**
```python
def validate_bucket_name(name):
    # Reglas de validación
```

**c) Gestores de Almacenamiento:**
```python
buckets_storage[bucket_name] = {...}
```

**d) Formateadores de Respuesta:**
```python
return jsonify({...}), 201
```

#### 3. Almacenamiento en Memoria
**Descripción:** Estructura de datos Python que simula una base de datos.

**Estructura completa:**
```python
buckets_storage = {
    # Clave: nombre del bucket
    "mi-bucket": {
        # Metadata del bucket
        "name": "mi-bucket",
        "createdAt": "2025-11-26T10:30:00Z",
        
        # Objetos contenidos
        "objects": {
            # Clave: key del objeto
            "documentos/reporte.pdf": {
                "key": "documentos/reporte.pdf",
                "bucket": "mi-bucket",
                "size": 204800,
                "contentType": "application/pdf",
                "metadata": {
                    "author": "John Doe",
                    "department": "IT",
                    "version": "1.0"
                },
                "createdAt": "2025-11-26T10:35:00Z",
                "lastModified": "2025-11-26T10:35:00Z",
                "content": "JVBERi0xLjQKJeLjz9..."  # Base64
            },
            "images/logo.png": {
                "key": "images/logo.png",
                "bucket": "mi-bucket",
                "size": 15360,
                "contentType": "image/png",
                "metadata": {
                    "width": "200",
                    "height": "200"
                },
                "createdAt": "2025-11-26T11:00:00Z",
                "lastModified": "2025-11-26T11:00:00Z",
                "content": "iVBORw0KGgoAAAANS..."  # Base64
            }
        }
    },
    "otro-bucket": {
        "name": "otro-bucket",
        "createdAt": "2025-11-26T12:00:00Z",
        "objects": {}
    }
}
```

**Ventajas del diseño:**
- ✅ Acceso O(1) a buckets por nombre
- ✅ Acceso O(1) a objetos por key
- ✅ Fácil de navegar y depurar
- ✅ No requiere base de datos externa

**Desventajas:**
- ❌ Se pierde al reiniciar el servidor
- ❌ Limitado por memoria RAM disponible
- ❌ No persistente
- ❌ No escalable a múltiples servidores

### Flujo Detallado de una Petición

**Ejemplo: Crear un Bucket**
```
1. CLIENTE envía petición:
   POST http://localhost:5000/api/buckets
   Content-Type: application/json
   
   {
     "name": "mi-nuevo-bucket"
   }

2. FLASK recibe en @app.route('/api/buckets', methods=['POST'])
   
3. PARSEO:
   data = request.get_json()
   # data = {"name": "mi-nuevo-bucket"}
   
4. VALIDACIÓN:
   a) ¿Tiene campo "name"? → SÍ
   b) ¿Longitud entre 3-63? → SÍ
   c) ¿Solo minúsculas? → SÍ
   d) ¿Ya existe? → NO
   ✅ Validación pasada
   
5. EJECUCIÓN:
   bucket_name = "mi-nuevo-bucket"
   buckets_storage[bucket_name] = {
       "name": bucket_name,
       "createdAt": "2025-11-26T15:30:00Z",
       "objects": {}
   }
   
6. RESPUESTA:
   HTTP/1.1 201 Created
   Content-Type: application/json
   
   {
     "message": "Bucket creado exitosamente",
     "bucket": {
       "name": "mi-nuevo-bucket",
       "createdAt": "2025-11-26T15:30:00Z",
       "objectCount": 0,
       "totalSize": 0
     }
   }
   
7. CLIENTE recibe y procesa respuesta
```

### Patrones de Diseño Aplicados

#### 1. RESTful API
- Recursos identificados por URIs
- Métodos HTTP semánticos
- Sin estado (stateless)
- Respuestas en JSON

#### 2. Separation of Concerns
- Validación separada de lógica de negocio
- Funciones auxiliares reutilizables
- Endpoints focalizados en una responsabilidad

#### 3. Error Handling
- Try-catch para excepciones
- Códigos HTTP descriptivos
- Mensajes de error claros

---

## 🎨 Diseño de la API

### Principios REST Aplicados

#### 1. Recursos como Sustantivos
```
✅ CORRECTO:
GET /api/buckets
POST /api/buckets

❌ INCORRECTO:
GET /api/getBuckets
POST /api/createBucket
```

#### 2. Métodos HTTP Semánticos

| Método | Uso | Idempotente | Safe |
|--------|-----|-------------|------|
| GET | Leer recursos | ✅ Sí | ✅ Sí |
| POST | Crear recursos | ❌ No | ❌ No |
| PUT | Actualizar completo | ✅ Sí | ❌ No |
| DELETE | Eliminar recursos | ✅ Sí | ❌ No |

#### 3. Códigos de Estado HTTP

| Código | Significado | Cuándo usar |
|--------|-------------|-------------|
| **200 OK** | Éxito | GET, PUT, DELETE exitosos |
| **201 Created** | Recurso creado | POST exitoso |
| **400 Bad Request** | Datos inválidos | Validación falló |
| **404 Not Found** | No existe | Recurso no encontrado |
| **409 Conflict** | Conflicto | Recurso ya existe |
| **500 Internal Server Error** | Error servidor | Excepción no manejada |

#### 4. Jerarquía de URLs
```
/api/                           (Raíz de la API)
├── /health                     (Health check)
├── /buckets                    (Colección de buckets)
│   ├── /                       (Listar todos)
│   ├── /{bucket_name}          (Bucket específico)
│   │   └── /objects            (Objetos del bucket)
│   │       ├── /               (Listar objetos)
│   │       └── /{object_key}   (Objeto específico)
```

### Diseño de Endpoints

#### Nomenclatura
```
GET    /api/buckets              → Colección
GET    /api/buckets/mi-bucket    → Recurso individual
POST   /api/buckets              → Crear en colección
DELETE /api/buckets/mi-bucket    → Eliminar individual
```

#### Versionamiento

Actualmente: **Sin versionamiento** (v1 implícita)

Futuro:
```
/api/v1/buckets
/api/v2/buckets  (con nuevas características)
```

### Formato de Peticiones y Respuestas

#### Peticiones (Request)

**Headers requeridos:**
```
Content-Type: application/json
```

**Body (JSON):**
```json
{
  "campo1": "valor1",
  "campo2": "valor2"
}
```

#### Respuestas (Response)

**Headers:**
```
Content-Type: application/json
```

**Body exitoso:**
```json
{
  "message": "Operación exitosa",
  "data": {...}
}
```

**Body con error:**
```json
{
  "error": "Descripción del error"
}
```

---

## 📊 Modelo de Datos

### Entidades Principales

#### 1. Bucket

**Descripción:** Contenedor principal de almacenamiento, similar a una carpeta raíz.

**Atributos:**

| Campo | Tipo | Descripción | Obligatorio | Ejemplo |
|-------|------|-------------|-------------|---------|
| `name` | String | Nombre único del bucket | ✅ Sí | "mi-bucket" |
| `createdAt` | String (ISO 8601) | Timestamp de creación | ✅ Sí | "2025-11-26T10:30:00Z" |
| `objectCount` | Integer | Número de objetos contenidos | ❌ No (calculado) | 5 |
| `totalSize` | Integer | Tamaño total en bytes | ❌ No (calculado) | 1048576 |
| `objects` | Object | Diccionario de objetos | ✅ Sí | {...} |

**Reglas de Validación:**
- ✅ Longitud: 3-63 caracteres
- ✅ Solo minúsculas, números, guiones (-), guiones bajos (_)
- ✅ No puede empezar con número
- ✅ Debe ser único en el sistema

**Ejemplo completo:**
```json
{
  "name": "documentos-2025",
  "createdAt": "2025-11-26T10:30:00Z",
  "objectCount": 3,
  "totalSize": 524288,
  "objects": {
    "contratos/contrato-001.pdf": {...},
    "facturas/factura-2025-01.pdf": {...},
    "reportes/reporte-mensual.docx": {...}
  }
}
```

#### 2. Object (Objeto)

**Descripción:** Archivo individual almacenado dentro de un bucket.

**Atributos:**

| Campo | Tipo | Descripción | Obligatorio | Ejemplo |
|-------|------|-------------|-------------|---------|
| `key` | String | Ruta/nombre único del objeto | ✅ Sí | "docs/file.pdf" |
| `bucket` | String | Nombre del bucket contenedor | ✅ Sí | "mi-bucket" |
| `size` | Integer | Tamaño en bytes | ✅ Sí | 204800 |
| `contentType` | String | Tipo MIME del contenido | ✅ Sí | "application/pdf" |
| `metadata` | Object | Datos adicionales (clave-valor) | ❌ No | {"author": "John"} |
| `createdAt` | String (ISO 8601) | Timestamp de creación | ✅ Sí | "2025-11-26T10:35:00Z" |
| `lastModified` | String (ISO 8601) | Última modificación | ✅ Sí | "2025-11-26T11:00:00Z" |
| `content` | String (Base64) | Contenido del archivo codificado | ✅ Sí | "JVBERi0xLjQK..." |

**Ejemplo completo:**
```json
{
  "key": "proyectos/2025/propuesta-cliente-a.pdf",
  "bucket": "documentos-empresa",
  "size": 524288,
  "contentType": "application/pdf",
  "metadata": {
    "author": "María García",
    "department": "Ventas",
    "client": "Cliente A",
    "version": "1.2",
    "status": "approved",
    "tags": "propuesta,2025,cliente-a"
  },
  "createdAt": "2025-11-26T10:35:00Z",
  "lastModified": "2025-11-26T14:20:00Z",
  "content": "JVBERi0xLjQKJeLjz9MKMSAwIG9iago8PC9UeXBlL0NhdGFsb2cvUGFnZXMgMiAwIF..."
}
```

### Relaciones Entre Entidades
Buena suerte! 🍀
