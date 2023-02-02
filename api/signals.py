from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Metaphor, Book


@receiver(post_save, sender=Metaphor)
def add_one_to_metaphors(sender, instance, created, **kwargs):
    if created:
        book = Book.objects.get(id=instance.book.id)
        if instance.event == 'metaphor':
            book.metaphors += 1
            book.number_of_borrowed_books += 1
            book.save()
        else:
            book.number_of_borrowed_books -= 1
            book.save()
