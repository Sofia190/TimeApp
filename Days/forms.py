


from django.forms import ModelForm

from .models import Day



class DaysTillaDateForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_date', 'second_date']



class YearsWithAttributesEqualToaValueForm(ModelForm):


	class Meta:

		model = Day

		fields = ['date_for_years_with_attributes_equal_to_a_value', 'value_for_attributes']




class BisectYearsinaDecadeForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_year_of_decade', 'second_year_of_decade']





class BisectYearsinaCenturyForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_year_of_century', 'second_year_of_century']




class AttributesofnthDayForm(ModelForm):


	class Meta:

		model = Day

		fields = ['date_to_sum_attributes', "nth_day_value", "nth_month_value"]




class BisectYearsinCenturiesForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_date_bisect_years_in_centuries', "second_date_bisect_years_in_centuries"]




class MonthsandDaystillthenextSpringEquinoxForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_date_next_spring_equinox', "second_date_next_spring_equinox"]




class MonthsandDaystillthenextAutumnEquinoxForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_date_next_autumn_equinox', "second_date_next_autumn_equinox"]






class PeriodsbetweenDateswithTotalLunarEclipseForm(ModelForm):


	class Meta:

		model = Day

		fields = ['first_date_with_total_lunar_eclipse', "second_date_with_total_lunar_eclipse"]





class Find_the_equivalent_of_timezone_with_USA_Form(ModelForm):


	class Meta:

		model = Day

		fields = ['inTimeDelta_hours', "inTZObject_name", "datetime_instance_var",]






class Find_the_difference_of_timezone_with_USA_Form(ModelForm):


	class Meta:

		model = Day

		fields = ['inTimeDelta_hours_diff', "inTZObject_name_diff", "datetime_instance_var_diff",]









