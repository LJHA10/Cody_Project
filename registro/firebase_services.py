# mi_app/firebase_services.py
from firebase_admin import firestore

def agregar_datos_a_firestore(coleccion, datos):
    db = firestore.client()
    doc_ref = db.collection(coleccion).add(datos)
    return doc_ref.id
