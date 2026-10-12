# API del backend

## Ejecucion local

Desde `backend/`, instalar las dependencias y ejecutar:

```sh
pip install -r requirements.txt
uvicorn app.main:app --reload
```

La API queda disponible en `http://localhost:8000`. La especificacion OpenAPI
se publica en `/openapi.json` y la interfaz interactiva en `/docs`.

## Estructura

- `app/main.py`: crea la aplicacion y registra routers y manejadores de errores.
- `app/api/router.py`: agrupa rutas bajo el prefijo versionado `/api/v1`.
- `app/api/routes/`: contiene los routers por recurso.
- `app/core/errors.py`: define el formato comun de errores.

## Endpoint inicial

### `GET /api/v1/health`

Comprueba que la API esta activa.

Respuesta `200`:

```json
{
  "status": "ok"
}
```

## Errores

Los errores HTTP se devuelven con el estado original y un cuerpo `error` que
incluye `code` y `message`. Los errores de validacion responden `422` y agregan
`details`, una lista con la ubicacion, el mensaje y el tipo del campo invalido.
Los errores inesperados responden `500` sin exponer detalles internos al cliente.