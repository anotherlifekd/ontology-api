import os
from owlready2 import AnnotationProperty, get_ontology, rdfs, Thing, ThingClass


ONTO_BASE = os.getenv("ONTO_BASE")
ONTO_SOURCE = "http://104.45.46.103/pot.owl"  # ONTO_SOURCE = f"{ONTO_BASE}v2/"
EXPORT_ONTO_URL = "https://standards.oftrust.net/v2/" # EXPORT_ONTO_URL = f"{ONTO_BASE}v2/"
ONTO = get_ontology(ONTO_SOURCE).load()

NAMESPACE = "https://standards.oftrust.net/v2/Vocabulary/"

class readonly(AnnotationProperty):
    namespace = get_ontology(ONTO_BASE).get_namespace(NAMESPACE)


class required(AnnotationProperty):
    namespace = get_ontology(ONTO_BASE).get_namespace(NAMESPACE)


class nest(AnnotationProperty):
    namespace = get_ontology(ONTO_BASE).get_namespace(NAMESPACE)


class label(AnnotationProperty):
    namespace = get_ontology(ONTO_BASE)


class comment(AnnotationProperty):
    namespace = get_ontology(ONTO_BASE)


class subPropertyOf(AnnotationProperty):
    namespace = rdfs


class subClassOf(AnnotationProperty):
    namespace = rdfs


class range(AnnotationProperty):
    namespace = rdfs


class domain(AnnotationProperty):
    namespace = rdfs


class restriction(AnnotationProperty):
    namespace = get_ontology('http://www.w3.org/2001/XMLSchema#')


class Link(Thing):
    namespace = get_ontology(ONTO_BASE).get_namespace(NAMESPACE)


class Identity(Thing):
    namespace = get_ontology(ONTO_BASE).get_namespace(NAMESPACE)


class Annotation(Thing):
    namespace = get_ontology(ONTO_BASE).get_namespace(NAMESPACE)
