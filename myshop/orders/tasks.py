from celery import task
from django.core.mail import send_mail
from .models import Order
from celery import Celery
from django.conf import settings

@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Dear {},\n\nYou have successfully placed an order. \'' \
              'You order id is {}'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [order.email],
                          fail_silently=False)
    return mail_sent










