# Question 1: By default, are Django signals executed synchronously or asynchronously?

# Answer:
# Django signals are executed synchronously by default. When a signal is triggered, the connected signal handler (receiver) is executed immediately in the same thread and process.

# Code:
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, created, **kwargs):
    print("Signal received, processing...")
    time.sleep(5)  # Simulate a time-consuming task
    print("Signal processing completed.")

# Trigger the signal by saving a user instance
user = User.objects.create(username="testuser")

print("User save completed")

# Output:
# Signal received, processing...
# After 5 seconds:
# Signal processing completed.
# User save completed

#Explanation:
# The delay caused by time.sleep(5) proves that the signal is executed synchronously. The main thread waits for the signal handler to finish before completing the save operation. If the signal was executed asynchronously, the "User save completed" message would be printed immediately after the "Signal received, processing..." message.