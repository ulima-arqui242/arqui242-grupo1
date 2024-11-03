import time
import redis
import logging
import signal
import sys

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Connect to Redis
redis_client = redis.Redis(host='redis', port=6379)

def signal_handler(sig, frame):
    logger.info('Graceful shutdown initiated.')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def process_appointments():
    # Check Redis connectivity
    try:
        redis_client.ping()
        logger.info("Connected to Redis")
    except redis.ConnectionError:
        logger.error("Could not connect to Redis. Exiting...")
        sys.exit(1)

    while True:
        try:
            appointment_id = redis_client.lpop('appointments')
            if appointment_id:
                logger.info(f'Processing appointment: {appointment_id.decode("utf-8")}')

                time.sleep(2)
            else:
                time.sleep(1) 
        except redis.RedisError as e:
            logger.error(f'Redis error: {e}')
            time.sleep(1)  

if __name__ == '__main__':
    process_appointments()
