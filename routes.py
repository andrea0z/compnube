from flask import Blueprint, render_template
# Importa tu base de datos si es necesario
# from database.db import db
# from database.models import KPI

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('dashboard_html.html')

# Agregar rutas con los nombres exactos de las URLs solicitadas
@main_bp.route('/kpis_equipo1_html.html')
def kpis_equipo1():
    # Descomenta estas líneas si estás usando una base de datos
    # kpis = KPI.query.filter_by(team='equipo1').all()
    # return render_template('kpis_equipo1_html.html', kpis=kpis)
    return render_template('kpis_equipo1_html.html')

@main_bp.route('/kpis_equipo2_html.html')
def kpis_equipo2():
    return render_template('kpis_equipo2_html.html')

@main_bp.route('/kpis_equipo3_html.html')
def kpis_equipo3():
    return render_template('kpis_equipo3_html.html')

@main_bp.route('/kpis_equipo4_html.html')
def kpis_equipo4():
    return render_template('kpis_equipo4_html.html')

@main_bp.route('/analisis_publicidad_html.html')
def analisis_publicidad():
    return render_template('analisis_publicidad_html.html')

# Mantener también las rutas originales por compatibilidad
@main_bp.route('/equipo1')
def equipo1():
    return render_template('kpis_equipo1_html.html')

@main_bp.route('/equipo2')
def equipo2():
    return render_template('kpis_equipo2_html.html')

@main_bp.route('/equipo3')
def equipo3():
    return render_template('kpis_equipo3_html.html')

@main_bp.route('/equipo4')
def equipo4():
    return render_template('kpis_equipo4_html.html')

@main_bp.route('/analisis-publicidad')
def analisis_publicidad_guion():
    return render_template('analisis_publicidad_html.html')