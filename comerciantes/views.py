from django.shortcuts import render
from .models import Comerciante

# FUNCION PARA MOSTRAR EL INDEX
def mostrarIndex(request):
    return render(request, "index.html")

# FUNCION PARA MOSTRAR EL LISTADO
def mostrarListado(request):
    comer = Comerciante.objects.all().values()
    datos = {'comer' : comer}
    return render(request, "listado.html", datos)

# FUNCION PARA MOSTRAR EL FORMULARIO DE REGISTRO
def mostrarFormularioRegistro(request):
    return render(request, "form_registrar.html") 

# FUNCION PARA INSERTAR UN NUEVO COMERCIANTE
def insertarComerciante(request):
    rut = request.POST['txtrut']
    raz = request.POST['txtraz']
    gir = request.POST['txtgir']
    com = request.POST['cbocom']
    dir = request.POST['txtdir']
    ven = request.POST['txtven']
    est = request.POST['opest']
    comer = Comerciante(rut=rut, razonsocial=raz, giro=gir, comuna=com, direccion=dir, numeroventas=ven, estado=est)
    comer.save()
    datos = {'r':'GENIAL!, Se registro con exito el nuevo COmerciante'}
    return render(request, 'form_registrar.html', datos)

# FUNCION PARA ELIMINAR AL COMERCIANTE SELECCIONADO
def eliminarComerciante(request, id):
    try:
        comer = Comerciante.objects.get(id=id)
        comer.delete()
        comer = Comerciante.objects.all().values()
        datos = {'comer' : comer, 'r':'Se Elimino con exito al Comerciante'}
        return render(request, "listado.html", datos)
    except:
        comer = Comerciante.objects.all().values()
        datos = {'comer' : comer, 'r2':'ERROR, No se pudo Eliminar al Comerciante'}
        return render(request, "listado.html", datos)

#FUNCION PARA MOSTRAR EL FORMULARIO DE ACTUALIZAR
def mostrarFormularioActualizar(request, id):
    try:
        comer = Comerciante.objects.get(id=id)
        datos = {'comer' : comer}
        return render(request, "form_actualizar.html", datos)
    except:
        comer = Comerciante.objects.all().values()
        datos = {'comer' : comer, 'r2':'ERROR, No se pudo Encontrar al Comerciante'}
        return render(request, "listado.html", datos)

def actualizarComerciante(request, id):
    try:
        rut = request.POST['txtrut']
        raz = request.POST['txtraz']
        gir = request.POST['txtgir']
        com = request.POST['cbocom']
        dir = request.POST['txtdir']
        ven = request.POST['txtven']
        est = request.POST['opest']
        comer = Comerciante.objects.get(id=id)
        comer.rut = rut
        comer.razonsocial = raz
        comer.giro = gir
        comer.comuna = com
        comer.direccion = dir
        comer.numeroventas = ven
        comer.estado = est
        comer.save()
        comer = Comerciante.objects.all().values()
        datos = {'comer' : comer,'r':'Se Actualizo con exito'}
        return render(request, "listado.html", datos)
    except:
        comer = Comerciante.objects.all().values()
        datos = {'comer' : comer, 'r2':'ERROR, No se pudo Actualizar al Comerciante'}
        return render(request, "listado.html", datos)




