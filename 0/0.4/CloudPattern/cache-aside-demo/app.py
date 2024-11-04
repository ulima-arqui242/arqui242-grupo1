import redis
import time

# Conexion a Redis
cache = redis.StrictRedis(host='redis', port=6379, db=0)

def get_data_from_db():

    # Simulación de un stream de base de datos
    time.sleep(2)
    return 'Hello, world!'

def get_data():

    # Se intenta acceder a la data en el cache de Redis
    cache_key = 'my_data'
    data = cache.get(cache_key)

    if data:
        # Se encontro data en el cache
        print('Cache hit')
        return data.decode('utf-8')
    else:
        # No hay data en el cache y en vez se recupera de la base de datos
        print('Cache miss')
        data = get_data_from_db()
        # Se guarda la data en el cache de Redis
        cache.setex(cache_key, 60, data)
        return data

if __name__ == '__main__':
    print(get_data())
    print(get_data())
