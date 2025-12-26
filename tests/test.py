from reader import Reader


reader = Reader("MOD021KM.A2025001.0000.061.2025001132345.hdf")

print(reader.keys())
print(reader.infos())
print(reader["Latitude"])