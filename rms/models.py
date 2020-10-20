from django.db import models

# Create your models here.


class dd(models.Model):
	"""docstring for ClassName"""
	Project = models.CharField(max_length=50,null=True,blank=True)
	System_RID_No = models.CharField(max_length=30,null=True,blank=True)
	Date = models.DateField(null=True,blank=True)
	RunTime_Hrs = models.FloatField(null=True,blank=True)
	Water_Discharge_Lts = models.FloatField(null=True,blank=True)
	Pump_Consumption_KWH = models.FloatField(null=True,blank=True)
	Inverter_Input_KWH = models.FloatField(null=True,blank=True)
	Inverter_Output_KWH = models.FloatField(null=True,blank=True)
	Total_KWH_Generation = models.FloatField(null=True,blank=True)
	Gross_KWH = models.FloatField(null=True,blank=True)


	def __str__(self):   
		return self.System_RID_No+  str(self.Date)


class md(models.Model):
	"""docstring for ClassName"""
	Project = models.CharField(max_length=50,null=True,blank=True)
	System_RID_No = models.CharField(max_length=30,null=True,blank=True)
	Date = models.DateField(null=True,blank=True)
	RunTime_Hrs = models.FloatField(null=True,blank=True)
	Water_Discharge_Lts = models.FloatField(null=True,blank=True)
	Pump_Consumption_KWH = models.FloatField(null=True,blank=True)
	Inverter_Input_KWH = models.FloatField(null=True,blank=True)
	Inverter_Output_KWH = models.FloatField(null=True,blank=True)
	Total_KWH_Generation = models.FloatField(null=True,blank=True)
	Gross_KWH = models.FloatField(null=True,blank=True)


	def __str__(self):   
		return self.System_RID_No+  str(self.Date)

class siteDtls(models.Model):
	"""docstring for ClassName"""
	Sid = models.CharField(max_length=30,null=True,blank=True)
	ConNum = models.IntegerField(null=True,blank=True)
	ConName = models.CharField(max_length=30,null=True,blank=True)
	ConMob = models.IntegerField(max_length=10, null=True,blank=True)
	LocName = models.CharField(max_length=30,null=True,blank=True)
	PumpDtls = models.CharField(max_length=30,null=True,blank=True)
	InvDtls = models.CharField(max_length=30,null=True,blank=True)
	


	def __str__(self):   
		return self.Sid+  str(self.ConName)



class meta:   #for admin database actions
	verbose_name = 'dd'
	erbose_name_plural = 'dd'

class meta:   #for admin database actions
	verbose_name = 'md'
	erbose_name_plural = 'md'

class meta:   #for admin database actions
	verbose_name = 'siteDtls'
	erbose_name_plural = 'siteDtls'
















	#def __init__(self, arg):
	#	super(ClassName, self).__init__()
	#	self.arg = arg

