from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def test_translation_fallback(self):
        faq = FAQ.objects.create(question="What is Django?", answer="A web framework")
        self.assertEqual(faq.get_translated_question('hi'), faq.question_hi)
        self.assertEqual(faq.get_translated_question('bn'), faq.question_bn)
