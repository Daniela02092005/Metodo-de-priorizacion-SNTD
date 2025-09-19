# Método de Priorización SNTD

Este proyecto es una aplicación en **Django** para registrar y priorizar requerimientos funcionales con el método **SNTD** (Satisfacción, Necesidad, Técnica y Dependencia), el cual cree como propuesta para un laboratorio de la matria de Desarrollo de Software II.

Con esta app se puede:  
- Registrar requerimientos funcionales.  
- Listarlos en orden de importancia.  
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
