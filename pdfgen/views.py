from django.views.generic import View
from django.utils import timezone
from .models import *
from pdfgen.render import Render
# Create your views here.

class Pdf(View):

	def get(self, request):
		sales = Sales.objects.all()
		today = timezone.now()

		params = {
			'today': today,
			'sales': sales,
			'request': render,
		}
		return Render.render('pdf.html', params)
