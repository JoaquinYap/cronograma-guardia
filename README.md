# Cronograma de guardias

Programa de una sola página para armar el cronograma mensual del personal y exportarlo a Excel (.xlsx) con el formato de la planilla "DEPOSITO DE FARMACIA".

## Cómo usarlo
Abrí `cronograma.html` con doble clic (Chrome o Edge). No necesita internet ni instalación. Funciona también en el celular.

- Elegí un pincel (24, 16, 12, 11, 10, 8, 7, RP, LE, LAR, Gris) y tocá o arrastrá sobre los días, o tocá el nombre de una persona para cargarle días con un calendario.
- Feriados: se marcan tocando los días en la barra de arriba (sábados y domingos van solos en amarillo).
- "Descargar como Excel" genera el `.xlsx`. "Importar Excel" lee un `.xlsx` con el mismo formato.
- Todo se guarda en el navegador; usá "Guardar respaldo" para tener una copia.

## Para desarrollo
- `src/app.html`: la aplicación (HTML + CSS + JS).
- `src/exceljs.min.js`: ExcelJS 4.4.0 (licencia MIT), usado para generar y leer los Excel.
- `build.py`: junta ambos en `cronograma.html` (`python3 build.py`).

Después de editar `src/app.html`, ejecutá `python3 build.py` para regenerar `cronograma.html`.
