# Question 3: By default, do Django signals run in the same database transaction as the caller?

# Answer:
# Yes, Django signals run in the same database transaction as the caller by default, meaning the signal handlers are executed within the transaction context of the caller.

# Code:
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, created, **kwargs):
    # Check if in a transaction
    if transaction.get_connection().in_atomic_block:
        print("Signal handler is inside a transaction")
    else:
        print("Signal handler is outside a transaction")

# Wrap in a transaction block
with transaction.atomic():
    user = User.objects.create(username="testuser")

# Output:
# Signal handler is inside a transaction

# Explanation:
# The output confirms that the signal handler is running inside the same database transaction as the caller. This behavior is the default for Django signals, ensuring that signal handlers are executed within the transaction context of the caller. If the signal was executed outside the transaction, the output would indicate that the signal handler is outside a transaction.