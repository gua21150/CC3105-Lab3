from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float64
from feast.value_type import ValueType
from datetime import timedelta

california_source = FileSource(
    path="data/california.parquet",
    timestamp_field="event_timestamp",
)

# En esta versión de Feast, value_type debe ser ValueType.INT64 (no feast.types.Int64)
house = Entity(
    name="house_id",
    join_keys=["house_id"],
    value_type=ValueType.INT64,
)

california_view = FeatureView(
    name="california_features",
    entities=[house],
    ttl=timedelta(days=1),
    schema=[
        Field(name="ingresos_medios", dtype=Float64),
        Field(name="promedio_edad_casas", dtype=Float64),
        Field(name="promedio_num_habitaciones", dtype=Float64),
        Field(name="promedio_num_dormitorios", dtype=Float64),
        Field(name="poblacion_distrito", dtype=Float64),
        Field(name="promedio_personas_casa", dtype=Float64),
        Field(name="latitud", dtype=Float64),
        Field(name="longitude", dtype=Float64),
        Field(name="ratio_habitaciones_hogar", dtype=Float64),
        Field(name="ratio_habitaciones_poblacion", dtype=Float64),
        Field(name="ratio_dormitorios_habitacion", dtype=Float64),
        Field(name="ingreso_persona", dtype=Float64),
        Field(name="target", dtype=Float64),
    ],
    online=True,
    source=california_source,
)
