from django.shortcuts import render
from .models import dd, md, siteDtls
from django.http import HttpResponse, JsonResponse

from datetime import datetime, timedelta
from django.db.models import Sum, Avg

import json

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):

	"""xaxis = list(md.objects.values('Date'))
	yaxis = list(md.objects.values('Inverter_Output_KWH'))
	return JsonResponse({'xaxis': xaxis, 'yaxis': yaxis})"""

	xaxis=[]
	yaxis=[]
	data = dd.objects.filter(System_RID_No='1001')[:4]
	t_GPower = md.objects.filter(System_RID_No='1001').aggregate(Sum('Gross_KWH')).get('Gross_KWH__sum')
	t_InvPower = md.objects.filter(System_RID_No='1001').aggregate(Sum('Inverter_Output_KWH')).get('Inverter_Output_KWH__sum')
	t_PumpPower = md.objects.filter(System_RID_No='1001').aggregate(Sum('Pump_Consumption_KWH')).get('Pump_Consumption_KWH__sum')
	t_PumpLtrs = md.objects.filter(System_RID_No='1001').aggregate(Sum('Water_Discharge_Lts')).get('Water_Discharge_Lts__sum')

	for x in data:
		xaxis.append(str(x.Date))
		yaxis.append(x.Inverter_Output_KWH)

		#now = datetime.now().date()
		#print(datetime.strptime(x.Date, "%Y-%m-%d")).date()
	return render(request, 'index.html', {'xaxis': xaxis, 'yaxis': yaxis, 't_GPower': t_GPower, 't_InvPower': t_InvPower, 't_PumpPower': t_PumpPower, 't_PumpLtrs': t_PumpLtrs})

	

		#return render(request, 'data.html', {'xaxis': xaxis, 'yaxis': yaxis})

	#return render(request, 'index.html')

def search(request):
	if request.method=="POST":

		id_no=request.POST['idno']

		xaxis=[]
		yaxis=[]
		chart_data = dd.objects.filter(System_RID_No=id_no)[:4]

		for x in chart_data:
			xaxis.append(str(x.Date))
			yaxis.append(x.Inverter_Output_KWH)

		t_GPower = md.objects.filter(System_RID_No=id_no).aggregate(Sum('Gross_KWH')).get('Gross_KWH__sum')
		t_InvPower = md.objects.filter(System_RID_No=id_no).aggregate(Sum('Inverter_Output_KWH')).get('Inverter_Output_KWH__sum')
		t_PumpPower = md.objects.filter(System_RID_No=id_no).aggregate(Sum('Pump_Consumption_KWH')).get('Pump_Consumption_KWH__sum')
		t_PumpLtrs = md.objects.filter(System_RID_No=id_no).aggregate(Sum('Water_Discharge_Lts')).get('Water_Discharge_Lts__sum')
		return render(request, 'index.html', {'xaxis': xaxis, 'yaxis': yaxis, 'id_no':id_no, 't_GPower': t_GPower, 't_InvPower': t_InvPower, 't_PumpPower': t_PumpPower, 't_PumpLtrs': t_PumpLtrs})
	else:
		return render(request, 'index.html')


def bldc(request):
	table_data = siteDtls.objects.all()
	return render(request, 'bldcsites.html', {'table_data': table_data})

def dayR(request):
	table_data = dd.objects.all()
	return render(request, 'dayR.html', {'table_data': table_data})

def monthR(request):
	table_data = md.objects.all()
	return render(request, 'monthR.html', {'table_data': table_data})

def openId(request, System_RID_No):
	xaxis=[]
	yaxis=[]
	chart_data = dd.objects.filter(System_RID_No=System_RID_No)[:4]

	for x in chart_data:
		xaxis.append(str(x.Date))
		yaxis.append(x.Inverter_Output_KWH)

	id_no = System_RID_No

	t_GPower = md.objects.filter(System_RID_No=System_RID_No).aggregate(Sum('Gross_KWH')).get('Gross_KWH__sum')
	t_InvPower = md.objects.filter(System_RID_No=System_RID_No).aggregate(Sum('Inverter_Output_KWH')).get('Inverter_Output_KWH__sum')
	t_PumpPower = md.objects.filter(System_RID_No=System_RID_No).aggregate(Sum('Pump_Consumption_KWH')).get('Pump_Consumption_KWH__sum')
	t_PumpLtrs = md.objects.filter(System_RID_No=System_RID_No).aggregate(Sum('Water_Discharge_Lts')).get('Water_Discharge_Lts__sum')
	return render(request, 'index.html', {'xaxis': xaxis, 'yaxis': yaxis, 'id_no':id_no, 't_GPower': t_GPower, 't_InvPower': t_InvPower, 't_PumpPower': t_PumpPower, 't_PumpLtrs': t_PumpLtrs})

@csrf_exempt
def GetInvDaysData(request):
    ddata=json.loads(request.body)
    # start_date=datetime.strptime(request.GET["start"],"%Y-%m-%d")
    #end_date=datetime.strptime(request.GET["end"],"%Y-%m-%d")+timedelta(days=1)
    # d = datetime.strptime(request.POST['TestDate'],"%Y-%m-%d").date()
    d = datetime.strptime(ddata["TestDate"],"%Y-%m-%d").date()
    p = ddata['ProjectName']
    c=datetime.now().date()
    #print(d)
                
    if d<c :
        data = list(dd.objects.filter(Date__startswith=d, Project=p).values('Project','System_RID_No','Date','RunTime_Hrs','Water_Discharge_Lts','Pump_Consumption_KWH','Inverter_Input_KWH','Inverter_Output_KWH','Total_KWH_Generation','Gross_KWH'))
        return JsonResponse({'Day Wise Data': data})
    else:
        return HttpResponse('<h1>Inavalid Date Request<h1>')
    #else:
        #return HttpResponse('Error!')

@csrf_exempt
def GetInvMonthData(request):
    ddata=json.loads(request.body)
    d = datetime.strptime(ddata["TestDate"],"%Y-%m-%d").date()
    p = ddata['ProjectName']

    data = list(md.objects.filter(Date__startswith=d, Project=p).values('Project','System_RID_No','Date','RunTime_Hrs','Water_Discharge_Lts','Pump_Consumption_KWH','Inverter_Input_KWH','Inverter_Output_KWH','Total_KWH_Generation','Gross_KWH'))
    return JsonResponse({'Month Wise Data': data})
