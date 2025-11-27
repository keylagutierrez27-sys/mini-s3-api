"""
Mini-S3 API - Simulación de Amazon S3
Implementación de API RESTful para gestión de buckets y objetos
"""

from flask import Flask, request, jsonify
from datetime import datetime
import base64
import json

app = Flask(__name__)

# Almacenamiento en memoria
buckets_storage = {}

# Funciones auxiliares
def get_current_timestamp():
    return datetime.utcnow().isoformat() + 'Z'

def validate_bucket_name(name):
    if not name or len(name) < 3 or len(name) > 63:
        return False, "El nombre debe tener entre 3 y 63 caracteres"
    if not name.islower():
        return False, "El nombre debe estar en minúsculas"
    return True, None

def bucket_exists(bucket_name):
    return bucket_name in buckets_storage

def calculate_bucket_stats(bucket_name):
    if not bucket_exists(bucket_name):
        return 0, 0
    objects = buckets_storage[bucket_name]['objects']
    count = len(objects)
    total_size = sum(obj['size'] for obj in objects.values())
    return count, total_size

# ENDPOINTS - BUCKETS
@app.route('/api/buckets', methods=['POST'])
def create_bucket():
    try:
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({'error': 'El campo "name" es requerido'}), 400
        
        bucket_name = data['name'].lower()
        is_valid, error_msg = validate_bucket_name(bucket_name)
        if not is_valid:
            return jsonify({'error': error_msg}), 400
        
        if bucket_exists(bucket_name):
            return jsonify({'error': f'El bucket "{bucket_name}" ya existe'}), 409
        
        buckets_storage[bucket_name] = {
            'name': bucket_name,
            'createdAt': get_current_timestamp(),
            'objects': {}
        }
        
        return jsonify({
            'message': 'Bucket creado exitosamente',
            'bucket': {
                'name': bucket_name,
                'createdAt': buckets_storage[bucket_name]['createdAt'],
                'objectCount': 0,
                'totalSize': 0
            }
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/buckets', methods=['GET'])
def list_buckets():
    try:
        buckets_list = []
        for bucket_name, bucket_data in buckets_storage.items():
            count, size = calculate_bucket_stats(bucket_name)
            buckets_list.append({
                'name': bucket_name,
                'createdAt': bucket_data['createdAt'],
                'objectCount': count,
                'totalSize': size
            })
        return jsonify({'buckets': buckets_list, 'count': len(buckets_list)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/buckets/<bucket_name>', methods=['GET'])
def get_bucket(bucket_name):
    try:
        if not bucket_exists(bucket_name):
            return jsonify({'error': f'El bucket "{bucket_name}" no existe'}), 404
        
        count, size = calculate_bucket_stats(bucket_name)
        bucket_data = buckets_storage[bucket_name]
        
        return jsonify({
            'name': bucket_name,
            'createdAt': bucket_data['createdAt'],
            'objectCount': count,
            'totalSize': size,
            'objects': list(bucket_data['objects'].keys())
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/buckets/<bucket_name>', methods=['DELETE'])
def delete_bucket(bucket_name):
    try:
        if not bucket_exists(bucket_name):
            return jsonify({'error': f'El bucket "{bucket_name}" no existe'}), 404
        
        if len(buckets_storage[bucket_name]['objects']) > 0:
            return jsonify({'error': 'No se puede eliminar un bucket con objetos'}), 409
        
        del buckets_storage[bucket_name]
        return jsonify({'message': f'Bucket "{bucket_name}" eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ENDPOINTS - OBJETOS
@app.route('/api/buckets/<bucket_name>/objects', methods=['POST'])
def upload_object(bucket_name):
    try:
        if not bucket_exists(bucket_name):
            return jsonify({'error': f'El bucket "{bucket_name}" no existe'}), 404
        
        data = request.get_json()
        if not data or 'key' not in data or 'content' not in data:
            return jsonify({'error': 'Los campos "key" y "content" son requeridos'}), 400
        
        object_key = data['key']
        content = data['content']
        content_type = data.get('contentType', 'application/octet-stream')
        metadata = data.get('metadata', {})
        
        if object_key in buckets_storage[bucket_name]['objects']:
            return jsonify({'error': f'El objeto "{object_key}" ya existe'}), 409
        
        size = len(content)
        timestamp = get_current_timestamp()
        obj = {
            'key': object_key,
            'bucket': bucket_name,
            'size': size,
            'contentType': content_type,
            'metadata': metadata,
            'createdAt': timestamp,
            'lastModified': timestamp,
            'content': content
        }
        
        buckets_storage[bucket_name]['objects'][object_key] = obj
        response_obj = {k: v for k, v in obj.items() if k != 'content'}
        
        return jsonify({'message': 'Objeto subido exitosamente', 'object': response_obj}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/buckets/<bucket_name>/objects', methods=['GET'])
def list_objects(bucket_name):
    try:
        if not bucket_exists(bucket_name):
            return jsonify({'error': f'El bucket "{bucket_name}" no existe'}), 404
        
        objects_list = []
        for obj_key, obj_data in buckets_storage[bucket_name]['objects'].items():
            obj_summary = {k: v for k, v in obj_data.items() if k != 'content'}
            objects_list.append(obj_summary)
        
        return jsonify({'bucket': bucket_name, 'objects': objects_list, 'count': len(objects_list)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/buckets/<bucket_name>/objects/<path:object_key>', methods=['GET'])
def get_object(bucket_name, object_key):
    try:
        if not bucket_exists(bucket_name):
            return jsonify({'error': f'El bucket "{bucket_name}" no existe'}), 404
        
        if object_key not in buckets_storage[bucket_name]['objects']:
            return jsonify({'error': f'El objeto "{object_key}" no existe'}), 404
        
        obj = buckets_storage[bucket_name]['objects'][object_key]
        return jsonify({'object': obj}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/buckets/<bucket_name>/objects/<path:object_key>', methods=['PUT'])
def update_object_metadata(bucket_name, object_key):
    try:
        if not bucket_exists(bucket_name):
            return jsonify({'error': f'El bucket "{bucket_name}" no existe'}), 404
        
        if object_key not in buckets_storage[bucket_name]['objects']:
            return jsonify({'error': f'El objeto "{object_key}" no existe'}), 404
        
        data = request.get_json()
        if not data or 'metadata' not in data:
            return jsonify({'error': 'El campo "metadata" es requerido'}), 400
        
        obj = buckets_storage[bucket_name]['objects'][object_key]
        obj['metadata'].update(data['metadata'])
        obj['lastModified'] = get_current_timestamp()
        
        response_obj = {k: v for k, v in obj.items() if k != 'content'}
        return jsonify({'message': 'Metadata actualizada exitosamente', 'object': response_obj}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/buckets/<bucket_name>/objects/<path:object_key>', methods=['DELETE'])
def delete_object(bucket_name, object_key):
    try:
        if not bucket_exists(bucket_name):
            return jsonify({'error': f'El bucket "{bucket_name}" no existe'}), 404
        
        if object_key not in buckets_storage[bucket_name]['objects']:
            return jsonify({'error': f'El objeto "{object_key}" no existe'}), 404
        
        del buckets_storage[bucket_name]['objects'][object_key]
        return jsonify({'message': f'Objeto "{object_key}" eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'Mini-S3 API',
        'timestamp': get_current_timestamp()
    }), 200

if __name__ == '__main__':
    print("=" * 50)
    print("Mini-S3 API iniciada")
    print("=" * 50)
    print("Endpoints disponibles:")
    print("  POST   /api/buckets")
    print("  GET    /api/buckets")
    print("  GET    /api/buckets/<n>")
    print("  DELETE /api/buckets/<n>")
    print("  POST   /api/buckets/<n>/objects")
    print("  GET    /api/buckets/<n>/objects")
    print("  GET    /api/buckets/<n>/objects/<key>")
    print("  PUT    /api/buckets/<n>/objects/<key>")
    print("  DELETE /api/buckets/<n>/objects/<key>")
    print("=" * 50)
    app.run(debug=True, port=5000)