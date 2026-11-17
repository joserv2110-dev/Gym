# FitTrack 💪 — tu app de condición física para iPhone

App web instalable (PWA), sin cuentas ni servidores: tus datos se guardan en tu iPhone y funciona sin conexión.

## Instalar en el iPhone
1. Publica la carpeta `docs/` en un hosting HTTPS gratuito (GitHub Pages: *Settings → Pages → rama → carpeta `/docs`*; o Netlify/Cloudflare Pages arrastrando la carpeta).
2. Abre la URL en **Safari** → botón Compartir → **Añadir a pantalla de inicio**.
3. Abre FitTrack, completa tu perfil (edad, peso, estatura, objetivo, nivel, días, minutos, equipo, meta). Las metas de calorías, proteína, agua, pasos y sueño se calculan solas.

## Qué incluye
- **Hoy**: % de cumplimiento diario, racha, menú de 10 accesos (entreno, peso, agua, actividad, comida, sueño, progreso, objetivos, resumen, ajustes), registro de agua en 1 toque y recomendaciones del momento.
- **Entreno**: **rutina por músculos** (eliges qué trabajar hoy y se genera sola) y plan semanal generado según tus días/tiempo/equipo/objetivo, series con kg y reps, **sugerencia de sobrecarga progresiva**, temporizador de descanso, entreno libre, cardio con calorías estimadas y detección de récords.
- **Comida**: calorías y proteína con comidas frecuentes de un toque. **Sueño**: horas y calidad. **Pasos**, **peso** y **medidas** con cambios.
- **Progreso**: gráficas (peso, pasos, agua), resumen semanal y mensual, constancia por día de la semana (detecta tu día más flojo) e historial editable.
- **Metas**: avance hacia tu peso meta y fecha estimada, metas de rendimiento (p. ej. sentadilla 100 kg), récords personales.
- **Recordatorios**: eventos semanales en Calendario con alarma (.ics), avisos con la app abierta y automatizaciones de Atajos.
- Respaldo/restauración JSON y exportación CSV.

## Siri, Salud y automatizaciones (Atajos)
La app registra datos al abrir una URL con parámetros: `agua`, `pasos`, `sueno`, `peso`, `kcal`, `prot`, `cardio`.
Ejemplo: `https://TU-URL/index.html?agua=250&pasos=8500&sueno=7.5`

Atajos recomendados (app Atajos → *Abrir URLs*):
- **Agua** (Siri: “Oye Siri, agua”): `?agua=250`.
- **Sincronizar Salud** (automatización diaria 21:00): *Buscar muestras de salud* (Pasos, hoy) → *Calcular estadísticas (Suma)*; *Buscar muestras de salud* (Sueño, últimas 24 h) → suma de horas; luego *Abrir URL* con `?pasos=[suma]&sueno=[horas]`. Opcionalmente añade `&peso=` desde la última muestra de Peso.
- **Recordatorios**: automatizaciones por hora (10:00 agua, 17:30 entreno, 21:30 revisar el día) con *Mostrar notificación*.

> Nota: iOS no permite que una web lea Apple Salud directamente; el puente son los Atajos.
