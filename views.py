from django.shortcuts import render

def First(request):
    return render(request, 'Hi.html')

def result(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    runtype = request.GET['type']
    if runtype=='division' and num2 == '0':
        ctx = {
            'result':'division by zero'
        }
    elif runtype=='sum':
        ctx={
            'result':int(num1)+int(num2)
        }
    elif runtype=='subtraction':
        ctx={
            'result':int(num1)-int(num2)
        }
    elif runtype=='multiple':
        ctx={
            'result':int(num1)*int(num2)
        }
    elif runtype=='divide':
        ctx={
            'result':int(num1)/int(num2)
        }
    return render(request, 'result.html', ctx)
