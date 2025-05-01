from flask import Flask, render_template
import os
from routes import main_bp  # Importamos el Blueprint

app = Flask(__name__)

# Registramos el Blueprint
app.register_blueprint(main_bp)

# Función para verificar templates
def check_template(template_name):
    template_path = os.path.join(app.template_folder, template_name)
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"¡Archivo no encontrado! Verifica que existe: {template_path}")

if __name__ == '__main__':
    app.template_folder = 'templates'  # Fuerza la ubicación
    # Verificación completa
    required_templates = [
        'dashboard_html.html',
        'kpis_equipo1_html.html',
        'kpis_equipo2_html.html',
        'kpis_equipo3_html.html',
        'kpis_equipo4_html.html',
        'analisis_publicidad_html.html'
    ]
    missing = [t for t in required_templates if not os.path.exists(f'templates/{t}')]
    if missing:
        print(f"❌ Faltan archivos: {missing}")
    else:
        print("✅ Todos los archivos están presentes")
        app.run(debug=True)