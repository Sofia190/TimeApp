from django.db import models

# Create your models here.


from datetime import timedelta, datetime, date

from django.utils import timezone

from django.db.models import Q




class DayQuerySet(models.query.QuerySet):

	def search(self, query):
		lookup = ( Q(date_time_field__icontains=query) )

		return self.filter(lookup)
				



class DayModelManager(models.Manager):


	def get_queryset(self):
		    return DayQuerySet(self.model, using=self._db)



	def search(self, query=None):
			if query is None:
				return self.get_queryset.none()
			return self.get_queryset().search(query)




class Day(models.Model):

	date_time_field = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)

	first_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	second_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	
	one_date_res = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
	two_date_res = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
	
	days_till_a_date_result = models.IntegerField(default=0)



	date_for_years_with_attributes_equal_to_a_value = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	date_for_years_with_attributes_equal_to_a_value_result = models.IntegerField(default=0)
	value_for_attributes = models.IntegerField(default=0)
	attributes_sum = models.IntegerField(default=0)


	first_year_of_decade = models.IntegerField(default=0)
	second_year_of_decade = models.IntegerField(default=0)
	bisect_years = models.TextField(default=0)
	days_in_a_decade = models.IntegerField(default=0)
	bisect_years_count = models.IntegerField(default=0)


	first_year_of_century = models.IntegerField(default=0)
	second_year_of_century = models.IntegerField(default=0)
	bisect_years_in_century = models.TextField(default=0)
	days_in_a_century = models.IntegerField(default=0)
	bisect_years_count_in_century = models.IntegerField(default=0)


	date_to_sum_attributes = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	date_to_sum_attributes_result = models.IntegerField(default=0)
	date_to_sum_attributes_days = models.IntegerField(default=0)
	nth_day_value = models.IntegerField(default=0)
	nth_month_value = models.IntegerField(default=0)


	first_date_bisect_years_in_centuries = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	second_date_bisect_years_in_centuries = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	bisect_years_in_centuries = models.TextField(default=0)
	days_in_centuries = models.IntegerField(default=0)
	bisect_years_count_in_centuries = models.IntegerField(default=0)


	first_date_next_spring_equinox = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	second_date_next_spring_equinox = models.DateField(auto_now=False, auto_now_add=False, default=date(2021,3,20))
	months_until_next_spring_equinox = models.IntegerField(default=0)
	days_until_next_spring_equinox = models.IntegerField(default=0)



	first_date_next_autumn_equinox = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	second_date_next_autumn_equinox = models.DateField(auto_now=False, auto_now_add=False, default=date(2021,9,22))
	months_until_next_autumn_equinox = models.IntegerField(default=0)
	days_until_next_autumn_equinox = models.IntegerField(default=0)


	first_date_with_total_lunar_eclipse = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	second_date_with_total_lunar_eclipse = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	months_between_dates_with_total_lunar_eclipse = models.IntegerField(default=0)
	minutes_between_dates_with_total_lunar_eclipse = models.IntegerField(default=0)

	inTimeDelta_hours = models.IntegerField(default=0)
	inTZObject_name = models.CharField(max_length=70, default='EDT')
	datetime_instance_var = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
	first_date_time_var = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
	second_date_time_var = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)



	inTimeDelta_hours_diff = models.IntegerField(default=0)
	inTZObject_name_diff = models.CharField(max_length=70, default='EDT')
	datetime_instance_var_diff = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
	first_date_time_var_diff = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)
	second_date_time_var_diff = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now)

	timezone_diff_days= models.IntegerField(default=0)
	timezone_diff_minutes = models.IntegerField(default=0)



	used_in_calculations_by_user = models.BooleanField(default=False)





	objects = DayModelManager() 








