from celery.utils.log import get_task_logger
from factorioprints.celery import app
from .models import Prints
from .views import ScrapeFactorio


logger = get_task_logger(__name__)
@app.task
def auto_update_prints():
    aa = ScrapeFactorio()
    aa.update_all()
    print("$$$$$$$$$$$$$$$$$4 DONE $$$$$$$$$$$$$$$$$$4")
    return {'status': 'sent successfully'}