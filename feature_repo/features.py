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
        Field(name="MedInc", dtype=Float64),
        Field(name="HouseAge", dtype=Float64),
        Field(name="AveRooms", dtype=Float64),
        Field(name="AveBedrms", dtype=Float64),
        Field(name="Population", dtype=Float64),
        Field(name="AveOccup", dtype=Float64),
        Field(name="Latitude", dtype=Float64),
        Field(name="Longitude", dtype=Float64),
        Field(name="ratio_rooms_house", dtype=Float64),
        Field(name="ratio_rooms_pop", dtype=Float64),
        Field(name="ratio_bed_per_room", dtype=Float64),
        Field(name="target", dtype=Float64),
    ],
    online=True,
    source=california_source,
)
