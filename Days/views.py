from django.shortcuts import render, redirect

# Create your views here.

import datetime

# from datetime import timedelta, datetime, date  



from.forms  import (DaysTillaDateForm, YearsWithAttributesEqualToaValueForm,

BisectYearsinaDecadeForm, BisectYearsinaCenturyForm,

AttributesofnthDayForm, BisectYearsinCenturiesForm, 
		    
MonthsandDaystillthenextSpringEquinoxForm,
		    
MonthsandDaystillthenextAutumnEquinoxForm, 
		    
PeriodsbetweenDateswithTotalLunarEclipseForm,

Find_the_equivalent_of_timezone_with_USA_Form,

 Find_the_difference_of_timezone_with_USA_Form,)



from .models import Day

from dateutil import parser



def view_days_till_a_date(request):

	if request.method == 'POST':

		form = DaysTillaDateForm(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			obj.days_till_a_date_result = (obj.second_date-obj.first_date).days

			obj.used_in_calculations_by_user = True

			obj.save()

			form = DaysTillaDateForm()

	else:

		form = DaysTillaDateForm()

	obj = Day.objects.last()
	

	template_path = "Days/days-till-a-date.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def view_days_till_a_date_display_attributes(request):

	if request.method == 'POST':

		form = DaysTillaDateForm(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			obj.days_till_a_date_result = (obj.second_date-obj.first_date).days

			obj.used_in_calculations_by_user = True

			obj.save()

			form = DaysTillaDateForm()

	else:

		form = DaysTillaDateForm()

	obj = Day.objects.last()
	
	template_path = "Days/days-till-a-date-display-attributes.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def view_years_with_equal_sum_of_attributes_to_a_value(request):

	
	if request.method == 'POST':

		form = YearsWithAttributesEqualToaValueForm(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			dt_obj = parser.parse(str(obj.date_for_years_with_attributes_equal_to_a_value))

			obj_d = date.fromordinal(dt_obj.toordinal())

			var = (sum(map(int, str(obj_d.year))) + obj_d.month + obj_d.day)

			if var == obj.value_for_attributes:
    
   				var1 = obj_d.year

   				obj.date_for_years_with_attributes_equal_to_a_value_result = var1

   				obj.used_in_calculations_by_user = True


   				obj.save()

   				form = YearsWithAttributesEqualToaValueForm()

			else:

				var2 = var

				obj.attributes_sum = var2

				obj.used_in_calculations_by_user = True

				obj.save()

				form = YearsWithAttributesEqualToaValueForm()
	else:

		form = YearsWithAttributesEqualToaValueForm()

	obj = Day.objects.last()
	
	template_path = "Days/attributes-equal-to-a-value.html"

	return render(request, template_path, {'form': form, "obj":obj, })







def view_leap_years_in_a_decade(request):


	if request.method == 'POST':

		form = BisectYearsinaDecadeForm(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()


			dl=[]

			count = 0

			dl_years = [i for i in range(obj.first_year_of_decade, obj.second_year_of_decade+1)]


			d = date(obj.first_year_of_decade, 1, 1)

			dt = date(obj.second_year_of_decade, 1, 1)


			td = dt - d

			obj.days_in_a_decade = td.days


			for i in dl_years:

				dl.append(date(i, 1, 1))


			obj.bisect_years = " "
            	


			for i in dl:

			    if (i.year % 4) == 0:
			        if (i.year % 100) == 0:

			        	if (i.year % 400) == 0:
			        		obj.bisect_years+=(str(i.year)+ ", ")
			        		count += 1
			           
			        else:
			            obj.bisect_years+=(str(i.year)+ ", ")

			            count += 1
			 
			obj.bisect_years_count = count

			obj.used_in_calculations_by_user = True


			obj.save()

			form = BisectYearsinaDecadeForm()
	else:

		form = BisectYearsinaDecadeForm()

	obj = Day.objects.last()
	
	template_path = "Days/bisect-years-in-a-decade.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def view_leap_years_in_a_century(request):


	if request.method == 'POST':

		form = BisectYearsinaCenturyForm(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()


			dl=[]

			count = 0

			dl_years = [i for i in range(obj.first_year_of_century, obj.second_year_of_century+1)]


			d = date(obj.first_year_of_century, 1, 1)

			dt = date(obj.second_year_of_century, 1, 1)


			td = dt - d

			obj.days_in_a_century = td.days


			for i in dl_years:

				dl.append(date(i, 1, 1))


			obj.bisect_years_in_century = " "
            	


			for i in dl:

			    if (i.year % 4) == 0:
			        if (i.year % 100) == 0:

			        	if (i.year % 400) == 0:
			        		obj.bisect_years_in_century+=(str(i.year)+ ", ")
			        		count += 1

			        else:
			            obj.bisect_years_in_century+=(str(i.year)+ ", ")

			            count += 1

			obj.bisect_years_count_in_century = count

			obj.used_in_calculations_by_user = True


			obj.save()

			form = BisectYearsinaCenturyForm()
	else:

		form = BisectYearsinaCenturyForm()

	obj = Day.objects.last()
	
	template_path = "Days/bisect-years-in-a-century.html"

	return render(request, template_path, {'form': form, "obj":obj, })





   	

def view_sum_of_attributes_of_nth_day_in_a_year(request):


	if request.method == 'POST':

		form = AttributesofnthDayForm(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()


			dl =[]

			dly = [obj.date_to_sum_attributes]

			dli = []


			for i in dly:

				dl.append(date(i.year, 1, 1))

			for i in dl:

				dli.append(i.replace(day=obj.nth_day_value, month=obj.nth_month_value))

			for i in dli:

				var = sum(map(int, str(i.year))) + i.month + i.day


			obj.date_to_sum_attributes_result = var

			obj.used_in_calculations_by_user = True


			obj.save()

			form = AttributesofnthDayForm()
	else:

		form = AttributesofnthDayForm()

	obj = Day.objects.last()
	
	template_path = "Days/sum-of-attributes-of-nth-day.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def view_how_many_bisect_years_in_the_last_nth_centuries(request):


	if request.method == 'POST':

		form = BisectYearsinCenturiesForm(request.POST)

		if form.is_valid():

			form.save()

			obj = Day.objects.last()


			dl=[]

			count = 0

			dl_years = [i for i in range(obj.first_date_bisect_years_in_centuries.year, 
				obj.second_date_bisect_years_in_centuries.year+100)]


			d = date(obj.first_date_bisect_years_in_centuries.year, 1, 1)

			dt = date(obj.second_date_bisect_years_in_centuries.year, 1, 1)


			td = dt - d

			obj.days_in_centuries = td.days


			for i in dl_years:

				dl.append(date(i, 1, 1))


			obj.bisect_years_in_centuries = " "
            	


			for i in dl:

			    if (i.year % 4) == 0:
			        if (i.year % 100) == 0:

			        	if (i.year % 400) == 0:
			        		obj.bisect_years_in_centuries+=(str(i.year)+ ", ")
			        		count += 1

			        else:
			            obj.bisect_years_in_centuries+=(str(i.year)+ ", ")

			            count += 1
	
			obj.bisect_years_count_in_centuries = count

			obj.used_in_calculations_by_user = True


			obj.save()

			form = BisectYearsinCenturiesForm()
	else:

		form = BisectYearsinCenturiesForm()

	obj = Day.objects.last()
	
	template_path = "Days/bisect-years-in-centuries.html"

	return render(request, template_path, {'form': form, "obj":obj, })






def how_many_months_and_days_till_the_next_spring_equinox(request):


	if request.method == 'POST':

		form = MonthsandDaystillthenextSpringEquinoxForm(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()


			d = obj.first_date_next_spring_equinox

			dt = obj.second_date_next_spring_equinox

			td = dt - d

			obj.days_until_next_spring_equinox = td.days

			obj.months_until_next_spring_equinox = td.days//30

			obj.used_in_calculations_by_user = True

			obj.save()

			form = MonthsandDaystillthenextSpringEquinoxForm()

	else:

		form = MonthsandDaystillthenextSpringEquinoxForm()

	obj = Day.objects.last()
	
	template_path = "Days/days-till-the-next-spring-equinox.html"

	return render(request, template_path, {'form': form, "obj":obj, })

    



def how_many_months_and_days_till_the_next_autumn_equinox(request):


	if request.method == 'POST':

		form = MonthsandDaystillthenextAutumnEquinoxForm(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()


			d = obj.first_date_next_autumn_equinox

			dt = obj.second_date_next_autumn_equinox

			td = dt - d

			obj.days_until_next_autumn_equinox = td.days

			obj.months_until_next_autumn_equinox = td.days//30

			obj.used_in_calculations_by_user = True

			obj.save()

			form = MonthsandDaystillthenextAutumnEquinoxForm()

	else:

		form = MonthsandDaystillthenextAutumnEquinoxForm()

	obj = Day.objects.last()
	
	template_path = "Days/days-till-the-next-autumn-equinox.html"

	return render(request, template_path, {'form': form, "obj":obj, })

    
	


def what_period_between_years_with_total_lunar_eclipse(request):


	if request.method == 'POST':

		form = PeriodsbetweenDateswithTotalLunarEclipseForm(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			res = []

			res_1 = []

			res_2 = []


			dt_le = [(obj.first_date_with_total_lunar_eclipse.year,
				obj.first_date_with_total_lunar_eclipse.month,
				obj.first_date_with_total_lunar_eclipse.day,)]

			dt_le_1= [(obj.second_date_with_total_lunar_eclipse.year,
				obj.second_date_with_total_lunar_eclipse.month,
				obj.second_date_with_total_lunar_eclipse.day,)]

			for i in range(1):


				if  (obj.second_date_with_total_lunar_eclipse.month != 1 and 
					obj.second_date_with_total_lunar_eclipse.day != 1) :
				

					res.append(dt_le_1[i][0]- dt_le[i][0])
					res_1.append(abs(dt_le_1[i][1] - dt_le[i][1]))
					res_2.append(abs(dt_le_1[i][2] - dt_le[i][2]))

				else:

					res.append(0)
					res_1.append(abs(12 - dt_le[i][1]))
					res_2.append(abs(30 - dt_le[i][2]))

			td = timedelta(days=res[0]*365 + res_2[0]+ (res_1[0]*4*7))


			print(str(obj.second_date_with_total_lunar_eclipse.month))
			print(str(obj.second_date_with_total_lunar_eclipse.day))

			print("days",td.days)
			print(res)
			print(res_1)
			print(res_2)


			obj.months_between_dates_with_total_lunar_eclipse = td.days//30
			obj.minutes_between_dates_with_total_lunar_eclipse = td.days * 1440

			obj.used_in_calculations_by_user = True

			obj.save()

			form = PeriodsbetweenDateswithTotalLunarEclipseForm()

	else:

		form = PeriodsbetweenDateswithTotalLunarEclipseForm()

	obj = Day.objects.last()
	

	template_path = "Days/periods-between-dates-with-total-lunar-eclipse.html"

	return render(request, template_path, {'form': form, "obj":obj, })

    



def find_the_equivalent_of_timezone_with_USA(request):


	if request.method == 'POST':

		form = Find_the_equivalent_of_timezone_with_USA_Form(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			inTimeDelta = datetime.timedelta(hours=obj.inTimeDelta_hours)

			inTZObject = datetime.timezone(inTimeDelta, obj.inTZObject_name)

			obj.datetime_instance_var = datetime.datetime(obj.datetime_instance_var.year,
			obj.datetime_instance_var.month, obj.datetime_instance_var.day, 
			obj.datetime_instance_var.hour, obj.datetime_instance_var.minute, 
			obj.datetime_instance_var.second, obj.datetime_instance_var.microsecond,
			 inTZObject)

			obj.first_date_time_var = inTZObject.fromutc(obj.datetime_instance_var)

			obj.second_date_time_var =  (obj.datetime_instance_var - obj.datetime_instance_var.utcoffset())

			obj.used_in_calculations_by_user = True

			obj.save()

			form = Find_the_equivalent_of_timezone_with_USA_Form()

	else:

		form = Find_the_equivalent_of_timezone_with_USA_Form()

	obj = Day.objects.last()
	
	
	template_path = "Days/find-the-equivalent-of-timezone-with-USA.html"

	return render(request, template_path, {'form': form, "obj":obj, })

    

	


def find_the_difference_of_timezone_with_USA(request):


	if request.method == 'POST':

		form = Find_the_difference_of_timezone_with_USA_Form(request.POST)


		if form.is_valid():

			form.save()

			obj = Day.objects.last()

			USANYTimeDelta = datetime.timedelta(hours=obj.inTimeDelta_hours_diff)

			USANYTZObject= datetime.timezone(USANYTimeDelta, obj.inTZObject_name_diff)

			obj.datetime_instance_var_diff = datetime.datetime(obj.datetime_instance_var_diff.year,
			obj.datetime_instance_var_diff.month, obj.datetime_instance_var_diff.day, 
			obj.datetime_instance_var_diff.hour, obj.datetime_instance_var_diff.minute, 
			obj.datetime_instance_var_diff.second, obj.datetime_instance_var_diff.microsecond,
			USANYTZObject)

			obj.first_date_time_var_diff = USANYTZObject.fromutc(obj.datetime_instance_var_diff)

			var  =  (obj.datetime_instance_var_diff - obj.datetime_instance_var_diff.utcoffset())

			obj.second_date_time_var_diff = USANYTZObject.fromutc(var)

			obj.timezone_diff_days = obj.datetime_instance_var_diff.utcoffset().days

			obj.timezone_diff_minutes =  abs(obj.datetime_instance_var_diff.utcoffset()).seconds // 60

			obj.used_in_calculations_by_user = True

			obj.save()

			form = Find_the_difference_of_timezone_with_USA_Form()

	else:

		form = Find_the_difference_of_timezone_with_USA_Form()

	obj = Day.objects.last()
	

	template_path = "Days/find-the-difference-of-timezone-with-USA.html"

	return render(request, template_path, {'form': form, "obj":obj, })

    

	








