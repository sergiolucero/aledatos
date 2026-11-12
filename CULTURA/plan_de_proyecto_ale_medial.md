# Plan de Desarrollo: Plataforma "Ale Medial"

## 1. Concepto y Visión General

**Ale Medial** se concibe como un "universo transmedial" interactivo enfocado en la Región y Comuna de Valparaíso. A diferencia de una web estática tradicional, el sitio actuará como un ecosistema vivo que conecta a los profesionales de la cultura, el patrimonio y el turismo creativo con la agenda cultural en tiempo real (impulsada por LinkedIn) y un mapeo territorial profundo.

**Inspiración Base:** *redterritoriosreativos.cl* (enfoque en redes y territorio), pero con una navegación más inmersiva y centrada en el dinamismo de las redes sociales profesionales.

## 2. Arquitectura del Sitio (Sitemap Propuesto)

La estructura se dividirá en 5 grandes áreas o "dimensiones" de este universo transmedial:

1. **Inicio: El Mapa Transmedial (Home)**
2. **Sociedad de Profesionales (El Catálogo)**
3. **Agenda "Not Gremio" (Feed en Tiempo Real)**
4. **Columnas de Opinión**
5. **Ecosistema de Festivales**

## 3. Desglose de Secciones

### 3.1. Inicio: El Mapa Transmedial

* **Interactividad Core:** La página principal no será un simple *scroll* de información, sino un mapa interactivo de Chile.
* **Prototipo de Navegación (Efecto Zoom):**
  * **Nivel 1:** Vista nacional (Chile).
  * **Nivel 2:** Al hacer clic, zoom in a la Región de Valparaíso.
  * **Nivel 3:** Zoom in a la Comuna de Valparaíso.
* **Contenido:** En este nivel de calle/comuna, el mapa revelará "puntos de luz" o nodos que representan a los profesionales, hitos patrimoniales y festivales.

### 3.2. Sociedad de Profesionales (Catálogo)

* **Objetivo:** Un directorio dinámico y visual de profesionales de la Región y Comuna de Valparaíso.
* **Categorías Principales:**
  * Cultura.
  * Turismo Creativo y de Intereses Especiales.
  * Patrimonio.
* **Fichas de Perfil:** Cada profesional tendrá una tarjeta visual que se puede expandir, mostrando su especialidad, proyectos destacados y enlaces de contacto.

### 3.3. Agenda "Not Gremio" (Integración LinkedIn)

* **Concepto:** Convertir la actividad de LinkedIn en el "pulso" o agenda en tiempo real del sitio.
* **Características:**
  * **Feed de Publicaciones:** Integración (vía API o *embeds*) del perfil **público** de LinkedIn de Alexandra Garín (Not Gremio). Al ser un perfil público, mostrará las publicaciones, fotos y videos recientes como una cartelera de lo que está ocurriendo ahora de forma transparente y accesible para todos los visitantes.
  * **Muro de Interacciones:** Una sub-sección en la parte inferior dedicada exclusivamente a mostrar los últimos comentarios de la comunidad en estas fotos y publicaciones, fomentando la sensación de una red viva y activa.

### 3.4. Columnas de Opinión

* **Enfoque:** Un espacio más editorial para el liderazgo de pensamiento.
* **Contenido:** Artículos y columnas de opinión extraídas/enlazadas directamente desde la sección de artículos nativos del perfil público de LinkedIn de Alexandra Garín. Diseño limpio, tipo blog o revista digital, para facilitar la lectura.

### 3.5. Ecosistema de Festivales

* **Objetivo:** Un calendario y vitrina permanente de los grandes hitos culturales anuales de la región.
* **Categorías de Cobertura:**
  * Danza.
  * Música.
  * Fotografía.
  * Artes Mediales.
  * Artes Visuales.
* **Visualización:** Puede integrarse como una capa adicional en el "Mapa Transmedial" (3.1) y como un calendario visual cronológico (timeline).

## 4. Diferencias Clave con la Referencia Original

Mientras que *redterritoriosreativos.cl* funciona más como un repositorio de iniciativas estáticas y mapeos institucionales, **Ale Medial** propone:

1. **Dinamismo Social:** El uso del perfil público de LinkedIn como motor de contenido (Not Gremio) asegura que la web nunca esté desactualizada.
2. **Navegación Geo-espacial:** El recorrido del usuario comienza desde la geografía (el zoom desde Chile a Valparaíso) en lugar de un menú tradicional.
3. **Foco en la Persona/Opinión:** Da protagonismo a la voz curatorial a través de las columnas de opinión y los comentarios de la comunidad.