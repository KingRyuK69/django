# Question 2: Do Django signals run in the same thread as the caller?

# Answer:
# Yes, Django signals run in the same thread as the caller by default.

# Code:
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, created, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

# Trigger the signal by saving a user instance
print(f"Main thread: {threading.current_thread().name}")
user = User.objects.create(username="testuser")

# Output:
# Main thread: MainThread
# Signal handler running in thread: MainThread

# Explanation:
# The output shows that the signal handler is running in the same thread as the main thread, which confirms that Django signals run in the same thread as the caller by default. If the signal was executed in a separate thread, the output would show a different thread name for the signal handler