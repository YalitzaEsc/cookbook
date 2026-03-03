document.addEventListener('DOMContentLoaded', function () {
    const addButton = document.getElementById('add-ingredient');
    const container = document.getElementById('ingredient-container');

    // Buscamos el input de TOTAL_FORMS dinámicamente
    const totalFormsInput = document.querySelector('input[id$="-TOTAL_FORMS"]');
    // Extraemos el prefijo (ej: "recipeingredient_set" o "form")
    const prefix = totalFormsInput.id.replace('id_', '').replace('-TOTAL_FORMS', '');

    addButton.addEventListener('click', function (e) {
        e.preventDefault();

        let formCount = parseInt(totalFormsInput.value);
        const rows = container.getElementsByClassName('ingredient-row');
        const lastRow = rows[rows.length - 1];

        // Clonamos la última fila
        const newRow = lastRow.cloneNode(true);

        // Limpiamos los valores y actualizamos los IDs/Names
        const inputs = newRow.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            // Reemplazamos el índice viejo por el nuevo (ej: -0- por -1-)
            const name = input.name.replace(`-${formCount - 1}-`, `-${formCount}-`);
            const id = input.id.replace(`-${formCount - 1}-`, `-${formCount}-`);

            input.name = name;
            input.id = id;
            input.value = ''; // Limpiar el contenido del clon

            // Si es un checkbox de borrar, lo desmarcamos
            if (input.type === 'checkbox') input.checked = false;
        });

        container.appendChild(newRow);

        // ¡Súper importante! Actualizar el contador total para Django
        totalFormsInput.value = formCount + 1;
    });

    // Lógica para borrar filas
    container.addEventListener('click', function (e) {
        if (e.target.closest('.remove-ingredient')) {
            const rows = container.getElementsByClassName('ingredient-row');
            if (rows.length > 1) {
                e.target.closest('.ingredient-row').remove();
                // Opcional: No siempre es necesario decrementar TOTAL_FORMS si se usa el checkbox DELETE,
                // pero para filas nuevas creadas con JS, eliminarlas físicamente está bien.
            }
        }
    });
});