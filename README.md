# Método de Priorización SNTD

Este proyecto es una aplicación en **Django** para registrar y priorizar requerimientos funcionales con el método **SNTD** (Satisfacción, Necesidad, Técnica y Dependencia), el cual cree como propuesta para un laboratorio de la matria de Desarrollo de Software II. 

Mi propuesta incluye la valoración de prioridades desde dos perspectivas:  
- **Cliente y usuario final** → con los ítems **Satisfacción** y **Necesidad**.  
- **Equipo desarrollador** → con los ítems **Técnica** y **Dependencia**.  

También tomo en cuenta que cada equipo puede tener diferentes enfoques, por lo cual propongo dos fórmulas:  

- ✖️ **Multiplicación:** `(S + N) * (T + D)`  
  👉 Prioriza lo **urgente y complejo**, ideal para equipos que desean empezar por lo difícil y crítico.  

- ➗ **División:** `(S + N) / (T + D)`  
  👉 Prioriza lo **urgente y sencillo**, ideal para equipos que desean avanzar rápido con lo fácil y urgente.  

---

Con esta app se puede:  
- Registrar secciones del proyecto.
- Registrar requerimientos funcionales en las secciones.  
- Ver los requerimientos listados en orden de importancia en cada sección.
- Ver listado general detallado.  
- Marcar como completados o eliminarlos.  

---

## Tecnologías
- Python 3.13  
- Django 5  
- HTML, CSS  

---

## Instalación rápida
```bash
git clone https://github.com/Daniela02092005/Metodo-de-priorizacion-SNTD.git
cd Metodo-de-priorizacion-SNTD
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py runserver
