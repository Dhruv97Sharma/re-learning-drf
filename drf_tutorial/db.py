import dj_database_url
import os

DATABASE_URL = os.environ.get('DATABASE_URL')

DATABASES = {
  'default': dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=10000,
        conn_health_checks=True
    )
}